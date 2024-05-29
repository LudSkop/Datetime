

"""
 Іменовані кортежі. Клас collections.namedtuple() дозволяє створити тип даних що поводиться як кортеж
з можливістю привласнити кожному елементу імя яким надалі можно отримати доступ.

"""


import collections

Dog = collections.namedtuple('Dog', ['nickname', 'age', 'owner'])
dog_object = Dog('Marsik','5','Oleg')
print(dog_object.nickname)
print(dog_object.age)
print(dog_object.owner)
print(type(dog_object))
