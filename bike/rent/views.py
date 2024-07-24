from django.shortcuts import render, HttpResponse


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
