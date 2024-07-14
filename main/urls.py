from django.urls import path
from .views import index, new_purchase ,mark_paid, mark_general_paid

urlpatterns = [
    path("", index, name="purchase_list"),
    path("new_purchase", new_purchase, name="new_purchase"),
    path('mark_paid/<int:purchase_id>/<str:field>/', mark_paid, name='mark_paid'),
    path('mark_general_paid/<int:purchase_id>/', mark_general_paid, name='mark_general_paid'),
    ]
    # other URL patterns
