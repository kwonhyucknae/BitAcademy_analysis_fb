'''
def squares(n=10):
    #0 부터 9 까지
    results=[]
    for i in range(n+1):
        results.append(i**2)

    return results
'''

def squares(n=10):
    #0 부터 9 까지
    results=[]
    for i in range(n+1):
        yield i**2

#yield는 루프가 끝날때까지 다시 올라가고?
#리스트를 완성 하지 않고 yield 를 쓰면 ??못들음



# in 뒤에는 리스트라던지 range 라던지 순서가 있는 콜렉터 객체가 나와야하는데 넘버값 하나가 나오니 에러
# 0~10부터 제곱한 값을 배열로 달라

#fb_fetch 는 통신을 해서 리스트에 담아서 리턴 , 즉 하는 행동은 똑같다


for x in [] <- squares(10):
    print(x)

