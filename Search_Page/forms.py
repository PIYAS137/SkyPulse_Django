from django.forms import ModelForm
from .models import CityName

class GetCityData(ModelForm):
    class Meta:
        model = CityName
        fields = '__all__'