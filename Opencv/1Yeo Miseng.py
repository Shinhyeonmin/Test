#사진 편집
import cv2
'''
cv2.imshow('COLOR',img)
cv2.imshow('Gray',w_b)
cv2.imshow('pure',clean)

cv2.imwrite('change1.jpg',w_b)
'''
def nam(change_name,img):

    cv2.imshow('COLOR', img)
    cv2.imwrite(change_name, img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

a = '/home/shinhyeonmin/Kail/hanguel.png'

while(True):
    b = raw_input()
    print(b)
    img = cv2.imread(a, cv2.IMREAD_COLOR)
    height, width, channel = img.shape

    w_b = cv2.imread(a,cv2.IMREAD_GRAYSCALE)
    clean = cv2.imread(a, cv2.IMREAD_UNCHANGED)
    small = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    zoom = cv2.resize(img,(width*2,height*3),interpolation=cv2.INTER_CUBIC)
    M = cv2.getRotationMatrix2D((height / 2, width / 2), 130, 0.5)
    rot = cv2.warpAffine(img, M, (height, width))

    if(b == 'COLOR'):
        nam('color.jpg',img)
    elif(b == 'GRAY'):
        nam('gray.jpg',w_b)

    elif(b == 'PURE'):
        nam('pure.jpg',clean)

    elif(b == 'small'):
        nam('small.jpg',small)

    elif(b == 'zoom'):
        nam('zoom.jpg',zoom)

    elif(b == 'rot'):
        nam('rot.jpg',rot)
    '''
    cv2.imshow('resize',small)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    height,width = w_b.shape
    '''

