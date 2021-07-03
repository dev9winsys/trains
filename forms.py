from dal import autocomplete
from django import forms
from .models import TrainLine

class TrainListForm(forms.ModelForm):
    city_form = forms.ModelChoiceField(
            queryset=TrainLine.objects.all(),
            widgets=autocomplete.ModelSelect2(url='linename_autocomplete')
        )
    class Meta:
        model = TrainLine
        fields = ('__all__')
