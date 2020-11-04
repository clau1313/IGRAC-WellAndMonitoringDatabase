# coding=utf-8
"""Urls for igrac apps."""

from django.conf.urls import url
from django.urls import include
from gwml2.api.upload_progress import get_progress_upload
from gwml2.api.task_progress import TaskProgress
from gwml2.api.well_downloader import WellDownloader
from gwml2.api.well_relation import WellRelationDeleteView, WellRelationListView
from gwml2.views.groundwater_form import WellView, WellFormView, WellFormCreateView
from gwml2.views.organisation import OrganisationFormView, OrganisationListView
from gwml2.views.well_uploader import WellUploadView
from gwml2.api.upload_session import UploadSessionApiView
from gwml2.api.download_session import DownloadSessionApiView

well_relation = [
    url(r'^delete',
        view=WellRelationDeleteView.as_view(),
        name='well-relation-delete'),
]
well_detail_urls = [
    url(r'^(?P<model>[\w\+%_& ]+)/(?P<model_id>\d+)/', include(well_relation)),
    url(r'^(?P<model>[\w\+%_& ]+)/list', WellRelationListView.as_view(), name='well-relation-list'),
    url(r'^edit',
        view=WellFormView.as_view(),
        name='well_form'),
    url(r'^',
        view=WellView.as_view(),
        name='well_view'),
]

well_url = [
    url(r'^download/',
        view=WellDownloader.as_view(),
        name='well_download'),
    url(r'^create/',
        view=WellFormCreateView.as_view(),
        name='well_create'),
    url(r'^(?P<id>\d+)/', include(well_detail_urls)),
]

organisation_url = [
    url(r'^(?P<pk>\d+)/edit',
        view=OrganisationFormView.as_view(),
        name='organisation_form'),
    url(r'^',
        view=OrganisationListView.as_view(),
        name='organisation_list')
]

urlpatterns = [
    url(r'^well-upload',
        view=WellUploadView.as_view(),
        name='well_upload_view'),
    url(r'^progress-upload',
        view=get_progress_upload,
        name='progress_upload'),
    url(r'^task/(?P<task_id>.+)/progress/',
        view=TaskProgress.as_view(),
        name='task_progress'),
    url(r'^well/', include(well_url)),
    url(r'^organisation/', include(organisation_url)),
    url(r'^upload-session/'
        r'(?P<token>\b[0-9a-f]{8}\b-[0-9a-f]{4}-'
        r'[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}\b)/',
        view=UploadSessionApiView.as_view(),
        name='upload_session_progress'),
    url(r'^download-session/'
        r'(?P<token>\b[0-9a-f]{8}\b-[0-9a-f]{4}-'
        r'[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}\b)/',
        view=DownloadSessionApiView.as_view(),
        name='download_session_progress'),
]
