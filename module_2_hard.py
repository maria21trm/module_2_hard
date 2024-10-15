import random
list_divisible = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
random_values= random.sample(list_divisible,len(list_divisible))
for k in random_values:
    string = ''
    for i in range(1,k ):
        for j in range(i+ 1,k):
            if k % (i + j) == 0 :
                string += str(i) + str(j)
                print(k,'-',string)




