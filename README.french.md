# Exercice école : 
## Etape 1 
Le directeur d'entreprise de produits chimiques souhite gérer les salaires et primes avec un programme

Un employée est caractérisée par : 
- Nom
- Prénom
- Age
- Date entrée

Fonction abstraite "calculerSalaire"
Fonction getNom return "L'employé "prenom" "nom"
-----------------
## Etape 2
4 Type d'employer : 
- Vente
- Représentation
- Technique
- Manutention



Calcul du salaire mensuel dépend du type de l'empoyer : 
- Vente : salaire_mens = 20% chiffre d'affaire + 400€
- Représentation : salaire_mens = 20% chiffre d'affaire + 800€
- Technique : salaire_mens = unité_produit * 5
- Manutention : salaire_mens = nb_heure * 65€


---------------------------------------
## Etape 3s
Certains employée sont dans des secteurs de risque et on ne prime mensuelle de 200€ -> PAS FAIS LA GESTION DE RISQUE
- Compléter votre programme en introduisant deux nouvelles sous class d'employes. Ces sous classes designent les employées des secteurs production & manutention.
- Satisfait de la hiérarchie proposée, notre directeur souhaite maintenant l'exploiter pour afficher le salaire de tout ses employes ainsi que le salaire moyen

Ajoutez une classe Personnel contenant une collection d'employés. Il s'agira d'une collection polymorphique d'Employe, définisser ensuite les methodes suivantes a la classes Personnel:

- ajoutEmploye(Employe), ajout un employé a la collection
- afficherSalaire(), affiche le salaire
- salaireMoyen(), affiche le salaire moyen de la collection -> PAS FAIT