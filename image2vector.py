import cv2

def resize():
    src = cv2.imread('images/2.png', cv2.IMREAD_COLOR)
    dst = cv2.resize(src, (28, 28), interpolation=cv2.INTER_AREA)
    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

resize()