from django.core.management.base import BaseCommand

from datacenter.models import Schoolkid
from scripts import fix_marks, remove_chastisements, create_commendation


def first_case():
    fio = 'Фролов Иван'
    subject = 'Математика'
    student = Schoolkid.objects.get(full_name__contains=fio)
    fix_marks(student)
    remove_chastisements(student)
    create_commendation(fio, subject)


def second_case(friend_fio):
    subject = 'Математика'
    student = Schoolkid.objects.get(full_name__contains=friend_fio)
    fix_marks(student)
    remove_chastisements(student)
    create_commendation(friend_fio, subject)


def third_case(achievement, subject_name):



class Command(BaseCommand):

    def handle(self, *args, **options):
        first_case()

        friend_fio = 'Баранова Евфросиния'
        second_case(friend_fio)

        fio = 'Белозеров Авдей'
        achievement = 'лучший'
        subject_name = 'Математика'
        third_case(fio, achievement, subject_name)


