from django import forms
from .models import Purchase  # Assuming your model is named Purchase

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['buyer', 'amount', 'description','hamze_share_of_purchase', 'is_paid_hamze','gholam_share_of_purchase', 'is_paid_gholam', 'atapoor_share_of_purchase', 'is_paid_ata','mobin_share_of_purchase', 'is_paid_mobin', 'matin_share_of_purchase', 'is_paid_matin']





