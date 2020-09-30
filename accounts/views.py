from django.shortcuts import render, redirect
from .models import *
from .modelform import OrderForm, CreateUserForm, CustomerForm
from django.forms import inlineformset_factory
from .filters import OrderFilter
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            
            Customer.objects.create(user=user,)
            return redirect('login')

    context = {'form':form}
    return render(request, 'accounts/register.html',context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request,username=username[:-10], password=password)
        if user is not None:
            login(request, user)
            if(username[:-10]=="kpcdesigner"):
                return redirect('busdevclerk')
            elif(username[:-10]=="kpengineer"):
                return redirect('engineer')
            elif(username[:-10]=="icms"):
                return redirect('icmsclerk')
            else:
                return redirect('home') #when its Sima the busdev clerk
            
    context = {}
    return render(request, 'accounts/login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    
    total_orders = orders.count()
    total_delivered = orders.filter(status='Standard Application').count()
    total_pending = orders.filter(status='Premium Application').count()
    
    context = {'orders':orders,'customers':customers, 'total_orders':total_orders,'total_delivered':total_delivered,'total_pending':total_pending}
    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
@admin_only
def busclerk(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    
    total_orders = orders.count()
    total_delivered = orders.filter(status='Standard Application').count()
    total_pending = orders.filter(status='Premium Application').count()
    
    context = {'orders':orders,'customers':customers, 'total_orders':total_orders,'total_delivered':total_delivered,'total_pending':total_pending}
    return render(request, 'accounts/busdevclerk.html', context)

@login_required(login_url='login')
@admin_only
def consengineer(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    
    total_orders = orders.count()
    total_delivered = orders.filter(status='Standard Application').count()
    total_pending = orders.filter(status='Premium Application').count()
    
    context = {'orders':orders,'customers':customers, 'total_orders':total_orders,'total_delivered':total_delivered,'total_pending':total_pending}
    return render(request, 'accounts/engineer.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders = request.user.customer.order_set.all()
    
    total_orders = orders.count()
    total_delivered = orders.filter(status='Delivered').count()
    total_pending = orders.filter(status='Pending').count()
    userid = [request.user.customer.id]
    print(userid)
    context = {'orders':orders,'total_orders':total_orders,'total_delivered':total_delivered,'total_pending':total_pending,'userid':userid}
    return render(request, 'accounts/user.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html',{'products':products})

@login_required(login_url='login')
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_count = orders.count()
    
    myfilter = OrderFilter(request.GET, queryset=orders)
    orders = myfilter.qs
    context = {'customer':customer,"orders":orders,'orders_count':orders_count,'myfilter':myfilter}
    
    return render(request, 'accounts/customer.html', context)

@login_required(login_url='login')
@admin_only
def customerforclerk(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    orders_count = orders.count()
    
    myfilter = OrderFilter(request.GET, queryset=orders)
    orders = myfilter.qs
    context = {'customer':customer,"orders":orders,'orders_count':orders_count,'myfilter':myfilter}
    
    return render(request, 'accounts/customerforclerk.html', context)



@login_required(login_url='login')
def create_order(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product','status','loc','appnum','appstatus','agreewayleave','agreebtn'))
    
    customer = Customer.objects.get(id=pk) 
    formset = OrderFormSet(instance=customer)
    
    #form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('create_order', pk=pk)
    
    orders = customer.order_set.all()
    orders_count = orders.count()
    
    myfilter = OrderFilter(request.GET, queryset=orders)
    orders = myfilter.qs
    context = {'formset':formset, 'customer':customer,"orders":orders,'orders_count':orders_count,'myfilter':myfilter}
    # = random.randint(1,101)
    return render(request, 'accounts/orderform.html',context)


@login_required(login_url='login')
def create_app(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product','status','loc','appnum','appstatus','agreewayleave','agreebtn'))
    
    customer = Customer.objects.get(id=pk) 
    formset = OrderFormSet(instance=customer)
    
    #form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('create_app', pk=pk)
    
    orders = customer.order_set.all()
    orders_count = orders.count()
    
    myfilter = OrderFilter(request.GET, queryset=orders)
    orders = myfilter.qs
    context = {'formset':formset, 'customer':customer,"orders":orders,'orders_count':orders_count,'myfilter':myfilter}
    # = random.randint(1,101)
    return render(request, 'accounts/appform.html',context)

def create_ordertwo(request, pk): #for the designer
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('siteinfo','appcontrol','appstatus'))
    
    customer = Customer.objects.get(id=pk) 
    formset = OrderFormSet(instance=customer)
    
    #form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('busdevclerk')
    
    #print(formset.form.)
    context = {'formset':formset}
    # = random.randint(1,101)
    return render(request, 'accounts/orderform.html',context)

def create_orderthree(request, pk): #for the engineer
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('appstatus','installnote'))
    
    customer = Customer.objects.get(id=pk) 
    formset = OrderFormSet(instance=customer)
    
    #form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('engineer')
    
    #print(formset.form.)
    context = {'formset':formset}
    # = random.randint(1,101)
    return render(request, 'accounts/orderform.html',context)

def supply_agreement(request, pk): #Supply Agreement form
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('agreebtn',))
    
    customer = Customer.objects.get(id=pk) 
    formset = OrderFormSet(instance=customer)
    
    #form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('customer', pk=pk)
    
    #print(formset.form.)
    context = {'formset':formset, 'customer':customer}
    # = random.randint(1,101)
    return render(request, 'accounts/orderform.html',context)

def wayleave_agreement(request, pk): #Wayleave Agreement form
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('agreewayleave',))
    
    customer = Customer.objects.get(id=pk) 
    formset = OrderFormSet(instance=customer)
    
    #form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('customer', pk=pk)
    
    #print(formset.form.)
    context = {'formset':formset, 'customer':customer}
    # = random.randint(1,101)
    return render(request, 'accounts/orderform.html',context)


def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            #return redirect('user')
        
    context = {'form':form}
    return render(request, 'accounts/orderform.html',context)

@login_required(login_url='login')
def delete(request, pk):
    order = Order.objects.get(id=pk)
    if request.method=="POST":
        order.delete()
        return redirect('create_order', pk=request.user.id)
    
    context = {'item':order}
    return render(request, 'accounts/delete.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountProfile(request):
    orders = Order.objects.all()
    customers = request.user
    
    total_orders = orders.count()
    total_delivered = orders.filter(status='Delivered').count()
    total_pending = orders.filter(status='Pending').count()
    
    context = {'orders':orders,'customers':customers, 'total_orders':total_orders,'total_delivered':total_delivered,'total_pending':total_pending}
    return render(request, 'accounts/user.html', context)


def indexPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username[:-10], password=password)
        if user is not None:
            login(request, user)
            return redirect('user')
    context = {}
    return render(request, 'accounts/index.html',context)

def userProfile(request):
    user = request.user.customer
    form = CustomerForm(instance=user)
    
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user')
    context = {'form':form, 'customer':user}
    
    return render(request, 'accounts/account_profile.html',context)

#Qouatation
def qoutations(request, pk): #Supply Agreement form
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    context = {'orders':orders, 'customer':customer}
    return render(request, 'accounts/qoute.html',context)
#Payment 
def payment(request, pk): #Supply Agreement form
    
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('payment',))
    
    formset = OrderFormSet(instance=request.user.customer)
    
    #form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, request.FILES, instance=request.user.customer)
        if formset.is_valid():
            formset.save()
            return redirect('home')
        
    order = Order.objects.all().get(id=pk)
    context = {'order':order, 'formset':formset}
    return render(request, 'accounts/orderform.html',context)


def icms(request, pk): #for the icms
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('qoutation','appstatus'))
    
    customer = Customer.objects.get(id=pk) 
    formset = OrderFormSet(instance=customer)
    
    #form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, request.FILES, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('home')
    
    #print(formset.form.)
    context = {'formset':formset}
    # = random.randint(1,101)
    return render(request, 'accounts/orderform.html',context)

def maplatlon(request, pk): #for the icms
    order = Order.objects.all().get(id=pk)
    context = {'order':order}
    return render(request, 'accounts/map.html',context)

def busdev(request, pk): #for the icms
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('appcontrol','appstatus'))
    
    customer = Customer.objects.get(id=pk) 
    formset = OrderFormSet(instance=customer)
    
    #form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('home')
    
    #print(formset.form.)
    context = {'formset':formset}
    # = random.randint(1,101)
    return render(request, 'accounts/orderform.html',context)

def proposal(request, pk): #for the icms
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('proposal','appstatus'))
    
    customer = Customer.objects.get(id=pk) 
    formset = OrderFormSet(instance=customer)
    
    #form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, request.FILES, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('busdevclerk')
    
    #print(formset.form.)
    context = {'formset':formset}
    # = random.randint(1,101)
    return render(request, 'accounts/orderform.html',context)



@login_required(login_url='login')
@admin_only
def icmsclerk(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    
    #Order Stats
    total_orders = orders.count()
    total_delivered = orders.filter(status='Standard Application').count()
    total_pending = orders.filter(status='Premium Application').count()
 
    context = {'orders':orders,'customers':customers, 'total_orders':total_orders,'total_delivered':total_delivered,'total_pending':total_pending}
    return render(request, 'accounts/icms.html', context)



#Analytics
def analytics(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    jobtypes = Product.objects.all()
    
    #Order Stats
    total_orders = orders.count()
    sites_visited = orders.filter(appstatus='Site Visited').count()
    app_installed = orders.filter(appstatus='Installed').count()
    print()
    
    #Job types Stats 
    tnew = Order.objects.filter( product__name__contains="New" ).count()
    tt = Order.objects.filter( product__name__contains="Temporary" ).count()
    tr = Order.objects.filter( product__name__contains="Routing" ).count()
    tga = Order.objects.filter( product__name__contains="Group Application" ).count()
    tal = Order.objects.filter( product__name__contains="Additional load" ).count()
    tms = Order.objects.filter( product__name__contains="Meter Seperation" ).count()
    context = {'orders':orders,'customers':customers, 'total_orders':total_orders,'sites_visited':sites_visited,'app_installed':app_installed, 'tnew':tnew, 'tt':tt, 'tr':tr, 'tga':tga, 'tal':tal, 'tms':tms}
    return render(request, 'accounts/analytics.html', context)
