from django import template
from django.urls import reverse

register = template.Library()

common_urls = {
    "login": reverse("apps.usuario:login"),
    "register": reverse("apps.usuario:registro"),
    "confirm_logout": reverse("apps.usuario:confirm_logout"),
    "index": reverse("index"),
}


@register.simple_tag(takes_context=True)
def login_path(context):
    request = context.get("request")
    current_path = request.path
    if current_path not in list(common_urls.values()):
        return common_urls["login"] + f"?next={current_path}"
    return common_urls["login"]


@register.simple_tag(takes_context=True)
def register_path(context):
    request = context.get("request")
    current_path = request.path
    if current_path not in list(common_urls.values()):
        return common_urls["register"] + f"?next={current_path}"
    return common_urls["register"]


@register.simple_tag(takes_context=True)
def confirm_logout_path(context):
    request = context.get("request")

    current_path = request.path
    if current_path not in list(common_urls.values()):
        return common_urls["confirm_logout"] + f"?next={current_path}"
    return common_urls["confirm_logout"]
