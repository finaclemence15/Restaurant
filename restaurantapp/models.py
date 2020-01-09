from django.db import models

# Create your models here.

class Location(models.Model):
    location_name = models.CharField(max_length =40)
    
    def __str__(self):
        return self.location
        
    def save_location(self):
        self.save()    
    
class Category(models.Model):
    category_name = models.CharField(max_length =40) 
    
    def __str__(self):
        return self.category
        
    def save_category(self):
        self.save()
class Restaurant(models.Model):
    resto_name = models.CharField(max_length =50)
    details= models.TextField()
    location = models.ForeignKey(Location,null = True)
    category = models.ForeignKey(Category, null = True)
    
    def __str__(self):
        return self.resto_name
      
    
    def save_restaurant(self):
        self.save()
    
        