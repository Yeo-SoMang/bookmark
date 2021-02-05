from django import forms
from .models import Bookmark

class BookmarkForm(forms.ModelForm):
    #라벨을 같이 만들어줌
    site_name = forms.CharField(label='사이트명')
    url = forms.CharField(label='주소')

    class Meta:
        model = Bookmark
        fields = '__all__'