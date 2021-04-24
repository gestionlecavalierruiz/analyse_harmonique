import numpy as np
import pandas as pd

gamme_majeur = np.array([1,2,3,4,5,6,7])


accord_maj_fond = np.array(["I","II","III","IV","V","VI","VII"])
accord_maj_premier_renv = np.array(["I6","II6","III6","IV6","V6","VI6","VII6"])
accord_maj_deuxie_renv = np.array(["I64","II64","III64","IV64","V64","VI64","VII64"])
accord_dom_7 =np.array(["V7","V65","V43","V2"])
accord_dom =np.array(["V","V6","V64"])
accord_predom=np.array(["II7","II65","II43","II2"])
dom_sec_fond = np.array(["V/II","V/III","V/IV","V/V","V/VI","V/VI","V/VII"])
dom_sec_premier = np.array(["V/II","V/III","V/IV","V/V","V/VI","V/VI","V/VII"])
dom_sec_second =np.array(["V/II","V/III","V/IV","V/V","V/VI","V/VI","V/VII"])
dom_sec_troisieme=np.array(["V7/II","V7/III","V7/IV","V7/V","V7/VI","V7/VI","V7/VII"])


melo =gamme_majeur[[1] + [2] + [0]] #Important d'ajuster pair pour que la longeur soit consequente

#print(melo[1]) # test pour position de la note

#############################################################################
#Options pour 1
n = 1 #initialiser
nombre_limite = 81 # pour le nombre en lien avec 9**n qui indique la limite
progression_harmonique = [] #initialiser la nouvelle liste
while n < 10:
        #print(len(progression_harmonique))
        for i in melo:

            if i == gamme_majeur[0] and (n < 2 or n%9 == 1):
                progression_harmonique.append(accord_maj_fond[0])
            elif i == gamme_majeur[0] and (n < 3 or n%9 == 2):
                progression_harmonique.append(accord_maj_premier_renv[0])
            elif i == gamme_majeur[0] and (n < 4 or  n%9 == 3):
                progression_harmonique.append(accord_maj_deuxie_renv[0])

            elif i == gamme_majeur[0] and (n < 10 and n%9 == 1):
               progression_harmonique.append(accord_maj_fond[0])
            elif i == gamme_majeur[0]  and (n < 19 and n%9 == 2):
                progression_harmonique.append(accord_maj_premier_renv[0])
            elif i == gamme_majeur[0]  and (n < 28 and n%9 == 3):
                progression_harmonique.append(accord_maj_deuxie_renv[0])
############################################################################
#Pour la deuxieme option qui est VI
############################################################################
            elif i == gamme_majeur[0] and (n < 5 or  n%9 == 4):
                progression_harmonique.append(accord_maj_fond[5])
            elif i == gamme_majeur[0] and (n < 6 or  n%9 == 5):
                progression_harmonique.append(accord_maj_premier_renv[5])
            elif i == gamme_majeur[0] and (n < 7 or  n%9 == 6):
                progression_harmonique.append(accord_maj_deuxie_renv[5])

            elif i == gamme_majeur[0] and (n < 37 and n%9 == 4):
               progression_harmonique.append(accord_maj_fond[5])
            elif i == gamme_majeur[0]  and (n < 46 and n%9 == 5):
                progression_harmonique.append(accord_maj_premier_renv[5])
            elif i == gamme_majeur[0]  and (n < 55 and n%9 == 6):
                progression_harmonique.append(accord_maj_deuxie_renv[5])

############################################################################
# Pour la troisieme option qui est IV
############################################################################
            elif i == gamme_majeur[0] and (n < 8 or  n%9 == 7):
                progression_harmonique.append(accord_maj_fond[3])
            elif i == gamme_majeur[0] and (n < 9 or  n%9 == 8):
                progression_harmonique.append(accord_maj_premier_renv[3])
            elif i == gamme_majeur[0] and (n < 10 or  n%9 == 0):
                progression_harmonique.append(accord_maj_deuxie_renv[3])

            elif i == gamme_majeur[0] and (n < 64 and n%9 == 7):
               progression_harmonique.append(accord_maj_fond[3])
            elif i == gamme_majeur[0]  and (n < 73 and n%9 == 8):
                progression_harmonique.append(accord_maj_premier_renv[3])
            elif i == gamme_majeur[0]  and (n < 82 and n%9 == 0):
                progression_harmonique.append(accord_maj_deuxie_renv[3])
#############################################################################
#Options pour 2 avec accord de II qui est 1
#############################################################################

            #elif len(progression_harmonique)%2 != 0:###!!!!!!Attention ligne problematique

            elif i == gamme_majeur[1] and ( n < 2 and n%9 == 1) or i == gamme_majeur[1]  and (n > 9 and n%9 == 1):
                progression_harmonique.append(accord_maj_fond[1])
            elif i == gamme_majeur[1] and (n < 3 or n%9 == 2) or i == gamme_majeur[1] and  (n > 9 and n%9 == 2):
                progression_harmonique.append(accord_maj_premier_renv[1])
            elif i == gamme_majeur[1] and (n < 4 or n % 9 == 3) or i == gamme_majeur[1] and (n > 9 and n%9 == 3):
                progression_harmonique.append(accord_maj_deuxie_renv[1])

            #elif i == gamme_majeur[1] and (n < 10):# pour les tours plus eleve
             #   progression_harmonique.append(accord_maj_fond[1])
            #elif i == gamme_majeur[1]  and (n < 19):
            #    progression_harmonique.append(accord_maj_premier_renv[1])
            #elif i == gamme_majeur[1]  and (n < 28):
            #    progression_harmonique.append(accord_maj_deuxie_renv[1])
###############################################################################
#Options pour 2 V
###############################################################################
            #elif len(progression_harmonique) == 0:

            elif i == gamme_majeur[1] and (n < 5 and  n%9 == 4) or i == gamme_majeur[1] and (n > 9 and n%9 == 4):
                progression_harmonique.append(accord_maj_fond[4])
            elif i == gamme_majeur[1] and (n < 6 and  n%9 == 5) or i == gamme_majeur[1] and (n > 9 and n%9 == 5):
                progression_harmonique.append(accord_maj_premier_renv[4])
            elif i == gamme_majeur[1] and (n < 7 and  n%9 == 6) or i == gamme_majeur[1] and (n > 9 and n%9 == 6):
                progression_harmonique.append(accord_maj_deuxie_renv[4])

            #elif i == gamme_majeur[1] and (n < 37):
            #   progression_harmonique.append(accord_maj_fond[4])
            #elif i == gamme_majeur[1]  and (n < 46):
            #    progression_harmonique.append(accord_maj_premier_renv[4])
            #elif i == gamme_majeur[1]  and (n < 55):
            #    progression_harmonique.append(accord_maj_deuxie_renv[4])
###############################################################################
#Options pour 2 VII
###############################################################################
            #elif len(progression_harmonique) == 0:

            elif i == gamme_majeur[1] and (n < 8 and  n%9 == 7) or i == gamme_majeur[1] and (n > 9 and n%9 == 7):
                 progression_harmonique.append(accord_maj_fond[6])
            elif i == gamme_majeur[1] and (n < 9 and  n%9 == 8) or i == gamme_majeur[1] and (n > 9 and n%9 == 8):
                 progression_harmonique.append(accord_maj_premier_renv[6])
            elif i == gamme_majeur[1] and (n < 10 and  n%9 == 0) or i == gamme_majeur[1] and (n > 9 and n%9 == 0):
                 progression_harmonique.append(accord_maj_deuxie_renv[6])

            #elif i == gamme_majeur[1] and (n < 64):
            #    progression_harmonique.append(accord_maj_fond[6])
            #elif i == gamme_majeur[1]  and (n < 73 ):
            #    progression_harmonique.append(accord_maj_premier_renv[6])
            #elif i == gamme_majeur[1]  and (n < 82):
            #    progression_harmonique.append(accord_maj_deuxie_renv[6])
###############################################################################
#Options pour 3 III qui est 2
###############################################################################
            #elif len(progression_harmonique) == 0:

            #elif i == gamme_majeur[2] and (n < 2 and n%9 == 1):
            #    progression_harmonique.append(accord_maj_fond[2])
            #elif i == gamme_majeur[2] and (n < 3 and n%9 == 2):
            #    progression_harmonique.append(accord_maj_premier_renv[2])
            #elif i == gamme_majeur[2] and (n < 4 and n%9 == 3) :
            #    progression_harmonique.append(accord_maj_deuxie_renv[2])

            elif i == gamme_majeur[2] and (n < 10 ):
                progression_harmonique.append(accord_maj_fond[2])
            elif i == gamme_majeur[2] and (n < 19 ):
                progression_harmonique.append(accord_maj_premier_renv[2])
            elif i == gamme_majeur[2] and (n < 28 ):
                 progression_harmonique.append(accord_maj_deuxie_renv[2])
#############################################################################
#Options pour 3 I qui est 2
#############################################################################
            #elif len(progression_harmonique) == 0:

            # elif i == gamme_majeur[2] and (n < 5 and  n%9 == 4) :
            #     progression_harmonique.append(accord_maj_fond[0])
            # elif i == gamme_majeur[2] and (n < 6 and  n%9 == 5) :
            #     progression_harmonique.append(accord_maj_premier_renv[0])
            # elif i == gamme_majeur[2] and (n < 7 and  n%9 == 6) :
            #     progression_harmonique.append(accord_maj_deuxie_renv[0])

            elif i == gamme_majeur[2] and (n < 37 ):
                progression_harmonique.append(accord_maj_fond[0])
            elif i == gamme_majeur[2] and (n < 46 ):
                progression_harmonique.append(accord_maj_premier_renv[0])
            elif i == gamme_majeur[2] and (n < 55 ):
                 progression_harmonique.append(accord_maj_deuxie_renv[0])
#############################################################################
#Options pour 3 VI qui est 2
#############################################################################
            #elif len(progression_harmonique) == 0:

            # elif i == gamme_majeur[2] and (n < 8 and  n%9 == 7) :
            #     progression_harmonique.append(accord_maj_fond[5])
            # elif i == gamme_majeur[2] and (n < 9 and  n%9 == 8) :
            #     progression_harmonique.append(accord_maj_premier_renv[5])
            # elif i == gamme_majeur[2] and (n < 10 and  n%9 == 0) :
            #     progression_harmonique.append(accord_maj_deuxie_renv[5])

            elif i == gamme_majeur[2] and (n < 64 ):
                progression_harmonique.append(accord_maj_fond[5])
            elif i == gamme_majeur[2] and (n < 73 ):
                progression_harmonique.append(accord_maj_premier_renv[5])
            elif i == gamme_majeur[2] and (n < 82 ):
                 progression_harmonique.append(accord_maj_deuxie_renv[5])
############################################################################
#Options pour 4 IV qui est 3
############################################################################
            #elif len(progression_harmonique) == 0:

            elif i == gamme_majeur[3] and (n < 10 and n%9 ==1) :
                progression_harmonique.append(accord_maj_fond[3])
            elif i == gamme_majeur[3] and (n < 19 and n%9 ==2) :
                progression_harmonique.append(accord_maj_premier_renv[3])
            elif i == gamme_majeur[3] and (n < 28 and n%9 ==3) :
                progression_harmonique.append(accord_maj_deuxie_renv[3])

            elif i == gamme_majeur[3] and (n < 2 ):
                progression_harmonique.append(accord_maj_fond[3])
            elif i == gamme_majeur[3] and (n < 3 ):
                progression_harmonique.append(accord_maj_premier_renv[3])
            elif i == gamme_majeur[3] and (n < 4 ) :
                 progression_harmonique.append(accord_maj_deuxie_renv[3])

############################################################################
#Options pour 4 II
############################################################################
            #elif len(progression_harmonique) == 0:

            elif i == gamme_majeur[3] and (n < 5 or  n%9 == 4) :
                progression_harmonique.append(accord_maj_fond[1])
            elif i == gamme_majeur[3] and (n < 6 or  n%9 == 5) :
                progression_harmonique.append(accord_maj_premier_renv[1])
            elif i == gamme_majeur[3] and (n < 7 or  n%9 == 6) :
                progression_harmonique.append(accord_maj_deuxie_renv[1])

            elif i == gamme_majeur[3] and (n < 37 ) :
                progression_harmonique.append(accord_maj_fond[1])
            elif i == gamme_majeur[3] and (n < 46 ) :
                progression_harmonique.append(accord_maj_premier_renv[1])
            elif i == gamme_majeur[3] and (n < 55 ) :
                 progression_harmonique.append(accord_maj_deuxie_renv[1])

############################################################################
# Options pour 4 VII
############################################################################
            #elif len(progression_harmonique) == 0:

            elif i == gamme_majeur[3] and (n < 8 or  n%9 == 7) :
                progression_harmonique.append(accord_maj_fond[6])
            elif i == gamme_majeur[3] and (n < 9 or  n%9 == 8) :
                progression_harmonique.append(accord_maj_premier_renv[6])
            elif i == gamme_majeur[3] and (n < 10 or  n%9 == 0) :
                progression_harmonique.append(accord_maj_deuxie_renv[6])

            elif i == gamme_majeur[3] and (n < 64 ) :
                progression_harmonique.append(accord_maj_fond[6])
            elif i == gamme_majeur[3] and (n < 73 ) :
                progression_harmonique.append(accord_maj_premier_renv[6])
            elif i == gamme_majeur[3] and (n < 82 ) :
                progression_harmonique.append(accord_maj_deuxie_renv[6])
############################################################################
# Options pour 5 V
############################################################################
            #elif len(progression_harmonique) == 0:

            elif i == gamme_majeur[4] and (n < 2 or n%9 == 1):
                progression_harmonique.append(accord_maj_fond[4])
            elif i == gamme_majeur[4] and (n < 3 or n%9 == 2):
                progression_harmonique.append(accord_maj_premier_renv[4])
            elif i == gamme_majeur[4] and (n < 4 or n%9 == 3) :
                progression_harmonique.append(accord_maj_deuxie_renv[4])

            elif i == gamme_majeur[4] and (n < 10 ):
                progression_harmonique.append(accord_maj_fond[4])
            elif i == gamme_majeur[4] and (n < 19 ):
                progression_harmonique.append(accord_maj_premier_renv[4])
            elif i == gamme_majeur[4] and (n < 28 ):
                progression_harmonique.append(accord_maj_deuxie_renv[4])
############################################################################
#Options pour 5 III
############################################################################
            #elif len(progression_harmonique) == 0:

            elif i == gamme_majeur[4] and (n < 5 or  n%9 == 4) :
                progression_harmonique.append(accord_maj_fond[2])
            elif i == gamme_majeur[4] and (n < 6 or  n%9 == 5) :
                progression_harmonique.append(accord_maj_premier_renv[2])
            elif i == gamme_majeur[4] and (n < 7 or  n%9 == 6) :
                progression_harmonique.append(accord_maj_deuxie_renv[2])

            elif i == gamme_majeur[4] and (n < 37 ):
                progression_harmonique.append(accord_maj_fond[2])
            elif i == gamme_majeur[4] and (n < 46 ):
                progression_harmonique.append(accord_maj_premier_renv[2])
            elif i == gamme_majeur[4] and (n < 55 ):
                progression_harmonique.append(accord_maj_deuxie_renv[2])
############################################################################
#Options pour 5 I
############################################################################
            #elif len(progression_harmonique) == 0:

            elif i == gamme_majeur[4] and (n < 8 or  n%9 == 7) :
                progression_harmonique.append(accord_maj_fond[0])
            elif i == gamme_majeur[4] and (n < 9 or  n%9 == 8) :
                progression_harmonique.append(accord_maj_premier_renv[0])
            elif i == gamme_majeur[3] and (n < 10 or  n%9 == 0) :
                progression_harmonique.append(accord_maj_deuxie_renv[0])

            elif i == gamme_majeur[4] and (n < 64 ):
                progression_harmonique.append(accord_maj_fond[0])
            elif i == gamme_majeur[4] and (n < 73 ):
                progression_harmonique.append(accord_maj_premier_renv[0])
            elif i == gamme_majeur[4] and (n < 82 ):
                progression_harmonique.append(accord_maj_deuxie_renv[0])
############################################################################
#Options pour 6 VI
############################################################################
            #elif len(progression_harmonique) == 0:

            elif i == gamme_majeur[5] and (n < 2 or n%9 == 1):
                progression_harmonique.append(accord_maj_fond[5])
            elif i == gamme_majeur[5] and (n < 3 or n%9 == 2):
                progression_harmonique.append(accord_maj_premier_renv[5])
            elif i == gamme_majeur[5] and (n < 4 or n%9 == 3) :
                progression_harmonique.append(accord_maj_deuxie_renv[5])

            elif i == gamme_majeur[5] and (n < 10 ):
                progression_harmonique.append(accord_maj_fond[5])
            elif i == gamme_majeur[5] and (n < 19 ):
                progression_harmonique.append(accord_maj_premier_renv[5])
            elif i == gamme_majeur[5] and (n < 28 ):
                progression_harmonique.append(accord_maj_deuxie_renv[5])
############################################################################
#Options pour 6 IV
############################################################################
            #elif len(progression_harmonique) == 0:

            elif i == gamme_majeur[5] and (n < 5 or  n%9 == 4) :
                progression_harmonique.append(accord_maj_fond[3])
            elif i == gamme_majeur[5] and (n < 6 or  n%9 == 5) :
                progression_harmonique.append(accord_maj_premier_renv[3])
            elif i == gamme_majeur[5] and (n < 7 or  n%9 == 6) :
                progression_harmonique.append(accord_maj_deuxie_renv[3])

            elif i == gamme_majeur[5] and (n < 37  ):
                progression_harmonique.append(accord_maj_fond[3])
            elif i == gamme_majeur[5] and (n < 46 ):
                progression_harmonique.append(accord_maj_premier_renv[3])
            elif i == gamme_majeur[5] and (n < 55 ):
                progression_harmonique.append(accord_maj_deuxie_renv[3])
############################################################################
#Options pour 6 II
############################################################################
            #elif len(progression_harmonique) == 0:

            elif i == gamme_majeur[5] and (n < 8 or  n%9 == 7) :
                progression_harmonique.append(accord_maj_fond[1])
            elif i == gamme_majeur[5] and (n < 9 or  n%9 == 8) :
                progression_harmonique.append(accord_maj_premier_renv[1])
            elif i == gamme_majeur[5] and (n < 10 or  n%9 == 0) :
                progression_harmonique.append(accord_maj_deuxie_renv[1])

            elif i == gamme_majeur[5] and (n < 64 ):
                progression_harmonique.append(accord_maj_fond[1])
            elif i == gamme_majeur[5] and (n < 73 ):
                progression_harmonique.append(accord_maj_premier_renv[1])
            elif i == gamme_majeur[5] and (n < 82):
                progression_harmonique.append(accord_maj_deuxie_renv[1])
############################################################################
#Options pour 7 VII
############################################################################
            #elif len(progression_harmonique) == 0:

            elif i == gamme_majeur[6] and (n < 2 or n%9 == 1):
                progression_harmonique.append(accord_maj_fond[6])
            elif i == gamme_majeur[6] and (n < 3 or n%9 == 2):
                progression_harmonique.append(accord_maj_premier_renv[6])
            elif i == gamme_majeur[6] and (n < 4 or n%9 == 3) :
                progression_harmonique.append(accord_maj_deuxie_renv[6])

            elif i == gamme_majeur[6] and (n < 10 ):
                progression_harmonique.append(accord_maj_fond[6])
            elif i == gamme_majeur[6] and (n < 19 ):
                progression_harmonique.append(accord_maj_premier_renv[6])
            elif i == gamme_majeur[6] and (n < 28 ):
                progression_harmonique.append(accord_maj_deuxie_renv[6])
############################################################################
# Options pour 7 V
############################################################################
            #elif len(progression_harmonique) == 0:

            elif i == gamme_majeur[6] and (n < 5 or  n%9 == 4) :
                progression_harmonique.append(accord_maj_fond[4])
            elif i == gamme_majeur[6] and (n < 6 or  n%9 == 5) :
                 progression_harmonique.append(accord_maj_premier_renv[4])
            elif i == gamme_majeur[6] and (n < 7 or  n%9 == 6) :
                 progression_harmonique.append(accord_maj_deuxie_renv[4])

            elif i == gamme_majeur[6] and (n < 37 and n%9 == 4):
                progression_harmonique.append(accord_maj_fond[4])
            elif i == gamme_majeur[6] and (n < 46 and n%9 == 5):
                progression_harmonique.append(accord_maj_premier_renv[4])
            elif i == gamme_majeur[6] and (n < 55 and n%9 == 6):
                progression_harmonique.append(accord_maj_deuxie_renv[4])
############################################################################
#Options pour 7 III
############################################################################
            #elif len(progression_harmonique) == 0:

            elif i == gamme_majeur[6] and (n < 8 or  n%9 == 7) :
                progression_harmonique.append(accord_maj_fond[2])
            elif i == gamme_majeur[6] and (n < 9 or  n%9 == 8) :
                progression_harmonique.append(accord_maj_premier_renv[2])
            elif i == gamme_majeur[6] and (n < 10 or  n%9 == 0) :
                progression_harmonique.append(accord_maj_deuxie_renv[2])

            elif i == gamme_majeur[6] and (n < 64 ):
                progression_harmonique.append(accord_maj_fond[2])
            elif i == gamme_majeur[6] and (n < 73 ):
                progression_harmonique.append(accord_maj_premier_renv[2])
            elif i == gamme_majeur[6] and (n < 82 ):
                progression_harmonique.append(accord_maj_deuxie_renv[2])
        n = n + 1
#print(progression_harmonique)
print(len(progression_harmonique))
pair = 3 # longueur de la sequence

# using list comprehension pour afficher par ligne
final = [progression_harmonique[i * pair:(i + 1) * pair] for i in range((len(progression_harmonique) + pair - 1) // pair)]
print(*final, sep='\n')