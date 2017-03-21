"""ngv_challenge URL Configuration
"""
from django.conf.urls import url
from django.contrib import admin
from scholarship_list.views import ScholarshipView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^scholarship-api/$', ScholarshipView.as_view()),
]
