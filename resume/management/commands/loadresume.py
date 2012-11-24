from django.core.management.base import BaseCommand
from resume.models import *
import datetime


class Command(BaseCommand):
    help = 'Creates fake data'

    def handle(self, *args, **options):
        user = User(username='nnasser', first_name='Nahim', last_name='Nasser', email='fakemail@gmail.com')
        user.set_password('testpassword')
        user.save()
        resume = Resume(title='Software Engineer', location='Toronto, Canada', industry='Software Engineering', user=user)
        resume.save()
        WorkExperience(resume=resume, position='Software Engineer', location='Toronto, ON', company='BNOTIONS', start_date=datetime.datetime.utcnow(), end_date=datetime.datetime.utcnow()).save()
        WorkExperience(resume=resume, position='Software Developer', location='Ottawa, ON', company='IBM', start_date=datetime.datetime.utcnow(), end_date=datetime.datetime.utcnow()).save()
        WorkExperience(resume=resume, position='Software Engineer', location='Ottawa, ON', company='Tradewind Scientific', start_date=datetime.datetime.utcnow(), end_date=datetime.datetime.utcnow()).save()
        Education(resume=resume, institution='Carleton University', degree='B.Eng Software Engineering', start_date=datetime.datetime.utcnow(), end_date=datetime.datetime.utcnow()).save()
        self.stdout.write("created factory data\n")
