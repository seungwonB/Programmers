import math

def solution(w,h):
    # w, h를 최대공약수로 나누어 w', h'를 만듦
    # w' * h'에서 잘려나가는 격자의 개수는 w'+h'-1임.
    # 제외되는 격자의 수는 w'+h'-1 * 최대공약수
    gcd_wh = math.gcd(w,h)
    ww = w/gcd_wh
    hh = h/gcd_wh
    
    return (w*h) - (gcd_wh * ((ww+hh)-1))
    