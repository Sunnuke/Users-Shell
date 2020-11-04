from django.shortcuts import render, HttpResponse
from .models import Users

# Create your views here.
def index(request):
    context = {
        'all_users': Users.objects.all()
    # Users.first_name
    # Users.last_name}
    # {{Users.email_address}}
    # {{Users.age}\
    }
    return render(request, 'index.html', context)


def process():
    pass