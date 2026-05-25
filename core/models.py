from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='todo_images/', blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.db.models.signals import post_delete
from django.dispatch import receiver

@receiver(post_delete, sender=Todo)
def delete_todo_image(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)
