from sport.models import FAQCategory, FAQElement


def get_faq() -> list:
    """
    Get FAQ
    """
    result = []
    for i in FAQCategory.objects.values('name'):
        result.append({'category': i['name'], 'values': list(FAQElement.objects.filter(name=i['name']))})
    return result
