from __future__ import unicode_literals

from django import apps
from django.utils.translation import ugettext_lazy as _

from common import menu_facet, menu_sidebar
from rest_api.classes import APIEndPoint

from .links import link_search, link_search_advanced, link_search_again


class DynamicSearchApp(apps.AppConfig):
    name = 'dynamic_search'
    verbose_name = _('Dynamic search')

    def ready(self):
        APIEndPoint('search', app_name='dynamic_search')

        menu_facet.bind_links(links=[link_search, link_search_advanced], sources=['search:search', 'search:search_advanced', 'search:results'])
        menu_sidebar.bind_links(links=[link_search_again], sources=['search:results'])