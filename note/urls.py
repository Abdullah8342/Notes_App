from django.urls import path
from .views import NoteView,NoteDetail,NoteCreate,NoteDelete,NoteUpdate,CustomSignup
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('signup/',CustomSignup.as_view(),name = 'signup'),
    path('login/',LoginView.as_view(template_name = 'note/login.html'),name='Login'),
    path('logout/',LogoutView.as_view(),name='Logout'),
    path('',NoteView.as_view(),name='NoteView'),
    path('detail/<int:pk>/',NoteDetail.as_view(),name='DetailNote'),
    path('delete/<int:pk>/',NoteDelete.as_view(),name='DeleteNote'),
    path('update/<int:pk>/',NoteUpdate.as_view(),name='UpdateNote'),
    path('create/',NoteCreate.as_view(),name = 'NoteCreate'),
]
