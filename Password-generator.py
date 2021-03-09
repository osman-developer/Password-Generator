import string
import random

lower ="abcdefghijklmnopqrstuvwxyz"
upper ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number ="0123456789"
symbol ="[]{}()*;/,_-"

combo = lower+upper+number+symbol;
length = 20
password ="".join(random.sample(combo,length))
print (password)