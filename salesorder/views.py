from django.shortcuts import render
from django.http import HttpResponse

from .models import Order

# Create your views here.
def index(request):

    context = {
        'column_name': [field.name for field in Order._meta.get_fields() if field.concrete],
        'all_data': list(Order.objects.all().values_list()),
    }
    return render(request, 'salesorder/child.html', context)