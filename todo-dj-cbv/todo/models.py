from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse



class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(_("title"), max_length=50)
    description = models.TextField(_("description"))
    complete = models.BooleanField(_("complete") , default=False)
    created = models.DateTimeField(_("created"), auto_now_add=True)


    class Meta:

        ordering = ['complete',]
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Task_detail", kwargs={"pk": self.pk})
