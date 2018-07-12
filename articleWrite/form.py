from django import forms


class article(forms.Form):
    title = forms.CharField(
        label='Title',
        max_length=50,
        required=True,
        error_messages={'required':u'标题不可为空', 'max_length':u'长度必须小于50个字符'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u'请输入标题',
                'class':u'form-control'
            }
        )
    )
    content = forms.CharField(
        label='Content',
        required=True,
        error_messages={'required':u'内容不可为空'},
        widget=forms.Textarea(
            attrs={
                'placeholder':u'请输入内容',
                'class':'form-control'
            }
        )
    )
