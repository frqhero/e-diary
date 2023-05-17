from django.core.management.base import BaseCommand

from datacenter.models import Schoolkid
from scripts import fix_marks, remove_chastisements, create_commendation



class Command(BaseCommand):

    @staticmethod
    def _first_case():
        fio = 'Фролов Иван'
        subject = 'Математика'
        student = Schoolkid.objects.get(full_name__contains=fio)
        fix_marks(student)
        remove_chastisements(student)
        create_commendation(fio, subject)

    @staticmethod
    def _second_case(friend_fio):
        student = Schoolkid.objects.get(full_name__contains=friend_fio)
        subject = 'Математика'
        fix_marks(student)
        remove_chastisements(student)
        create_commendation(friend_fio, subject)

    @staticmethod
    def _third_case(fio, subject_name, achievement):
        student = Schoolkid.objects.get(full_name__contains=fio)
        fix_marks(student)
        remove_chastisements(student)
        create_commendation(fio, subject_name, achievement)

    def handle(self, *args, **options):
        # self._first_case()
        #
        # friend_fio = 'Баранова Евфросиния'
        # self._second_case(friend_fio)
        #
        # fio = 'Белозеров Авдей'
        # achievement = 'лучший'
        # subject_name = 'Музыка'
        # self._third_case(fio, subject_name, achievement)

        fio = ''
        create_commendation(fio)
