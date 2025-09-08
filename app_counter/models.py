from django.db import models
from django.conf import settings


class Counter(models.Model):
    value = models.IntegerField(blank=False, null=False, default=0)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return f"id={self.id} value={self.value}"
