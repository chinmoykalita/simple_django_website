from django.db import models


class Images(models.Model):
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return str(self.image)
