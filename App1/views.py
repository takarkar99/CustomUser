# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Product
# from django.shortcuts import get_object_or_404


# def test_view(request, product_id):
#     obj = get_object_or_404(Product, product_id=product_id)
#     name = 'car'
#     obj.product_name = name
#     return HttpResponse('update value {}'.format(obj.product_name))



# def quantities_view (request):

#     quantity = request.GET.get('quantity_view')

#     try:
#         quantity = int(quantity)


#     except (ValueError, TypeError):
#         return HttpResponse("specifies the quantity")
    

#     if quantity:
#             a = Product.product_value_limit(int(quantity))
#             return HttpResponse(f'product quantity {a}',a)

#     return HttpResponse(quantity)