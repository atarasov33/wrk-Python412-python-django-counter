from django.db import models
from django.conf import settings


class Counter(models.Model):
    value = models.IntegerField(blank=False, null=False, default=0)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='counters'
    )
    is_favorite = models.BooleanField(default=False)

    def clean(self):
        super().clean()
        if self.is_favorite and self.user:
            Counter.objects.filter(
                user =self.user,
                is_favorite =True
            ).exclude(pk=self.pk).update(is_favorite=False)

    def __str__(self):
        return f"id={self.id} value={self.value}"

    def save(self,*args, **kwargs):
        self.full_clean()
        super().save(*args,**kwargs)
