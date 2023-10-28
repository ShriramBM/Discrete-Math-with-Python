

def multipleGCD(arr:list)->int:
    result:int = -1
    for i in range(1, len(arr)):
        result =  gcd(arr[i-1], arr[i])
    return result

def gcd(a:int , b:int)->int:
    return b if a%b ==0 else gcd(b, a%b)

print(multipleGCD([34 ,88, 288]))