from django import template


register = template.Library()


@register.filter()
def multiply(value, arg):
    return float(value) * arg


@register.filter()
def money_format(value, arg):
    return f"{value}{arg}"

@register.simple_tag
def total_amount(request):
    total_productos = 0
    
    for key, value in request.session['cart'].items():
        total_productos = total_productos + (float(value['precio']) * value['cantidad'])
        return {'cart_total_productos_amount': total_productos}