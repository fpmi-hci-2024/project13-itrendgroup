
menu_header = [
                {'title': 'О сайте', 'url_name': 'about'},
                {'title':'Предложить новость','url_name': 'addpost'},
                {'title':'Обратная связь','url_name': 'contact'},
                ]

class DataMixin:
    title_page = None
    extra_context = {}
    paginate_by = 5
    
    def get_mixin_context(self, context, **kwargs):
        context.update(kwargs)
        return context

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

        


