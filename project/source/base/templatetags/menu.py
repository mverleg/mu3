
from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag(name = 'conditional_active_class', takes_context = True)
def conditional_active_class(context, url_name):
    if 'request' in context:
        url = reverse(url_name)
        if context['request'].path == url:
            return u'menu_active'


