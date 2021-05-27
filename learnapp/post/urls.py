from django.urls import path

from .views import index_page, sign_in, sign_up, sections, by_section, by_post, log_out, profile, change_password

urlpatterns = [
    path('main', index_page, name='index'),
    path('sign_in', sign_in, name='sign_in'),
    path('logout/', log_out, name='log_out'),
    path('sign_up', sign_up, name='sign_up'),
    path('sections', sections, name='sections'),
    path('section/<int:subject_id>', by_section, name='by_section'),
    path('post/<int:post_id>', by_post, name='by_post'),
    path('profile', profile, name='profile'),
    path('change_password', change_password, name='change_password')
]
