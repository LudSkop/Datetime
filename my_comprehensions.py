"""
list Comprehensions[] дозволяє нам в один рядок заповнити
список простими або складними значеннями.
"""
even_nums = []

for x in range(21):
    if x % 2 == 0:
        even_nums.append(x)
print(even_nums)
a = [element for element in range(21) if element % 2 == 0]
print(a)
b = ['парне'if element % 2 == 0 else 'не парне' for element in range(21)]
print(b)
