from .models import Key
from django import forms




class ImagePurchasedForm(forms.ModelForm):
    class Meta:
        model = Key
        fields = ('img_confirm_purchased',)


    # def __init__(self, id, *args, **kwargs):
    #     super(ImageForm, self).__init__(*args, **kwargs)
    #     self.fields['user'].queryset = User.objects.get(id=id)