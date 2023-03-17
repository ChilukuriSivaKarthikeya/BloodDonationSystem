from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('forgot',views.forgot,name="forgot"),
    path('user/passwordchange',views.reset,name="reset"),
    path('user',views.user,name="user"),
    path('user/Myprofile',views.profile,name="profile"),
    path('search',views.search,name="search"),
    path('user/search',views.usersearch,name="usersearch"),
    path('user/profile/edit',views.edit,name="edit"),
    path('user/profile/photoedit',views.photoedit,name="photoedit"),
    path('user/donate',views.donate,name="donate"),
    path('',views.logout,name="logout"),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)