from django.conf import settings

from feincms.module.page.models import Page
from feincms.translations import short_language_code


def feincms_pages(request):
    lang = short_language_code()

    try:
        feincms_page = Page.objects.for_request(request, best_match=True)
    except Page.DoesNotExist:
        try:
            feincms_page = Page.objects.get(slug=lang)
        except Page.DoesNotExist:
            feincms_page = None

    try:
        footer = Page.objects.get(language=lang, slug="footer")
    except Page.DoesNotExist:
        try:
            footer = Page.objects.filter(slug="footer")[0]
        except:
            footer = None

    return {
        'feincms_page': feincms_page,
        'footer': footer
    }


def config(request):
    return {
        'GA_CODE': settings.GA_CODE,
    }
