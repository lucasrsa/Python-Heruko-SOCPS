from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

# Create your views here.
def index(request):

    #data_atual = date.today()
    #return HttpResponse(data_atual)
    return render(request, "index.html")

def page2(request):

    return render(request, "page2.html")

def page3(request):

    html = '''
    <html>
        <head><title>Página 3</title></head>
        <body>
            <h1>Python no Heroku - SOCPS</h1>
            <h2>Página 3</h2>
            <a href="../">index</a><br>
            <a href="../page5/">page5</a>
        </body>
    </html>
    '''
    return HttpResponse(html)

def page4(request):

    return render(request, "page4.html")

def page5(request):
    now = datetime.now().strftime('%H:%M %d/%m/%Y')
    html = f'''
    <html>
        <head><title>Página 5</title></head>
        <body>
            <h1>Python no Heroku - SOCPS</h1>
            <h2>Página 5</h2>
            <p>Agora: {now}</p>
            <a href="../page3/">page3 (dinâmica)</a><br>
            <a href="../page4/">page4 (estática)</a>
        </body>
    </html>
    '''
    return HttpResponse(html)

