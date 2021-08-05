from django.forms.widgets import ClearableFileInput, DateTimeInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'matches/custom_widget_templates/custom_\
clearable_file_input.html'


class CustomDateTimeInput(DateTimeInput):
    input_type = "datetime-local"
    template_name = 'matches/custom_widget_templates/custom_\
datetime.html'
