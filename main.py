import random


class Student:
    def __init__(self, firstname):
        self.firstname = firstname
        self.knowledge = 0
        self.today_mood = 15
        self.energy = 10
        self.today_satiety = 10
        self.alive = True


class Lessons(Student):
    def math(self):
        self.knowledge += 1
        self.today_mood -= 1
        self.energy -= 1.5
        self.today_satiety -= 1

    def biology(self):
            self.knowledge += 1
            self.today_mood -= 0.5
            self.energy -= 1.5
            self.today_satiety -= 1

    def geography(self):
        self.knowledge += 1
        self.today_mood -= 0.5
        self.energy -= 1.5
        self.today_satiety -= 1

    def english(self):
        self.knowledge += 1
        self.today_mood -= 1
        self.energy -= 1.5
        self.today_satiety -= 1

    def german(self):
        self.knowledge += 0.5
        self.today_mood -= 1
        self.energy -= 1.5
        self.today_satiety -= 1

    def chinese(self):
        self.knowledge += 0.5
        self.today_mood -= 1
        self.energy -= 1.5
        self.today_satiety -= 1

    def spanish(self):
        self.knowledge += 1
        self.today_mood -= 1
        self.energy -= 1.5
        self.today_satiety -= 1

    def pe(self):
        self.today_mood += 1
        self.energy -= 3
        self.today_satiety -= 1

    def history(self):
        self.knowledge += 1
        self.today_mood -= 1
        self.energy -= 1.5
        self.today_satiety -= 1

    def business(self):
        self.knowledge += 1
        self.energy -= 1
        self.today_satiety -= 1

    def physics(self):
        self.knowledge += 1
        self.energy -= 1
        self.today_satiety -= 1

    def chemistry(self):
        self.knowledge += 0.5
        self.today_mood -= 1
        self.energy -= 1.5
        self.today_satiety -= 1

    def python(self):
        self.knowledge += 10
        self.today_mood += 5
        self.energy -= 0
        self.today_satiety -= 1

    def blender(self):
        self.knowledge += 0.5
        self.energy -= 1
        self.today_satiety -= 1

    def ukr_literature(self):
        self.knowledge += 1
        self.today_mood += 1
        self.energy -= 1
        self.today_satiety -= 1

    def world_literature(self):
        self.knowledge += 2
        self.today_mood += 1
        self.energy -= 1
        self.today_satiety -= 1

    def ukr_language(self):
        self.knowledge += 1
        self.today_mood += 1
        self.energy -= 1
        self.today_satiety -= 1

    def civil_education(self):
        self.knowledge += 1
        self.today_mood -= 1
        self.energy -= 1.5
        self.today_satiety -= 1

    def national_defense(self):
        self.knowledge += 1
        self.today_mood -= 1
        self.energy -= 1.5
        self.today_satiety -= 1


class Time:
    def __init__(self):
        super(Time, self).__init__()
        self.lesson_time = 2700
        self.progect_time = 9000
        self.break1_time = 300
        self.break2_time = 600
        self.dinner = 1500

    def rest_time(self):
        print('Time to rest')
        self.knowledge -= 0.5
        self.mood += 2
        self.energy += 1

    def sleep(self):
        print('Time to sleep')
        self.energy += 2

    def pause(self):
        if self.mood < 5:
            self.rest_time()
        elif self.energy < 5:
            self.sleep()

    def lunch(self):
            print('Час їсти')
            self.today_satiety += 2

    def study(self):
        print('Час вчитися')
        cube = random.randint(1, 19)
        if cube == 1:
            self.math()
        elif cube == 2:
            self.biology()
        elif cube == 3:
            self.geography()
        elif cube == 4:
            self.english()
        elif cube == 5:
            self.german()
        elif cube == 6:
            self.chemistry()
        elif cube == 7:
            self.spanish()
        elif cube == 8:
            self.pe()
        elif cube == 9:
            self.history()
        elif cube == 10:
            self.business()
        elif cube == 11:
            self.physics()
        elif cube == 12:
            self.chemistry()
        elif cube == 13:
            self.python()
        elif cube == 14:
            self.blender()
        elif cube == 15:
            self.ukr_literature()
        elif cube == 16:
            self.world_literature()
        elif cube == 17:
            self.ukr_language()
        elif cube == 18:
            self.civil_education()
        elif cube == 19:
            self.national_defense()


class Home(Student):
    def play(self):
        print('Time to play')
        self.today_mood += 10
        self.energy -= 5
        self.knowladge -= 1

    def self_development(self):
        print('Time to develop yourself')
        self.today_mood -= 1
        self.energy -= 6
        self.knowledge += 8

    def dinner(self):
        print('Time to eat')
        self.today_mood += 5
        self.energy += 7

    def sport(self):
        print('Time to do sport')
        self.energy -= 4

    def sleep(self):
        print('Time to sleep')
        self.energy += 3


class Life(Student):
    def life(self):
        if self.today_mood < -20:
            print('Depression')
        elif self.today_satiety < -15:
            print('Student has died')
        else:
            print("Everything OK")


class Pause(Lessons):
    def rest_time(self):
        print('Час відпочивати')
        self.today_mood += 2
        self.energy += 2

    def sleep(self):
        print('Час спати')
        self.knowledge -= 1
        self.energy += 2

    def lunch(self):
        print('Час їсти')
        self.today_satiety += 2

    def get_today(self, day):
        print(f'День {day:^5d} з життя {self.first_name}а')
        print(f'Настрій = {self.today_mood}')
        print(f'Ситість = {self.today_satiety}')
        print(f'Знання = {round(self.knowledge, 2)}')

    def pause(self):
        if self.today_mood < 5:
            self.rest_time()
        elif self.energy < 5:
            self.sleep()
        elif self.knowledge < 5:
            self.study()
        elif self.today_satiety < 5:
            self.lunch()


student = Pause('школярик')
for day in range(1, 365):
    student.pause()
    student.get_today(day)

print(Life)
