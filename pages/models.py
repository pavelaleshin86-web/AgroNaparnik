from django.db import models


class ContactMessage(models.Model):
    name = models.CharField("Имя", max_length=100)
    email = models.EmailField("Email")
    message = models.TextField("Сообщение")
    created_at = models.DateTimeField("Дата", auto_now_add=True)
    is_processed = models.BooleanField("Обработано", default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self) -> str:
        return f"{self.name} ({self.email})"
