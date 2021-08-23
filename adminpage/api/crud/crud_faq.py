from sport.models import FAQCategory, FAQElement


def get_faq() -> list:
    """
    Get FAQ
    """
    result = [{i[0]: {FAQElement.objects.filter(name=i[0])}} for i in FAQCategory.objects.values('name')]
    return result
