if ... elif ... else
====================

Les tests
---------

Un test compare des valeurs et renvoie un booléen de valeur ``True`` ou ``False``.

Les opérateurs de comparaison sont:

-  ``==`` pour comparer deux valeurs égales : ``a == 3``,
-  ``!=`` pour comparer deux valeurs non égales, différentes : ``a != 3``.
-  ``<``, ``>``, ``<=`` et ``>=`` pour comparer comme en maths : :math:`<`, :math:`>`, :math:`\leqslant` et :math:`\geqslant`.

.. admonition:: Exemple

   Soit la variable :code:`a=5` :

   >>> a < 3
   False
   
   >>> a != 0
   True
   
   >>> a > 0
   True
   
si / if
-------

On peut soumettre l’exécution d’une instruction à une condition.

La structure est de la forme:

.. code:: python

   if test:
       instructions

Le test renvoie une valeur booléenne.

-  Si la valeur du test est ``True``, les instructions sont exécutées;
-  Si la valeur du test est ``False``, aucune instruction n'est exécutée.

.. admonition:: Exemple

    .. code-block:: python
    
        if a >= 0:
            print("Le nombre a est positif")
    
    Si la variable `a` est positive ou nulle, alors l'affichage du message est réalisé.
    Dans le cas contraire, aucune instruction n'est exécutée.

si … sinon / if … else
----------------------

Lorsque le test de la condition ``if`` est à ``False``, il est possible d’exécuter d’autres instructions. Elles sont introduites par le mot ``else``. La structure ``if ... else`` permet de gérer les exceprions à la condition.

La structure devient :

.. code:: python

   if test:
       instructions
   else:
       autres instructions

.. admonition:: Exemple

    .. code-block:: python
    
        if a >= 0:
            print("Le nombre a est positif")
        else:
            print("Le nombre a est négatif")
    
    Si la variable `a` est positive ou nulle, alors l'affichage du message "Le nombre a est positif" est réalisé.
    Sinon (le nombre est négatif) le message "Le nombre a est négatif" est réalisé

.. warning::

    Il n'y a pas de test placé après le ``else``. Cela correspond à tous les autres cas de figure ne vérifiant pas le test.

si … sinon si / if … elif
-------------------------

Suite à un premier test, il est possible de soumettre un nouveau test avec la commande ``elif``. La structure est alors de la forme:

.. code:: python

   if test 1:
       instructions
   elif test 2:
       autres instructions
   elif test 3:
       encore des instructions
   else:
       les dernières instructions

.. warning::

    Le dernier ``else`` traitant les autres cas de figure n'est pas obligatoire.

.. admonition:: Exemple

    .. code-block:: python
    
        if a>0:
            print("Le nombre a est strictement positif")
        elif a<0:
            print("Le nombre a est strictement négatif")
        else:
            print("Le nombre a est nul")  
