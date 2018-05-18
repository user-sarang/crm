from django import forms


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )


class CommentForm(forms.Form):
	text = forms.CharField(label='Your comment', max_length=100)




