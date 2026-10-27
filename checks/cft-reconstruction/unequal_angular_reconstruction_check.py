"""Exact probes for the unequal-central-charge extension, not an all-k proof."""
from fractions import Fraction as F
from math import comb
from angular_reconstruction_check import product, independent


def ordered_group(p):
    d = 3*p
    n = d+1
    i = tuple(tuple(int(a == b) for b in range(n)) for a in range(n))
    s = tuple(tuple((-1)**a*comb(b,a) if a <= b else 0
                    for b in range(n)) for a in range(n))
    t = tuple(tuple((-1)**((a-p)%2)*comb(d-b,a-b) if b <= a else 0
                    for b in range(n)) for a in range(n))
    st, ts = product(s,t), product(t,s)
    out = (i,s,t,st,ts,product(st,s))
    assert len(set(out)) == 6
    return out


def basis(p,q):
    a,b=ordered_group(p),ordered_group(q)
    nl,nr=3*p+1,3*q+1
    def avg(c,d):
        return [sum(a[z][i][c]*b[z][j][d] for z in range(6))
                for i in range(nl) for j in range(nr)]
    return independent(avg(c,d) for c in range(nl) for d in range(nr))


def jets(v,p,q,x,r):
    nl,nr=3*p+1,3*q+1
    z=F(0)
    for a in range(nl):
        for b in range(nr):
            if not v[a*nr+b] or a+b < r:
                continue
            c=sum((-1)**h*comb(a,r-h)*comb(b,h) for h in range(r+1)
                  if h <= b and r-h <= a)
            z += v[a*nr+b]*c*x**(a+b-r)
    return z


def rankcheck(p,q):
    k=(p+q)//2
    b=basis(p,q)
    pivot=next(v for v in b if v[0])
    b=independent([[x-v[0]/pivot[0]*y for x,y in zip(v,pivot)] for v in b])
    nr=3*q+1
    assert all(v[0] == v[1] == v[nr] == 0 for v in b)
    max_order=3*min(p,q)
    rows=[[jets(v,p,q,F(1,j),r) for v in b]
          for j in range(2,k+2) for r in range(max_order+1)]
    rank=len(independent(rows))
    assert rank == len(b)
    print(f'(p,q)=({p},{q}): fixed-vacuum dimension={len(b)}, rank={rank}')


def top(p,q,x,y):
    assert p>q and (p-q)%2 == 0
    m=(p-q)//2
    b=(1-x+x*x)**3
    a=x*(1-x)*(2*x-1)*(x+1)*(x-2)
    polynomial=b**m if q%2 == 0 else a*b**(m-1)
    return (x-y)**(3*q)*polynomial/((x*(1-x))**p*(y*(1-y))**q)


def test_top():
    for p,q in [(3,1),(5,1),(4,2),(6,2),(5,3)]:
        for x,y in [(F(1,3),F(1,4)),(F(2,5),F(3,7))]:
            f=top(p,q,x,y)
            assert f != 0
            assert f == top(p,q,1-x,1-y)
            assert f == top(p,q,x/(x-1),y/(y-1))
    print('Unequal top-order kernels: exact S,T checks PASS')


if __name__ == '__main__':
    for p,q in [(3,1),(1,3),(4,2),(2,4),(5,1)]:
        rankcheck(p,q)
    test_top()
