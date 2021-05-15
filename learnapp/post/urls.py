from django.urls import path

from .views import index_page, sign_in, sign_up, sections, by_section

urlpatterns = [
    path('', index_page, name='index'),
    path('sign_in', sign_in, name='sign_in'),
    path('sign_up', sign_up, name='sign_up'),
    path('sections', sections, name='sections'),
    path('sections/<int:subject_id>', by_section, name='by_section'),
]
