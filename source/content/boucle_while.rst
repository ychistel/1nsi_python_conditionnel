Boucle conditionnelle
=====================

Une boucle **conditionnelle** répète une ou plusieurs instructions autant de fois que la **condition** de boucle est vraie. En Python, une boucle conditionnelle se fait avec le mot clé ``while`` suivi de la condition à vérifier.

.. note::

    -  La boucle ``while`` exécute les instructions contenues dans la boucle **tant que la condition donnée est vraie**.
    -  Une boucle ``while`` peut être infinie et ne jamais s’arrêter. Si la condition est toujours vraie!
    -  La boucle ``while`` est **non bornée**. On ne sait pas combien de fois vont être répétées les instructions dans la boucle.

La syntaxe d’une boucle ``while`` est la suivante:

.. code:: python

   while condition:
       instruction 1
       instruction 2
       etc
   # on désindente en fin de boucle

.. admonition:: Exemple

    On demande la saisie d'un nombre entier positif et on veut afficher les nombres pairs positifs inférieurs au nombre saisi.

    .. code-block:: python
    
        n = int(input("saisir un nombre entier:"))
        i = 2
        while i <= n:
            print(i)
            i = i + 2

    Si on saisit le nombre 9, on obtient l'affichage:
    
    .. code-block:: python
    
        2
        4
        6
        8

.. warning::

    Lorsqu'on utilise une boucle ``while`` pour exécuter un nombre fini de fois des instructions, il faut s'assurer de la terminaison de la boucle, c'est à dire que le test peut prendre la valeur ``False`` et ainsi arrêter la boucle.
