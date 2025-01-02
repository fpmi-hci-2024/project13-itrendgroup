from news.utils import menu_header

def get_news_context(request):
    return {'mainmenu':menu_header}