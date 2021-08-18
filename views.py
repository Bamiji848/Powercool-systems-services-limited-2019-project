from django.shortcuts import render, redirect,get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from powercool.settings import EMAIL_HOST_USER
from django.views.generic import View
from django.contrib.auth.models import User
from powercool_app.models import Contact,Product,Media,Carosue,Core_team,Blog,CategoryP,ShopProduct,Services,Index_writeup,Vision_mission,Stats,Quote,About,Our_clients
from django.contrib import messages
from django.http import Http404, HttpResponse, HttpResponseRedirect
from powercool_app.forms import ContactForm,CommentForm,QuoteForm
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, EmptyPage,\
    PageNotAnInteger


def index(request, category_slug=None):
    service = Services.objects.all()
    carosue = Carosue.objects.all()
    blog = Blog.objects.all()
    write_up = Index_writeup.objects.all()
    vmv = Vision_mission.objects.all()
    stat = Stats.objects.all()
    quote = Quote.objects.all()
    category = None
    categories = CategoryP.objects.all()
    products = ShopProduct.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(CategoryP, slug=category_slug)
        products = ShopProduct.objects.filter(category=category)
    if request.method == 'POST':
        form = QuoteForm(request.POST, request.FILES)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_services = form.cleaned_data['services']
            sender_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            email_msg = EmailMessage(subject=f"{sender_name}" 'I need a Quote for' f"{sender_services}", body=message, from_email='helpdesk@powercoolsystemsltd.com',
            to=['helpdesk@powercoolsystemsltd.com'],headers={'Reply-To': sender_email}) 
            email_msg.send()
            form = QuoteForm()
    else:
        form = QuoteForm()
    return render(request, 'powercool_app/index.html',{'carosue':carosue,'stat':stat,'blog':blog, 'services':services, 'write':write_up, 'vmv':vmv,'quote':quote,'form':form,'category': category,'categories': categories,'products': products,'service':service})

def about(request, category_slug=None):
    team = Core_team.objects.all()
    about = About.objects.all()
    vmv = Vision_mission.objects.all()
    clients = Our_clients.objects.all()
    category = None
    categories = CategoryP.objects.all()
    products = ShopProduct.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(CategoryP, slug=category_slug)
        products = ShopProduct.objects.filter(category=category)
    return render(request, 'powercool_app/about.html',{'about':about,'vmv':vmv,'clients':clients,'category': category,'categories': categories,'products': products,'team':team})

def services(request, category_slug=None):
    service = Services.objects.all()
    category = None
    categories = CategoryP.objects.all()
    products = ShopProduct.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(CategoryP, slug=category_slug)
        products = ShopProduct.objects.filter(category=category)
    return render(request, 'powercool_app/services.html',{'service':service,'category': category,'categories': categories,'products': products})

def team(request, category_slug=None):
    media = Media.objects.all()
    team = Core_team.objects.all()
    category = None
    categories = CategoryP.objects.all()
    products = ShopProduct.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(CategoryP, slug=category_slug)
        products = ShopProduct.objects.filter(category=category)
    return render(request, 'powercool_app/team.html', {'team': team, 'media': media,'category': category,'categories': categories,'products': products})

def blog(request, category_slug=None):
    object_list = Blog.objects.all()
    paginator = Paginator(object_list, 6)  # 6 posts in each page
    page = request.GET.get('page')
    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        blog = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        blog = paginator.page(paginator.num_pages)
    category = None
    categories = CategoryP.objects.all()
    products = ShopProduct.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(CategoryP, slug=category_slug)
        products = ShopProduct.objects.filter(category=category)
    return render(request, 'powercool_app/blog.html',{'blog':blog,'category': category,'categories': categories,'products': products,'page': page})


def contact(request, category_slug=None):
    contact = Contact.objects.all()
    category = None
    categories = CategoryP.objects.all()
    products = ShopProduct.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(CategoryP, slug=category_slug)
        products = ShopProduct.objects.filter(category=category)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            if form.is_valid():
                sender_name = form.cleaned_data['name']
                sender_email = form.cleaned_data['email']
                sender_subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                email_msg = EmailMessage(subject=f"{sender_name}" 'from powercoolltd contact page' f"{sender_subject}", body=message, from_email='helpdesk@powercoolsystemsltd.com',
                                     to=['helpdesk@powercoolsystemsltd.com'], headers={'Reply-To': sender_email})
                email_msg.send()
                form = ContactForm()
    else:
        form = ContactForm()
    return render(request, 'powercool_app/contact.html', {'contact': contact, 'form': form,'category': category,'categories': categories,'products': products})

def blog_single(request, id, category_slug=None):
    post = get_object_or_404(Blog, id=id)
    comments = post.comments.filter(active=True)
    new_comment = None
    category = None
    categories = CategoryP.objects.all()
    products = ShopProduct.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(CategoryP, slug=category_slug)
        products = ShopProduct.objects.filter(category=category)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST,request.FILES)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'powercool_app/blog-single.html', {'blog_key': post,'comments': comments,'new_comment': new_comment,'comment_form': comment_form,'category': category,'categories': categories,'products': products})


def service_detail(request,id, category_slug=None):
    category = None
    categories = CategoryP.objects.all()
    products = ShopProduct.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(CategoryP, slug=category_slug)
        products = ShopProduct.objects.filter(category=category)
    try:
        detail = Services.objects.get(id=id)
    except Services.DoesNotExist:
        Http404('The page you are accessing does not exist')
    return render(request, 'powercool_app/services_detail.html', {'key': detail,'category': category,'categories': categories,'products': products})
 
def products(request, category_slug=None):
    product=Product.objects.all()
    category = None
    categories = CategoryP.objects.all()
    products = ShopProduct.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(CategoryP, slug=category_slug)
        products = ShopProduct.objects.filter(category=category)
    return render(request,'powercool_app/product.html',{'product':product,'category': category,'categories': categories,'products': products})
    
def products_detail(request,id, category_slug=None):
    category = None
    categories = CategoryP.objects.all()
    products = ShopProduct.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(CategoryP, slug=category_slug)
        products = ShopProduct.objects.filter(category=category)
    try:
        detail = Product.objects.get(id=id)
    except Product.DoesNotExist:
        Http404('The page you are accessing does not exist')
    return render(request, 'powercool_app/products_detail.html', {'key': detail,'category': category,'categories': categories,'products': products})

def profile_view(request, category_slug=None):
    category = None
    categories = CategoryP.objects.all()
    products = ShopProduct.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(CategoryP, slug=category_slug)
        products = ShopProduct.objects.filter(category=category)
    return render(request,'powercool_app/powercoolsystemsltd.html',{'category': category,'categories': categories,'products': products})


def shop(request, category_slug=None):
    category = None
    categories = CategoryP.objects.all()
    products = ShopProduct.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(CategoryP, slug=category_slug)
        products = ShopProduct.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'powercool_app/shop.html', context)


def shop_single(request, id, slug, category_slug=None):
    category = None
    categories = CategoryP.objects.all()
    products = ShopProduct.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(CategoryP, slug=category_slug)
        products = ShopProduct.objects.filter(category=category)
    product = get_object_or_404(ShopProduct, id=id, slug=slug, available=True)
    context = {
        'product': product,
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'powercool_app/shop-single.html', context)

