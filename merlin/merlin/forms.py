from django import forms

class LearnPlatformVoiceInput(forms.Form):
    disable_interface_voice_input = forms.CharField(label='Number to Call', max_length=12)

class LearnPlatformSMSInput(forms.Form):
    disable_interface_sms_input = forms.CharField(label='Number to Text', max_length=12)