from django.shortcuts import render
from . import generator
from .forms import QuizForm
from django.contrib.auth.decorators import login_required


def getUserAnswers(request):
    form = QuizForm(request.POST)
    if form.is_valid() :
        user_answers = [form.cleaned_data['user_answer'+str(i+1)] for i in range(10)]
        return user_answers

@login_required
def quiz_view(request):
    if request.method =="POST" :
        liste_questions = request.session['liste_questions']
        user_answers = getUserAnswers(request)
        correction = [generator.isCorrect(user_answers[i],liste_questions[i]) for i in range(len(user_answers))]
        l = [(liste_questions[i],user_answers[i],correction[i][0],correction[i][1]) for i in range(len(liste_questions))]
        context = {'liste_questions' : liste_questions, 'correction' : correction, 'l' : l}
    else :
        demande = "génère moi une liste de questions réponses type quiz sur le thème du sida"
        liste_questions = generator.liste_questions(demande)
        request.session['liste_questions'] = liste_questions
        form = QuizForm()
        l = [(liste_questions[i],form["user_answer"+str(i+1)]) for i in range(len(liste_questions))]
        context = {'liste_questions' : liste_questions, 'l' : l, 'form' : form}


    return render(request, 'quizz.html', context=context)


