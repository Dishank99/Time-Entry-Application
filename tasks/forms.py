from django.forms import ModelForm
from .models import Task
from django import forms
from .models import *
from datetime import date, time

class AddTaskForm(ModelForm):
    start_time = forms.TimeField(
        widget=forms.TimeInput(attrs={ 'type':'time'}),
        initial = time.min
    )
    end_time = forms.TimeField(
        widget=forms.TimeInput(attrs={ 'type':'time'}),
        initial = time.max
    )
    is_task_started = forms.BooleanField(label='Do you want to start the task', required=False)

    class Meta:
        model = Task
        fields = '__all__'
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(AddTaskForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})
        self.fields['date_time_of_task_starting'].widget.attrs.update({'disabled':True})
        self.fields['date_time_of_task_ending'].widget.attrs.update({'disabled':True})
        self.fields['is_task_started'].widget.attrs.update({'class':'form-check-input'})

        

class TaskFilterForm(forms.Form):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        initial = date.today()
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        initial = date.today()
    )