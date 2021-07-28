from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group as AuthGroup
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

from sport.models import Semester, Sport, Trainer, Group, Schedule

User = get_user_model()


def get_or_create_student_group():
    return AuthGroup.objects.get_or_create(
        verbose_name=settings.STUDENT_AUTH_GROUP_VERBOSE_NAME,
        defaults={
            "name": settings.STUDENT_AUTH_GROUP_NAME,
        }
    )[0]


def get_or_create_trainer_group():
    return AuthGroup.objects.get_or_create(
        verbose_name=settings.TRAINER_AUTH_GROUP_VERBOSE_NAME,
        defaults={
            "name": settings.TRAINER_AUTH_GROUP_NAME,
        }
    )[0]


@receiver(post_save, sender=Semester)
def special_groups_create(sender, instance, created, **kwargs):
    if created:
        # get_or_create returns (object: Model, created: bool)
        other_sport, _ = Sport.objects.get_or_create(
            name=settings.OTHER_SPORT_NAME,
            special=True
        )
        trainer_group = get_or_create_trainer_group()
        sport_dep_user, _ = User.objects.get_or_create(
            first_name="Sport",
            last_name="Department",
            email=settings.SPORT_DEPARTMENT_EMAIL,
            defaults={
                "is_active": True,
            }
        )
        sport_dep_user.groups.add(trainer_group)
        sport_dep, _ = Trainer.objects.get_or_create(user=sport_dep_user)
        kwargs = {
            'is_club': False,
            'sport': other_sport,
            'semester': instance,
            'trainer': sport_dep
        }
        Group.objects.create(
            name=settings.SC_TRAINERS_GROUP_NAME_FREE,
            capacity=9999,
            **kwargs
        )
        Group.objects.create(
            name=settings.SC_TRAINERS_GROUP_NAME_PAID,
            capacity=9999,
            **kwargs
        )
        Group.objects.create(
            name=settings.SELF_TRAINING_GROUP_NAME,
            capacity=9999,
            **kwargs
        )
        Group.objects.create(
            name=settings.EXTRA_EVENTS_GROUP_NAME,
            capacity=0,
            **kwargs,
        )
        Group.objects.create(
            name=settings.MEDICAL_LEAVE_GROUP_NAME,
            capacity=0,
            **kwargs
        )
    else:
        # if semester changed, recalculate all future related schedules
        semester_schedules = Schedule.objects.filter(
            group__semester=instance.pk
        )
        for schedule in semester_schedules:
            post_save.send(
                sender=Schedule,
                instance=schedule,
                created=False
            )
