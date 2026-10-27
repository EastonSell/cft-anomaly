"""Physical sharpness at all k from explicit neighboring Narain codes.

Run: python verify_bell_recursion.py

The all-k conclusion uses the Bell-product identity proved in the paired
note; this program verifies the two literal seed codes, implements the
recursive generator construction, and exactly enumerates the k=3 instance.
Only Python's standard library is required.
"""
from math import comb, factorial


def xor_rank(vectors):
    piv={}
    for v in vectors:
        while v:
            i=v.bit_length()-1
            if i in piv:
                v ^= piv[i]
            else:
                piv[i]=v
                break
    return len(piv)


class Pair:
    def __init__(self,n,S,a,ap):
        self.n,self.S,self.a,self.ap=n,S,a,ap
        self.h=2*n
        self.mask=(1<<self.h)-1

    def wt(self,v):
        return sum(((v>>(2*i))&3)!=0 for i in range(self.n))

    def q(self,v):
        return (self.wt(v & self.mask)+self.wt(v>>self.h))%2

    def b(self,v,w):
        return self.q(v^w)^self.q(v)^self.q(w)

    def check(self):
        assert len(self.S)==self.h-1 and xor_rank(self.S)==self.h-1
        assert xor_rank(self.S+[self.a])==self.h
        assert xor_rank(self.S+[self.ap])==self.h
        assert all(0<=v<(1<<(2*self.h)) and self.q(v)==0
                   for v in self.S+[self.a,self.ap])
        assert all(self.b(v,w)==0 for v in self.S
                   for w in self.S+[self.a,self.ap])
        assert self.b(self.a,self.ap)==1

    def matrix(self,which):
        gens=self.S+([self.a] if which==0 else [self.ap])
        words=[0]
        for v in gens:
            words += [x^v for x in words]
        assert len(words)==len(set(words))==1<<self.h
        weights=[0]*(1<<self.h)
        for i in range(1,len(weights)):
            weights[i]=weights[i>>2]+int(i&3 != 0)
        out=[[0]*(self.n+1) for _ in range(self.n+1)]
        for v in words:
            l,r=weights[v&self.mask],weights[v>>self.h]
            assert (l+r)%2==0
            out[l][r]+=1
        assert out[0][0]==1
        return out


def neighbor(n,basis,f,replacement):
    p=(f & -f).bit_length()-1
    a=basis[p]
    S=[v^(a if (f>>i)&1 else 0) for i,v in enumerate(basis) if i!=p]
    result=Pair(n,S,a,replacement)
    result.check()
    return result


def bell(A,B):
    n=A.n+B.n
    newh=2*n
    def embed_a(x):
        return (x & A.mask) | ((x>>A.h)<<newh)
    def embed_b(x):
        return ((x & B.mask)<<A.h) | ((x>>B.h)<<(newh+A.h))
    S=([embed_a(v) for v in A.S]+[embed_b(v) for v in B.S]
       +[embed_a(A.a^A.ap)^embed_b(B.a^B.ap)])
    a=embed_a(A.a)^embed_b(B.a)
    ap=embed_a(A.a)^embed_b(B.ap)
    out=Pair(n,S,a,ap)
    out.check()
    return out


def difference(P):
    m0,m1=P.matrix(0),P.matrix(1)
    return [[x-y for x,y in zip(row0,row1)] for row0,row1 in zip(m0,m1)]


def expected(n,sign=1):
    r=n if n%2==0 else n-1
    out=[[0]*(n+1) for _ in range(n+1)]
    for j in range(r+1):
        d=sign*((-1)**j)*comb(r,j)
        out[j][r-j]+=d
        if n%2:
            out[j+1][r-j+1]+=3*d
    return out


basis2=[4280689,4003343,13490061,15943387,4783610,4517512,
        8704049,3143493,9304945,11135812,2974764,11955798]
pair2=neighbor(6,basis2,30,5138)
basis1=[(1<<i)|(1<<(6+i)) for i in range(6)]
pair1=neighbor(3,basis1,10,5)
assert difference(pair2)==expected(6,1)
assert difference(pair1)==expected(3,-1)
print('PASS: k=1 and k=2 seed code identities and neighbor conditions')

pair3=bell(pair2,pair1)
assert difference(pair3)==expected(9,-1)
print('PASS: explicit k=3 pair has difference -W^8 Z_D4 at all levels')
print('k3 common 17 generators:',pair3.S)
print('k3 a, a-prime:',pair3.a,pair3.ap)
print('first eighth spin-moment difference:',-(8**8)*factorial(8))

# Validate the recursive algebraic generator formula without enumerating
# exponentially many words. All k use the Bell identity from the note.
current=pair2
for k in range(4,13,2):
    current=bell(current,pair2)
    assert current.n==3*k
    odd=bell(current,pair1)
    assert odd.n==3*(k+1)
print('PASS: recursive isotropy, rank, and neighbor checks through k=13')
