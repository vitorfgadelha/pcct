from rest_framework import viewsets, filters

from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    @action(detail=False)
    def generate_barcode(*args, **kwargs):
        #INSERIR AQUI O CÓDIGO PARA GERAR OS CÓDIGOS DE BARRAS DOS ALUNOS
        return Response("Código Gerado")

    @action(detail=False)
    def read_barcode(*args, **kwargs):
        bar_code = 1 #INSERIR AQUI O CÓDIGO PARA LEITURA DO CÓDIGO DE BARRAS
        student_query = Student.objects.filter(registration = bar_code)
        return Response(student_query[0].name)