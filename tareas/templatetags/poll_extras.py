import re
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
@stringfilter
def template_filter(tarea):
	result = re.sub('(#(\d+))',"<a href='/tareas/" + "\\2" + "/'>" + "\\1" + "</a>", tarea)
	return mark_safe(result)
