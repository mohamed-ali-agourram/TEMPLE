from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .models import templates
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView)


class TempelListView(ListView):
    model = templates
    template_name = 'HOME/DB_templates.html'
    context_object_name = 'query'
    ordering = ['-date_posted']
    paginate_by = 10


def search(request):

    if 'q' in request.GET:
        search = request.GET['q']
        quests = templates.objects.filter(
            Q(title__icontains=search) |
            Q(tags__name__icontains=search) |
            Q(category__title__icontains=search) |
            Q(description__icontains=search)).distinct()
        total = 0
        for i in quests:
            total += 1
        paginator = Paginator(quests, 9)
        page_num = request.GET.get('page', 1)

        quests = paginator.page(page_num)
        context = {
            'search': search,
            'title': search,
            'query': quests,
            'total': total
        }
        return render(request, 'HOME/search.html', context)
    elif 'tag' in request.GET:
        search = request.GET['tag']
        quests = templates.objects.filter(
            tags__name__icontains=search).distinct()
        total = 0
        for i in quests:
            total += 1
        paginator = Paginator(quests, 9)
        page_num = request.GET.get('page', 1)

        quests = paginator.page(page_num)
        context = {
            'search': search,
            'title': search,
            'query': quests,
            'total': total
        }
        return render(request, 'HOME/search.html', context)
    elif 'category' in request.GET:
        search = request.GET['category']
        quests = templates.objects.filter(
            category__title__icontains=search).distinct()
        total = 0
        for i in quests:
            total += 1
        paginator = Paginator(quests, 9)
        page_num = request.GET.get('page', 1)

        quests = paginator.page(page_num)
        context = {
            'search': search,
            'title': search,
            'query': quests,
            'total': total
        }
        return render(request, 'HOME/search.html', context)
    else:
        return render(request, 'HOME/search.html')


class TempleDetailView(DetailView):
    model = templates


def AboutUs(request):
    context = {
        'title': 'About Us',
    }
    return render(request, 'HOME/AboutUs.html', context)


def ContactUs(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'full_name': form.cleaned_data['full_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'W7aicha.123@gmail.com',
                          ['W7aicha.123@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(
                request, 'Your message has been sent to our team!')
            return redirect('templates')
    form = ContactForm()
    context = {
        'title': 'Contact Us',
        'form': form
    }
    return render(request, 'HOME/contactUs.html', context)
