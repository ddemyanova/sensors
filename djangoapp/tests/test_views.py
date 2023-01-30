
from django.urls import reverse
from django.test import TestCase
from djangoapp.models import Temperature, Humidity, Pressure


class ViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        numOfvalues = 10
        for x in range(numOfvalues):
            Temperature.objects.create(temperature=30)
            Humidity.objects.create(humidity=70.0)
            Pressure.objects.create(pressure=700.0)

    def postAndUpdate(self, name, value):
        post = self.client.post(f'/api/{name}/', {name: value})
        self.assertEqual(post.status_code, 201)
        get = self.client.get('/measurements/')
        self.assertEqual(get.status_code, 200)
        return get

    def test_TemplateForMeasuremens(self):
        get = self.client.get("/measurements/")
        self.assertTemplateUsed(get, 'measurement_list.html')
        getByName = self.client.get(reverse('measurements-list'))
        self.assertTemplateUsed(getByName, 'measurement_list.html')

    def test_WithData(self):
        get = self.client.get(reverse('measurements-list'))
        self.assertEqual(get.status_code, 200)
        self.assertEqual(len(get.context['humidity']), 10)
        self.assertEqual(len(get.context['temperature']), 10)
        self.assertEqual(len(get.context['pressure']), 10)

    def test_AddTemperatureSuccessfully(self):
        name = 'temperature'
        get = self.postAndUpdate(name, 80)
        self.assertEqual(len(get.context[name]), 11)

    def test_AddHumiditySuccessfully(self):
        name = 'humidity'
        get = self.postAndUpdate(name, 80.0)
        self.assertEqual(len(get.context[name]), 11)

    def test_AddPressureSuccessfully(self):
        name = 'pressure'
        get = self.postAndUpdate(name, 800.0)
        self.assertEqual(len(get.context[name]), 11)

    def test_AddingFailed(self):
        post = self.client.post(f'/api/temperature/', {'errorname': 10})
        self.assertEqual(post.status_code, 400)
