from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.getlist('sort')
    if 'name' in sort:
        phones = Phone.objects.all().order_by(*sort)
        return render(request, template, {'phones': phones})
    if 'min_price' in sort:
        phones = Phone.objects.all().order_by('price')
        return render(request, template, {'phones': phones})
    if 'max_price' in sort:
        phones = Phone.objects.all().order_by('-price')
        return render(request, template, {'phones': phones})

    phones = Phone.objects.all()
    return render(request, template, {'phones': phones})



def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {
        'phone_record': phone,
        'name': phone.name,
        'image': phone.image,
        'price': phone.price,
        'release_date': phone.release_date,
        'slug': phone.slug,
    }
    return render(request, template, {'phone': context})
