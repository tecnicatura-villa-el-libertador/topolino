import re
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from tareas.models import Tarea

register = template.Library()
patron = re.compile('#(\d+)')

@register.filter
@stringfilter
def template_filter(texto):

    result = re.findall(patron,texto)
    for match in result:
        try:
            tarea_valida = Tarea.objects.get(id = match)

        except Tarea.DoesNotExist:
            tarea_valida = None

        if tarea_valida:
            link = "<a href='/tareas/" + match + "/'>#" + match + "</a>"
            if tarea_valida.esta_finalizado:
                link = "<del>"+ link + "</del>"
            else:
                link = link
            texto = texto.replace('#' + match, link)
    return mark_safe(texto)
