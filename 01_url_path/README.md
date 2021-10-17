# Hledání cesty mezi webovými stránkami (1. cvičení)

## Zadání
Vstupem programu jsou URL webových stránek dvou prestižních informatických škol,
například www.fit.cvut.cz a www.mit.edu. Navrhněte algoritmus, který nalezne cestu skrz
internetové odkazy z jednoho vstupního webu na druhý.

## Řešení
V rámci řešení jsem použil přístup prohledávání do šířky, kde si držím frontu nalezených webových URL adres a postupně na ně posílám požadavky, které zpracuji a získám z nich odkazy další úrovně.
Jelikož jsem při experimentaci zaznamenal, že hledání často uvízne na jistých doménách, které pravděpodobně nepovedou k dobrému výsledku, tak jsem tyto domény vyfiltroval. Jedná se konkrétně o: google.com, facebook.com, twitter.com a youtube.com.

Pro demonstraci jsem použil zmíněný příklad cesty z domény fit.cvut.cz na mit.edu a pro tento vstup byl výstup mého programu následující:

 --- Target http://jmlr.csail.mit.edu/papers/v11/jaksch10a.html acquired! ---
 
URL path:

4 http://jmlr.csail.mit.edu/papers/v11/jaksch10a.html
3 https://en.wikipedia.org/wiki/Reinforcement_learning
2 https://casopis.fit.cvut.cz/osobnost/pavel-kordik-praha-jako-centrum-umele-inteligence-vsichni-musime-tahnout-za-jeden-provaz
1 https://casopis.fit.cvut.cz
0 http://fit.cvut.cz

Visited pages: 561
