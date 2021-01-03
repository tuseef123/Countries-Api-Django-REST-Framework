from rest_framework import serializers
from countries.models import Countries


class CountriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Countries
        #after countries remove the , to make it working perfectly
        fields = ('id','name','capital')