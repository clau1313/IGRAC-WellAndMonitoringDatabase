from django import template
from django.forms.models import model_to_dict
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def render_label(field):
    label = field.label
    if field.field.required:
        return f'<b>{label}*</b>'
    else:
        return label


@register.simple_tag
def field_as_row(field, unit=''):
    help_text = ''
    if field.help_text:
        help_text = '<i class="fa fa-question-circle-o" aria-hidden="true" data-toggle="tooltip" title="{}">'.format(
            field.help_text)
    return mark_safe(
        '<tr>'
        '   <td>{label} {help_text}</i></td>'
        '   <td>'
        '       <div class="input">{input} {unit}</div>'
        '   </td>'
        '</tr>'.format(
            help_text=help_text,
            label=render_label(field),
            input=field,
            unit=unit
        ))
