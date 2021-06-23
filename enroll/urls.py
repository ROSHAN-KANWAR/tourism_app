from django.urls import path
from enroll import views
urlpatterns = [
  path("",views.Home_view,name="home"),
  path("cgtourism/About_us_page/", views.About_view, name="about"),
  path("cgtourism/templeview/?^page<int:id>/", views.Templedetail_view, name="templeview"),
  path("cgtourism/galleryview/?^&page<int:id>/", views.Gallery_imageview, name="galleryview"),
  path("cgtourism/Contact_page/", views.Contact_view, name="contact"),
  path("cgtourism/temple_page/",views.Filters,name="temple"),
  path("cgtourism/gallery_page/", views.Filtersgallery, name="gallery"),
  path("cgtourism/webapp/?^page$admin_login/",views.Admin_login,name="admin_login"),
  path("cgtourism/webapp/?^page$dashboard_admin/",views.dashboard,name="dash"),
  path('cgtourism/webapp/?^page$Admin_logout/', views.Admin_logout, name="user_logout"),
  path('cgtourism/webapp/?^page$delete/<int:id>/', views.delete_data, name="delete"),
  path('cgtourism/webapp/?^page$delete_gl/<int:id>/', views.delete_data_gl, name="delete1"),
  path('cgtourism/webapp/?^page$edit/<int:id>/', views.edit_data, name="edit"),
  path('cgtourism/webapp/?^page$edit_gl/<int:id>/', views.edit_data_gl, name="edit1"),
  path("cgtourism/webapp/?^page$templeaddphoto",views.Templephotoadd,name="temadd"),
  path("cgtourism/webapp/?^page$galleryaddphoto",views.Galleryphotoadd,name="temadd1"),
]
