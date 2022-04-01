from Storage.models import *

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        themes = Themes.objects.all()
        context['themes'] = themes
        return context
