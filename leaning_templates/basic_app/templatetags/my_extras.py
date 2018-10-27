from django import template

# Get the template tag from Django Library
register = template.Library()

# Using django decorator to register template tag also can do
@register.filter(name='cut_out')
def cut_out(value, arg):
    """
    This cuts out all values of 'arg' from the string
    """
    return value.replace(arg,'')

# Register the new created template tag to Library
# The string 'cut_out' meaning the tag when we call template tag in HTML file
# register.filter('cut_out', cut_out)
