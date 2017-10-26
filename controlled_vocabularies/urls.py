from django.conf.urls import patterns, url
from controlled_vocabularies.views import (
    vocabulary_list, verbose_vocabularies, about,
    all_vocabularies, term_list, vocabulary_file
)

urlpatterns = patterns(
    '',
    # Search View
    url(r'^$', vocabulary_list, name="vocabulary_list"),
    url(r'^all-verbose/?$', verbose_vocabularies, name="verbose_vocabularies"),
    url(r'^about/', about, name="about"),
    url(r'^all/?$', all_vocabularies, name="all_vocabularies"),
    url(r'^(?P<vocabulary_name>[\w-]+)/$', term_list, name="term_list"),
    url(r'^(?P<list_name>[\w-]+)/(?P<file_format>\w+)/$', vocabulary_file, name="vocabulary_file"),
)
