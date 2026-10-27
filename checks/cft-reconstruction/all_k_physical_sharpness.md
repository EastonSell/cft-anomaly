# Physical sharpness of the angular cutoff for every k

## Result

For every integer `k>=1`, there are two compact unitary Narain CFTs with
unique vacuum, `c_L=c_R=12k`, integer total dimensions and integer spins,
whose thermal traces and state-spin moments of all orders below

    R_k = 3k     (k even),
    R_k = 3k-1   (k odd)                                    (1)

agree at every temperature, while their order-`R_k` moments differ.
Thus the angular cutoff `R_k` in [the manuscript](../../preprints/cft-reconstruction/source/main.tex)
is sharp **within actual CFTs for every k**, not only among formal modular
spectra. No claim is made here about finite-temperature sampling sharpness,
or about the existence of a vanishing primary level.

The exact partition-function differences, with a choice of orientation, are

    k=2m >= 2:  Z_+-Z_- = W^(6m),
    k=2m+1:     Z_+-Z_- = -W^(6m+2) Z_D4,                    (2)

where `W=U(tau)V(sigma)-V(tau)U(sigma)`, `Z_D4=U(tau)U(sigma)+
3V(tau)V(sigma)`, and `U,V` are the vacuum and a nonvacuum level-one D4
character. On the physical slice `sigma=-conj(tau)`, `W` vanishes to
first order on the thermal line. Moreover `W` and `Z_D4` have leading
expansions that show the first changed state/primary level is
`Delta=R_k/2=floor(3k/2)`, and the first changed order-`R_k` state-spin
moment is, respectively,

    +8^R_k R_k!     (k even),
    -8^R_k R_k!     (k odd).                                 (3)

The sign can of course be reversed by interchanging the two CFTs.

## Even unimodular code lattices

For `n` D4 factors on each chirality let `A_n=(F2^2)^(n,n)` be the
discriminant group of `D4^n (+) (-D4^n)`. In each two-bit block the zero
class has norm `0 mod 2`, and each of the other three has norm `1 mod 2`.
Write `q_n(x)` for the total norm parity and `B_n(x,y)=q_n(x+y)-q_n(x)-
q_n(y)` for the associated nondegenerate bilinear form. An isotropic
`2n`-dimensional subspace `C` of `A_n` is maximal. Its preimage in the
dual lattice is even unimodular of signature `(4n,4n)`: the base lattice
has determinant magnitude `4^(2n)`, while the glue has index `2^(2n)`.
It therefore defines a genuine `4n`-boson Narain CFT with the stated
properties. Triality makes its partition function the complete weight
enumerator of `C`, evaluated on the four coset characters `U,V,V,V`.

References for the physical lattice construction and character
decomposition include https://arxiv.org/abs/2312.16296 and
https://arxiv.org/abs/hep-th/0211230. Code and Narain-CFT connections
have substantial prior literature, e.g. https://arxiv.org/abs/2205.00025;
priority of the exact moment-sharpness construction is not established.

## Bell product of neighboring codes

Let `C=S+<a>` and `C'=S+<a'>` be two maximal isotropic subspaces in a
nondegenerate discriminant form. Assume their common subspace `S` has
codimension one in each. Then

    q(a)=q(a')=0,  B(a,S)=B(a',S)=0,  B(a,a')=1.          (4)

For the last identity, `S^perp/S` is a hyperbolic plane; its two
distinct nonzero isotropic lines pair to one. Let `D=T+<b>` and
`D'=T+<b'>` be another such pair. Define two subspaces of the direct sum:

    E_+ = S (+) T (+) <(a,b),(a',b')>,
    E_- = S (+) T (+) <(a,b'),(a',b)>.                    (5)

All four displayed generators are isotropic, and the pairings of each
displayed pair vanish because `1+1=0` in F2. Their dimensions equal half
that of the total discriminant space, so both are maximal isotropic. Their
intersection is exactly

    (S (+) T) (+) <(a+a',b+b')>,                            (6)

which has codimension one in each; the output is again a neighboring
pair, so the operation may be iterated.

Let `Theta_{S+a}` denote the D4-coset character sum of a code coset.
The complete weight enumerator is multiplicative under direct sum.
Expanding the four cosets of each `E_+` and `E_-`, the common terms
cancel and give the exact identity

    Z(E_+)-Z(E_-)
      = (Theta_{S+a}-Theta_{S+a'})(Theta_{T+b}-Theta_{T+b'})
      = (Z(C)-Z(C'))(Z(D)-Z(D')).                          (7)

Equation (7) is an equality of full angular partition functions, not
just a finite coefficient check or a statement about the thermal line.

## Explicit seeds and recursion

Encode a codeword by `left + 2^(2n) right`, with two-bit blocks in order.
If `v_i` are independent isotropic code generators and `f` is a nonzero
binary mask, let `p` be its least set-bit position and set

    a=v_p,
    S=span{v_i + f_i v_p : i != p}.                        (8)

For the `k=1` seed take `n=3`,

    v_i=2^i+2^(6+i)  (0<=i<6),  f=10,  a'=5.             (9)

The first code is the diagonal D4^3 gluing; the second is the diagonal
D8_1 x D4_1 gluing. Direct enumeration gives

    Z(S+<a>)-Z(S+<a'>) = -W^2 Z_D4.                        (10)

Equivalently the D8 characters decompose as `U^2+V^2`, `2UV`, `2V^2`,
`2V^2`, giving `Z_D8-Z_D4^2=W^2`.

For the `k=2` seed take `n=6`, `f=30`, `a'=5138`, and

    (v_0,...,v_11) =
    (4280689,4003343,13490061,15943387,4783610,4517512,
     8704049,3143493,9304945,11135812,2974764,11955798).   (11)

Here `p=1`. Exact enumeration of 4096 words per code gives

    Z(S+<a>)-Z(S+<a'>) = W^6.                              (12)

Form the Bell product of `m` copies of the `k=2` pair. Repeatedly using
(6) and (7) gives a neighboring pair with difference `W^(6m)`. When k
is odd, make one further Bell product with the `k=1` seed. The resulting
`3k` D4 factors have `c_L=c_R=12k`, and (2) follows. Every step produces
actual even unimodular Narain lattices with one vacuum.

## Coefficients, nulls and reproducibility

Write `u=exp(pi i tau)`, `v=exp(pi i sigma)`. Then

    U=u^(-1/3)(1+O(u^2)),  V=8u^(2/3)(1+O(u^2)).

Multiplying (2) by the vacuum-energy factor `u^k v^k` gives

    u^k v^k (Z_+-Z_-) = +/- 8^R_k (v-u)^R_k
                         + higher total degree.             (13)

Thus the state coefficients at `(h,hbar)=(j/2,(R_k-j)/2)` differ by
`+/-8^R_k (-1)^j binom(R_k,j)`. All lower state coefficients agree.
Virasoro-primary coefficients have the same first difference: the
primary-to-state relation is unitriangular and all earlier vacuum,
chiral-null and descendant contributions cancel. The finite-difference
identity gives (3), while the exact factor `W^R_k` forces all lower spin
moments to agree at every temperature. The two CFTs are distinct because
their angular traces differ.

Run the standard-library certificate

    python verify_bell_gluing.py

It checks both seed ranks, isotropy, neighbor conditions, and complete
enumerator identities; enumerates the two 262144-word `k=3` codes and
verifies their complete character difference `-W^8 Z_D4`; and checks
the explicit recursive generators through `k=13`. The proof for all k
is the algebraic identity (7), not that finite diagnostic. For k=3 the
first changed eighth moment equals `-676457349120`.
