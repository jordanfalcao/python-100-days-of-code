# def add(*num):
#     sum = 0
#     for n in num:
#         sum += n
#     print(sum)
#
# add(3, 5, 7, 2, 8)

class Car():
    def __init__(self, **kw):  # **kwargs, all they are optional
        self.make = kw['make']
        self.model = kw.get('model')  # .get still works, but it doesn't return error


my_car = Car(make='Hyundai')
print(my_car.make)
