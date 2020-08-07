#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import hashlib
import sys

mdp = input("Insérer ici un mot de passe à cracker : ")
#md5 très faillible, il renvoit des bytes et hexigest permet de retourner un string
mdp_md5 = hashlib.md5(mdp.encode("utf8")).hexdigest()


def hash_crack():
    try:
        liste_mot = open("./liste_francais.txt", "r")
        trouver = False
        for mot in liste_mot:
            mot = mot.strip("\n").encode("utf8")
            mot_hashed = hashlib.md5(mot).hexdigest()
            if mot_hashed == mdp_md5:
                print(f'Mot de passe trouvé : {mot} dont le hash est : {mot_hashed} en {time.time() - debut_crack} secondes')
                trouver = True
            if trouver:
                break
        if not trouver:
            print("Mot de passe non-trouvé")
        liste_mot.close()
    except FileNotFoundError:
        print("Fichier non trouvé")
        sys.exit(1)
    except Exception as err:
        print("Erreur trouvé dans hash_crack() :", err)
        sys.exit(2)


debut_crack = time.time()
res = hash_crack()
