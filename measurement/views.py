from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, get_object_or_404
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def perform_create(self, serializer):
        sensor = get_object_or_404(Sensor, id=self.request.data.get('sensor'))
        return serializer.save(sensor=sensor)


class SensorView(ListCreateAPIView):
    def get_queryset(self):
        pk = self.kwargs.get('pk',None)
        if pk is None:
            self.serializer_class = SensorSerializer
            return Sensor.objects.all()
        else:
            self.serializer_class = SensorDetailSerializer
            return Sensor.objects.filter(pk=pk)

    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        serializer = SensorSerializer(Sensor.objects.all().get(pk=pk), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
