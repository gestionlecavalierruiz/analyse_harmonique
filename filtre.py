import random

accord_majeur_fond = ["I","II","III","IV","V","VI","VII"] #pourquoi travailler encore avec des chiffres romains,
accord_majeur_premier_renv = ["I6","II6","III6","IV6","V6","VI6","VII6"]
accord_majeur_deuxie_renv = ["I64","II64","III64","IV64","V64","VI64","VII64"]
accord_dom_7 =["V7","V65","V43","V2"]
accord_dom =["V","V6","V64"]
accord_predom=["II7","II65","II43","II2"]
dom_sec_fond = ["V/II","V/III","V/IV","V/V","V/VI","V/VI","V/VII"]
dom_sec_premier = ["V/II","V/III","V/IV","V/V","V/VI","V/VI","V/VII"]
dom_sec_second =["V/II","V/III","V/IV","V/V","V/VI","V/VI","V/VII"]
dom_sec_troisieme=["V7/II","V7/III","V7/IV","V7/V","V7/VI","V7/VI","V7/VII"]
######################################################
#une categorie speciale est necessaire pour isole les notes de la melodie ayant un lien avec le V
#Inventaire VD, IID ### attention au d minuscule ou majuscule.
######################################################

melodie =("NUL","I","II","III","V","II","NUL")

#""I","I","II","III","II","III","IV","III","II","II","I","NUL")
# travail 3 premieNUL","III","IV","III","II","I","VII","I","II","II","II","I","NUL")
######################################################
#ajout d'une fonction pour être en mesure de travailler directement dans le terminal
def melodie_notes(a):
    liste_note = []
    print (a)
    return
######################################################
sequence = []
#repertoire des options

long = len(melodie)


for i in range(1, long): #modification sur le range pour cibler toutes les notes

    a = random.randrange(0, 2) #pour tenir compte des echanges

    if melodie[i] == "I":
        if melodie[i-1] == "NUL":
            sequence.append(accord_majeur_fond[0]) # si le premier accord

        elif melodie[i-1] == "VII":
            try:
                if sequence.index("V43",i-2):
                    sequence.append(accord_majeur_premier_renv[0])
                elif sequence.index("I64", i - 2):
                    sequence.append(accord_majeur_fond[0])
            except:
                    sequence.append(accord_majeur_fond[0])
        elif melodie[i-1] == "I" and melodie[i+1] == "II":
            sequence.append(accord_majeur_fond[5])
        elif melodie[i-1] == "I":
            sequence.append(accord_majeur_fond[3])
        elif melodie[i-1] == "V":
            sequence.append(accord_majeur_premier_renv [0])
        elif melodie[i-1] == "II":
            try:
                if sequence.index("II6",i-2):
                    sequence.append(accord_majeur_deuxie_renv[0])
            except:
                    sequence.append(accord_majeur_fond[0])
        elif melodie[i-1] == "IID":
            sequence.append(accord_majeur_fond[0])


    elif melodie[i] == "II":
        if melodie[i-1] == "IV":
            sequence.append(accord_majeur_fond[4])
        else:
            sequence.append(accord_majeur_premier_renv[1]) #regle du renversement de II6

    elif melodie[i] == "IID": # ecriture pour indiquer avec le D qu'il s'agit d'une dominante.
        if melodie[i-1] == "III":
            sequence.append(accord_dom[0])
        else:
            sequence.append(accord_majeur_premier_renv[4]) #regle du renversement de II6

    elif melodie[i] == "IID1": # ici il s'agit plutot d'indiquer une dominante seconde avec la matrice de dominante secondaire
            sequence.append(dom_sec_fond[3]) # attention parce qu'il n'y a pas encore les alterations

    elif melodie[i] == "III":
        if melodie[i-1] == "NUL":
            sequence.append(accord_majeur_fond[0])  # progression I VI
        elif melodie[i-1] == "VII":
            sequence.append(accord_majeur_fond[0])
        elif melodie[i-1] == "II":
            if sequence.index("II6",i-2) and melodie[i+1] == "IV":
                sequence.append(accord_majeur_fond [1])
            if sequence.index("II6",i-2):
                sequence.append(accord_majeur_deuxie_renv[0])
        elif melodie[i-1] == "IV":
            if sequence.index("II6",i-2):
                sequence.append(accord_majeur_deuxie_renv[0])
        elif melodie[i-1] == "III" and melodie[i+1] == "II":
            sequence.append(accord_majeur_fond[5])
        elif melodie[i-1] == "IVD":
            sequence.append(accord_majeur_fond[0])
        elif melodie[i-1] == "VD":
            sequence.append(accord_majeur_fond[0])
###########Pour tenir compte de la zone dominante ##################
        #elif melodie[i-1] == "VI" and  sequence.index("VI",i-2): #Il faudra creer des categorie speciale pour les IV comme IVd pour signifier dans la melodie l'intention dune zone dominante
        #    sequence.append(accord_majeur_fond[5])
        else:
            sequence.append(accord_majeur_fond[2])# fondamental

    elif melodie[i] == "IV":
        if melodie[i-1] == "IV":
            sequence.append(accord_dom[0])
        if melodie[i-1] == "III":
            sequence.append(accord_majeur_premier_renv[1]) # pour le renversement II6
        #elif a == 0:
        #    sequence.append(accord_majeur_premier_renv[1])
        else:
            sequence.append(accord_majeur_fond[3])

    elif melodie[i] == "IVD":
        if melodie[i-1] == "V":
            sequence.append(accord_dom_7[1])
        else:
            sequence.append(accord_majeur_fond[3])


    elif melodie[i] == "V":
        if melodie[i-1] == "NUL":
            sequence.append(accord_majeur_fond[0]) # si le premier accord
        elif melodie[i-1] == "V":
            sequence.append(accord_majeur_fond[0])
        elif melodie[i+1] == "IV" and melodie[i+2] == "IV":
            sequence.append(accord_majeur_premier_renv[0])
        else:
            sequence.append(accord_majeur_fond[4])

    elif melodie[i] == "VD":
        if melodie[i-1] == "III":
            sequence.append(accord_dom[1])
        elif melodie[i-1] == "V":
            sequence.append(accord_dom[1])
        else:
            sequence.append(accord_majeur_fond[4])


    elif melodie[i] == "VI":
        if melodie[i-1] == "I" or melodie[i+1] == "VII":
            sequence.append(accord_majeur_fond[5])  # progression I VI ou I IV. Il est necessaire de faire appel au cycle des quintes
        elif melodie[i-1] == "V":
            sequence.append(accord_majeur_fond[3])
        elif melodie[i-1] == "I":
            sequence.append(accord_majeur_fond[3])
        elif melodie[i-1] == "VI":
            sequence.append(accord_majeur_fond[1])
        else:
            sequence.append(accord_majeur_fond[5]) # fondamental

    elif melodie[i] == "VII":
        if melodie[i-1] == "I":
            sequence.append(accord_majeur_fond[4])  # progression I VI
        elif melodie[i-1] == "II":
            sequence.append(accord_majeur_fond[4])
        elif melodie[i-1] == "III":
            sequence.append(accord_dom_7[2])
        elif melodie[i-1] == "IV":
            sequence.append(accord_majeur_fond[4])
        elif melodie[i-1] == "VI":
            sequence.append(accord_majeur_fond[4])
        elif melodie[i-1] == "VII":
            sequence.append(accord_majeur_fond[4])
        else:
            sequence.append(accord_majeur_fond[6])# fondamental



print(sequence)

###########################################################

# inventaire
#Tonique: I Extension I6, IV, VI
#Predominant: IV , II6, VI
#Dominant: V
#Cadence
#

#################################################
#
#probleme du V V7, à quel moment choisir l'une ou l'autre des formes
#
#Probleme du choix entre deux progressions, exemple [I IV ii V I] et [I IV VI V I]