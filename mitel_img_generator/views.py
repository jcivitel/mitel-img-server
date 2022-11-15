import io

from PIL import Image
from django.http import HttpResponse

from .models import *


def get_image(request, customer, phonemodel):
    my_customer = Customer.objects.get(customer_tag=customer)
    my_phonemodel = PhoneModel.objects.get(phone_model=phonemodel)
    renderd_img = Image.new(mode="RGBA", size=(my_phonemodel.size_x, my_phonemodel.size_y), color=(255, 255, 255))
    cus_img = Image.open(my_customer.customer_logo)
    cus_img = cus_img.resize((70, 50))
    renderd_img.paste(cus_img, (my_phonemodel.pos_x, my_phonemodel.pos_y))
    output = io.BytesIO()
    renderd_img.save(output, format='PNG')
    return HttpResponse(output.getvalue(), content_type="image/png")
