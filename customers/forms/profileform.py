from django import forms

from customers.models import Customer


class CustomerProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Customer
        fields = ('profile_picture', 'address', 'city', 'country', 'name', 'email')



