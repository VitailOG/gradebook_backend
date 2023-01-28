from rest_framework import serializers, viewsets

from methodist.models import Department, Permission


class DS(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"


class DV(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DS


class PS(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = "__all__"


class PV(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PS
