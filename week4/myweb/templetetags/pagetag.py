from django import template

register = template.Library

@register.filter
def mytag(val):
    """
    自定义过滤器
    :param val:
    :return:
    """

    return val.upper()

@register.simple_tag
def tagjoin(val):
    """
    自定义标签
    :param val:
    :return:
    """

    return val.upper()