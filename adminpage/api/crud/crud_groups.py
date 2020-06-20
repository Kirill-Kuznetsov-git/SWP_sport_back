from typing import Optional

from django.db import connection

from django.conf import settings
from api.crud.utils import dictfetchall, dictfetchone
from sport.models import Sport, Student, Trainer


def get_sports(all=False, student: Optional[Student] = None):
    """
    Retrieves existing sport types
    @param all - If true, returns also special sport types
    @param student - if student passed, get sports applicable for student
    @return list of all sport types
    """
    qs = Sport.objects.filter(
        group__minimum_medical_group__lte=100 if student is None else student.medical_group,
    ).distinct()
    # w/o distinct returns a lot of duplicated
    return qs.all().values() if all else qs.filter(special=False).values()


def get_clubs(student: Optional[Student] = None):
    """
    Retrieves existing clubs
    @return list of all club
    """
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT '
            'g.id AS id, '
            'g.name AS name, '
            'sport.name AS sport_name, '
            's.name AS semester, '
            'capacity, description, trainer_id, is_club, '
            'count(e.id) AS current_load '
            'FROM sport, semester s, "group" g '
            'LEFT JOIN enroll e ON e.group_id = g.id '
            'WHERE s.id = current_semester() '
            'AND sport_id = sport.id '
            'AND semester_id = s.id '
            'AND is_club = TRUE '
            'AND  %(student_medical_group)s >= g.minimum_medical_group '
            'GROUP BY g.id, sport.id, s.id', {
                "student_medical_group": 100 if student is None else student.medical_group
            })
        return dictfetchall(cursor)


def get_student_groups(student: Student):
    """
    Retrieves groups, where student is enrolled
    @return list of group dicts
    """
    with connection.cursor() as cursor:
        cursor.execute('SELECT '
                       'g.id AS id, '
                       'g.name AS name, '
                       's.name AS sport_name, '
                       'e.is_primary AS is_primary '
                       'FROM enroll e, "group" g, sport s '
                       'WHERE g.semester_id = current_semester() '
                       'AND e.group_id = g.id '
                       'AND e.student_id = %s '
                       'AND s.id = g.sport_id '
                       'ORDER BY e.is_primary DESC', (student.pk,))
        return dictfetchall(cursor)


def get_trainer_groups(trainer: Trainer):
    """
    For a given trainer return all groups he/she is training in current semester
    @return list of group trainer is trainings in current semester
    """
    with connection.cursor() as cursor:
        cursor.execute('SELECT '
                       'g.id AS id, '
                       'g.name AS name, '
                       's.name AS sport_name '
                       'FROM "group" g, sport s '
                       'WHERE g.semester_id = current_semester() '
                       'AND g.sport_id = s.id '
                       'AND g.trainer_id = %s', (trainer.pk,))
        return dictfetchall(cursor)


def get_sc_training_group():
    """
    Finds sc training group for current semester
    @return group dict
    """
    with connection.cursor() as cursor:
        cursor.execute('SELECT '
                       'g.id AS id, '
                       'g.name AS name, '
                       'sport.name AS sport_name '
                       'FROM "group" g, sport, semester s '
                       'WHERE g.semester_id = current_semester() '
                       'AND sport_id = sport.id '
                       'AND g.name = %s', (settings.SC_TRAINERS_GROUP_NAME,))
        row = dictfetchone(cursor)
    if row is None:
        raise ValueError("Unable to find SC training group")
    return row
