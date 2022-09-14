from ast import Delete
from datetime import datetime
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from bookapp.models import User, Book
from django.http import response, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.hashers import make_password, check_password

def Signup(request):
    return render(request, 'login.html')

def Home(request):
    token = request.GET.get('token')
    userdata = AccessToken(token)
    role = userdata['role']
    allBooks = Book.objects.all()
    data = {
        'role':role,
        'allBooks': allBooks,
    }
    return render(request, 'home.html', context=data)

def Logout(request):
    return JsonResponse({"Message":"Success"})

def Login(request):
    emailId = request.POST['emailId']
    password = request.POST['userPassword']
    try:
        user = User.objects.get(emailId=emailId)
    except:
        return JsonResponse({"Message": "Failure"})
    accessToken = AccessToken.for_user(request.user)
    if user.emailId == emailId and check_password(password, user.__dict__['password']):
        accessToken['role'] = 1
    else:
        accessToken['role'] = 2
    return JsonResponse({"Message": "Success", 'token':str(accessToken)})


class UserRegister(APIView):
    def post(self, request):
        firstName = request.POST['fName']
        lastName = request.POST['lName']
        emailId = request.POST['emailId']
        userPassword = request.POST['userPassword']
        if firstName == 'admin' and lastName == 'admin':
            role = 1
        else:
            role = 2 
        hashedPassword = make_password(userPassword)
        User.objects.create(firstName=firstName, lastName=lastName, emailId=emailId, role=role, lastLogin=datetime.now(), password=hashedPassword)
        return Response({"Message":"Success"}, status=status.HTTP_201_CREATED)


class AddBook(APIView):
    def post(self, request):
        bookName = request.POST['bookName']
        bookCategory = request.POST['bookCategory']
        try:
            book = Book.objects.create(name=bookName, category=bookCategory)
            return Response({"Book id":str(book.id)})
        except:
            return Response({"Message":"Please try again later"}, status=status.HTTP_400_BAD_REQUEST)


class RemoveBook(APIView):

    def delete(self, request):
        token = request.META['HTTP_AUTHORIZATION']
        accessTokenData = AccessToken(token)
        role = accessTokenData['role']
        if role != 2:
            return Response({"Messsage": "You don't have the authority to delete any books, Please register as admin"}, status=status.HTTP_401_UNAUTHORIZED)
        bookId = request.POST['bookId']
        try:
            pass
            # Book.objects.get(id=bookId).delete()
            # return Response({"message":"Success"}, status=status.HTTP_200_OK)
            return Response({"Message":"Object does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"Message":"Object does not exist"}, status=status.HTTP_400_BAD_REQUEST)
