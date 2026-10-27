import numpy as np
from itertools import product
for N in range(3,9):
 for p in range(1,N):
  t=np.exp(2j*np.pi*p/N)
  d=abs(1-t)**2
  lower=d/(N*N*(2+d))
  for h in range(N):
   U=np.zeros((N*N,N*N),complex)
   for a,b in product(range(N),repeat=2):
    r=(b-a)%N
    U[N*((a+1)%N)+(b+1)%N,N*a+b]=(1 if r<=h else t)
   Up=np.eye(N*N,dtype=complex);rho=np.zeros_like(U)
   for k in range(N):
    rho+=Up/N**2
    Up=U@Up
   assert np.allclose(Up,np.eye(N*N))
   pt=rho.reshape(N,N,N,N).transpose(2,1,0,3).reshape(N*N,N*N)
   eig=np.linalg.eigvalsh(pt)
   if h<N-1:
    s=(1 if h==0 else (h+2)%N)
    inds=[N*i+(s-i)%N for i in range(3)]
    m=pt[np.ix_(inds,inds)]
    assert np.isclose(np.linalg.det(m),-d/N**6,atol=1e-15), (N,p,h,np.linalg.det(m))
    assert eig[0]<=-lower+1e-12, (N,p,h,eig[0],lower)
   else:
    assert eig[0]>-1e-12
 print(f'N={N}: all p and h checked')
print('all general-h checks pass')
