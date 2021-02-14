from rest_framework import serializers
from .models import Meme 





MEME_READ_ONLY_FIELDS = ('id',)

class MemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meme
        fields= ['id','name','url','caption']
        read_only_fields = MEME_READ_ONLY_FIELDS 

    

class MemeUpdateSerializer(MemeSerializer):

    class Meta(MemeSerializer.Meta):
        read_only_fields = MEME_READ_ONLY_FIELDS + ('name',)  