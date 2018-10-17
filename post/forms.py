from django import forms
form django-google-maps import map_fields

class createPostForm(forms.PostForm):
    title = forms.CharField(max_length=100)
    location = map_fields.AddressField:
                {'widget': map_widgets.GoogleMapsAddressWidget}
    hours = forms.IntegerField()
    
