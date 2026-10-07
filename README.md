### Model de Machine Learning pentru categorizarea titlurilor de produse.

Ungureanu George

Salutare si bine ati venit la proiectul meu pentru categorizarea automata a produselor.

### 1 Cum functioneaza?

#### 1.1 Prezentarea modelului si scopului proiectului.

Acest proiect folosește un model de Machine Learning pentru a prezice din ce categorie de produse face parte un produs, astfel facilitând cu ușurință denumirea produselor când sunt prea multe sau când trebuie să le transpunem în categoriile lor în site-urile online.

Modelul este entrenat pe un set de date de 30.000 de produse si are o acuratete de aproximativ 97% in setul de date curent care are un numar mic de categorii (1.2)

#### 1.2 Prezentarea datelor

Datele provin dintr-un set de date cu produse care include și caracteristici ale acestora. Dearece folosim Scikit-Learn, trebuie să avem aceleași coloane la antrnare ca și la inferență, așadar doar coloana "product_title" a fost aleasă pentru antntrenament. (pentru antrenare cu mai multe date și inferență cu un nuamr diferit putem folosii alte librării)

#### 1.3 Prezentarea antrenării

Antrenarea mai multe modele și luăm cel cu echilibrul cel mai bun (scorul f1 cel mai mare), cel mai bun model este LinearSVC.

#### 1.4 Modelul ca obiect binar

După ce termină antrenarea, îl salvăm ca obiect .pkl (best_model.pkl din models/)

### 2 Cum îl folosim

#### 2.1 Importatea

în fișierul 'use_model.py' extragem modelul și facem o buclă while, care rulează la infinit până scriem "exit".

#### 2.2 Datele introduse manual

Introducem de la tastatură fiecare titlu și primim categoria, dar poate fii extinsă funcționalitatea astfel încât să fie extrase și refăcute dintr-un excel sau DataFrame (dacă facem asta îi oferim toată coloana nu fiecare în parte, dar pentru mai multe categorii trebuie reantrenat modelul).

#### 2.3 Folosirea 

Rulăm fișierul din consolă cu "python use_model.py" și introducem de la tastatură fiecare nume în parte, și sub acesta va apărea categoria acestuia. (categorii disponibile doar în engleză : mobile_phones, tvs, cpus, digital_cameras, microwaves, dishwashers, washing_machines, freezers, fridges)
