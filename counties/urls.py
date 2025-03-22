from django.urls import path

from . import views


app_name = 'counties'

urlpatterns = [
    path("login/", views.log_in, name="login"),
    path("singin", views.sing_in, name="sing_in"),
    path("logout", views.log_out, name="logout"),
    path("", views.index, name="index"),
    path("county/<str:county_name>/", views.county, name="county"),
    path("edit/<str:last_name>/<str:first_name>/", views.edit, name="edit"),
    path("change/<str:last_name>/<str:first_name>/", views.change, name="change"),
    path("all_admins/", views.all_admins, name="all_admins")
]