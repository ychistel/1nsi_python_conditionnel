Exercices : structure conditionnelle
====================================

Exercice 1
----------

On considère les variables ``a = 4`` et ``b = 7``. 

1. Les tests suivants sont-ils vrais ou faux ?

   a. ``a < 5``
   b. ``b > 7``
   c. ``-a > -2``
   d. ``b % a == 2`` 
   
2. Écrire des tests pour vérifier si :

   a. La variable ``a`` est négative.
   b. La variable ``a`` différente de 0.
   c. La variable ``b`` supérieure à la variable ``a``
   d. La variable ``b`` est divisible par la variable ``a``.
   
Exercice 2
----------

Pour savoir si un nombre est pair, on effectue l'opération **modulo** avec le symbole ``%``. Ce modulo donne le reste de la division entière. Par exemple : ``5 % 2`` qui vaut 1.

1. Quel est le reste de la division d'un nombre ``n`` par 2 lorsqu'il est pair ? impair ?
2. Écrire un code qui affiche si un nombre ``n`` donné est pair ou impair.

Exercice 3
----------

Une année est bissextile si elle est divisible par 4 mais pas par 100 ou si elle est divisible par 400. Écrire un code en Python qui pour une année donnée affiche si c'est une année bissextile.

Exercice 4
----------

La variable ``t`` est un tableau contenant les valeurs ``t=[1,9,3,8,4,7,2,6,5]``. Pour chaque question, on reprendra le tableau ``t`` donné initialement.

#. Écrire un code qui remplace chaque nombre impair du tableau par 0.
#. Écrire un code qui affiche la valeur maximale contenue dans le tableau.
#. Écrire un code qui affiche la valeur minimale contenue dans le tableau.

Exercice 5
----------

.. caution::
   
   Plutôt réservé aux élèves qui suivent la spécialité maths.

Pour saisir une valeur entière en Python et l'affecter à une variable, on utilise les fonctions ``int`` et ``input``. On donne un exemple d'utilisation:

.. code-block:: python

   a = int(input("valeur du coefficient: "))

1. Écrire un code pour saisir trois nombres entiers ``a``, ``b`` et ``c`` correspondant aux coefficients d'un polynôme du second degré :math:`ax^{2}+bx+c`.
2. Écrire le code de la fonction ``discriminant`` qui a 3 paramètres ``a``, ``b`` et ``c`` et qui renvoie la valeur du discriminant du polynôme. 
3. Écrire un code qui affirme si le polyôme admet 0, 1 ou 2 racines.
4. Compléter votre code pour donner la valeur des racines quand elles existent. Il faut importer la fonction ``sqrt()`` du module ``math`` qui calcule la racine carrée d'un nombre passé en argument.
