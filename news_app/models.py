from django.db import models

class Category(models.Model):
    name = models.CharField("Название категории", max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField("Заглавление новости",max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, verbose_name="Категория")
    description = models.TextField("Сипаттамасы", )
    image_url = models.CharField("URL ссылка картинки", max_length=500)
    created_at = models.DateTimeField("Дата выпуска", auto_now_add=True)

    def __str__(self):
        return self.title


class Adv(models.Model):
    name = models.CharField("Company name", max_length=255, default="Company Name")
    image_url = models.CharField("URL ссылка", max_length=500)

    def __str__(self):
        return self.name