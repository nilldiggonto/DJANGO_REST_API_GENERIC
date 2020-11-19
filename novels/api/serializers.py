from rest_framework import serializers
from novels.models import Novel,Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        # fields = '__all__'
        exclude = ('novel',)



class NovelSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many=True,read_only=True)
    class Meta:
        model = Novel
        fields = '__all__'
