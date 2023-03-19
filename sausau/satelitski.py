class HipSlog:
    def __init__(self, kljuc, podaci):
        self.kljuc = kljuc
        self.podaci = podaci

class HipSaPodacima:
    def __init__(self):
        self.A = []

    def __repr__(self):
        return "HipSaPodacima: " + " ".join(str(e.kljuc) for e in self.A)

def roditelj(i):
    return i // 2

def levoDete(i):
    return 2 * i

def desnoDete(i):
    return 2 * i + 1

def reorganizujHip(A, i):
    n = len(A)
    l = levoDete(i)
    d = desnoDete(i)
    najveci = l if l <= n and A[i-1].kljuc < A[l-1].kljuc else i
    if d <= n and A[najveci-1].kljuc < A[d-1].kljuc:
        najveci = d
    if najveci != i:
        A[i-1], A[najveci-1] = A[najveci-1], A[i-1]
        reorganizujHip(A, najveci)

def maksimum(h):
    if len(h.A) > 0:
        return h.A[0].kljuc
    else:
        raise Exception("Hip nema elemenata")

def izdvojMaksimum(h):
    if len(h.A) < 1:
        raise Exception("Hip nema elemenata")
    prvi = h.A[0]
    h.A[0] = h.A[-1]
    h.A.pop()
    reorganizujHip(h.A, 1)
    return prvi.kljuc, prvi.podaci

def dodaj(h, kljuc, podaci):
    inf = -2**63
    hs = HipSlog(inf, podaci)
    h.A.append(hs)
    povecajKljuc(h, len(h.A), kljuc)

def povecajKljuc(h, i, kljuc):
    if kljuc < h.A[i-1].kljuc:
        raise Exception("Nedovoljna vrednost ključa")
    h.A[i-1].kljuc = kljuc
    while i > 1 and h.A[roditelj(i)-1].kljuc < h.A[i-1].kljuc:
        k = roditelj(i)
        h.A[k-1], h.A[i-1] = h.A[i-1], h.A[k-1]
        i = k

##########
# Primer

class Slog:
    def __init__(self, a, b):
        self.a = a
        self.b = b

h = HipSaPodacima()
dodaj(h, 1, Slog(10,11))
dodaj(h, 10, Slog(100,101))
dodaj(h, 100, Slog(1000,1001))
dodaj(h, 21, Slog(21,211))

print(h)
print(h.A)
print(h.A[2].podaci.a)

povecajKljuc(h,3,31)
m = maksimum(h)
print(h)
print(izdvojMaksimum(h))
