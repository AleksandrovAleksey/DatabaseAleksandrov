import random

from django.contrib.auth.models import User
from faker import Faker
from django.core.management import BaseCommand, CommandError

from app.models import Tag, Profile, Question, Answer


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int)

    def handle(self, *args, **options):
        ratio = options['ratio']
        fake = Faker()

        tags = set()
        for i in range(ratio):
            tag_name = fake.word()
            tags.add(tag_name)

        for tag_name in tags:
            Tag.objects.get_or_create(tag=tag_name)

        usernames = set()
        users = []
        existing_usernames = set(User.objects.values_list('username', flat=True))
        while len(users) < ratio:
            username = fake.user_name()
            if username not in usernames and username not in existing_usernames:
                usernames.add(username)
                users.append(User(username=username))

        User.objects.bulk_create(users)
        saved_users = User.objects.filter(username__in=usernames)

        profiles = [Profile(user=user, avatar=fake.image_url()) for user in saved_users]
        Profile.objects.bulk_create(profiles)

        questions = []
        for i in range(ratio * 10):
            question = Question(
                user=random.choice(saved_users),
                title=fake.sentence(),
                text=fake.text(),
            )
            questions.append(question)

        Question.objects.bulk_create(questions)

        saved_questions = Question.objects.all()
        saved_tags = Tag.objects.all()

        # answers = []
        # for i in range(ratio * 100):
        #     answer = Answer(
        #         question = random.choice(saved_questions),
        #         user = random.choice(saved_users),
        #         text = fake.text()
        #     )
        #     answers.append(answer)
        #
        # Answer.objects.bulk_create(answers)

        # for question in saved_questions:
        #     num_tags_to_select = random.randint(1, 5)
        #     num_tags_to_select = min(num_tags_to_select, len(saved_tags))
        #     selected_tags = random.sample(list(saved_tags), num_tags_to_select)
        #     question.tags.set(selected_tags)
