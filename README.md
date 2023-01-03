# Setup

Install Python (at least 3.7) and pip
1. > https://www.python.org/downloads/
2. > python -m ensurepip --upgrade

Install the requirements from requirements.txt
> pip install -r requirements.txt

# Run
> python3 BoundingBoxTest.py 

# Problem

Se da o imagine de dimensiuni width x height si un dicționar de forma {clasa1: [lista de dreptunghiuri], clasa2: [lista de dreptunghiuri], ...} cu maxim 8 clase
Listele de dreptunghiuri au forma [[x1, y1, x2, y2], [x1, y1, x2, y2], ...]; dreptunghiurile se pot suprapune intre ele

In primul rand, toate perechile de dreptunghiuri (doua sau mai multe) care se suprapun si apartin aceleiasi clase trebuie trebuie unite intr+un nou dreptunghi care sa fie de arie minima si sa le contina pe toate

Apoi, pentru fiecare dreptunghi trebuie determinata pozitia din imagine x,y la care se poate afisa un text de dimensiune width_text, height_text (care afiseaza numele clasei), astfel incat textul sa fie cat mai aproape de unul din colturile dreptunghiului aferent, sa nu se afle pe perimetrul niciunui dreptunghi si daca se poate, acesta trebuie sa nici nu se afle in interiorul niciunui dreptunghi

# Code

Codul dat citeste imaginea img.jpeg si lista de dreptunghiuri din bounding_boxes.json, le afiseaza pe imagine (de mai multe ori, pentru a calcula timpul de executie), apoi salveaza rezultatul in fisierul out.jpeg. Codul trebuie modificat sub linia MODIFY THIS