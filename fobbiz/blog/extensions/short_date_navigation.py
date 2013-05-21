"""
    filename:       short_date_navigation.py
    author:         R. Coroneo
    date:           21.05.2013
    description:    little changes for the generation of the archiv navigation.
                    modified:  
                        month=u%s' % ugettext(all_months[month-1].strftime('%B')),
                        year= '%s' % year,
"""

from django.utils.translation import ugettext_lazy as _, ugettext

from elephantblog.navigation_extensions.common import *
from elephantblog.models import Entry

from feincms.module.page.extensions.navigation import (NavigationExtension,
    PagePretender)



class ShortDateNavigation(NavigationExtension):
    """
    Navigation extension for FeinCMS which shows a year and month Breakdown:
    2012
        April
        March
        February
        January
    2011
    2010
    """
    name = _('Blog date')

    def children(self, page, **kwargs):
        for year, months in date_tree():
            yield PagePretender(
                title=u'%s' % year,
                url='%s%s/' % (page.get_absolute_url(), year),
                tree_id=page.tree_id, # pretty funny tree hack
                lft=0,
                rght=len(months)+1,
                level=page.level+1,
                slug='%s' % year,
                )
            for month in months:
                entry_count = Entry.objects.filter(is_active=True,
                    published_on__month=month).count()
                if entry_count:
                    yield PagePretender(
                        # Only the next two lines has been changed
                        month=u'%s' % ugettext(all_months[month-1].strftime('%B')),
                        year= '%s' % year,
                        # The lines below already existed
                        url='%s%04d/%02d/' % (page.get_absolute_url(), year, month),
                        tree_id=page.tree_id, # pretty funny tree hack
                        last=month == 12,
                        lft=0,
                        rght=0,
                        level=page.level+2,
                        slug='%04d/%02d' % (year, month),
                    )