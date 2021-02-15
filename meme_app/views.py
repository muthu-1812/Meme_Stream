from django.core.exceptions import ValidationError
#need apiview
from django.core.validators import URLValidator
from django.http import HttpResponse, JsonResponse
from django.http.response import Http404
from django.shortcuts import redirect, render
from rest_framework import generics, serializers, status
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .forms import memesForm
from .models import Meme
from .serializers import MemeUpdateSerializer  # change to update serializer
from .serializers import MemeSerializer

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



#CLASS BASED VIEWS FOR GET AND POST REQUESTS
class MemeAPIView(generics.ListCreateAPIView):                                        # generics.ListCreateAPIView
    serializer_class = MemeSerializer                                  
    queryset = Meme.objects.all().order_by('-id')[:100]   #TO GET THE LATEST 100 MEMES IN DESCENDING ORDER

    #RETURNS 100 MEMES AS JSON RESPONSE
    def list(self, request):
        queryset = self.get_queryset()                                                      
        serializer = MemeSerializer(queryset, many=True)                 
        return Response(serializer.data, status=status.HTTP_201_CREATED)  #RETURN RESPONSE AND APPROPRIATE STATUS CODE
        # make this return a json Response


    #API TO CREATE A MEME WHEN REQUEST SENT TO /MEMES
    #POST REQUEST
    def create(self, request):                                                              
        serializer = MemeSerializer(data=request.data)  
        if serializer.is_valid():                       
            new_name=request.data['name']
            new_caption=request.data['caption']
            new_url=request.data['url']
            duplicate_meme=Meme.objects.filter(name=new_name,url=new_caption,caption=new_caption)

            if duplicate_meme.exists():         #CHECK IF MEME EXISTS IN DB AND RETURNS RELEVANT STATUS CODE
                return Response("Duplicate Values of Meme",status=status.HTTP_409_CONFLICT)  
            serializer.save()          
            validate = URLValidator() 
            value = serializer.data['url']  


            if value:                           #CHECK FOR VALID VALUES                                
                try:
                    validate(value)
                except ValidationError:
                    return HttpResponse(status=status.HTTP_400_BAD_REQUEST)     #ERROR STATUS CODE

            created_id={"id":str(Meme.objects.last().id)}
            
            
            return Response(created_id, status=status.HTTP_201_CREATED)    #RETURN ID FOR SUCESSFUL POST REQUEST
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #RELEVANT STATUS CODE FOR ERROR RETURNED



#VIEW FOR THE FOLLOWIN THE PATCH UPDATE API AND DETAILED VIEW API
class MemeUpdateAPIView(generics.RetrieveUpdateAPIView):           
    serializer_class = MemeSerializer                                          
    queryset = Meme.objects.all()                                             

    lookup_field = 'id'                                                      
    
    # DETAILED VIEW OF A SELECTED MEME
    def retrieve(self, request, id=None):
        try:                                                       
            meme = Meme.objects.get(id=id)
        except Meme.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)  

        serializer = MemeSerializer(meme)                
        #INga JSONresponse work aavuthu up it isnt            
        return Response(serializer.data,status=status.HTTP_201_CREATED)                        
    
    
    # PATCH UPDATE ENDPOINT VIEW
    def patch(self, request, id):
        try:                                                        
            meme = Meme.objects.get(id=id)                          
        except Meme.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)     
       
        serializer = MemeUpdateSerializer(meme, data=request.data,partial=True)  
                                                                    
    
        if serializer.is_valid():     

            serializer.save()
            return Response(status=status.HTTP_201_CREATED)                        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
     
    # TO DELETE A CERTAIN MEME
    def delete(self,request,id):
        try:                                                        
            meme = Meme.objects.get(id=id)
        except Meme.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)   
        meme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  

#VIEW TO DISPLAY LIST OF MEMES TO THE USER
def memes_List(request):
    context = {'memes_List' : Meme.objects.all().order_by('-id')[:100] }
    return render(request, "meme_app/memes_List.html",context)

#VIEW FOR THE FORM TO FILLL IN DETAILS OF MEME TO BE UPLOADED
def memes_form(request, id=0):
    try:
        if request.method == 'GET':
            if id==0:               #IF NO MEMES PRESENT REDIRECT TO FORM
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
    except Meme.DoesNotExist:               #IF INVALID ID ENTERED
        raise Http404('Page not found')

#VIEW TO DELETE A SPECIFIC MEME BY THE USER
def memes_delete(request, id):
    meme = Meme.objects.get(pk=id)
    meme.delete()
    return redirect('/memes-list/')

#VIEW TO GIVE A DETAILED VIEW OF A PARTICULAR MEME TO THE USER
def memes_json(request, id):
    context = {
        'meme_list': Meme.objects.filter(pk=id),
    }
    return render(request, "meme_app/memes_json.html", context)