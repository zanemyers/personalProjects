from django.forms import ModelForm
from .models import LearningProject


class LearningProjectForm(ModelForm):
    class Meta:
        model = LearningProject
        fields = '__all__'
        exclude = ['vote_total', 'vote_ratio']

    def __init__(self, *args, **kwargs):
        super(LearningProjectForm, self).__init__(*args, **kwargs)

        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'input', 'placeholder': value.label})

        # this is the same as the above for loop
        # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Title'})


