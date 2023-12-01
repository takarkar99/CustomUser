from django.contrib import admin
from django.urls import path
#from App1.views import quantities_view #test_view, 

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('<int:product_id>/', test_view, name='test_api')
    #path('quanity_view/',  quantities_view, name='quanity_view')
]
