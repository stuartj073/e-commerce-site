def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item, item_data in bag.items():
        if ininstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += quantity
            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
            })
        else:
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context {
        bag_items'
        total 
        product_count
        free
    }


def add_to_bag(request):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None

    if 'product_size' in request.POST:
        size = request.POST['size']
    bag = request.session.get('bag', {})
    
    if size:
        if bag[item_id] in list(bag.keys()):
            if bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if bag[item_id] in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantitu


def remove_from_bag(request, item_id):
    size = None
    try:
        if 'product_size' in request.POST:
            size = request.POST.get('size')
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_sizes'][size]
            if not bag[item_id]['items_by_sizes']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)
        
        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
    
