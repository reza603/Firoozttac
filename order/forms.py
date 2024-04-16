from django import forms
from order.models import tblOrder,Document
from django.core.validators import FileExtensionValidator
class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ('File_addr',)





class UploadFileForm(forms.Form):
  title = forms.CharField(max_length=50)
  file = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['xml'])])
