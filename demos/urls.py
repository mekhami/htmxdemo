from django.urls import path

from . import views


urlpatterns = [
    path("", views.home),
    path("now", views.now),
    path("form", views.forms_page),
    path("forms", views.forms),
    path("inline/<str:which>", views.inline_validate),
    path("inline", views.inline_page),
    path("modals", views.modals_page),
    path("modal", views.modal),
    path("polling", views.polling),
    path("load", views.load),
    path("out-of-bounds", views.out_of_bounds),
    path("perform-task", views.perform_task),
    path("miscellany", views.miscellany),
]
