from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from gwml2.authentication import GWMLTokenAthentication
from gwml2.serializer.well.minimized_well import WellMeasurementMinimizedSerializer
from gwml2.mixin import EditWellFormMixin
from gwml2.models.well import Well
from gwml2.views.form_group.form_group import FormNotValid
from gwml2.views.groundwater_form import WellEditing


class WellEditAPI(WellEditing, APIView, EditWellFormMixin):
    authentication_classes = [SessionAuthentication, BasicAuthentication, GWMLTokenAthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, id, *args, **kwargs):
        data = request.data.copy()
        well = get_object_or_404(Well, id=id)

        try:
            self.edit_well(well, data, self.request.FILES, request.user)
            return JsonResponse({
                'level_measurement': WellMeasurementMinimizedSerializer(
                    [form.instance for form in self.level_measurement.measurements], many=True).data,
                'quality_measurement': WellMeasurementMinimizedSerializer(
                    [form.instance for form in self.quality_measurement.measurements], many=True).data,
                'yield_measurement': WellMeasurementMinimizedSerializer(
                    [form.instance for form in self.yield_measurement.measurements], many=True).data
            })

        except KeyError as e:
            return HttpResponseBadRequest('{} is needed'.format(e))
        except (ValueError, FormNotValid, Exception) as e:
            return HttpResponseBadRequest('{}'.format(e))
