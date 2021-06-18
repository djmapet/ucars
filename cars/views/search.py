from cars.models import Car, Manufacturer, CarModel
from django.http import HttpResponse, Http404
from django.shortcuts import render


def search(request,car_id):
    #try:
        #search_car = car.carmodel.get(pk=request.POST['car'])
    #except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        #return render(request, 'cars/search.html', {
            #'car': car,
            #'error_message': "You didn't select a car.",
        #})
    #else:
        #selected_ca.color += 6
        #selected_ca.gear += 3
        #selected_ca.drive += 6
        #selected_ca.body_type += 7
        #selected_ca.plate_category += 5
        #selected_car.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return render(request, 'search.html')
