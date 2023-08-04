from django.forms import ModelForm
from .models import Note


class noteForm(ModelForm):
    class Meta:
        model = Note
        fields = "__all__"
        exclude = ["user"]
