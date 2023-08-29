# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response

class SensorListView(ListCreateAPIView):
    pass


class MeasurementUpdateView(RetrieveUpdateAPIView):
    pass


class SensorCreateAPIView(CreateAPIView):
    pass
