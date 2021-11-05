# Module de conversion d'image en .webp
# Les images à convertir doivent être dans le dossier "fichiers_sources"
# Les images traitées (.png), vont être déplacé une fois le processus terminé dans le dossier "fichiers_traités"
# Les images convertis (.webp), vont être déplacé dans le dossier "exports_webp"

import os
import shutil
import sys
from subprocess import call
from posix import listdir


directory_path = os.getcwd()
fichiers = [f for f in listdir(directory_path + '/fichiers_sources/')]

def execute_commande(commande):
    try:
        retcode = call(commande, shell=True)
        if retcode < 0:
            print("Child was terminated by signal", -retcode, file=sys.stderr)
        else:
            print("Child returned", retcode, file=sys.stderr)
    except OSError as e:
        print("Execution failed:", e, file=sys.stderr)

def main():
    for fichier in fichiers:
        fichier_sans_extension = fichier[0:-4]
        nom_export = fichier_sans_extension + ".webp"
        commande = "cwebp -q 80 ./fichiers_sources/" + fichier +" -o ./exports_webp/" + nom_export
        execute_commande(commande)
        shutil.move('./fichiers_sources/'+ fichier, "fichiers_traités/"+fichier)


if __name__ == "__main__":
    main()