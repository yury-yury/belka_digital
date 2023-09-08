from django.db.models import Min, Max, Avg
from django.utils import timezone
from rest_framework import request
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import OreSample
from main.serializers import OreSampleCreateSerializer, OreSampleSerializer


class OreSampleCreateView(CreateAPIView):
    serializer_class = OreSampleCreateSerializer

    def perform_create(self, serializer) -> None:
        """
        The perform_create function overrides the parent class method.
        Sets the value of the creator field.
        """
        serializer.save(creator=self.request.user)


class OreSampleStatsView(APIView):
    serializer_class = OreSampleSerializer

    def get(self, request):
        queryset = OreSample.objects.all()

        year = request.query_params.get('year', None)
        month = request.query_params.get('month', None)

        if year is None:
            year = timezone.datetime.now().year
        if month is None:
            month = timezone.datetime.now().month

        start_date = timezone.datetime(int(year), int(month), 1, tzinfo=timezone.utc)
        if int(month) < 12:
            end_date = timezone.datetime(int(year), int(month) + 1, 1, tzinfo=timezone.utc)
        else:
            end_date = timezone.datetime(int(year) + 1, int(month) - 11, 1, tzinfo=timezone.utc)
        end_date = end_date - timezone.timedelta(days=1)

        queryset = queryset.filter(created__gte=start_date, created__lte=end_date)

        if queryset:
            min_values = {
                field: queryset.aggregate(Min(field))['{}__min'.format(field)]
                for field in ["iron_content", "silicon_content", "aluminum_content", "calcium_content","sulfur_content"]
            }

            max_values = {
                field: queryset.aggregate(Max(field))['{}__max'.format(field)]
                for field in ["iron_content", "silicon_content", "aluminum_content", "calcium_content","sulfur_content"]
            }

            avg_values = {
                field: queryset.aggregate(Avg(field))['{}__avg'.format(field)]
                for field in ["iron_content", "silicon_content", "aluminum_content", "calcium_content","sulfur_content"]
            }
        else:
            raise ValidationError(f"No data available for the period {month} months {year}.")

        return Response({
            'period': f'{month}. {year}',
            'min': min_values,
            'max': max_values,
            'avg': avg_values
        })
