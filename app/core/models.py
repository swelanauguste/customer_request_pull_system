import uuid

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from users.models import User
from hitcount.models import HitCountMixin

class Ministry(models.Model):
    uid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    ministry = models.CharField(max_length=100)

    class Meta:
        ordering = ["ministry"]

    class Meta:
        verbose_name_plural = "Ministries"

    def __str__(self):
        return self.ministry


class RequestStatus(models.Model):
    uid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["status"]
        verbose_name_plural = "Request Statuses"

    def __str__(self):
        return self.status
    
class CustomerRequestManagerUnassigned(HitCountMixin, models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=1)


class CustomerRequest(models.Model, HitCountMixin):
    uid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=100, blank=True)
    status = models.ForeignKey(RequestStatus, on_delete=models.CASCADE, default=1)
    assigned_to = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True
    )
    customer_email = models.EmailField("email", max_length=254)
    customer_telephone = models.CharField(
        max_length=50, help_text="468-5050 or 456-5050"
    )
    customer_name = models.CharField("name", max_length=254)
    customer_ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE)
    customer_department = models.CharField("department", max_length=254)
    desc = models.TextField("description")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = models.Manager()
    unassigned_objects = CustomerRequestManagerUnassigned()

    class Meta:
        ordering = ["-updated_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.uid)
        super(CustomerRequest, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    def get_pull_url(self):
        return reverse("pull", kwargs={"slug": self.slug})

    def __str__(self):
        return self.customer_name


# class CustomerRequestComment(models.Model):
#     uid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
#     customer_request = models.ForeignKey(
#         CustomerRequest, on_delete=models.CASCADE, related_name="comments"
#     )
#     comment = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ["-updated_at"]

#     def __str__(self):
#         return self.comment[:25] + "..."
