# Problém N-královen v MiniZinc solveru (2. cvičení)

Úkolem bylo napsat v MiniZinc IDE zadání pro řešení úlohy N-královen. 
Skript přijímá libovolné N a tento počet královen rozmístí na šachovnici o rozměrech NxN tak, že se královny navzájem neohrožují, což dosahuje pomocí podmínky *allDifferent*.

Skript předaný MiniZinc solveru lze vidět v textovém souboru *n_queens.txt*.

V souboru *minizinc_outputs.txt* lze vidět 3 výstupy pro různé hodnoty N (konkrétně 8, 30 a 150).

---

Příklad výstupu pro N = 30:

Running untitled_model.mzn, additional arguments -D queens=30;

Q-----------------------------

------------------Q-----------

-Q----------------------------

-----Q------------------------

--Q---------------------------

------------Q-----------------

-------Q----------------------

----------------Q-------------

----------------------Q-------

----------------------------Q-

--------------------------Q---

---------------------Q--------

---------------------------Q--

-------------------------Q----

-----------Q------------------

---------Q--------------------

-----------------------------Q

----------Q-------------------

------------------------Q-----

--------------Q---------------

-----------------------Q------

-------------Q----------------

------Q-----------------------

---Q--------------------------

--------------------Q---------

----Q-------------------------

---------------Q--------------

--------Q---------------------

-------------------Q----------

-----------------Q------------

Finished in 638msec