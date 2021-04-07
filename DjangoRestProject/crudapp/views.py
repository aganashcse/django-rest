from django.shortcuts import render
from django.http import request, JsonResponse, Http404
from .models import Employee
from django.views import View

#csrf - for security purpose
from django.views.decorators.csrf import csrf_exempt, csrf_protect

#api view wrappers
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

#Serializer
from .serializer import EmployeeSerializer


# Create your views here.
@csrf_exempt
@api_view(["GET"])
def EmployeeDetails(request):
    if request.method == "GET":
        obj = Employee.objects.all()
        data = {"response": list(obj.values("id", "name"))}
        return JsonResponse(data)

    elif request.method == "POST":
        name = request.POST['name']
        obj = Employee(name=name)
        obj.save()
        data = {"id":obj.id, "name":obj.name}
        return JsonResponse(data)

# class ListEmployee(View): - this is old one before using APIView wrapper
# for jwt:
from rest_framework.permissions import IsAuthenticated
class ListEmployee(APIView):
    permission_classes = (IsAuthenticated, ) # this line of code needed to add jwt authentication

    # You need to decorate the dispatch method for csrf_exempt to work. 
    # What it does is set an csrf_exempt attribute on the view function itself to True, 
    # and the middleware checks for this on the (outermost) view function.
    # We don't need to use the below if we use APIView Wrapper which handles csrf token issue automatically
    # @csrf_exempt
    # def dispatch(self, request, *args, **kwargs):
    #     return super(ListEmployee, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        obj = Employee.objects.all()
        # data = {"response": list(obj.values("id", "name"))}
        serializer_obj = EmployeeSerializer(obj, many=True)
        # return JsonResponse(data) # when APIView not used. but will work with APIView also
        return Response(serializer_obj.data) # especially used when APIView is used. 
        #status(http code), headers(can be used for auth), template_name(usually none), content_type(json/xml) 
            # are the optional parameter of Response Object   


    
    def post(self, request):
        # name = request.POST['name'] # this will not work if we use APIView wrapper and send post body as JSON
        # request.get('name') - to get query parameters of api request (will not work with APIView)
        #request.queryparams('name') - to get query parameter of api request if we use APIView
        
        # name = request.data['name']
        # obj = Employee(name=name)
        # obj.save()
        data = request.data
        serializer_obj = EmployeeSerializer(data=data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        


        # data = {"response": {"id":obj.id, "name":obj.name}}
        # return JsonResponse(data) #work with both APIView and not APIView
        # return Response(data) # used when APIView is used
        return Response(serializer_obj.errors)

class UpdateEmployee(APIView):

    def get_Object(self,id):
        try:
            obj = Employee.objects.get(id = id)
            return obj
        except Employee.DoesNotExist:
            raise Http404


    def put(self, request, id):
        data = request.data
        # obj = Employee.objects.get(id=id)
        obj = self.get_Object(id)
        serializer_obj = EmployeeSerializer(obj, data=data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)

    def delete(self, request, id):
        # obj = Employee.objects.get(id = id)
        obj = self.get_Object(id)
        obj.delete()
        return Response({"response": "Employee is successfully deleted!"})

#Basic django auth code
from django.contrib.auth.forms import UserCreationForm
@csrf_exempt
@api_view(["GET", "POST"])
def authenticateIndex(request):
    return render(request, 'authIndex.html')

from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
@csrf_exempt
@api_view(["GET", "POST"])
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('authenticateIndex')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', context={'form':form})



# for other kindof rest framework UI & jwt:
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class ListEmployeeRest(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, ) # this line of code needed to add jwt authentication
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

#email (gmail)
from django.core.mail import send_mail

def send_email(request):
    #dummy recipeint emails can be generated from https://temp-mail.org/en
    send_mail("hello from ganesh", "hi, this is an automated msg", 'aganashcse@gmail.com', ['migeg23971@0pppp.com'], fail_silently=False)
    return JsonResponse({"response":"email sent!"})