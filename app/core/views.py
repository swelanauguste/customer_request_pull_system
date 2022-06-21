from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django.views.generic.edit import FormMixin
from hitcount.views import HitCountDetailView, HitCountMixin

from .forms import CustomerRequestForm, CustomerRequestPullForm
from .models import CustomerRequest, RequestStatus


class CustomerRequestListView(ListView):
    model = CustomerRequest
    paginate_by: int = 10

    def get_queryset(self):
        return CustomerRequest.unassigned_objects.all()


class CustomerRequestDetailView(FormMixin, HitCountDetailView):
    model = CustomerRequest
    form_class = CustomerRequestPullForm
    success_url = reverse_lazy("list")
    count_hit = True
    
    def form_valid(self, form):
        form.instance.assigned_to = self.request.user
        form.instance.status = RequestStatus.objects.get(pk=2)
        return super().form_valid(form)


class CustomerRequestCreateView(CreateView):
    model = CustomerRequest
    form_class = CustomerRequestForm


class CustomerRequestPullUpdateView(UpdateView):
    model = CustomerRequest
    form_class = CustomerRequestPullForm
    success_url = reverse_lazy("list")
    count_hit = True

    def form_valid(self, form):
        form.instance.assigned_to = self.request.user
        form.instance.status = RequestStatus.objects.get(pk=2)
        return super().form_valid(form)
