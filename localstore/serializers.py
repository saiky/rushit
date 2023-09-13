from rest_framework import serializers
from localstore.models import Country, State, Company

class CountrySerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(max_length=200)
	code = serializers.CharField(max_length=3)
	time_zone = serializers.CharField(max_length=20)
	isd_code = serializers.IntegerField()

	class Meta:
		model = Country
		fields = [id, name, code, time_zone, isd_code]

	def create(self, validated_data):
		return Country.objects.create(**validated_data)

	def update(self, instance, validated_date):
		instance.name = validated_data.get('name', instance.name)
		instance.code = validated_data.get('code', instance.code)
		instance.time_zone = validated_data.get('time_zone', instance.time_zone)
		instance.isd_code = validated_data.get('isd_code', instance.isd_code)
		instance.save()
		return instance

