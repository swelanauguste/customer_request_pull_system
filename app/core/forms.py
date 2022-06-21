from django import forms

from .models import CustomerRequest


class CustomerRequestForm(forms.ModelForm):
    class Meta:
        model = CustomerRequest
        fields = (
            "customer_email",
            "customer_telephone",
            "customer_name",
            "customer_ministry",
            "customer_department",
            "desc",
        )


class CustomerRequestPullForm(forms.ModelForm):
    class Meta:
        model = CustomerRequest
        fields = ("assigned_to", "status")
        widgets = {"status": forms.HiddenInput(), "assigned_to": forms.HiddenInput()}
