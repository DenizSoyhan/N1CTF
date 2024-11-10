from Crypto.Util.number import *
flag="soner"

def gen(nbit, m):
    kbit = int(nbit * 0.4512) #462
    key = getPrime(kbit) #random prime num with 462 bits long 
    
    while True:
        p = getPrime(nbit // 2 - 1) #511 bit long random prime number
        if isPrime(p * 2 + 1):
            print("firstP: " ,p)
            p = p * 2 + 1
            print("secondP: " ,p)
            break

    while True:
        q = getPrime(nbit // 2 - 1)#511 bit long random prime number
        if isPrime(q * 2 + 1):
            print("firstQ: " ,q)
            q = q * 2 + 1
            print("secondQ: " ,q)
            break   
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e, k = [], []
    for i in range(m):
        dd = key + 2 * i + 2
        ee = inverse(dd, phi)
        kk = (ee * dd - 1) // phi #an integer value
        e.append(ee % 2 ** (nbit - kbit))
        k.append(kk)
    
    return n, e, k

n, e, k = gen(1024, 12)
enc = pow(bytes_to_long(flag.encode()), 65537, n)
"""
with open("data.txt","w") as f:
    print(f"{n = }\n{enc = }\n{e = }\n{k = }\n")"""
"""n=99345524792842167764664160165134777663365760824986332338968400372165410475730304747903560096687030936528630416833184938273413670854910531882417741259241319650651925387742200353246334965830925187667489846053240543293868669431359887365912062914529521790577630534962758070045016889637661875180188423624316276329
enc = pow(bytes_to_long(flag.encode()), 65537, n)
print(enc)"""