from django.urls import path

from .views import PostListView, index_page, sign_in, sign_up, themes, sections, paragraph_1, log_out

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('main', index_page),
    path('logout/', log_out, name='log_out'),
    path('sign_in', sign_in, name='sign_in'),
    path('sign_up', sign_up, name='sign_up'),
    path('themes', themes, name='themes'),
    path('sections', sections, name='sections'),
    path('paragraph_1', paragraph_1, name='paragraph_1'),
]



