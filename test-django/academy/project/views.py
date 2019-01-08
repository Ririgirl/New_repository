from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import View 
from django.shortcuts import redirect
from django.views.generic import ListView 

def index(request):
    return render(request, "index.html")

class CandCreate(View):
	def get(self, request):
		quest1 = Answer.objects.all()
		form = CandForm()
		return render(request, "candidate/candidate_form.html", context={'form': form, 'quest1': quest1})

	def post(self, request):
		bound_form = CandForm(request.POST)
		new_form = bound_form.save()
		return redirect('questions/')
		return render(request, 'candidate/candidate_form.html', context = {'form': bound_form})

class Question_answer(View):
	def get(self, request):
		quest = Answer.objects.all()
		cd = Cand.objects.all()
		return render(request, "candidate/candidate_questions.html", context={'quest': quest, 'cd': cd})

	def post(self, request):
		bound_form = QuestionForm(request.POST)
		new_form = bound_form.save()
		return render(request, 'candidate/candidate_questions.html', context = {'form': bound_form})

# def Question_answer(request, id, id_cand_a):
# 		model = Cand, Answer
# 		id = Cand.objects.get(id__iexact=id_cand_a)
# 		field = Cand.objects.all()
# 		field_a = Answer.objects.all()
# 		return render(request, 'jedi/jedi_candidate.html', context={'id_cand_a':id_cand_a, 'field':field, 'field_a':field_a})

class JediView(ListView):
    model = Jedi
    template_name = 'jedi/jedi.html'
    context_object_name = 'jedis'

def Jedi_name(request, id):
		model = Jedi, Cand
		id = Jedi.objects.get(id__iexact=id)
		field = Jedi.objects.all()
		field_cand = Cand.objects.all()
		return render(request, 'jedi/jedi_list.html', context={'id':id, 'field':field, 'field_cand':field_cand})

def Jedi_cand(request, id, id_cand):
		model = Cand, Answer
		id = Cand.objects.get(id__iexact=id_cand)
		field = Cand.objects.all()
		field_question = Answer.objects.all()
		return render(request, 'jedi/jedi_candidate.html', context={'id_cand':id_cand, 'field':field, 'field_cand':field_question})



