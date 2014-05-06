
from django.utils.html import escape, mark_safe
from django import template

register = template.Library()


'''
    obfuscate a single letter; not cryptographically strong
    but simple and should be good enough to stop some spam bots  
'''
def obfuscate_letter(letter, pos, mi, ma):
    nr = ord(letter)
    if mi <= nr <= ma:
        return chr((nr - mi + pos ** 2) % (ma - mi) + mi)
    return letter

''' the inverse is not actually used in python, just js version '''
def deobfuscate_letter(letter, pos, mi, ma):
    nr = ord(letter)
    if mi <= nr <= ma:
        return chr((nr - mi - pos ** 2) % (ma - mi) + mi)
    return letter

''' 
    obfuscate text (probably email) with javascript
    (40 chosen to exclude &)
'''
@register.filter(name='obfuscate')
def obfuscate(clear, mi = 32, ma = 126):
    ''' the obfuscation '''
    cypher = ''.join(obfuscate_letter(letter, pos, mi, ma) for pos, letter in enumerate(escape(clear)))
    print 'decyphered:', ''.join(deobfuscate_letter(letter, pos, mi, ma) for pos, letter in enumerate(escape(cypher)))
    ''' wrap it to mark for deobfuscating '''
    span = '<span class=\'obfuscated\' title=\'this text was obfuscated to hide it from spammers; please enable javascript to see it\'>[enable JS]<span style="display: none;">%s</span></span>' % cypher
    return mark_safe(span)


