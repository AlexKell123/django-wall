from django.shortcuts import render


def main_page(request):
    return render(request, 'wall/index.html')
