# Automatický vysavač (1. cvičení)

## Zadání
Uvažujte svět vysavače, tj. pravidelnou mřížku čtvercovou mřížku, kde každé políčko je
buď prázdné, nebo obsahuje smetí. Dále se v prostředí pohybuje automatický vysavač, který
se vždy nachází na některém políčku mřížky. Vysavač se může pohybovat na sousední políčko
nebo může vysávat, čehož výsledkem je prázdné políčko tam, kde se vysavač vyskytuje.

## Řešení

### Reprezentace stavového prostoru

Stavy jsou reprezentovány jako 2D pole obsahující různé číslice, každý se svým speciálním významem:
* 0 - prázdné pole
* 1 - překážka/zeď
* 2 - smetí
* 3 - robot stojící na prázdném poli
* 4 - robot stojící na smetí

Funkce následníka je schopna pro zadanou konfiguraci 2D pole vygenerovat seznam všech možných sousedů, na které lze přejít dostupnými akcemi (posun nahoru, dolu, doprava, doleva, vysátí smetí).

Program dostane jako vstup na prvním řádku počet smetí, které je nutné vysát a dále následuje zápis polí matice po řádkách (číslice odděleny čárkou).

*Příklad vzorového souboru input3.txt:*

*8*

*1,1,2,1,1,0,0,1,1,2,1,1,3*

*2,2,0,0,0,0,0,2,1,0,0,1,0*

*1,0,0,0,0,0,0,0,1,1,0,0,0*

*1,0,2,0,0,0,0,0,0,0,0,0,0*

*0,0,2,0,0,0,0,0,0,0,0,2,0*       

### Algoritmus

K nalezení nejkratší cesty takové, že vysavač uklidí veškeré smetí v zadané místnosti, byl použit algoritmus BFS.

V první implementované variantě je použita funkce, která vygeneruje všechny možné koncové stavy. To jsou ty, kde všechna pole, kde bylo smetí, jsou nyní prázdná, s výjimkou jednoho, kde vysavač stojí již sám. Následně je spuštěn algoritmus BFS z počátečního stavu do každého koncového a nejkratší z řešení je ukládáno. Nevýhodou tohoto přístupu je, že je poměrně pomalý pro větší počet smetí (BFS poběží tolikrát, kolik je smetí). Funkce využívající tento přístup se nazývá *naive_cleaner*.

Dále bylo implementováno vylepšení, které smetí hledá postupně ve vlnách. Je tedy zadán počáteční stav a počet smetí, které je nutné uklidit. Algoritmus pak použije BFS k tomu, aby nalezl první nejbližší kus smetí. Jakmile ho najde, stává se tento stav novým počátečním stavem a BFS pokračuje v hledání druhého nejbližšího smetí atd. dokud nejsou nalezeny všechny. Kompletní cesta se přitom postupně spojuje za sebe. Tento přístup je implementován funkcí *fast_cleaner*. 

Experimentálně bylo ověřeno, že přestože obě řešení poskytují stejnou vzdálenost, tak je druhý zmínený přístup podstatně rychlejší. Toto lze pozorovat v následující tabulce testovacích dat:

| Vstupní soubor | Algoritmus (funkce) | Velikost pole | Počet smetí | Nejkratší nalezená cesta   | CPU čas (s) |
|-------|----------|-------------|----------------|-------------|----------------|
| input1.txt | *naive_cleaner* | 3x5 | 4 | 15  | 0.018980979919433594 |
| input1.txt | *fast_cleaner*  | 3x5 | 4 | 15  | 0.008963584899902344 |
| input2.txt | *naive_cleaner* | 5x6 | 3 | 17  | 0.023996353149414062 |
| input2.txt | *fast_cleaner*  | 5x6 | 3 | 17  | 0.01598501205444336 |
| input3.txt | *naive_cleaner* | 5x13 | 8 | 42  | 4.504834890365601 |
| input3.txt | *fast_cleaner*  | 5x13 | 8 | 42  | 0.04303121566772461 | 
| input4.txt | *naive_cleaner* | 8x10 | 7 | 49 | 2.7977044582366943 |
| input4.txt | *fast_cleaner*  | 8x10 | 7 | 49 | 0.06994462013244629 |

Ačkoliv v provedených experimentech obě metody nalezly nejkratší cestu, domnívám se, že existují případy, kdy by rychlejší metoda selhala, jelikož funguje greedy principem a nebere v potaz umístění vzdálenějších kusů smetí. Proto pokud bychom si skutečně chtěl být jistí nejkratší vzdáleností, použil bych funkci *naive_cleaner*.

*Příklady nalezených sekvencí stavů lze vidět v souborech output{}.txt*.
