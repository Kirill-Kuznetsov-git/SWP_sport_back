from sport.models import FAQCategory, FAQElement


def get_faq() -> dict:
    """
    Get FAQ
    """
    result = {}
    for i in FAQCategory.objects.values('name'):
        result[i['name']] = list(FAQElement.objects.filter(name=i['name']))
    return result
