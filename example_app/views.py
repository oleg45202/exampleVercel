from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Zeit Now!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)