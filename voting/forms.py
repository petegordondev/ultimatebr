from django import forms
from .models import Poll, VotingItem, Subject  # Updated import

class PollForm(forms.ModelForm):  # Renamed from VotingPanelForm
    subjects = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Poll  # Updated model reference
        fields = ['title', 'start_date', 'end_date', 'subjects']

    def save(self, commit=True):
        panel = super().save(commit=False)
        if commit:
            panel.save()
            # Create VotingItem for each selected subject
            subjects = self.cleaned_data['subjects']
            for subject in subjects:
                VotingItem.objects.create(panel=panel, subject=subject)
        return panel
