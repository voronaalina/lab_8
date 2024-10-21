import numpy as np

M = int(input("введіть кількість рядків M: "))
N = int(input("введіть кількість стовпців N: "))

#діапазон [1,20]
masiv = np.zeros((M,N))
for i in range(M):
    for j in range(N):
        masiv[i][j]=np.random.randint(1,21)

print(masiv)

max_index = np.argmax(np.sum(masiv, axis=1))

print("рядок з найбільшою сумою елементів:", masiv[max_index])