from django import forms
from .models import Post
#from django_google_maps import fields as map_fields
#from django_google_maps import widgets as map_widgets


class PostForm(forms.ModelForm):

    # location = map_fields.AddressField:
    #            {'widget': map_widgets.GoogleMapsAddressWidget}
    class Meta:
        model = Post
        fields = (
            'title',
            'location',
            'type',
            'estimate_hours',
            'work_date',
            'description',
            'company',
            'company_logo',
        )
        widgets = {
            # 'location' : GoogleStaticOverlayMapWidget,
        }
