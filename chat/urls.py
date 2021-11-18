from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<str:room>/", views.room, name="room"),
    path("checkview", views.checkview, name="checkview"),
    path("send", views.send, name="send"),
    path("getMessages/<str:room>/", views.getMessages, name="getMessages"),
]
# <str:room> Whatever url a person goes to or inputs will be seen as a room
# path checkview checks if  a room exist
