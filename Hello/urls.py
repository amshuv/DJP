from django.urls import path, re_path
from django.contrib import admin
from Hello import views
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',views.Hello, name='Hello'),
    # re_path(r"^amshu/",views.amshu,name="amshu"),
    re_path(r"^List/",views.list_view,name="list_view"),
]