from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MemeSerializer
from .models import Meme
# from .serializers import IdSerializer
from django.http import HttpResponse
from django.http.response import Http404
# from .serializers import MemeUpdateSerializer
from rest_framework import generics

from rest_framework import status
#need apiview
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from .serializers import MemeUpdateSerializer               #change to update serializer

from .forms import memesForm





# @api_view(['GET'])
# def Meme_overview(request):
#     api_urls={
#             'List':'/task-list/',
#             'Detail View':'task-detail/<str:pk>',
#             'Create':'/task-create/',
#             'Update':'/task-update/<str:pk>/',
#             'Delete':'/task-delete/<str:pk>/',
#     }
#     return Response(api_urls) 
#   #Response was JSONResponse


class MemeAPIView(generics.ListCreateAPIView):                                        # generics.ListCreateAPIView
    serializer_class = MemeSerializer                                  
    queryset = Meme.objects.all().order_by('-id')[:100]   





    def list(self, request):
        queryset = self.get_queryset()                                                       #display 100 memes
        serializer = MemeSerializer(queryset, many=True)                 
        return Response(serializer.data, status=status.HTTP_201_CREATED)



    def create(self, request):                                                              #post the meme
        serializer = MemeSerializer(data=request.data)  
        if serializer.is_valid():                       
            new_name=request.data['name']
            new_caption=request.data['caption']
            new_url=request.data['url']
            duplicate_meme=Meme.objects.filter(name=new_name,url=new_caption,caption=new_caption)



            if duplicate_meme.exists():
                return Response("Duplicate Values of Meme",status=status.HTTP_409_CONFLICT)  
            serializer.save()          
            validate = URLValidator() 
            value = serializer.data['url']  


            if value:                                                           
                try:
                    validate(value)
                except ValidationError:
                    return HttpResponse(status=status.HTTP_400_BAD_REQUEST)     

            a={"id":str(Meme.objects.last().id)}
            
            
            return Response(a, status=status.HTTP_201_CREATED)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 




class MemeUpdateAPIView(generics.RetrieveUpdateAPIView):            #ds
    serializer_class = MemeSerializer                                          
    queryset = Meme.objects.all()                                             

    lookup_field = 'id'                                                      
    
    # detailed view
    def retrieve(self, request, id=None):
        try:                                                       
            meme = Meme.objects.get(id=id)
        except Meme.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)  

        serializer = MemeSerializer(meme)                           
        return Response(serializer.data)                        
    
    
    # UPDATE  patch
    def patch(self, request, id):
        try:                                                        
            meme = Meme.objects.get(id=id)                          
        except Meme.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)     
       
        serializer = MemeUpdateSerializer(meme, data=request.data)  
                                                                    
    
        if serializer.is_valid():                                 
            serializer.save()
            return Response(serializer.data)                        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
     
    
    def delete(self,request,id):
        try:                                                        #delete meme
            meme = Meme.objects.get(id=id)
        except Meme.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)   
        meme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  





# memes list 
def memes_List(request):
    context = {'memes_List' : Meme.objects.all().order_by('-id') }
    return render(request, "meme_app/memes_List.html",context)

# memes forms
def memes_form(request, id=0):
    try:
        if request.method == 'GET':
            if id==0:
                form = memesForm()
            else:
                meme = Meme.objects.get(pk=id)
                form = memesForm(instance=meme)    
            return render(request, "meme_app/memes_form.html", {'form': form})
        else:
            if id == 0:
                form = memesForm(request.POST)
            else:
                meme = Meme.objects.get(pk=id)
                form = memesForm(request.POST,instance=meme)
            if form.is_valid():
                form.save()
            return redirect('/memes-list')
    except Meme.DoesNotExist:
        raise Http404('Page not found')

# memes delete options
def memes_delete(request, id):
    meme = Meme.objects.get(pk=id)
    meme.delete()
    return redirect('/memes-list/')

# memes json for particular id
def memes_json(request, id):
    context = {
        'meme_list': Meme.objects.filter(pk=id),
    }
    return render(request, "meme_app/memes_json.html", context)