from django.forms.widgets import ClearableFileInput, DateTimeBaseInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'matches/custom_widget_templates/custom_\
clearable_file_input.html'


# class DateTimeInput(DateTimeBaseInput):
#     input_type = 'date'
#     format_key = 'DATETIME_INPUT_FORMATS'
#     template_name = 'matches/custom_widget_templates/custom_datetime.html'
