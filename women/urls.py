from django.urls import path
from . import views


urlpatterns = [
    path('', views.WomenHome.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.AddPage.as_view(), name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', views.WomenCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>', views.WomenTags.as_view(), name='tag'),
    path('edit/<slug:slug>', views.UpdatePage.as_view(), name='editpage'),
    path('delete/<slug:slug>', views.DeletePage.as_view(), name='deletepage'),
]
