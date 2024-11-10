from Crypto.Util.number import *
flag="soner"

def gen(nbit, m):
    kbit = int(nbit * 0.4512) #462
    key =11701945964602377416372683570803762031619787880266814501076957212783115025902453320312953073432148499720225114478097149152175920815742924751 #random prime num with 462 bits long 
    
    while True:
        p = 5524436632391725899655614688750718389982655058072467442056401232078782690541548862368693631294558141434295603434246328253977092862697595058142581804793649 #511 bit long random prime number
        if isPrime(p * 2 + 1):
            p = p * 2 + 1
            break
    while True:
        q = 6610489706930091732643196315936825565982006006793165657962615783311792689792898043559081802901791220283898537388034513798495729274236166561865157103410519#511 bit long random prime number
        if isPrime(q * 2 + 1):
            q = q * 2 + 1
            break   
    n = p * q
    print("n:", n)
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
"""n, e, k = gen(1024, 12)
enc = pow(bytes_to_long(flag.encode()), 65537, n)"""

"""with open("data.txt","w") as f:
    print(f"{n = }\n{enc = }\n{e = }\n{k = }\n")"""

enc = pow(bytes_to_long(flag.encode()), 65537, n)
print(enc)