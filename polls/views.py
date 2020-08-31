from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Questions, UserScore
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
user_answer_list = []
answer_list = []
answers = Questions.objects.all()
for answer in answers:
    answer_list.append(answer.answer)

@login_required
def home(request):
    return render(request, 'polls/home.html')

@login_required
def questions_view(request):
    questions = Questions.objects.all()
    if request.method == 'POST':
        for question in questions:
            fields = request.POST[str(question.id)]
            user_answer_list.append(fields)
        print(user_answer_list)
        return redirect('polls:results')
    else:
        context = {'questions': questions}
        return render(request, 'polls/index.html', context)

@login_required
def result(request):
    score = 0
    # user_answers = UserAnswer.objects.all()
    print(user_answer_list)
    print(answer_list)
    for i in range(len(answer_list)):
        if user_answer_list[i] == answer_list[i]:
            score += 5
    score_percentage = (score * 100) / 15
    user_score = UserScore.objects.create(user=request.user, score=score_percentage)
    user_score.user = request.user
    user_score.save()
    context = {'score': user_score}
    return render(request, 'polls/results.html', context)


