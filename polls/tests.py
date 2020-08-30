from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question
from django.urls import reverse


def create_question(question_text, days):
    """
    Create a question with the given question_text and published the
    given number of days offset to now
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTest(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate page is displayed
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_questions(self):
        """
        Questions with pub_date in the past are published on the index page
        """

        create_question(question_text='Past question', days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question>'])

    def test_future_questions(self):
        """
        Questions with pub_date in the future are not published on the index page yet
        """

        create_question(question_text='past question', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, 'No polls are available')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_and_future_questions(self):
        """
        Questions with pub_date in the past and future should only have
        the past questions published on the index page
        """

        create_question(question_text='Past question', days=-30)
        create_question(question_text='Future question', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question>'])

    def test_two_past_questions(self):
        """
        Questions with pub_date in the past and future should display
        the past questions on the index page starting from the most recent one
        """

        create_question(question_text='Past question 1', days=-30)
        create_question(question_text='Past question 2', days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question 2>',
                                                                            '<Question: Past question 1>'])


class QuestionDetailTests(TestCase):
    def test_future_question(self):
        future_question = create_question(question_text='Future Question', days=5)
        response = self.client.get(reverse('polls:details', args=(future_question.id,)))
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question(question_text='Past Question', days=-5)
        response = self.client.get(reverse('polls:details', args=(past_question.id,)))
        self.assertContains(response, past_question.question_text)


class QuestionModelTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently () returns false for questions whose pub_date
        is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently () returns false for questions whose pub_date
        is older than 1 day
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently () returns false for questions whose pub_date
        is older than 1 day
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


