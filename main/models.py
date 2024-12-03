from django.db import models



class Index(models.Model):
    name = models.CharField(max_length=60, verbose_name='Заголовок')
    image = models.ImageField(upload_to='carusel_images', blank=True, null=True, verbose_name='Изображение в центре')
    text = models.TextField(blank=True, null=True, verbose_name='Текст в центре')
    
    class Meta:
        verbose_name='главная центр'
        verbose_name_plural='Главная центр'
   
    def __str__(self):
        return self.text
    
class Right(models.Model):
    name = models.CharField(max_length=60, verbose_name='Заголовок')
    image = models.ImageField(upload_to='carusel_images', blank=True, null=True, verbose_name='Изображение справа')
    text = models.TextField(blank=True, null=True, verbose_name='Текст справа')
    
    class Meta:
        verbose_name='главная справа'
        verbose_name_plural='Главная справа'
   
    def __str__(self):
        return self.text
    


class About(models.Model):
    name = models.CharField(max_length=60, verbose_name='Заголовок')
    image = models.ImageField(upload_to='carusel_images', blank=True, null=True, verbose_name='Изображение в центре')
    text = models.TextField(blank=True, null=True, verbose_name='Текст в центре')
    
    class Meta:
        verbose_name='про нас центр'
        verbose_name_plural='Про нас центр'
   
    def __str__(self):
        return self.text
    
class Rightab(models.Model):
    name = models.CharField(max_length=60, verbose_name='Заголовок')
    image = models.ImageField(upload_to='carusel_images', blank=True, null=True, verbose_name='Изображение справа')
    text = models.TextField(blank=True, null=True, verbose_name='Текст справа')
    
    class Meta:
        verbose_name='про нас справа'
        verbose_name_plural='Про нас справа'
   
    def __str__(self):
        return self.text
    


class Contacts(models.Model):
    name = models.CharField(max_length=60, verbose_name='Заголовок')
    image = models.ImageField(upload_to='carusel_images', blank=True, null=True, verbose_name='Изображение в центре')
    text = models.TextField(blank=True, null=True, verbose_name='Текст в центре')
    
    class Meta:
        verbose_name='контакты центр'
        verbose_name_plural='Контакты центр'
   
    def __str__(self):
        return self.text
    
class Rightcon(models.Model):
    name = models.CharField(max_length=60, verbose_name='Заголовок')
    image = models.ImageField(upload_to='carusel_images', blank=True, null=True, verbose_name='Изображение справа')
    text = models.TextField(blank=True, null=True, verbose_name='Текст справа')
    
    class Meta:
        verbose_name='контакты справа'
        verbose_name_plural='Контакты справа'
   
    def __str__(self):
        return self.text
    


class Menu(models.Model):
    name = models.CharField(max_length=60, verbose_name='Заголовок')
    image = models.ImageField(upload_to='carusel_images', blank=True, null=True, verbose_name='Изображение в центре')
    text = models.TextField(blank=True, null=True, verbose_name='Текст в центре')
    
    class Meta:
        verbose_name='Меню центр'
        verbose_name_plural='меню центр'
   
    def __str__(self):
        return self.text
    
class Rightmen(models.Model):
    name = models.CharField(max_length=60, verbose_name='Заголовок')
    image = models.ImageField(upload_to='carusel_images', blank=True, null=True, verbose_name='Изображение справа')
    text = models.TextField(blank=True, null=True, verbose_name='Текст справа')
    
    class Meta:
        verbose_name='меню справа'
        verbose_name_plural='меню справа'
   
    def __str__(self):
        return self.text


