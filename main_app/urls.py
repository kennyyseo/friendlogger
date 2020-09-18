from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('friends/', views.friends_index, name='index'),
    path('friends/<int:friend_id>/', views.friends_detail, name='detail'),
    path('friends/create/', views.FriendCreate.as_view(), name='friends_create'),
    path('friends/<int:pk>/update/',
         views.FriendUpdate.as_view(), name='friends_update'),
    path('friends/<int:pk>/delete/',
         views.FriendDelete.as_view(), name='friends_delete'),
    path('friends/<int:friend_id>/add_meeting/',
         views.add_meeting, name='add_meeting'),
    path('memories/', views.MemoryList.as_view(), name='memories_index'),
    path('memories/<int:pk>/', views.MemoryDetail.as_view(), name='memories_detail'),
    path('memories/create/', views.MemoryCreate.as_view(), name='memories_create'),
    path('memories/<int:pk>/update/',
         views.MemoryUpdate.as_view(), name='memories_update'),
    path('memories/<int:pk>/delete/',
         views.MemoryDelete.as_view(), name='memories_delete'),
    path('friends/<int:friend_id>/assoc_memory/<int:memory_id>/',
         views.assoc_memory, name='assoc_memory'),
]
