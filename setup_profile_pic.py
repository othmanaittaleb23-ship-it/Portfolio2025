import shutil
import os

def copy_profile_pic():
    # Chemin source de votre photo de profil
    source = r'C:\Users\3tttman\CascadeProjects\Portfolio2025\CV_2025-10-16_Othman_Ait taleb.pdf'  # Remplacez par le chemin réel de votre photo
    
    # Chemin de destination pour la photo de profil
    destination_dir = 'portfolio/static/images'
    destination = os.path.join(destination_dir, 'profile.jpg')
    
    try:
        # Créer le dossier de destination s'il n'existe pas
        os.makedirs(destination_dir, exist_ok=True)
        
        # Copier la photo de profil
        shutil.copy2(source, destination)
        print(f"Photo de profil copiée avec succès vers : {destination}")
        
    except Exception as e:
        print(f"Erreur lors de la copie de la photo de profil : {e}")
        print("\nVeuillez copier manuellement votre photo de profil dans le dossier :")
        print(f"{os.path.abspath(destination_dir)}/profile.jpg")

if __name__ == "__main__":
    copy_profile_pic()
