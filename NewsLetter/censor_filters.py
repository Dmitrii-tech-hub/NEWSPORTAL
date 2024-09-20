from django import template
import re

register = template.Library()

# List of words to censor
CENSORED_WORDS = ['редиска']

@register.filter(name='censor')
def censor(value):
    if not isinstance(value, str):
        raise ValueError("Censor filter can only be applied to strings")

    for word in CENSORED_WORDS:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        value = pattern.sub(lambda match: '*' * len(match.group()), value)

    return value
