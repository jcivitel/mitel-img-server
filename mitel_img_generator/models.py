from django.db import models


class Customer(models.Model):
    customer_name = models.CharField(max_length=30)
    customer_tag = models.CharField(max_length=30)
    customer_logo = models.ImageField(
        upload_to="mitel-img.CustomerFiles/bytes/filename/mimetype",
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.customer_name


class PhoneModel(models.Model):
    phone_model = models.CharField(max_length=30)
    pos_x = models.IntegerField(default=0)
    pos_y = models.IntegerField(default=0)

    def __str__(self):
        return self.phone_model
