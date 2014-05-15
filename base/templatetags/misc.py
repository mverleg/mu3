
from django.utils.html import escape, mark_safe
from django import template
from mu3.base.functions.list_sample import list_sample
from mu3.base.functions.obfuscate import obfuscate_letter
from base.functions.html_filter import html_filter


register = template.Library()


''' 
	obfuscate text (probably email) with javascript
	(40 chosen to exclude &)
'''
@register.filter(name = 'obfuscate')
def obfuscate(clear, mi = 32, ma = 126):
	''' the obfuscation '''
	cypher = ''.join(obfuscate_letter(letter, pos, mi, ma) for pos, letter in enumerate(escape(clear)))
	''' wrap it to mark for deobfuscating '''
	span = '<span class=\'obfuscated\' title=\'this text was obfuscated to hide it from spammers; please enable javascript to see it\'>[enable JS]<span style="display: none;">%s</span></span>' % cypher
	return mark_safe(span)


''' 
	given an ordered collection (list, tuple, ...), return a string representation
	of the first limit items (or fewer), e.g. "itemA, itemB, itemC and 7 more"
'''
@register.filter(name = 'shortlisttxt')
def shortlisttxt(collection, limit = 3):
	return list_sample(collection, limit)


''' 
	apply a whitelist filter, which allows a limited selection of 
	secure HTML tags and attributes
'''
@register.filter(name = 'noscr')
def noscr(text):
	return mark_safe(html_filter(text))


