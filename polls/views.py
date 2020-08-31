from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Questions, Quiz, QuizTaker
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
# user_answer_list = []
# answer_list = []
# answers = Questions.objects.all()
# for answer in answers:
#     answer_list.append(answer.answer)


def home(request):
    stories = Quiz.objects.all()
    context = {'stories': stories}
    return render(request, 'polls/home.html', stories)

@login_required
def questions_view(request):
    questions = Questions.objects.all()
    score = 0
    try:
        if request.method == 'POST':
            for question in questions:
                fields = request.POST[str(question.id)]
                if fields == question.answer:
                    score += 5
            score_percentage = (score * 100) / 50
            score_percentage_converted = float(score_percentage)
            user_score = QuizTaker.objects.create(quiz_taker=request.user, score=score_percentage_converted)
            user_score.save()

            return redirect('polls:results')
        else:
            context = {'questions': questions}
            return render(request, 'polls/index.html', context)
    except:
        messages.error(request, 'It is either you did not answer all the questions or you have done this screening before')
        return redirect('polls:index')


@login_required
def result(request):
    score = get_object_or_404(QuizTaker, quiz_taker=request.user)
    context = {'score': score}
    return render(request, 'polls/results.html', context)


