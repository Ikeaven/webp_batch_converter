# Module de conversion d'image en .webp
# Les images à convertir doivent être dans le dossier "fichiers_sources"
# Les images traitées (.png), vont être déplacé une fois le processus terminé dans le dossier "fichiers_traités"
# Les images convertis (.webp), vont être déplacé dans le dossier "exports_webp"

import os
import shutil
import sys
from subprocess import call
from posix import listdir
from PIL import Image




CWD = os.getcwd()
FICHIERS = [f for f in listdir(CWD + '/fichiers_sources/')]
RESIZES = [350, 250, 155]

def execute_commande(commande):
    try:
        retcode = call(commande, shell=True)
        if retcode < 0:
            print("Child was terminated by signal", -retcode, file=sys.stderr)
        else:
            print("Child returned", retcode, file=sys.stderr)
    except OSError as e:
        print("Execution failed:", e, file=sys.stderr)

def resize_image(image_url):
    image = Image.open("fichiers_sources/"+image_url)

    for resize in RESIZES:
        new_image = image.resize((resize, resize))
        new_image.save("./exports_resizes/"+image_url[0:-4]+"_"+str(resize)+image_url[-4:])



def main():
    for fichier in FICHIERS:
        fichier_sans_extension = fichier[0:-4]
        nom_export = fichier_sans_extension + ".webp"
        commande = "cwebp -q 80 ./fichiers_sources/" + fichier +" -o ./exports_webp/" + nom_export
        execute_commande(commande)
        resize_image(fichier)
        shutil.move('./fichiers_sources/'+ fichier, "fichiers_traités/"+fichier)


if __name__ == "__main__":
    main()