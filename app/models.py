from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class IceCream(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    flavor = models.CharField(max_length=100, verbose_name="Вкус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Мороженое"
        verbose_name_plural = "Мороженое"