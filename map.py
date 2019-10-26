def get_number(x, y):
    num = 0
    if(0<x<101 and 0<y<101):
        num = 0
    elif(100<x<200 and 5<y<100):
        num = 1
    elif(200<x<300 and 10<y<100):
        num = 2
    elif(0<x<101 and 100<y<201):
        num = 3
    elif(105<x<195 and 100<y<195):
        num = 4
    elif(100<x<290 and 100<y<190):
        num = 5
    elif(5<x<100 and 200<y<290):
        num = 6
    elif(105<x<195 and 200<y<290):
        num = 7
    elif(200<x<295 and 200<y<295):
        num = 8
    elif(300<x<700 and 50<y<150):
        num = 9
    elif(235<x<735 and 150<y<250):
        num = 10
    return num

def get_pos_from_number(number):
#숫자가 들어오면 좌표를 내보내는 것
    if (number == 0):
        location =(10,10)
    elif(number == 1):
        location = (100,10)
    elif(number == 2):
        location = (200,10)
    elif(number == 3):
        location = (10,100)
    elif(number == 4):
        location = (100,100)
    elif(number == 5):
        location = (200,100)
    elif(number == 6):
        location = (10,200)
    elif(number == 7):
        location = (100,200)
    elif(number == 8):
        location = (200,200)
    return location
