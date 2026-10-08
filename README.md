English version, Romanian version bellow (Versiune în Română mai jos)

### Machine Learning Model for Categorizing Product Titles

Ungureanu George

Hello and welcome to my project for automatic product categorization.

### 1 How Does It Work?

#### 1.1 Overview of the Model and Project Purpose

This project uses a Machine Learning model to predict which product category a product belongs to, thus making it easier to name products when there are too many or when we need to place them into their categories on online sites.

The model is trained on a dataset of 30,000 products and has an accuracy of approximately 97% on the current dataset, which has a small number of categories (1.2).

#### 1.2 Data Overview

The data comes from a product dataset that also includes product features. Because we use Scikit-Learn, we must have the same columns during training as during inference, so only the `"product_title"` column was chosen for training. (For training with more data and inference with a different number, we can use other libraries.)

#### 1.3 Training Overview

We train multiple models and take the one with the best balance (the highest F1 score). The best model is LinearSVC.

#### 1.4 The Model as a Binary Object

After training finishes, we save it as a `.pkl` object (`best_model.pkl` in `models/`).

### 2 How We Use It

#### 2.1 Importing

In the `use_model.py` file, we extract the model and make a `while` loop that runs indefinitely until we type `"exit"`.

#### 2.2 Manually Entered Data

We enter each title from the keyboard and receive its category, but the functionality can be extended so that they are extracted and recreated from an Excel file or DataFrame (if we do this and provide the entire column, not each one separately, but for more categories the model must be retrained).

#### 2.3 Usage

* [ ] We run the file from the console with `"python use_model.py"` and enter each name individually from the keyboard, and below it its category will appear. (Categories available only in English: `mobile_phones`, `tvs`, `cpus`, `digital_cameras`, `microwaves`, `dishwashers`, `washing_machines`, `freezers`, `fridges`)

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
