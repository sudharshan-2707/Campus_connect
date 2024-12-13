from django.contrib import admin                                                                                                    
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg',views.register,name='reg'),
    path('',views.home,name='home'),
    path('event2',views.event,name="event2"),
    path('eventd',views.eventdet,name="eventd"),
    path('dis',views.dispevent,name="dis"),
    path('disp/<str:name>',views.dispeventdet,name="disp"),
    path('aboutus',views.aboutus,name="aboutus"),
    path('course',views.course,name="course"),
    path('fac',views.facility,name="fac"),
    path('pla',views.plac,name="pla"),   
    path('thank',views.thank,name="thank"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
