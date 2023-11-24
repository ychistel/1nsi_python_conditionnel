TP turtle et boucle conditionnelle
==================================

On reprend le code de la tortue qui se déplace aléatoirement dans 6 directions différentes comme le montre la figure ci-dessous:

   .. image:: ../img/6_directions.svg
      :align: center
      :width: 240

La tortue se déplace un nombre de fois fixé par la variable ``n``. On souhaite que la tortue se déplace tant qu'elle vérifie une condition, un test.

Cette structure est la **boucle conditionnelle**. Cela signidie que les instructions placées dans la boucles sont exécutées **tant que** la condition est vraie. 

En Python, la syntaxe de cette boucle conditionnelle est:

   .. code-block:: python
   
      while "condition":
          instructions

1. Écrire la fonction ``direction_aleatoire()`` qui choisit aléatoirement la direction de la tortue parmi les 6 possibles.
2. La fonction ``position()`` renvoie les coordonnées ``x`` et ``y`` de la position de la tortue.

   .. code-block:: python
   
      x,y = position()
      
   Écrire une boucle qui déplace aléatoirement la tortue tant que la valeur de ``y`` est supérieure ou égale à 0. Ne pas oublier de récupérer la position de la tortue à chaque itération!
   
3. Transformer votre code pour que la tortue se déplace tant que la valeur de ``x`` est inférieure à 100.

4. On souhaite que la tortue se déplace tant que la variable ``y`` est comprise entre -100 et 100.

   a. Comment écrit-on cette condition ?
   b. Transformer votre code pour que la tortue respecte cette condition.

5. La tortue se déplace dans un carré centré en ``(0,0)`` de côté défini par la variable ``dimension``. 
   
   .. image:: ../img/tortue_dans_carre.png
      :align: center
      :width: 240
      
   a. Comment écrire la condition de la boucle ? 
   b. Écrire le code de la fonction ``trace`` qui trace le carré centré de côté ``dimension``.
   c. Transformer votre code pour que la tortue se déplace à l'intérieur de ce carré.
