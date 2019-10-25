#영화 선호도 표시(2개)
from math import sqrt

critics ={
    'Hen':{'guardians of th glaxy 2':5,'christmas in august':4,'boss baby':1.5},
    'Rim':{'christmas in august':5,'boss baby':2},
    'Min':{'guardians of th glaxy 2':2.5,'christmas in august':2,'boss baby':1},
    'Sou':{'guardians of th glaxy 2':3.5,'christmas in august':4,'boss baby':5}
}
#처음
'''
#Rim&Hen
ch_bs = critics.get('Rim').get('boss baby')
hhd_bs= critics.get('Hen').get('boss baby')
num = ch_bs-hhd_bs

ch_bs = critics.get('Rim').get('christmas in august')
hhd_bs= critics.get('Hen').get('christmas in august')
num_2 = ch_bs-hhd_bs

print('Hen:',1/(1+sqrt((pow(num,2))+pow(num_2,2))))

#Rim&Min
ch_bs = critics.get('Rim').get('boss baby')
hhd_bs= critics.get('Min').get('boss baby')
num = ch_bs-hhd_bs

ch_bs = critics.get('Rim').get('christmas in august')
hhd_bs= critics.get('Min').get('christmas in august')
num_2 = ch_bs-hhd_bs

print('Min:',1/(1+sqrt((pow(num,2))+pow(num_2,2))))

#Rim&Sou
ch_bs = critics.get('Rim').get('boss baby')
hhd_bs= critics.get('Sou').get('boss baby')
num = ch_bs-hhd_bs

ch_bs = critics.get('Rim').get('christmas in august')
hhd_bs= critics.get('Sou').get('christmas in august')
num_2 = ch_bs-hhd_bs

print('Sou:',1/(1+sqrt((pow(num,2))+pow(num_2,2))))
'''
#처음을 짧게 만든 것과 높은 평점
def sim(num1,num2):
    return 1/(1 + sqrt((pow(num1,num2))+pow(num2,2)))
k = 0
temp = 0
for i in critics:
    if(i != 'Rim'):
        num1 = critics.get('Rim').get('christmas in august')-critics.get(i).get('christmas in august')
        num2 = critics.get('Rim').get('boss baby')-critics.get(i).get('boss baby')
        if(k<sim(num1,num2)):
            k = sim(num1,num2)
            temp = i
        print(i," :",sim(num1,num2))
print('가장 높은 평점은?:',critics.get(temp).get('guardians of th glaxy 2'))