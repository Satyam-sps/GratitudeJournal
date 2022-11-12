from .models import GratitudeJournal 
from django.forms import ModelForm
from django import forms


class GratitudeForm(ModelForm):
    journal_entry = forms.Textarea(attrs={'rows':4,'cols':15})
    images        = forms.ImageField()
    images.widget.attrs.update({'multiple':'multiple'})
    class Meta:
        model = GratitudeJournal
        fields = "__all__"
       

# class gratitudeAttach(ModelForm):
#     class Meta:
#         model = Attachment
#         fields = ['grat_attach_img']

# class lifelogAttach(ModelForm):
#     class Meta:
#         model = LifeLogJournal
#         fields = "__all__"