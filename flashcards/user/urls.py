from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandingPageView.as_view(),name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    #Profile
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/settings/change-email/', views.ChangeEmailView.as_view(), name='logout'),
    path('profile/settings/change-password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('profile/settings/change-username/', views.ChangeUsernameView.as_view(), name='change_password'),


    #Dont know if these below are part of user just remove them if not
    #Notification
    #gibalhin ra nako - jm was here
    # path('notification/', views.NotificationView.as_view(), name='notification'),

    #Deck
    #moved to deck app
    # path('deck/add', views.DeckCreateView.as_view(), name='deck'),

    #Card
    # moved to card app
    # path('card/', views.CardView.as_view(), name='card'),

    #Folder
    path('folder/add', views.FolderCreateView.as_view(), name='folder'),
]
