from django.db import models

from billing.models import BillingProfile

ADDRESS_TYPES = (
    ('billing', 'Billing'),
    ('shipping', 'Shipping')
)


class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile)
    address_type    = models.CharField(max_length=120, choices=ADDRESS_TYPES)
    address_line    = models.CharField(max_length=120)
    address_line    = models.CharField(max_length=120, null=True, blank=True)
    city            = models.CharField(max_length=120)
    country         = models.CharField(max_length=120, default='Ukraine')
    state           = models.CharField(max_length=120)
    postal_code     = models.CharField(max_length=120)

    def __srt__(self):
        return str(self.billing_profile)
    
