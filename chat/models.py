from django.conf import settings
from django.db import models

class Message(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="messages",
        verbose_name="Користувач"
    )
    text = models.TextField(verbose_name="Повідомлення")
    is_from_manager = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        role = "Менеджер" if self.is_from_manager else "Користувач"
        return f"{role}: {self.text[:30]}"
