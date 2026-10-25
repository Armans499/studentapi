from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Student
from .serializers import studentSerializer

@api_view(['GET','POST'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = studentSerializer(students,many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = studentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            ) 
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['PUT'])
def student_detail(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(
            {"error":"Student not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    serializer = studentSerializer(student,data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(
        serializer.errors,
        status=status.HTTP_404_BAD_REQUEST
    )

@api_view(['DELETE'])
def student_delete(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(
            {"Error":"Student Not Found"},
            status=status.HTTP_404_NOT_FOUND
        )
    student.delete()
    return Response(
        {"Message":"Student Deleted Successfully"},
        status=status.HTTP_200_OK
    )

