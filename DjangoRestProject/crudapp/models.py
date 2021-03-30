from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

#--------------------------------------------------------------------#
#ManyToOne or OneToMany

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    #Relationship should be declared in child. Because, Parent may have many child but child will have only one parent.
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

#--------------------------------------------------------------------#
#OneToOne

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s the place" % self.name

class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name



#--------------------------------------------------------------------#
#ManyToMany

class Publication1(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Article1(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication1)

    def __str__(self):
        return self.headline
