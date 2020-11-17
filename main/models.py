from django.db import models

class MovieManager(models.Manager):
  '''Query all related data or single related data (person) across a single query'''
  def all_with_related_persons(self):
    qs = get_queryset()
    qs = qs.select_related('director')
    qs = qs.prefetch_related('writers', 'actors')
    return qs

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
  director = models.ForeignKey(to="Person", on_delete=models.SET_NULL, blank=True, null=True, related_name='directed')
  writers = models.ManyToManyField(to="Person", related_name="writing_credits", blank=True)
  actors = models.ManyToManyField(to="Person", through="Role", related_name='acting_credits', blank=True)

  objects = MovieManager()

  class Meta:
    # Table options
    db_table = "movie"
    ordering = ('-year', 'title')

  def __str__(self):
    # String representaion on print
    return '{} ({})'.format(self.title, self.year)

class PersonManager(models.Manager):
  '''Query all related data (movies) across a single query'''
  def all_with_prefetch_movies(self):
    qs = self.get_queryset()
    return qs.prefetch_related('directed', 'writing_credits', 'role_set__movie')

class Person(models.Model):
  '''Table of people who have appeared in a film, written or directed a film'''
  first_name = models.CharField(max_length=140, db_column="first_name")
  last_name = models.CharField(max_length=140, db_column="last_name")
  born = models.DateField()
  died = models.DateField(null=True, blank=True)

  objects = PersonManager()

  class Meta:
    ordering = ('last_name', 'first_name')
    db_table = "person"

  def __str__(self):
    if self.died:
      return '{}, {} ({}-{})'.format(self.last_name, self.first_name,
      self.born, self.died)
    return '{}, {} ({})'.format(self.last_name, self.first_name,
      self.born)

class Role(models.Model):
  '''Actor role in a film'''
  name = models.CharField(max_length=140)
  movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
  person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)

  class Meta:
    unique_together=('movie', 'person', 'name')

  def __str__(self):
    return '{} {} {}'.format(self.movie.id, self.person.id, self.name)