from django.db import models

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




