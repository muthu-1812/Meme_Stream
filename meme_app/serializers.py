from rest_framework import serializers

from .models import Meme

MEME_READ_ONLY_FIELDS = ('id',)


#SERIALIZER FOR ALL THE FIELDS FOR GET AND POST REQUESTS
class MemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meme
        fields= ['id','name','url','caption']
        read_only_fields = MEME_READ_ONLY_FIELDS 

    
#SERIALIZER USED FOR THE PATCH UPDATE REQUEST
class MemeUpdateSerializer(MemeSerializer):

    class Meta(MemeSerializer.Meta):
        read_only_fields = MEME_READ_ONLY_FIELDS + ('name',)  #TO MAKE SURE THE AUTHOR NAME CAN'T BE MODIFIED