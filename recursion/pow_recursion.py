# Быстрое возведение в степень
def pow(a: float, n:int):
    if n==0:
        return 1
    else:
        return pow(a, n-1)*a

# Для того чтобы сделать логарифмическую сложность сделаем еще одно условие для четных степеней

def quick_pow(a:float, n:int):
    if n==0:
        return 1
    elif n%2 ==1: # нечет
        return quick_pow(a, n-1)*a
    else: # четное
        return quick_pow(a**2, n//2)


#print(quick_pow(12.3, 177))
print(pow(12.3, 277))