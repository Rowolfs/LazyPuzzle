from django.db import models

class BasicSettings(models.Model):
    class Meta():
        abstract = True
        ordering = ['is_published', 'time_publication']
    time_publication = models.DateTimeField(
        auto_now=False, verbose_name="Дата появления", auto_now_add=True)
    is_published = models.BooleanField(
        default=True, verbose_name="Публичность")

class Puzzle(BasicSettings):
    class Meta():
        abstract = True
        ordering = ['likes','author','difficulty','title','is_published', 'time_publication']
    title = models.CharField(
        max_length=50, blank=True, verbose_name="Заголовок")
    likes = models.IntegerField(
        default=0, verbose_name="Лайки")
    author = models.CharField(
        max_length=30, blank=True, verbose_name="Автор",
        default="LazzyPuzzle")
    difficulty = models.CharField(
        max_length=15,blank=True, verbose_name="Сложность",
        default="Normal")

class Themes(models.Model):
    class Meta():
        db_table = "db_bP_themes"
    theme = models.CharField(
        max_length=15, blank=True, verbose_name="Тема",
        default="Random")

class VerbalRiddles(BasicSettings):
    class Meta():
        db_table = "db_bP_verbal_riddles"
        verbose_name = "словесные загадки"
        verbose_name_plural = "словесные загадки"
        ordering = ['question', 'is_published','time_publication']
    question = models.TextField(
        max_length=150, blank=True, verbose_name="Вопрос")
    answer = models.CharField(
        max_length = 20,blank=True, verbose_name="Ответ")
    themes = models.ManyToManyField(Themes)

class Crossword(Puzzle):
    class Meta():
        db_table = "db_bP_crossword"
        verbose_name = "кроссворды"
        verbose_name_plural = "кроссворды"
    riddles = models.ManyToManyField(VerbalRiddles)
    themes = models.ManyToManyField(Themes)
