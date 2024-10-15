from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer
from django.shortcuts import get_object_or_404

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def list(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            person = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        person = get_object_or_404(Person, pk=pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    def update(self, request, pk=None, partial=False):
        person = get_object_or_404(Person, pk=pk)
        serializer = PersonSerializer(person, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        person = get_object_or_404(Person, pk=pk)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


