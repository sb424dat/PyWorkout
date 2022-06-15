name = 'world'
print(f'Hello, {name}')

x = 100
y = 'abcd'
print(f'x * 2 = {x*2}, and y.capitalize() is {y.capitalize()}')

first = 'Reuven'
last = 'Lerner'
print(f'Hello, {first:#<10} {last:#>10}')

def mysum(*numbers):
   output = 0
   for number in numbers:
           output += number
   return output

print(mysum(10, 20, 30, 40))
print(mysum(10, 20, 30, 40, 50))