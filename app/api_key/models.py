from django.db import IntegrityError, models, transaction

from app.core.utils import generate_api_key
from app.tenants.models import Tenant


class ApiKey(models.Model):
    """
    Instead of using domain url Api Key is used to identify the Tenant
    key needs to be passed in the authorization headers
    """

    agency = models.ForeignKey(Tenant, related_name="api_key", on_delete=models.CASCADE)
    key = models.CharField(max_length=40, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key

    def save(self, *args, **kwargs):
        if not self.pk:
            while True:
                try:
                    with transaction.atomic():
                        self.key = generate_api_key()
                        return super(ApiKey, self).save(*args, **kwargs)
                except IntegrityError:
                    self.key = generate_api_key()
        return super(ApiKey, self).save(*args, **kwargs)
