from faker import Faker
import random
from datetime import datetime

from department.models import Department
from .models import Worker


dep_levels = ['level_1', 'level_2', 'level_3', 'level_4', 'level_5']


def departmentFactory():
    deps = []
    new_department = Department()
    new_department.name = dep_levels.pop(0)
    new_department.parent = None
    new_department.save()
    deps.append(new_department)
    try:
        for parent in deps:
            new_department = Department()
            if len(dep_levels) > 0:
                new_department.name = dep_levels.pop(0)
                new_department.parent = parent
                new_department.save()
                deps.append(new_department)
            else:
                print('List is empty')
    except:
        print('finish')


def workerFactory():
    departments = Department.objects.all()
    fake = Faker()
    for _ in range(10):
        new_worker = Worker()
        new_worker.department = random.choice(list(departments))
        new_worker.username = fake.name()
        new_worker.position = fake.job()
        new_worker.hire_date = fake.past_date(start_date="-30d", tzinfo=None)
        new_worker.salary = random.randint(100, 10000)
        new_worker.save()
