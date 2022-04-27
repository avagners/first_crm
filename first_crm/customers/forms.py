from django import forms

from .models import Customer

STATUS_CHOICES = (
    (True, 'Активный'),
    (False, 'Неактивный')
)


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('last_name', 'first_name', 'email', 'phone_number', 'status')
        widgets = {
            'status': forms.Select(choices=STATUS_CHOICES)
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'placeholder': field})


class UploadFileForm(forms.Form):
    file = forms.FileField()
