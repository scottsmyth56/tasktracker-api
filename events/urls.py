from django.urls import path
from . import views
from .views import accept_invitation

urlpatterns = [
    path('events/', views.EventListAPIView.as_view(), name='task-list'),
    path('events/<int:pk>/', views.EventRetrieveUpdateDestroyAPIView.as_view(), name='event-detail'),
    path('events/invite/', views.EventInvitationCreateAPIView.as_view(), name='event-invite'),
    path('event-invitations/<int:pk>/accept/', accept_invitation, name='accept-invitation'),

]
