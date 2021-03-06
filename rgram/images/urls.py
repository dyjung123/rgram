from django.conf.urls import url
from . import views

app_name = "images" # Django 2.0 need it.
urlpatterns = [
    url(
        regex=r'^all/$',
        view=views.ListAllImages.as_view(),
        name='all_images'
    ),
    url(
        regex=r'^comments/$',
        view=views.ListAllComment.as_view(),
        name='all_images'
    ),
    url(
        regex=r'^likes/$',
        view=views.ListAllLike.as_view(),
        name='all_images'
    )
]