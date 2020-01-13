from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Location(models.Model):
    location_name = models.CharField(max_length =40)
    
    def __str__(self):
        return self.location_name
        
    def save_location(self):
        self.save()    
    
class Category(models.Model):
    category_name = models.CharField(max_length =40) 
    
    def __str__(self):
        return self.category_name
        
    def save_category(self):
        self.save()
class Restaurant(models.Model):
    resto_name = models.CharField(max_length =50)
    image = models.ImageField(upload_to = 'images/')
    details= models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    
    def __str__(self):
        return self.resto_name

    @classmethod
    def search_by_location(cls,search_term):
        location = cls.objects.filter(location__location_name__icontains=search_term)
        return location    
          
    
    def save_image(self):
        self.save()

      
        
class Rating(models.Model):
    your_rate= models.TextField()
    restaurant = models.ForeignKey(Restaurant)
    username= models.ForeignKey(User,on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.your_rate
    
    def save_rating(self):
        self.save()
        
    def update_rating(self):
        self.update()

    def delete_rating(self):
        self.delete()           