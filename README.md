# analyse_harmonique
#Programme d'analyse musicale
#Ce logiciel permet de donner l'ensemble des combinaisons pour une série de note
#La mélodie est en fonction d'une gamme majeur ou mineur qui est une matrice ou plutôt un vecteur

#Les notes de la gamme indiquent dans le cas d'un accord à trois notes 3 possibilités d'accord

#Le calcul combinatoire permet de constater qu'il existe 9**n en fonction du nombre de note dans la mélodie
#Ceci indique qu'il y a une combinaison élevé de possibilité tout en restant dans le domaine du quantifiable

#À titre d'exemple la note Do ou C peut avoir trois nature différente: accorde do, accord de fa, accord de la.
#Également pour chaque accord il existe de position. Fondamentale, premier et deuxième renversement

#L'objectif du programme est de réduire les combinaisons et cela en faisant usage à la fois du cycle de quinte(Voir Luce Beaudet) et les mécaniques de progression de Schoenberg
#L'harmonie tonale contient des règles implicite qui semblent répondre à une logique plus profonde.

#L'étape dans laquelle je suis en date du 24 mars est de faire la démonstration de l'ensemble des combinaisons avant d'ajouter des filtres sur les combinaisons