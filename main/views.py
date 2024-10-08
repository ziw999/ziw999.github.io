from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Categories
from main.models import About, Contact, Delivery


class IndexView(TemplateView):
    template_name='main/index.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='КАЛИНКА-Главная'
        context['content']='Магазин мебели "КАЛИНКА"'
        return context
    
    
class DeliveryView(TemplateView):
    template_name='main/delivery.html'
    
    def get_context_data(self, **kwargs):
        form=Delivery.objects.order_by('-id')
        context=super().get_context_data(**kwargs)
        context['title']='КАЛИНКА-Доставка'
        context['form']=form
        return context
        
        
class ContactView(TemplateView):
    template_name='main/contacts.html'
    
    def get_context_data(self, **kwargs):
        form=Contact.objects.all()
        context=super().get_context_data(**kwargs)
        context['title']='КАЛИНКА-Наши контакты'
        context['form']=form
        return context
    

class AboutView(TemplateView):
    template_name='main/about.html'
    
    def get_context_data(self, **kwargs):
        form=About.objects.order_by('-id')
        context=super().get_context_data(**kwargs)
        context['title']='КАЛИНКА-Про нас'
        context['form']=form
        return context
        
        

# def index(request):
    
#     context={
#         'title': 'КАЛИНКА-Главная',
#         'content': 'Интернет магазин мебели КАЛИНКА',
#     }
#     return render(request, 'main/index.html', context)


# def about(request):
#     form=About.objects.order_by('-id')
#     context={
#         'title': 'КАЛИНКА-Про нас',
#         'form': form
#     }
#     return render(request, 'main/about.html', context)


# def contacts(request):
#     form=Contact.objects.all()
#     context={
#         'title': 'КАЛИНКА-Наши контакты',
#         'form': form 
#     }
#     return render(request, 'main/contacts.html', context)

# def delivery(request):
#     form=Delivery.objects.order_by('-id')
#     context={
#         'title': 'КАЛИНКА-Доставка и оплата',
#         'form': form
#     }
#     return render(request, 'main/delivery.html', context)
