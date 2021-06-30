from django.shortcuts import render, get_object_or_404
#from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from .models import Main
def main_show(request):
    pst_all = Main.objects.all()
    return render(request,
    'home/index.html',
    {'posts': pst_all})
