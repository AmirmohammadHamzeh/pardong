from django.shortcuts import render, redirect, get_object_or_404
from .models import Purchase


# from django.contrib.auth.decorators import login_required


def index(request):
    username = request.user.first_name
    debt_of_hamze_gholam = None
    debt_of_gholam_hamzeh = None
    data = None
    if request.method == 'GET':
        data = Purchase.objects.filter(is_paid=False)
        if username == "amirmohammad":
            debt_of_hamze_gholam = Purchase.objects.filter(buyer__nickname="tandorost", is_paid_gholam=False,is_paid=False)
            debt_of_gholam_hamzeh = Purchase.objects.filter(buyer__nickname="gholami", is_paid_hamze=False,is_paid=False)
        elif username == "amirhossein":
            debt_of_hamze_gholam = Purchase.objects.filter(buyer__nickname="tandorost", is_paid_gholam=False,is_paid=False)
            debt_of_gholam_hamzeh = Purchase.objects.filter(buyer__nickname="gholami", is_paid_hamze=False,is_paid=False)
        return render(request, "main/index.html",
                      {"data": data,
                       "debt_of_hamze_gholam": debt_of_hamze_gholam,
                       "debt_of_gholam_hamzeh": debt_of_gholam_hamzeh})


from .forms import *


def new_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('purchase_list')  # Redirect to the purchase list after saving
    else:
        form = PurchaseForm()
    return render(request, 'main/new_purchase.html', {'form': form})


def mark_paid(request, purchase_id, field):
    purchase = get_object_or_404(Purchase, id=purchase_id)
    if field == 'hamze':
        purchase.is_paid_hamze = True
    elif field == 'gholam':
        purchase.is_paid_gholam = True
    elif field == 'ata':
        purchase.is_paid_ata = True
    elif field == 'mobin':
        purchase.is_paid_mobin = True
    elif field == 'matin':
        purchase.is_paid_matin = True
    purchase.save()
    return redirect('purchase_list')  # Redirect to the purchase list after updating



def mark_general_paid(request, purchase_id):
    purchase = get_object_or_404(Purchase, id=purchase_id)
    purchase.is_paid = True
    purchase.save()
    return redirect('purchase_list')  # Redirect to the purchase list after updating







# TODO build delete method (is paid)
# TODO share with members
# TODO fix new table
