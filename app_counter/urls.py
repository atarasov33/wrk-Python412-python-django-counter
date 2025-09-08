from django.urls import path
from app_counter import views


app_name = "app_counter"

urlpatterns = [
    path("", views.index, name="index"),
    path("counter/", views.counter, name="counter"),
    path("counter/create/", views.create_counter, name="create_counter"),
    path("counter/increase/", views.increase_counter, name="increase_counter"),
    path("counter/decrease/", views.decrease_counter, name="decrease_counter"),
    path("counter/manage_counter/", views.manage_counter, name = "manage_counter"),
    path("counter/set_favorit/<int:counter_id>", views.set_favorit, name = "set_favorit")

]