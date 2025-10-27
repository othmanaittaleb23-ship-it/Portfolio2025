@echo off
echo Arrêt des processus Python en cours...
taskkill /F /IM python.exe

echo Mise à jour des données du portfolio...
python update_portfolio.py

echo Copie de la photo de profil...
python setup_profile_pic.py

echo Rechargement des données...
python manage.py loaddata portfolio/fixtures/sample_data.json

echo Démarrage du serveur...
start "" "%COMSPEC%" /k "python manage.py runserver"

echo.
echo Votre portfolio est en cours de démarrage...
echo Accédez à votre portfolio à l'adresse : http://127.0.0.1:8000/
echo.
pause
