# create my own fitlers for the templates

from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    # value is from the template
    """
    THIS cuts all values of 'arg' from the string!
    """
    return value.replacte(arg,'')

# what to call this filter second one is direct call to this function
# pass this filter in as a decorator
# register.filter('cut',cut)
