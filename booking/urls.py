"""
URL configuration for booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/',include('accounts.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('',include('main.urls')),

]
urlpatterns = [
    path('', views.index, name='index'),
    path('tables/', views.table_list, name='table_list'),
    path('menu/', views.menu_list, name='menu_list'),
    path('booking/create/', views.booking_create, name='booking_create'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('edit_booking/<int:booking_id>/', views.booking_edit, name='edit_booking'), # Edit booking - added from updated zip
    path('check-table-availability/<int:table_id>/<int:number_of_people>/', views.check_table_availability, name='check_table_availability'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
admin.site.site_title = 'Restaurant Booking Admin Panel'
admin.site.site_header = 'Restaurant Booking Admin Panel'

handler404='accounts.views.page_handler'