from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .fuzzifier import *

class TemplateView(TemplateView):
	template_name = "templates/index.html"


class DeciderView(generics.ListCreateAPIView):

	permission_classes = (AllowAny,)
	
	def get(self, request, format=None):
		return Response('API TIP CALCULATOR FUZZY', status=status.HTTP_200_OK)

	def post(self, request, format=None):

		if(request.data.get('nota_qualidade') and request.data.get('nota_servico')):
			resposta = fuzzifier(request.data['nota_qualidade'], request.data['nota_servico'])
			return Response(resposta, status=status.HTTP_200_OK)
		return Response("ERRO do JSON", status=status.HTTP_400_BAD_REQUEST)
