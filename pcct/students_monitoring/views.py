from rest_framework import viewsets, filters

from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

from PIL import Image, ImageDraw, ImageFont
import barcode
from barcode import Code39
from barcode.writer import ImageWriter

media_path = "students_monitoring/media/"
class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    @action(detail=False)
    def generate_barcode(*args, **kwargs):
        students = Student.objects.all().order_by('id')
        for student in students:
            barcode = Code39(student.registration, writer=ImageWriter(), add_checksum=False)
            barcode_img = barcode.render()
            barcode_img.save(media_path + student.name + ".png")
        return Response("FOI")

    @action(detail=False)
    def read_barcode(*args, **kwargs):
        bar_code = 1 #INSERIR AQUI O CÓDIGO PARA LEITURA DO CÓDIGO DE BARRAS
        student_query = Student.objects.filter(registration = bar_code)
        return Response(student_query[0].name)