from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """ View to see bag page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the bag """
    product = Product.objects.get(pk=item_id)
    quantity = request.POST.get('quantity')
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if bag[item_id]['items_by_sizes'].keys():
                bag[item_id]['items_by_sizes'] += quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
            else:
                bag[item_id]['items_by_sizes'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
        else:
            bag[item_id] = {'items_by_sizes': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to bag')
    
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Add a quantity of the specified product to the bag """

    quantity = request.POST.get('quantity')
    size = None
    
    if 'product_size' in request.POST:
        size = request.POST['size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Removed {size.upper()} {product.name} from your bag')
        else:
            del bag[item_id]['items_by_size'][size]
    
    else:
        if quantity > 0:
            bag[item_id] = quantity 
            messages.success(request, f'Added size {product.name} to your bag')

        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """ Add a quantity of the specified product to the bag """

    try:
        size = None
        
        if 'product_size' in request.POST:
            size = request.POST['size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
        
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
