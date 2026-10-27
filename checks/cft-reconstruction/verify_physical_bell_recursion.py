"""Independent exact certificate for the physical all-k Bell-gluing family.

Only standard-library arithmetic is used.  The k=1 seed is constructed
directly from the D8 extension, independently of the matrix-team script;
the neighboring k=2 seed uses the separately verified f=30 replacement.
The program checks every basis and coset, exact seed identities, the full
k=3 code enumerator, and recursive rank/isotropy through k=13. The proof
that the Bell identity holds for arbitrary k is algebraic, not numerical.
"""
from math import comb, factorial

def rank(vectors):
    pivot = {}
    for v in vectors:
        while v:
            lead = v.bit_length()-1
            if lead in pivot:
                v ^= pivot[lead]
            else:
                pivot[lead]=v
                break
    return len(pivot)

def q(v, n):
    return sum(((v >> (2*i)) & 3) != 0 for i in range(2*n)) % 2

def b(v, w, n):
    return sum(((v >> (2*i)) & 3) != 0 and
               ((w >> (2*i)) & 3) != 0 and
               ((v >> (2*i)) & 3) != ((w >> (2*i)) & 3)
               for i in range(2*n)) % 2

def validate(pair):
    n,S,a,ap = pair
    assert len(S)==2*n-1 and rank(S)==2*n-1
    assert rank(S+[a])==rank(S+[ap])==2*n
    assert all(0 <= v < (1 << (4*n)) and q(v,n)==0 for v in S+[a,ap])
    assert all(b(v,w,n)==0 for v in S for w in S+[a,ap])
    assert b(a,ap,n)==1

def matrix(pair, use_prime):
    n,S,a,ap = pair
    basis=S+[ap if use_prime else a]
    words=[0]
    for g in basis:
        words += [v^g for v in words]
    assert len(set(words))==2**(2*n)
    weights=[0]*(1 << (2*n))
    for v in range(1,len(weights)):
        weights[v]=weights[v >> 2]+int(v&3 != 0)
    mask=(1 << (2*n))-1
    out=[[0]*(n+1) for _ in range(n+1)]
    for v in words:
        left,right=weights[v&mask],weights[v>>(2*n)]
        assert (left+right)%2==0
        out[left][right]+=1
    assert out[0][0]==1
    return out

def difference(pair):
    m1,m2=matrix(pair,False),matrix(pair,True)
    return [[a-b for a,b in zip(r1,r2)] for r1,r2 in zip(m1,m2)]

def bell(A,B):
    n1,S1,a1,ap1=A
    n2,S2,a2,ap2=B
    n=n1+n2
    mask1=(1<<(2*n1))-1
    mask2=(1<<(2*n2))-1
    def one(x):
        return (x & mask1) | ((x >> (2*n1)) << (2*n))
    def two(x):
        return ((x & mask2) << (2*n1)) | ((x >> (2*n2)) << (2*n+2*n1))
    S=([one(x) for x in S1]+[two(x) for x in S2]+
       [one(a1^ap1)^two(a2^ap2)])
    out=(n,S,one(a1)^two(a2),one(a1)^two(ap2))
    validate(out)
    return out

def expected(power, extra=False):
    n=power+int(extra)
    out=[[0]*(n+1) for _ in range(n+1)]
    for j in range(power+1):
        value=(-1)**j*comb(power,j)
        out[j][power-j]+=value
        if extra:
            out[j+1][power-j+1]+=3*value
    return out

def main():
    # D8_1 x D4_1 minus D4_1^3, so the difference is +W^2 Z_D4.
    one=(3,[65,260,650,1040,2080],320,130)
    validate(one)
    assert difference(one)==expected(2,True)

    # The independently verified neighboring k=2 codes, with difference +W^6.
    basis=[4280689,4003343,13490061,15943387,4783610,4517512,
           8704049,3143493,9304945,11135812,2974764,11955798]
    f=30
    pivot=1
    a=basis[pivot]
    S=[v ^ (a if (f>>i)&1 else 0) for i,v in enumerate(basis) if i!=pivot]
    two=(6,S,a,5138)
    validate(two)
    assert difference(two)==expected(6)
    print('PASS: explicit k=1 and k=2 neighboring seed spectra')

    three=bell(two,one)
    assert difference(three)==expected(8,True)
    print('PASS: all 262144 codewords in each k=3 code give +W^8 Z_D4')
    print('k=3 first differing eighth moment:',8**8*factorial(8))

    current=two
    for k in range(4,14,2):
        current=bell(current,two)
        assert current[0]==3*k
        odd=bell(current,one)
        assert odd[0]==3*(k+1)
    print('PASS: recursive neighbor ranks and isotropy through k=13')
    print('All-k moment and jet claims follow from the exact coset identity.')

if __name__=='__main__':
    main()
