from django.conf import settings
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from dajaxexamples.utils import render_response


def multiply(request):
    return render_response(request, 'examples/multiply_example.html')


def maps(request):
    return render_response(request, 'examples/google_map_example_page.html',
                            {'GOOGLE_API_KEY': settings.GOOGLE_API_KEY})


def random_example(request):
    return render_response(request, 'examples/random_example.html')


def form_example(request):
    return render_response(request, 'examples/form_example.html')


def get_pagination_page(page=1):
    items = range(0, 100)
    paginator = Paginator(items, 10)
    try:
        page = int(page)
    except ValueError:
        page = 1

    try:
        items = paginator.page(page)
    except (EmptyPage, InvalidPage):
        items = paginator.page(paginator.num_pages)

    return items


def pagination_example(request):
    items = get_pagination_page(1)
    return render_response(request, 'examples/pagination_example.html',
                           {'items': items})


def index(request):
    return render_response(request, 'examples/index.html')


def full_form_example(request):
    from forms import ExampleForm
    example_form = ExampleForm()
    return render_response(request, 'examples/full_form_example.html',
                           {'form': example_form})


def flickr_example(request):
    return render_response(request, 'examples/flickr_example.html')
