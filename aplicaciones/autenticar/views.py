from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import SignUpForm, EditProfileForm
from django.contrib.auth.decorators import login_required

def home(request):
	return render(request,'autenticar/home.html',{})

def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request,('Has Ingresado'))
			return redirect('home')  
		else:
			messages.success(request,('Error de Ingreso - Por Favor Intenta de Nuevo!'))
			return redirect("login")
	else:
		return render(request,'autenticar/login.html',{})


@login_required(login_url="/authenticate/login/")
def logout_user(request):
	logout(request)
	messages.success(request,("Has Salido!"))
	return redirect('home')

def register_user(request):
	if request.method=='POST':
		form= SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data['username']
			password=form.cleaned_data['password1']
			user = authenticate(request, username=username, password=password)
			login(request, user)
			messages.success(request,('Te Has Registrado Exitosamente'))
			return redirect('home') 
	else:
		form= SignUpForm()

	context={'form':form}
	return render(request,'autenticar/register.html',context)

@login_required(login_url="/authenticate/login/")
def edit_profile(request):
	if request.method=='POST':
		form= EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request,('Tu perfil ha sido actualizado con éxito!'))
			return redirect('home') 
	else:
		form= EditProfileForm(instance=request.user)

	context={'form':form}
	return render(request,'autenticar/edit_profile.html',context)

@login_required(login_url="/authenticate/login/")
def change_password(request):
	if request.method=='POST':
		form= PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)#to retain login session
			messages.success(request,('Tu contraseña ha sido actualizada con éxito!'))
			return redirect('home') 
	else:
		form= PasswordChangeForm(user=request.user)

	context={'form':form}
	return render(request,'autenticar/change_password.html',context)




