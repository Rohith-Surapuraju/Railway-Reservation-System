from django.forms import ModelForm
from .models import person
from django.contrib.auth.models import User

class PersonForm(ModelForm):
    class Meta:
        model = person
        fields = '__all__'
        exclude = ['user', 'date_and_time_of_booking', 'train','email']

