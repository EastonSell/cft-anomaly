"""Finite-size checks of positive and Wang-Santos-Wen link branches."""
import itertools
import numpy as np

for n in (3,4):
    omega=np.exp(2j*np.pi/n)
    xi=np.exp(2j*np.pi/n**2)
    sizes=(3,4,5) if n==3 else (3,4)
    for L in sizes:
        states=list(itertools.product(range(n),repeat=L))
        idx={v:i for i,v in enumerate(states)}
        dim=n**L
        for p in range(1,n):
            for branch in ('positive','published'):
                U=np.zeros((dim,dim),complex)
                for j,g in enumerate(states):
                    diffs=[(g[(i+1)%L]-g[i])%n for i in range(L)]
                    power=sum(diffs) if branch=='positive' else sum(d-n*(d!=0) for d in diffs)
                    U[idx[tuple((x+1)%n for x in g)],j]=xi**(p*power)
                assert np.allclose(np.linalg.matrix_power(U,n),np.eye(dim),atol=1e-10)
                for charge in range(n):
                    R=sum(omega**(-charge*k)*np.linalg.matrix_power(U,k) for k in range(n))/dim
                    for cut in range(1,L):
                        da,db=n**cut,n**(L-cut)
                        pt=R.reshape(da,db,da,db).transpose(2,1,0,3).reshape(dim,dim)
                        norm=np.abs(np.linalg.eigvalsh(pt)).sum()
                        assert norm>1+1e-9,(n,L,p,branch,charge,cut,norm)
                        if n==3: assert np.isclose(norm,(5+8*np.cos(np.pi/9))/9,atol=1e-10)
                    print(n,L,p,branch,charge,'all connected cuts NPT; last norm',round(norm,12),flush=True)
