guessesTaken = 0

print('hi what is your name')

Name = input()
print('well, ' + Name + ' say a number')
number = input()

print('cool say another one')
anotherone = input()

print('well, ' + Name + ' what is ' + number + '+' + anotherone + ' okay') 
anwser = number + anotherone
for guessesTaken in range(7):
guess = input()
g