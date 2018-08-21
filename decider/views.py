from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .fuzzifier import *

class DeciderView(generics.ListCreateAPIView):

	permission_classes = (AllowAny,)
	
	def get(self, request, format=None):
		return Response('API DIABETES IA', status=status.HTTP_200_OK)

	def post(self, request, format=None):
		resposta = fuzzifier(request.data['nota_qualidade'], request.data['nota_servico'])
		return Response(resposta, status=status.HTTP_200_OK)
