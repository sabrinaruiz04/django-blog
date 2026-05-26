# Blog Django M3-UF6

## Introducció
Projecte de blog desenvolupat amb Django com a part del mòdul M3-UF6. Permet gestionar posts, autors i etiquetes.

## Instal·lació ràpida

### 1. Clona el repositori
git clone <URL_DEL_TEU_REPOSITORI>
cd my_site

### 2. Crea i activa l'entorn virtual
python -m venv venv
.\venv\Scripts\Activate.ps1

### 3. Instal·la les dependències
pip install -r requirements.txt

### 4. Executa les migracions
python manage.py migrate

### 5. Carrega les dades inicials
python manage.py loaddata blog/fixtures/initial_data.json

## Execució del projecte
python manage.py runserver

Accedeix al blog a: http://127.0.0.1:8000
Accedeix al panell d'administració a: http://127.0.0.1:8000/admin
