# Pillangó efektustól a káosz elméletig

## A pillangó effektus

Ismerős számotokra a pillangó efektus fogalma? Biztosan hallottatok már róla, számtalan film is készült a jelenségről, illetve sok viccesebbnél viccesebb meme is.

(filmekről képek, és meme-k a pillangó effektusról)

A pillangó effektus dióhéjban elmagyarázva, azt a jelenséget próbálja megmutatni, hogy egy apró változás, milyen drasztikus hatással lehet a jövőre nézve.

Szerintem, azért is érdekes ez az egész jelenség, mert egy izgalmas kérdét vet fel:
**Mennyire jól megjósolható a jövő?**

## A megjósolhatóság megkérdőjelezése

A Newton-i fizika alapján, a világunk teljesen megjósolható. Ha ismerjük a kezdeti feltételeket, és a rendszerünket leíró egyenleteket, akkor a jövőt is meg tudjuk jósolni.

Ez a megközelítés azonban nem minden esetben működik. A legegyszerűbb példa rá a három test problémája. A három test problémája egy olyan rendszer, ahol három testet vizsgálunk, és a kölcsönhatásukat.
A probléma ezzel a rendszerrel az, hogy a három test kölcsönhatása nem lineáris, így a rendszer nem megjósolható könnyedén.

(manim animáció a három test problémájáról)

## Edward Lorenz és a káoszelmélet születése

Edward Lorenz egy meteorológus volt, aki a 60-as években egy szeretett volna egy olyan modellt készíteni, ami megjósolja az időjárást.

A kezdeti modelljében 12 egyetlen és 12 változó volt, mint a hőmérséklet, a szél sebessége, a páratartalom, stb.
Egy alkalommal szerette volna újra futtatni a modelljét, de nem akarta megvárni, hogy a számítógépe végig fusson rajta, így a futtatás közben leállította a számítógépet, és a futtatást folytatta egy korábbi pontból.

Viszont a modell nem ugyanazt az eredményt adta, mint az előző futtatásnál.

Először azt hitte, hogy a számítógép hibázott, de később rájött, hogy a modell nem lineáris, így a két futtatás nem ugyanazt az eredményt adja.

## Paraméter érzékenység

Lorenz rájött, hogy a modell paraméterei mennyire érzékenyek a kezdeti feltételekre. Ezt a jelenséget nevezzük paraméter érzékenységnek.

Később Lorenz egy 3 változós modellt készített, amit manapság a Lorenz egyenleteknek nevezünk.

## Lorenz egyenletek

$$
\begin{aligned}
\frac{dx}{dt} &= \sigma \cdot (y-x) \\
\frac{dy}{dt} &= x \cdot (\rho-z)-y \\
\frac{dz}{dt} &= x \cdot y-\beta \cdot z
\end{aligned}
$$

Ezek a differenciálegyenletek együtt alkotják az egyenletrendszert, ahol $x$, $y$ és $z$ a változók, $\sigma$, $\rho$ és $\beta$ pedig a paraméterek.

(manim animáció a Lorenz egyenletekről)

## A káosz és a meghatározottság paradoxona

Talán a legérdekesebb aspektusa a Lorenz-ábrának az, hogy noha a rendszer determinisztikus - azaz teljesen meghatározott a kezdeti feltételek ismeretében - hosszú távon mégis kiszámíthatatlannak tűnik.

Ez a determinisztikus káosz vagy kaotikus meghatározottság paradoxona. Ez az amire Lorenz is rámutatott, mégpedig, hogy kicsi változások a kezdeti feltételekben, nagy változásokat okoznak a rendszer végállapotában.

Vegyük példának ezt a
kettős ingát, ahol a két inga hossza és a kezdeti szög is kicsit eltérő. A két inga mozgása az elején nagyon hasonló, de később már teljesen más lesz.

(manim animáció a kettős ingáról oldalról)

### Fázis tér bevezetése

Az inga mozgását egy úgynevezett fázis térben is ábrázolhatjuk, ahol
az $x$ tengelyen az inga szöge, az $y$ tengelyen pedig a inga sebessége ábrázolódik.

Ezt mindkét ingára levetítve látható, hogy egy idő után egy 0-hoz hasonló formát alakítanak ki a görbék.

Egyszerű inga esetében pedig egy befele haladó spirált kapunk.

A spirál közepe lesz az úgynevezett attraktor, ami a rendszer végállapota.

(manim animáció a kettős ingáról fázis térben, illetve az egyszerű ingáról fázis térben)

### Példa a fázis térben és a Lorenz egyenletekkel

Mi történik viszont, ha a Lorenz egyenleteket ábrázoljuk fázis térben?

Vegyünk három kicsit eltérő kezdeti feltételt a Lorenz egyenletekhez. A három kezdeti feltétel közül az egyik a Lorenz által használt, a másik kettő pedig csak egy kicsit tér el tőle.

Amint láthatjuk a három görbe az elején mintha teljesen együtt mozogna a térben, de később már teljesen más irányba haladnak.

(manim animáció a Lorenz egyenletekről három különböző kezdeti feltétellel)

Ez az izgalmas példa jól illusztrálja, hogy a Lorenz-ábrát és a fázis teret összekapcsolva milyen mélyebb betekintést nyerhetünk a káosz és a determinisztikus rendszerek viselkedésébe. A fázis tér segít megérteni, hogyan változik a rendszer állapota az idő múlásával, és hogyan reagál a kezdeti feltételek változásaira.

Ami különösen figyelemre méltó, hogy a fázis térben kapott görbék egy pillangó formához hasonlítanak, tovább erősítve a pillangó effektus és a káosz közötti kapcsolatot.

(manim animáció a Lorenz egyenletekről három különböző kezdeti feltétellel, és a pillangóhoz hasonló formával)

## A káoszelmélet használata a mindennapokban

A káoszelmélet, bár eredetileg a természeti jelenségek magyarázatára született, számos területen alkalmazható a mindennapi életünk során. Például, a káosz elméletét felhasználhatjuk a pénzpiaci ingadozások megértésére, a meteorológiai előrejelzések fejlesztésére, vagy akár a közlekedési rendszerek optimalizálására.

Azáltal, hogy elfogadjuk, hogy a kis változások és bizonytalanságok hatalmas hatással lehetnek a rendszerek viselkedésére, képesek lehetünk rugalmasabb és hatékonyabb megoldásokat találni a változó környezetünk kezelésére.

## Befejezés

A pillangó effektustól a káoszelméletig vezető utunkon bepillantást nyertünk abba, hogy mennyire érzékenyek lehetnek a determinisztikus rendszerek a kezdeti feltételek és paraméterek kis változásaira. Edward Lorenz káoszelmélete megmutatta számunkra, hogy bizonyos rendszerek bonyolult, kaotikus viselkedést mutathatnak, még akkor is, ha determinisztikusak.

Ez a felismerés nem csak az időjárás-előrejelzésekre vagy az áramlások modellezésére korlátozódik; a káoszelmélet mélyebb betekintést nyújt abba, hogy miként működnek a rendszerek és hogyan reagálnak a változásokra.

A káoszelméletből levonható tanulságok kiterjednek az élet különböző területeire, és segíthetnek abban, hogy rugalmasabban kezeljük a változó körülményeket és döntéseinket. Végül is, a káosz elmélete arra emlékeztet bennünket, hogy még a látszólag kiszámíthatatlan és kaotikus rendszerekben is megtalálhatók a minták és a rend.
