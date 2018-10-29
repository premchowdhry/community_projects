from django import forms
from .models import Post
#from django-google-maps import map_fields

class PostForm(forms.ModelForm):
    #location = map_fields.AddressField:
    #            {'widget': map_widgets.GoogleMapsAddressWidget}
    class Meta:
        model = Post
        fields = (
                    'title',
                    'location',
                    'estimate_hours',
                    'work_date',
                    'description',
                    'company',
                    'company_logo',
                )
