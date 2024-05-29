

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

temp = [1.3, 0.0, -0.5, -0.5, 0.0, -1.3, -1.3, -1.3]
tem = collections.Counter(temp)
print(tem)                #Counter({-1.3: 3, 0.0: 2, -0.5: 2, 1.3: 1})
print(tem.most_common(3)) #[(-1.3, 3), (0.0, 2), (-0.5, 2)]
print(tem.most_common(1)) #[(-1.3, 3)]

