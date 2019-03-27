from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from department.models import Department
from .models import Worker


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    """ Create an Employee at /employee/new/"""
    model = Worker
    fields = ['department', 'username',
              'position', 'hire_date', 'salary', 'image']
    template_name = 'workers/employee_form.html'
    login_url = 'login'
    success_url = '/employee/all/'

    def form_valid(self, form):
        return super().form_valid(form)


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    """ Create an Employee Details View at /employee/<id>/details/ """
    model = Worker
    template_name = 'workers/worker-detail.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class EmployeeListView(LoginRequiredMixin, ListView):
    """ Create an Employee List View at /employee/all/ """
    model = Worker
    context_object_name = 'workers'
    paginate_by = 7
    login_url = 'login'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        employee_list = Worker.objects.all()
        paginator = Paginator(employee_list, self.paginate_by)
        page = self.request.GET.get('page')
        ctx['page'] = self.request.GET.get('page')
        if ctx['page'] is None:
            ctx['page'] = ''
        return ctx

    def get_queryset(self, *args, **kwargs):
        order = self.request.GET.get('order_by', 'id')
        direction = self.request.GET.get('direction')
        if direction == 'desc':
            order = self.request.GET.get('-order_by', 'id')
        new_context = Worker.objects.all().order_by(order)
        return new_context


class SearchListView(ListView):
    """ Create a Search View at /search/ """
    template_name = 'workers/search.html'

    def get_context_data(self, *args, **kwargs):
        context = super(). get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q', None)
        if query is not None:
            return Worker.objects.search(query)
        return Worker.objects.features()


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    """ Create an Employee Update View at /employee/<id>/update/ """
    model = Worker
    fields = ['department', 'username',
              'position', 'hire_date', 'salary', 'image']
    template_name = 'workers/employee_update_form.html'
    login_url = 'login'

    def form_valid(self, form):
        return super().form_valid(form)


""" Create a Delete Employee at /employee/<id>/delete/ """


@login_required(login_url='login')
def deleteEmployee(request, pk):
    if request.method == 'POST':
        Worker.objects.filter(id=pk).delete()
        return redirect('all-employee')
