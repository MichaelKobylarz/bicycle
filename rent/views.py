import datetime
from django.shortcuts import render, HttpResponse
#from django.utildjangs.html import escape

# Create your views here.
def rent_view(request):
    return HttpResponse("rent rent")

def hi_view(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
        <head>
        </head>
        <body>
            <h2>Hello, world!</h2>
        </body>
    </html>
    """)

def hi2_view(request):
    return render(request, 'rent.html')

def jurek_view(request):
    return HttpResponse("Witaj, Jurek!")


def jacek_view(request):
    return HttpResponse("Witaj, Jacek!")


def ksawier_view(request):
    return HttpResponse("Witaj, Ksawier!")


# Podatność XSS - przykład
def name_view(request, name):
    # importy powinny być zawsze na samej górze
#from django.utils.html import escape

    # always remember to escape your output
    print(name)
    escaped_name = escape(name)
    print(escaped_name)

    return HttpResponse(f"Witaj, {name}!")


# kontekst szablonu
def name_view2(request, name):
    return render(
        request,
        'rent2.html',
        {"name": name}
    )

def collection_view(request):
    fruits = [
        'apple',
        'banana',
        'pinaple',
        'blueberry',
        'orange',
    ]



    return render(
        request,
        'collection.html',
        {'fruits': fruits}
    )