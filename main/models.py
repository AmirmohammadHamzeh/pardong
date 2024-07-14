from django.db import models
from accounts.models import CustomUser


class Purchase(models.Model):
    buyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='خریدار')
    amount = models.IntegerField(verbose_name="مبلغ خرید")
    description = models.TextField(null=True, blank=True, verbose_name="توضیحات")
    matin_share_of_purchase = models.IntegerField(null=True, blank=True, verbose_name="سهم متینک")
    is_paid_matin = models.BooleanField(default=False,)
    gholam_share_of_purchase = models.IntegerField(null=True, blank=True, verbose_name="سهم غلامی")
    is_paid_gholam = models.BooleanField(default=False, )
    hamze_share_of_purchase = models.IntegerField(null=True, blank=True, verbose_name="سهم مهندس همزه")
    is_paid_hamze = models.BooleanField(default=False, )
    mobin_share_of_purchase = models.IntegerField(null=True, blank=True, verbose_name="سهم مبینی")
    is_paid_mobin = models.BooleanField(default=False, )
    atapoor_share_of_purchase = models.IntegerField(null=True, blank=True, verbose_name="سهم ترپ")
    is_paid_ata = models.BooleanField(default=False, )
    is_paid = models.BooleanField(default=False, )
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.description} - {self.amount}'

    class Meta:
        db_table = 'debt'
