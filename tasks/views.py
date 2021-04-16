from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, FormView
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.core.exceptions import ValidationError
from django.contrib import messages
import datetime
from django.utils import timezone
from django.contrib.messages.views import SuccessMessageMixin

class HomeView(LoginRequiredMixin, ListView, FormView):
    model = Task
    template_name = 'tasks/home.html'
    context_object_name = 'tasks'
    ordering = ['-dateTimeOfCreation']

    form_class = TaskFilterForm

    def get_context_data(self, *args, **kwargs):
        # edits add now key to context as current datetime for comparisions on home screen
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['now'] = datetime.datetime.now()
        return context

    def get_queryset(self):
        # get the queryset for dasboard | normal + filtered
        self.form = TaskFilterForm(self.request.GET)
        queryset = Task.objects.filter(user = self.request.user)
        if self.form.is_valid():
            # filtering queryset acc to dates
            start_date = self.form.data['start_date']
            end_date = self.form.data['end_date']
            print(start_date, end_date)
            if start_date > end_date:
                messages.error(self.request, 'Date ranges are not correct')
            if start_date and end_date: queryset = queryset.filter(dateTimeOfCreation__date__range = (start_date, end_date))
        return queryset

class AddTask(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'tasks/create_task.html'
    # model = Task
    # fields = ['name', 'project', 'start_time', 'end_time', ]
    form_class = AddTaskForm
    success_url = '/'
    success_message = 'New Task Added'

    def get_context_data(self, **kwargs):
        # update context with project queryset for default field so that user get ot see only his/her project only
        context = super(AddTask, self).get_context_data(**kwargs)
        context['form'].fields['project'].queryset = Project.objects.filter(user = self.request.user)
        return context

    def form_valid(self, form):
        # attaching current logged in user to new task
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        if self.object.is_task_started:
            self.object.date_time_of_task_starting = timezone.now()
        return super().form_valid(form)

class UpdateTask(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'tasks/create_task.html'
    # model = Task
    # fields = ['name', 'project', 'start_time', 'end_time', ]
    form_class = AddTaskForm
    success_url = '/'
    success_message = 'Task Updated'

    def get_object(self, **kwargs):
        # get task object to update
        print('task',Task.objects.get(id = self.kwargs['pk']).date_time_of_task_ending)
        return Task.objects.get(id = self.kwargs['pk'])

    def form_valid(self, form):
        # logic bfore saving form
        print(form.cleaned_data)
        is_task_started = form.cleaned_data['is_task_started']
        if not is_task_started: #condition for ending the task
            # if is_task_started checkbox is off then store the task ending time as current time
            self.object.date_time_of_task_ending = timezone.now()
            form.cleaned_data = self.object.date_time_of_task_starting = timezone.now()
            print('dte',self.object.date_time_of_task_ending)
        else:
            self.object.date_time_of_task_starting = timezone.now()
        return super().form_valid(form)


