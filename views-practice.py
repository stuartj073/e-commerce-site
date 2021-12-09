def adjust_bag(request, item_id):

    quantity = request.POST.get('quantity')
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size: 
        if quantity > 0:
            bag[item_id]['items_by_id'][size] = quantity
        else:
            del bag[item_id]['items_by_id'][size]
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = session.request.get('bag', {})

    if size:
        del bag[item_id]['items_by_size'][size]
        if not bag[item_id]['items_by_size']:
            bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)
    request.session['bag'] = bag
    return rediret(reverse('view_bag'))
