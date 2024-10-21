from array import *

n = input("введіть цілі числа через пробіл: ")
numbers = list(map(int, n.split()))
masiv = array('i', numbers)
sered_aryfm = sum(masiv)/len(masiv)

print("середнє арифметичне: ", sered_aryfm)
