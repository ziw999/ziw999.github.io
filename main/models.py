from django.db import models


class About(models.Model):
    content=models.CharField(max_length=50, verbose_name='Тема:')
    article=models.TextField(verbose_name='Информация:')
    
    class Meta:
        verbose_name='Информацию'
        verbose_name_plural='Информация'
   
    def __str__(self):
        return self.content
    
    
class Contact(models.Model):
    address=models.CharField(max_length=250, verbose_name='Адрес:')
    phone=models.CharField(max_length=20, verbose_name='Телефон:')
    email=models.EmailField(max_length=30, verbose_name='E-mail:')
    
    class Meta:
        verbose_name='Контакт'
        verbose_name_plural='Контакты'
   
    def __str__(self):
        return self.address
    
    
class Delivery(models.Model):
    content=models.CharField(max_length=50, verbose_name='Тема:')
    article=models.TextField(verbose_name='Информация:')
    
    class Meta:
        verbose_name='Доставку'
        verbose_name_plural='Доставка'
   
    def __str__(self):
        return self.content
