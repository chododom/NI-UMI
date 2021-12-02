# Multi-agent path finding (MAPF)

## Zadání

Pokuste se zformulovat úlohu multiagentního hledání cest jako plánovací problém v jazyce PDDL a pokuste se najít její řešení pomocí plánovače.
Máme ve vrcholech grafu umístěné agenty, přesun agenta je možný skrz hranu do neobsazeného vrcholu, každý agent má cílový vrchol.


## Řešení

Pro formulaci problému je třeba vytvořit dva soubory:
* [**domain_def.pddl**](./domain_def.pddl)
    * tento soubor obsahuje definici domény problému, tedy jaké existují predikáty a akce, které mohou měnit stav
    * predikáty: 
        * (node ?n) - objekt n je vrchol grafu
        * (agent ?a) - objekt a je agent hledající cestu do svého cíle
        * (at ?a ?n) - agent se nachází ve vrcholu n
        * (next ?n1 ?n2) - existuje orientovaná hrana z vrcholu n1 do vrcholu n2
        * (empty ?n) - vrchol není obsazený žádným agentem
    * akce:
        * move - pohyb agenta z jednoho vrcholu na druhý za předpokladu, že se na prvním nachází a cílový vrchol je neobsazený
* [**problem_def.pddl**](./problem_def.pddl)
    * tento soubor obsahuje formulaci konkrétního problému, který lze vidět na obrázku ze cvičení
    * je zadefinováno 18 vrcholů
    * je zadefinováno 6 agentů
    * každý agent je umístěn na svou počáteční pozici, zbytek vrcholů je prázdný
    * je definováno které hrany spolu sousedí
    * cílový stav je definovaný umístěním každého agenta na svém cílovém vrcholu


![alt text](./MAPF.JPG?raw=true "MAPF")


Pro řešení úlohy byl použit online [automatický plánovač](http://editor.planning.domains/), který si problém reprezentuje jako stavový prostor, který řeší pomocí Iterative Width algoritmu.
Plánovač vygeneroval 4368 stavů, z nichž 4189 expandoval.
Plán nalezený plánovačem měl cenu 72, detailnější výstup je [zde](./solver_output.txt).

**Nalezený plán je následující:**

(move blue n16 n17)

(move blue n17 n18)

(move blue n18 n11)

(move blue n11 n12)

(move yellow n15 n16)

(move yellow n16 n17)

(move yellow n17 n18)

(move yellow n18 n11)

(move yellow n11 n10)

(move blue n12 n11)

(move yellow n10 n9)

(move yellow n9 n5)

(move light_blue n2 n3)

(move green n8 n7)

(move green n7 n6)

(move light_blue n3 n4)

(move red n14 n13)

(move red n13 n12)

(move light_blue n4 n3)

(move yellow n5 n4)

(move green n6 n5)

(move green n5 n9)

(move yellow n4 n5)

(move yellow n5 n6)

(move yellow n6 n7)

(move green n9 n10)

(move yellow n7 n8)

(move pink n1 n2)

(move yellow n8 n1)

(move blue n11 n18)

(move green n10 n11)

(move blue n18 n17)

(move green n11 n18)

(move red n12 n11)

(move red n11 n10)

(move red n10 n9)

(move red n9 n5)

(move red n5 n6)

(move light_blue n3 n4)

(move light_blue n4 n5)

(move pink n2 n3)

(move pink n3 n4)

(move light_blue n5 n9)

(move pink n4 n5)

(move light_blue n9 n10)

(move pink n5 n9)

(move red n6 n5)

(move green n18 n11)

(move green n11 n12)

(move light_blue n10 n11)

(move pink n9 n10)

(move light_blue n11 n18)

(move pink n10 n11)

(move green n12 n13)

(move pink n11 n12)

(move green n13 n14)

(move pink n12 n13)

(move green n14 n15)

(move pink n13 n14)

(move green n15 n16)

(move pink n14 n15)

(move light_blue n18 n11)

(move light_blue n11 n12)

(move blue n17 n18)

(move blue n18 n11)

(move blue n11 n10)

(move blue n10 n9)

(move light_blue n12 n11)

(move light_blue n11 n10)

(move green n16 n17)

(move green n17 n18)

(move green n18 n11)
