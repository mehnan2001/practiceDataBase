from django.forms import ModelForm
from blog.models import ContactUs


class ContactForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'


