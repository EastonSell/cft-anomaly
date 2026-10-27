"""Exact small-ring diagnostics for the proposed CZX entanglement theorem.

All phase, eigenspace, orthogonality, and reduced-purity checks use exact
integer-valued complex arithmetic.  The finite block checks are diagnostics,
not a proof for all L; see the manuscript for the analytic argument.
"""
from itertools import product
from math import log, sqrt


def bits(x, n):
    return tuple((x >> (n-1-j)) & 1 for j in range(n))


def phase(b):
    return sum(b[j]*b[(j+1) % len(b)] for j in range(len(b))) % 2


def triangle(x):
    a,b,c=x
    return (a+a*b+b*c+c*a) % 2


def check_blocks():
    total=0
    for L in (4,6,8,10):
        count=0
        for la in range(1,L-1):
            for lb in range(1,L-la):
                lc=L-la-lb
                starts=(0,la,la+lb)
                remaining=[i for i in range(L) if i not in starts]
                groups=([*range(la)],[*range(la,la+lb)],[*range(la+lb,L)])
                for pattern in product((0,1), repeat=L-3):
                    base=[0]*L
                    for i,value in zip(remaining,pattern):base[i]=value
                    q={}
                    for u in product((0,1),repeat=3):
                        b=base.copy()
                        for region,flip in zip(groups,u):
                            for i in region:b[i]^=flip
                        q[u]=phase(b)
                    q0=q[(0,0,0)]
                    ell=tuple(q[tuple(int(i==j) for i in range(3))]^q0
                              for j in range(3))
                    assert sum(ell)%2==1
                    for u,v in q.items():
                        a,b,c=u
                        expect=(q0+sum(e*x for e,x in zip(ell,u))
                                +a*b+b*c+c*a)%2
                        assert v==expect
                        assert v==q[tuple(1-x for x in u)]
                    # Encoded local X conjugations send the odd linear part
                    # to the canonical choice, up to one global sign.
                    good=False
                    for t in product((0,1),repeat=3):
                        diff={q[tuple(x^y for x,y in zip(u,t))]^triangle(u)
                              for u in q}
                        if len(diff)==1:good=True;break
                    assert good
                    count+=1
        total+=count
        print(f'L={L}: {count} complement blocks and all cuts pass')
    print(f'PASS: {total} blocks in total')


def U(v):
    out=[0j]*8
    for i,value in enumerate(v):out[i^7]+=(-1)**triangle(bits(i,3))*value
    return out


def dot(a,b):
    return sum(x.conjugate()*y for x,y in zip(a,b))


def reduced(v, which):
    m=[[0j,0j],[0j,0j]]
    for i,vi in enumerate(v):
        bi=bits(i,3)
        for j,vj in enumerate(v):
            bj=bits(j,3)
            if all(bi[r]==bj[r] for r in range(3) if r!=which):
                m[bi[which]][bj[which]]+=vi*vj.conjugate()
    return m


def tr_square(m):
    return sum(m[i][j]*m[j][i] for i in range(2) for j in range(2))


def mul(a,b):
    return [[sum(a[i][t]*b[t][j] for t in range(8))
             for j in range(8)] for i in range(8)]


def dagger(a):
    return [[a[j][i].conjugate() for j in range(8)] for i in range(8)]


def pauli(which,typ):
    m=[[0j]*8 for _ in range(8)]
    for i in range(8):
        bit=bits(i,3)[which]
        target=i^(1<<(2-which)) if typ in 'XY' else i
        factor={'X':1,'Y':1j*(-1)**bit,'Z':(-1)**bit}[typ]
        m[target][i]=factor
    return m


def check_anticommutators():
    ident=[[int(i==j) for j in range(8)] for i in range(8)]
    z=[[0j]*8 for _ in range(8)]
    Utri=[[0j]*8 for _ in range(8)]
    for i in range(8):
        a,b,c=bits(i,3)
        Utri[i^7][i]=1j*(-1)**(a*b+b*c+c*a)
    assert mul(Utri,Utri)==ident
    for a in range(3):
        others=[i for i in range(3) if i!=a]
        for typ,sgn in (('X',1),('Y',-1)):
            op=pauli(a,typ)
            got=mul(mul(Utri,op),dagger(Utri))
            expected=mul(mul(op,pauli(others[0],'Z')),pauli(others[1],'Z'))
            expected=[[sgn*val for val in row] for row in expected]
            assert got==expected
            for other in others:
                for other_typ in ('X','Y'):
                    q=pauli(other,other_typ)
                    ab,ba=mul(got,q),mul(q,got)
                    assert [[ab[i][j]+ba[i][j] for j in range(8)]
                            for i in range(8)]==z
        conjz=mul(mul(Utri,pauli(a,'Z')),dagger(Utri))
        assert conjz==[[-v for v in row] for row in pauli(a,'Z')]
    print('PASS: encoded symmetry conjugation and pairwise anticommutators')


def check_saturators():
    bal=[1,1,1,1j,-1j,1,1,1]
    assert U(bal)==bal and dot(bal,bal)==8
    for j in range(3):
        r=reduced(bal,j)
        assert r[0][0]==4 and r[1][1]==4
        assert r[0][0]*r[1][1]-r[0][1]*r[1][0]==8
    # The four even-pair-Z images are orthogonal and remain in the + sector.
    balanced=[]
    for mask in (0,3,5,6):
        v=[x*(-1)**((i&mask).bit_count()) for i,x in enumerate(bal)]
        assert U(v)==v
        assert all(dot(v,w)==0 for w in balanced)
        balanced.append(v)

    bell=[[1,1,0,0,0,0,1,1], [1,-1,0,0,0,0,-1,1],
          [0,0,1,1j,-1j,1,0,0], [0,0,1,-1j,1j,1,0,0]]
    for i,v in enumerate(bell):
        assert U(v)==v and dot(v,v)==4
        assert all(dot(v,w)==0 for w in bell[:i])
        purities=[tr_square(reduced(v,j)) for j in range(3)]
        assert purities==[8,8,16]
    p=(2+sqrt(2))/4
    h=-p*log(p)-(1-p)*log(1-p)
    print('PASS: explicit balanced and party-Bell sector bases;')
    print('candidate E3 (natural logs) =',1.5*h)
    print('balanced weight threshold wmax/W =',1-h/log(2))


if __name__=='__main__':
    check_blocks()
    check_anticommutators()
    check_saturators()
    print('Finite diagnostics only; independent proof and prior-art review required.')
