from django import template
import mistune

register = template.Library()


@register.filter
def markdown(value):
    markdown = mistune.Markdown()
    indented = "".join([f"    {x}" for x in value.splitlines(1)])
    return markdown(indented)
