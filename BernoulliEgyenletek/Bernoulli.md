# Bernoulli differnciál egyenletek levezetés

## Bevezetés

Sziasztok! Ebben a videóban a Bernoulli differenciálegyenletek levezetését szeretném bemutatni.

## Lépések

### Első lépés

Az első lépés hogy le kell írjuk az egyenletet standard formában.

(Manimban megjelenik a következő egyenlet)

$$
y' + P(x)y = Q(x)y^n
$$

ahol:

$$
\forall n \in \mathbb{R} \backslash \{0,1\}
$$

Hiszen ha $n=0$ akkor az egyenlet átalakul egy lineáris egyenletté, és ha $n=1$ akkor az egyenlet átalakul egy szétválaszható változojú egyenletté.

Amint ilyen alakban van az egyenletünk, fel kell tudnunk ismerni P(x) és Q(x) függvényeket.

(Manimban aláhúzom a P(x) és Q(x) függvényeket, és bekeretezem a n hatvány tagot.)

### Második lépés

Ezután meg kell keressük az integrál faktort, ami a következő alakban van:

(Manimban megjelenik az integrál faktor)

$$
I(x) = e^{\int [1-n]P(x)dx}
$$

### Harmadik lépés

Amint megvan az integrál faktor, használhatjuk a következő egyenletet, hogy megoldjuk az egyenletet:

(Manimban megjelenik a megoldó egyenlet)

$$
y^{1-n} = \left[ \frac{1}{I(x)} \int [1-n]Q(x)I(x)dx +c\right]
$$

### Példa

Most nézzünk egy példát, hogy hogyan kell megoldani egy Bernoulli egyenletet.

(Manimban megjelenik a példa egyenlet)

$$
y' + \left( \frac{2}{x} \right) y = x^2y^3
$$

Látható, hogy ez az egyenlet alapból standard formában van.

(Manimban megjelenik az egyenlet P(x) és Q(x) függvényekkel)

$$
y' +P(x)y = Q(x)y^n
$$

Látható, hogy:

$$
P(x) = \frac{2}{x}
$$

És hogy:

$$
Q(x) = x^2
$$

Illetve, hogy $n=3$.
