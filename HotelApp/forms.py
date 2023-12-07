from django import forms
from .models import Hotel

class HotelForm(forms.ModelForm):
    domain = forms.CharField(max_length=100, help_text="Enter the domain for the tenant")

    class Meta:
        model = Hotel
        fields = ['schema_name', 'name', 'address', 'phone_number', 'description', 'stars', 'email', 'name2', 'primary_color', 'secondary_color']

    def __init__(self, *args, **kwargs):
        super(HotelForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
