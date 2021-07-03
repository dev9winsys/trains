from .models import TrainLine, StationList
import json
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from pykakasi import kakasi

kakasi = kakasi()
kakasi.setMode('H', 'a')
kakasi.setMode('K', 'a')
kakasi.setMode('J', 'a')
conv = kakasi.getConverter()


class IndexView(ListView):
    template_name = 'trains/index.html'
    context_object_name = 'station_list'

    def get_queryset(self):
        q = self.request.GET.get('name')
        if q != None:
            return StationList.objects.filter(trainName__istartswith=q).order_by('stationNo')
        else:
            return None


def linename_autocomplete(request):
    q = request.GET.get('term')
    if q != None:
        lines = TrainLine.objects.filter(trainSearch__istartswith=conv.do(q))[:10]
        results = []
        for line in lines:
            line_json = {}
            line_json['id'] = line.trainName
            line_json['label'] = line.trainName
            line_json['value'] = line.trainName
            results.append(line_json)
        data = json.dumps(results)
    else:
        results = []
        data = json.dumps(results)
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
