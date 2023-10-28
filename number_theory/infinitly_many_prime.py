
def multiplication(p:list):
    res:int = 1
    for i in p:
        res*=i
    return res

def generatingPrime(p:list) -> list:
    for i in range(0,6):    
        p.append(multiplication(p)+1)
        print(p," ->  ",multiplication(p)+1)
    


prime = [2]

generatingPrime(prime)