from django.db import models

class BasicSettings(models.Model):
    class Meta():
        db_table = "db_basic_setting"
    time_publication = models.DateTimeField(
        auto_now=False, verbose_name="Дата появления")
    is_published = models.BooleanField(
        default=True, verbose_name="Публичность")

class Puzzle(models.Model):
    class Meta():
        db_table = "db_basicPuzzle"
        verbose_name = "базовые пазлы"
        verbose_name_plural = "базовые пазлы"
        ordering = ['author','likes', 'basic_settings']
    basic_settings = models.OneToOneField(BasicSettings, on_delete=models.CASCADE)
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

class VerbalRiddles(models.Model):
    class Meta():
        db_table = "db_bP_verbal_riddles"
        verbose_name = "словесные загадки"
        verbose_name_plural = "словесные загадки"
        ordering = ['question', 'basic_settings']
    question = models.TextField(
        max_length=150, blank=True, verbose_name="Вопрос")
    answer = models.CharField(
        max_length = 20,blank=True, verbose_name="Ответ")
    basic_settings = models.OneToOneField(BasicSettings, on_delete=models.CASCADE)
    themes = models.ManyToManyField(Themes)

class Crossword(models.Model):
    class Meta():
        db_table = "db_bP_crossword"
        verbose_name = "базовые пазлы"
        verbose_name_plural = "базовые пазлы"
        ordering = ['info']
    riddles = models.ManyToManyField(VerbalRiddles)
    info = models.OneToOneField(Puzzle, on_delete=models.CASCADE)
    themes = models.ManyToManyField(Themes)
