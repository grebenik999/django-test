from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, CreateView
from .models import Department
from workers.models import Worker
from workers.seeder import departmentFactory, workerFactory


class HomePageView(TemplateView):
    """
    for create a random departments and workers
    please uncomment the lines below and just save the changes:
    """
    # departmentFactory()
    # workerFactory()

    template_name = 'department/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = Department.objects.all()
        context['workers'] = Worker.objects.all()
        return context


class DepartmentCreateView(LoginRequiredMixin,
                           SuccessMessageMixin,
                           CreateView):
    """ Create a Department View at /department/new/ """
    model = Department
    fields = ['name', 'parent']
    login_url = 'login'
    success_url = '/'
    success_message = ('Department was created.')

    def form_valid(self, form):
        return super().form_valid(form)


""" Delete a Department at /department/<id>/delete/ """


@login_required(login_url='login')
def deleteDepartment(request, id):
    if request.method == 'POST':
        name_dep = Department.objects.get(id=id)
        Department.objects.filter(id=id).delete()
        messages.add_message(request, messages.INFO,
                             f'You deleted {name_dep} department')
        return redirect('/')
