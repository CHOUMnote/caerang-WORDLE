#from rest_framework.views import APIView
from django.http import HttpResponse
from django.views.generic import View

class IndexAPI(View):
    def get(self, request):
        return HttpResponse("ㅎㅇ")