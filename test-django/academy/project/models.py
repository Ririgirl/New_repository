from django.db import models
  
class Planet(models.Model): #Планеты
    planet_name = models.CharField(max_length=50, help_text="Введите планету")

    def __str__(self):
    	return self.planet_name

class Jedi(models.Model): #Джедаи 
	name = models.CharField(max_length=50, help_text="Введите имя")
	planet = models.ForeignKey(Planet, on_delete = models.DO_NOTHING)

	def __str__(self):
		return self.name


class Cand(models.Model): #Кандидаты
    name = models.CharField(max_length=50, help_text="Введите имя")
    age = models.IntegerField(help_text="Сколько вам лет?")
    email = models.EmailField(help_text="ivanov@gmail.com")
    planet = models.ForeignKey(Planet, on_delete = models.DO_NOTHING)
    his_jedi = models.ForeignKey(Jedi, null=True, on_delete = models.SET_NULL)
    num_answer = models.IntegerField(null = True, help_text="Количество правильных ответов")

    def __str__(self):
        return "{}, {}, количество правильных ответов {}".format(self.name, self.age, self.num_answer)

class Answer(models.Model): #Вопросы
	answer = models.TextField(help_text="Введите вопрос")

	def __str__(self):
		return self.answer
