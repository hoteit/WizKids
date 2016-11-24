from django import template
from wizkids import settings
from quizes.models import UserPreferences
register= template.Library()

@register.simple_tag
def bootswatch(user_id):
    try:
        get_theme = UserPreferences.objects.get(user__pk=user_id)
        if get_theme:
            return settings.STATIC_URL+"/bower_components/bootswatch/"+get_theme.theme.theme_name+"/bootstrap.min.css"
        else:
            return settings.STATIC_URL+"/bower_components/bootswatch/cosmo/bootstrap.min.css"
    except:
        return settings.STATIC_URL+"/bower_components/bootswatch/cosmo/bootstrap.min.css"