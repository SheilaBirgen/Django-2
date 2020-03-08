from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [

    path('register/', views.registration, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='home'),
    # path('profile/', views.profile, name='profile'),
    # path('posts/', views.post, name='posts'),
    path('post_create/', views.post_create, name="createpost"),
    path('comment/<post_id>/', views.comment, name="comment"),
    # path('commenting/<post_id>', views.commenting, name="commenting"),
    # path('search/', views.search_user, name="search"),
    # path('likes/<post_id>', views.likes, name="likes"),
    
]