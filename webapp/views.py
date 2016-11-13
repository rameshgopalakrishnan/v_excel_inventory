from django.shortcuts import render
from people.models import Customer
from people.models import Service
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

class ServicesList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'services_list.html'

    def get(self, request):
        queryset = Service.objects.all()
        return Response({'services': queryset})
