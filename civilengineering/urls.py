from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [

    # ADMIN
    

    # HOME
    path("", views.home, name='home'),

    # PROJECTS (ALL)
    path("project/", views.project, name='project'),

    # CATEGORY FILTER (IMPORTANT FOR YOUR NEW UI)
    path(
        "category/<str:category>/",
        views.category_page,
        name='category'
    ),

    # AUTH
    path("login_view/", views.login_view, name='login_view'),

    path("signup_view/", views.signup_view, name='signup_view'),

    path("user_signup/", views.user_signup, name='user_signup'),

    path("user_login/", views.user_login, name='user_login'),

    # STATIC PAGES
    path("about/", views.about, name='about'),

    path("contact/", views.contact, name='contact'),

    path("privacy/", views.privacy, name='privacy'),

    path('logout/', views.logout_view, name='logout'),
    path('watch/<int:id>/',views.watch_video,name='watch_video'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)