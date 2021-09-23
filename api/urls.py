from django.urls import include, path
from . import views

app_name = 'api'

urlpatterns = [
 path('test/', views.test_api, name='test_api_communication'),
 path('is-fraud/', views.run_fraud_detection_inference, name='run_fraud_detection'),
]
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)