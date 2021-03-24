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


melo =gamme_majeur[[0] + [1]]

#print(melo[0])

###########################
#Options pour 1
n = 0
progression_harmonique = []
while n < 18:

        for i in melo:

            if i == gamme_majeur[0] and (n < 1 or n - 9 == 0):
                progression_harmonique.append(accord_maj_fond[0])
            elif i == gamme_majeur[0] and (n < 2 or n - 9 == 1):
                progression_harmonique.append(accord_maj_premier_renv[0])
            elif i == gamme_majeur[0] and (n < 3 or  n - 9 == 2):
                progression_harmonique.append(accord_maj_deuxie_renv[0])
############################################################################
#Pour la deuxieme option qui est VI
############################################################################
            elif i == gamme_majeur[0] and (n < 4 or  n - 9 == 3):
                progression_harmonique.append(accord_maj_fond[5])
            elif i == gamme_majeur[0] and (n < 5 or  n - 9 == 4):
                progression_harmonique.append(accord_maj_premier_renv[5])
            elif i == gamme_majeur[0] and (n < 6 or  n - 9 == 5):
                progression_harmonique.append(accord_maj_deuxie_renv[5])
############################################################################
# Pour la troisieme option qui est IV
############################################################################
            elif i == gamme_majeur[0] and (n < 7 or  n - 9 == 6):
                progression_harmonique.append(accord_maj_fond[3])
            elif i == gamme_majeur[0] and (n < 8 or  n - 9 == 7):
                progression_harmonique.append(accord_maj_premier_renv[3])
            elif i == gamme_majeur[0] and (n < 9 or  n - 9 == 8):
                progression_harmonique.append(accord_maj_deuxie_renv[3])

        #Options pour 2
            elif i == gamme_majeur[1]:
               progression_harmonique.append(accord_maj_fond[1])
            elif i == gamme_majeur[1]:
                progression_harmonique.append(accord_maj_premier_renv[1])
            elif i == gamme_majeur[1]:
                progression_harmonique.append(accord_maj_premier_renv[1])
        #Options pour 3
            elif i == gamme_majeur[2]:
                #print(i)
                progression_harmonique.append(accord_maj_fond[2])
        #Options pour 4
            elif i == gamme_majeur[3]:
                progression_harmonique.append(accord_maj_fond[3])
                #print(i)
        #Options pour 5
            elif i == gamme_majeur[4]:
                progression_harmonique.append(accord_maj_fond[4])
                #print(i)
        #Options pour 6
            elif i == gamme_majeur[5]:
                progression_harmonique.append(accord_maj_fond[5])
                #print(i)
        #Options pour 7
            elif i == gamme_majeur[6]:
                progression_harmonique.append(accord_maj_fond[6])
                #print(i)
        n = n + 1
print(progression_harmonique)