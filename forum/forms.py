from django import forms

from forum.models import Message


class MessageForm(forms.Form):

    text = forms.CharField(label='', widget=forms.Textarea(
        attrs={'placeholder': 'Здесь вы можете высказать своё мнение по данной теме.', 'cols': 44, 'rows': 7, 'style': 'font-size: 20px;', })
    )
