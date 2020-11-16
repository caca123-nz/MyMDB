from django.db import models

class Person(models.Model):
  '''Table of people who have appeared in a film, written or directed a film'''
  first_name = models.CharField(max_length=140, db_column="first_name")
  last_name = models.CharField(max_length=140, db_column="last_name")
  born = models.DateField()
  died = models.DateField(null=True, blank=True)

  class Meta:
    ordering = ('last_name', 'first_name')
    db_table = "person"

  def __str__(self):
    if self.died:
      return '{}, {} ({}-{})'.format(self.last_name, self.first_name,
      self.born, self.died)
    return '{}, {} ({})'.format(self.last_name, self.first_name,
      self.born)

class Movie(models.Model):
  '''Creating db table for movies'''

  NOT_RATED = 0
  RATED_G = 1
  RATED_PG = 2
  RATED_R = 3
  RATINGS = (
        (NOT_RATED, "NR - Not Rated"),
        (RATED_G, "G - General Audiences"),
        (RATED_PG, "PG - Parental Guidance Suggested"),
        (RATED_R, "R - Restricted"))
  
  title = models.CharField(max_length=140)
  plot = models.TextField()
  year = models.PositiveIntegerField()
  rating = models.IntegerField(choices=RATINGS, default=NOT_RATED
  )
  runtime = models.PositiveIntegerField()
  website = models.URLField(blank=True)

  class Meta:
    # Table options
    db_table = "movie"
    ordering = ('-year', 'title')

  def __str__(self):
    # String representaion on print
    return '{} ({})'.format(self.title, self.year)




