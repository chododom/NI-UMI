# Formulace plánovacího problému v jazyce PDDL pro hru Lišák/8-puzzle (4. cvičení)


## Zadání

Pokuste se zformulovat úlohu Lišáka jako plánovací problém v jazyce PDDL a pokuste se najít její řešení pomocí plánovače.

## Řešení

Pro formulaci problému je třeba vytvořit dva soubory:
* [**domain_def.pddl**](/domain_def.pddl)
    * tento soubor obsahuje definici domény problému, tedy jaké existují predikáty a akce, které mohou měnit stav
    * predikáty: 
        * (square ?sqr) - objekt sqr je čtvereček, kterým lze hýbat po hracím poli
        * (coordinate ?x ?y) - dvojice (x,y) jsou platné souřadnice hracího pole
        * (empty ?x ?y) - na daných souřadnicích (x,y) se nevyskytuje žádný čtvereček, tedy pole je prázdné
        * (at ?sqr ?x ?y) - konkrétní čtvereček sqr se vyskytuje na souřadnicích (x,y)
    * akce:
        * move_x - pohyb po x-ové ose za předpokladu, že cílová souřadnice je platná a prázdná
        * move_y - pohyb po y-ové ose za předpokladu, že cílová souřadnice je platná a prázdná
* [**problem_def.pddl**](/problem_def.pddl)
    * tento soubor obsahuje formulaci konkrétního problému, který lze vidět na obrázku ze cvičení
    * je zadefinováno 8 čtverců
    * každému čtverec je umístěn na konkrétní souřadnice
    * zbylá souřadnice je prázdná
    * cílem je umístit čtverečky tak, aby ten s číslem 1 byl na první pozici, 2 na druhé, atd... a poslední pozice byla prázdná


Pro řešení úlohy byl použit online [automatický plánovač](http://editor.planning.domains/), který si problém reprezentuje jako stavový prostor, který řeší pomocí BFS.
Plánovač vygeneroval 181 stavů, z nichž 45 expandoval.
Plán nalezený plánovačem měl cenu 20, detailnější výstup je [zde](/solver_output.txt).

**Nalezený plán je následující:**

(move_y sqr5 x1 y0 y1)

(move_x sqr8 x2 y0 x1)

(move_x sqr7 x0 y0 x2)

(move_y sqr4 x0 y2 y0)

(move_x sqr1 x2 y2 x0)

(move_y sqr3 x2 y1 y2)

(move_x sqr2 x0 y1 x2)

(move_y sqr1 x0 y2 y1)

(move_x sqr3 x2 y2 x0)

(move_x sqr6 x1 y2 x2)

(move_y sqr8 x1 y0 y2)

(move_x sqr4 x0 y0 x1)

(move_y sqr1 x0 y1 y0)

(move_y sqr3 x0 y2 y1)

(move_x sqr6 x2 y2 x0)

(move_x sqr8 x1 y2 x2)

(move_x sqr6 x0 y2 x1)

(move_y sqr3 x0 y1 y2)

(move_x sqr2 x2 y1 x0)

(move_y sqr8 x2 y2 y1)
