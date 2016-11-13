from django.shortcuts import render
from v_excel_inventory.people.models import Customer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


def index(request):
    return render(request, 'index.html')

class CustomerList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'customer_list.html'

    def get(self, request):
        queryset = Customer.objects.all()
        return Response({'customers': queryset})
