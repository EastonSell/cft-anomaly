# Finite-temperature reconstruction: independent audit

This earlier audit predates the physical sharpness construction for every k.
See [the all-k construction](all_k_physical_sharpness.md) and the
[manuscript](../../preprints/cft-reconstruction/source/main.tex) for that result.

This note proves an injectivity statement for the **complete torus partition
function** under the assumptions below. The temperature and angular moments
must be known exactly; no claim of numerical stability or physical
realizability of every solution of the modular equations is made. Priority of
the finite-sampling statement has not been established.

## Statement and measured data

Let `k >= 1`. Consider a compact, unitary two-dimensional CFT with discrete
spectrum and finite torus trace at every positive temperature, a unique
vacuum, `c_L = c_R = 12k`, integer total dimensions, and an unmultiplied
`SL(2,Z)`-invariant torus partition function. Full T-invariance and the
vacuum imply integer spin; equivalently, it can be assumed explicitly. Put

```text
Z(tau,sigma) = Tr exp(2 pi i tau (L0-k/2)
                       + 2 pi i sigma (Lbar0-k/2)),
F_r(t) = (d/dz)^r Z(it+z,it-z) at z=0,   z real,
R_k = 3k if k is even, and 3k-1 if k is odd.
```

The physical torus is `sigma=-conjugate(tau)`; hence each `F_r(t)` is a
physical angular derivative. More explicitly,

```text
F_r(t)=(2 pi i)^r sum_(h,hbar) D_(h,hbar) (h-hbar)^r
                       exp[-2 pi t (h+hbar-k)].                         (1)
```

**Theorem.** The exact numbers `F_r(t_i)`, for every `0 <= r <= R_k`,
determine `Z` uniquely in the stated class if either

* `k` distinct temperatures satisfy `t_i >= 1`; or
* `2k-1` distinct temperatures satisfy `t_i > 0`.

Both assertions use the known unit vacuum coefficient. Without this
normalization, the same proof uses `k+1` distinct `t_i >= 1`, or `2k+1`
arbitrary distinct `t_i > 0`. These are **sufficient**, not claimed optimal,
temperature counts. Parity symmetry is not assumed: all odd as well as even
moments in the displayed range are part of the data. The labels `t` are
dimensionless inverse temperatures; the physical inverse temperature on a
circle of circumference `2 pi` is `2 pi t`.

To reconstruct rather than merely distinguish two solutions, form a basis of
the finite invariant space in (4), substitute the theta-series expressions
for `lambda(it+z)` and `lambda(it-z)` through degree `R_k`, and solve the
resulting finite linear system together with the vacuum condition. The proof
below establishes that this system has at most one solution. Its joint
Fourier expansion gives every state multiplicity `D_(h,hbar)`. This concerns
the genus-one spectrum, not OPE coefficients or uniqueness of the CFT.

## Justification of the finite modular space

The trace is jointly holomorphic on `H x H`: on compact sets, nonnegative
state multiplicities and `h,hbar >= 0` bound the absolute sum by a finite
thermal trace at the smaller of the two imaginary parts. The same argument
at a slightly smaller imaginary part bounds arbitrary finite derivatives.
A holomorphic function vanishing on `sigma=-conjugate(tau)` vanishes on
`H x H`, because its local double Taylor series restricts to independent
monomials in `z` and `conjugate(z)`. Physical `S,T` invariance therefore
continues to independent arguments.

For `gamma=[[a,b],[c,d]]`, write
`iota(gamma)=[[a,-b],[-c,d]]`. Continued invariance gives

```text
Z(gamma tau, sigma) = Z(tau, iota(gamma)^(-1) sigma).                    (2)
```

Integer dimension and spin give `2h,2hbar in Z`. Because `c_L=c_R=12k`,
each independent `tau -> tau+2` or `sigma -> sigma+2` has no multiplier.
Conjugating these shifts by simultaneous S gives separate actions of
`S T^2 S^(-1)`, so each variable is invariant under `Gamma(2)`. In the
quotient by `Gamma(2)`, `iota` acts trivially: consequently the remaining
full modular invariance is the diagonal six-element anharmonic group.

For fixed `sigma` and `T >= T0 > 0`, positivity and unitarity yield the
uniform strip bound

```text
|Z(tau,sigma)| <= exp[pi k (T-T0)] Z(i T0, i Im(sigma)),
T=Im(tau).                                                               (3)
```

Thus the periodic cusp expansion at infinity is meromorphic with pole order
at most `k` in `u=exp(pi i tau)`. For any other cusp choose `gamma` mapping
infinity there and apply (2): the partner argument remains a fixed point of
`H`, and (3) gives the same pole order. This proof applies uniformly over a
compact set of partner arguments and also with the arguments exchanged. It
does not assume independent full `SL(2,Z)` invariance.

Write `x=lambda(tau)`, `y=lambda(sigma)`, `D(x)=x(1-x)`. The modular curve
`X(2)` is a sphere with cusps `0,1,infinity`, and `lambda=16u+O(u^2)` at
the cusp infinity. The cusp bound therefore gives

```text
V_k = span{1,x^j,x^(-j),(1-x)^(-j): 1<=j<=k},
Z in I_k := (V_k tensor V_k)^S3,
Z = P(x,y)/[D(x)D(y)]^k,    deg_x P,deg_y P <= 3k.                     (4)
```

To justify the tensor product without assuming behavior at intersections of
cusps: evaluate the first-variable function at `3k+1` interior points with
invertible evaluation matrix. The coefficients of its `V_k` expansion are
linear combinations of those evaluations; the already proved second-variable
cusp bound places each coefficient in `V_k`. Diagonal `S3` acts as

```text
S: x -> 1-x,           T: x -> x/(x-1),                                (5)
```

simultaneously on both arguments. Standard references for these lambda
transformation laws include [DLMF §23.18](https://dlmf.nist.gov/23.18).

## Proof of the sampling theorem

Take the difference `G` of two allowed partition functions with equal data,
and call its numerator `P`. Their common unit vacuum and integral total
dimensions imply

```text
P(x,y) = O((x,y)^2) at (x,y)=(0,0),                                    (6)
```

where the notation means that the constant and both linear Taylor terms
vanish. Indeed, in `u=exp(pi i tau), v=exp(pi i sigma)`, the vacuum-free
series `u^k v^k G` has only even total degrees and begins at degree at least
two; multiplication by `(D(x)/u)^k(D(y)/v)^k` does not change that order.
Invariance carries the same local statement to each *diagonal* cusp.

Induct on `r`. If all previous diagonal coefficients vanish, then
`P=(x-y)^r Q_r`, with `deg_x Q_r,deg_y Q_r <= 3k-r`. Define

```text
N_r(x)=Q_r(x,x),             deg N_r <= 6k-2r.                          (7)
```

The lambda function is locally unramified on `H`, and along the physical
angular path

```text
lambda(it+z)-lambda(it-z) = 2 lambda'(it) z + O(z^3),  lambda'(it) != 0.
```

Thus equality of the `r`th measured derivative implies `N_r(x_i)=0`, where
`x_i=lambda(it_i) in (0,1)`. Moreover

```text
a_r(x) := N_r(x)/D(x)^(2k)
          = lim_(y->x) G(x,y)/(x-y)^r
```

transforms as `a_r(gx)=a_r(x)/g'(x)^r` for `g in S3`. Consequently each
sampled root propagates to its full anharmonic orbit. An interior real
point has six distinct orbit points except `x=1/2`, whose orbit has three.
Only `x` and `1-x` from a generic orbit lie in `(0,1)`. Since
`lambda(it)` is a bijection `(0,infinity) -> (0,1)` and maps `[1,infinity)`
to `(0,1/2]`, either allowed sampling set supplies at least `6k-3` distinct
finite orbit roots of `N_r`.

The diagonal cusp condition (6) gives, in addition:

* for `r=0`, two roots at each of the three cusps;
* for `r=1`, after dividing by `x-y`, one root at each of the three cusps.

Here a root at infinity is counted in the projective degree `6k-2r`: its
multiplicity is `6k-2r-deg N_r`. For example, under `x -> 1/x` the numerator
transforms by `P(1/x,1/y)=P(x,y)/(x^(3k)y^(3k))`, so the same local cusp
order applies at infinity. The orbit roots are finite and different from all
cusps. For `r=0`, there are at least `(6k-3)+6 > 6k` roots; for `r=1`, at
least `(6k-3)+3 > 6k-2`; for `r>=2`, the orbit roots alone satisfy
`6k-3 > 6k-2r`. Thus `N_r` is identically zero at every induction step,
and `x-y` divides `Q_r`. This completes the induction.

For even `k`, the order range includes `r=3k`, so a polynomial of
`x`-degree at most `3k` divisible by `(x-y)^(3k+1)` is zero. For odd `k`,
the last given order is `3k-1`: then `P=C(x-y)^(3k)` for a constant `C`,
and invariance under `S` changes its sign, forcing `C=0`.

Without fixed vacuum, omit the cusp roots. The larger sample sets in the
theorem supply at least `6k+3` distinct orbit roots, exceeding all the
bidegree bounds in (7). This proves the weaker count too.

## Maximum angular order and a limitation on sharpness

In the fixed-vacuum **signed modular-function space**, the indicated maximum
derivative order cannot be lowered, even with data at every temperature. Put
`d=3k`. Both nonzero functions below are separately `Gamma(2)` invariant,
diagonally `S3` invariant, have the allowed cusp orders and zero vacuum:

```text
H_even = (x-y)^d / [D(x)D(y)]^k,                         k even;
H_odd  = (x-y)^(d-1) (2xy-x-y+2) / [D(x)D(y)]^k,       k odd.          (8)
```

For odd `k`, the numerator factor obeys
`Q(1-x,1-y)=Q(x,y)` and
`(1-x)(1-y)Q(x/(x-1),y/(y-1))=Q(x,y)`; these identities prove invariance.
Their first potentially nonzero angular derivatives have precisely the
orders `R_k`. They establish sharpness for the signed modular space, **not**
automatically for pairs of genuine CFTs. The physical `k=1` example below
does establish sharpness there.

## Two actual `k=1` CFTs with identical thermal trace

Let `U=chi_0` and `V=chi_v=chi_s=chi_c` be the `SO(8)_1` characters, so
the diagonal `D4` theory has `Z_D4=U_x U_y+3 V_x V_y`. Let
`chi_E8=U^2+3V^2`. The two physical theories are

```text
A = (SO(8)_1 diagonal)^3,
B = (E8_1 holomorphic x anti-E8_1) tensor SO(8)_1 diagonal.
```

Each has `c_L=c_R=12`, a unit vacuum, integer total dimensions and spin,
and full modular invariance. Their complete thermal traces are identical:
`Z_A(it,it)=Z_B(it,it)=j(it)`. Their angular partition functions differ:

```text
Z_B-Z_A = 3 Z_D4 (U_x V_y - V_x U_y)^2 = 96 H_odd at k=1.
Z_A = 32 (2-x-y+2xy)^3 / [D(x)D(y)].                                  (9)
```

For (9), use `U/V=(2-x)/x` and `V^3=2x^2/(1-x)`. At the self-dual
temperature `t=1`, `x=y=1/2`, both have `F_0(1)=j(i)=1728` and
`F_1(1)=0`, but

```text
F_2^A(1)=-864  pi^2 theta_3(i)^8,
F_2^B(1)=-2016 pi^2 theta_3(i)^8.                                     (10)
```

Here `lambda'=i pi theta_3^4 lambda(1-lambda)`. Formula (10) follows by
expanding (9) at `x=1/2+s,y=1/2-s` and observing that the tangent derivative
of the common `j` vanishes at `x=1/2`. The theta convention is
`theta_3(tau)=sum_(n in Z) exp(pi i n^2 tau)`.

The basic thermal ambiguity predates this note: Ashrafi and Loran,
[*Non-chiral 2d CFT with integer energy levels*, §5.1](https://arxiv.org/abs/1607.08516), exhibit the `SO(8)_1^2` versus
`E8_1 x anti-E8_1` example at total central charge 16. Tensoring both by
the diagonal `SO(8)_1` theory gives (9). That paper also develops the
related chiralization and theta-function finite-dimensional description.
We do not claim priority for the new-looking sampling bound without a wider
literature check.

## Independent checks and scope

`angular_reconstruction_check.py` uses standard-library exact rational
arithmetic to construct the six-element action, group-average all numerator
monomials, and verify ranks for `k=1,2,3`. The fixed-vacuum dimensions and
sample ranks are `2,8,16`. The script checks (8) for `k=1,...,6`, and (9)
and the diagonal `j` identity at rational lambda values. It checks a
linearized lambda path; the proof above, not the finite check, establishes
the all-`k` result for the actual angular path. No finite scan is used as an
all-`k` proof. Exact continuum data at finitely many temperatures is still
an idealization, and no stable-error bound follows from injectivity alone.

## Optional extension to every allowed central-charge split

The equal-central-charge assumption can be relaxed. Assume instead the same
physical hypotheses with `c_L+c_R=24k` and `c_L,c_R>0`. The unmultiplied
T-invariance and the unit vacuum give `c_L-c_R in 24 Z`; hence

```text
c_L=12p, c_R=12q,  p,q positive integers,  p+q=2k.
```

The separate T-squares are still trivial. The argument in (2)--(4) gives
`Z=P(x,y)/[D(x)^p D(y)^q]` with degrees `3p,3q`. The physical angular
derivatives are moments of `J-(p-q)/2`, an invertible triangular change of
variables from moments of `J`. Each diagonal denominator is again
`D(x)^(p+q)=D(x)^(2k)`, and after division by `(x-y)^r` the polynomial
`N_r` has degree at most `3(p+q)-2r=6k-2r`. The vacuum cusp and orbit-root
arguments are unchanged. Thus the same `k` temperatures on `t>=1`, or
`2k-1` arbitrary positive temperatures, suffice with derivatives through

```text
R=3 min(p,q),
```

and in the special case `p=q=k` odd the previously stated reduction to
`R=3k-1` applies. No new positivity assumption is used.

For `p>q`, put `m=(p-q)/2` and define

```text
B(x)=(1-x+x^2)^3,
A(x)=x(1-x)(2x-1)(x+1)(x-2),
Q(x)=B(x)^m                      if q is even,
     A(x) B(x)^(m-1)             if q is odd.
```

Then `(x-y)^(3q)Q(x)/[D(x)^p D(y)^q]` is a zero-vacuum invariant of exact
angular order `3q`, proving that the unequal-charge order is sharp in the
signed modular space. The case `p<q` follows by exchanging variables. This
is not a statement that the witness is a difference of actual CFTs. The
independent exact checker `unequal_angular_reconstruction_check.py` verifies
the finite sample ranks for `(p,q)=(3,1),(1,3),(4,2),(2,4),(5,1)` and
checks the witness under S and T. The proof of the extension is the same
all-`k` argument, not this finite calculation.
