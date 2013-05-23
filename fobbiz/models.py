"""
    filename:       models.py
    author:         R. Coroneo
    date:           21.05.2013
    description:    For FeinCMS needed settings, with template, Content Types, Extensions
"""

from django.utils.translation import ugettext_lazy as _

from feincms.module.page.models import Page
from feincms.content.medialibrary.models import MediaFileContent
from feincms.content.richtext.models import RichTextContent
from feincms_oembed.contents import OembedContent
from feincms.content.raw.models import RawContent
from feincms.content.application.models import ApplicationContent

from elephantblog.models import Entry
from elephantblog.contents import BlogEntryListContent

from fobbiz.veranstaltungen.contents import VeranstaltungContent
from fobbiz.moodboard.contents import ShowMoodboard
from fobbiz.blog.extensions import short_date_navigation



MEDIA_TYPE_CHOICES = (
    ('default', _('Full width')),
)

OEMBED_TYPE_CHOICES = (
    ('default', _('Default'), {'maxwidth': 760, 'maxheight': 480, 'wmode': 'opaque'}),
)

# Feincms Setup
Page.register_templates(
    {
        'title': 'Base template',
        'path': 'base.html',
        'regions': (
            ('main', _('Main content area')),
            ('sidebar', _('Sidebar content area')),
            ('moodboard', _('Moodboard area')),
        ),

})

Page.register_extensions(
    'feincms.module.extensions.translations',
    'feincms.module.extensions.ct_tracker',
    'feincms.module.page.extensions.navigation',
)

Page.create_content_type(RichTextContent)
Page.create_content_type(MediaFileContent, TYPE_CHOICES=MEDIA_TYPE_CHOICES)
Page.create_content_type(OembedContent, TYPE_CHOICES=OEMBED_TYPE_CHOICES)
Page.create_content_type(RawContent)
Page.create_content_type(BlogEntryListContent)
# Moodboard Content
Page.create_content_type(ShowMoodboard)


Page.create_content_type(ApplicationContent, APPLICATIONS=(
    ('elephantblog.urls', _('Blog'),),
))


# Elephantblog Setup
Entry.register_regions(
    ('main', _('Main content area')),
)

Entry.register_extensions(
    'feincms.module.extensions.translations',
)

Entry.create_content_type(RichTextContent)
Entry.create_content_type(MediaFileContent, TYPE_CHOICES=MEDIA_TYPE_CHOICES)
Entry.create_content_type(OembedContent, TYPE_CHOICES=OEMBED_TYPE_CHOICES)
Entry.create_content_type(RawContent)

# Event Content
Entry.create_content_type(VeranstaltungContent)
