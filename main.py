#!/usr/bin/env python 

from abc import ABC, abstractmethod

class Personnel():
    def __init__(self):
        self.index = -1
        self.__collection_employer = []
        pass
    
    def ajouterEmploye(self,Employer) -> []:
        self.__collection_employer.append(Employer)


    def afficherSalaire(self):
        for employer in self.__collection_employer:
            print(f"Salaire de {employer.getNom()}, est de {employer.calculerSalaire()}")


    def __iter__(self):
        return self

    #  Use to iter over __collection_employer
    def __next__(self):
        self.index += 1
        if self.index == len(self.__collection_employer):
            raise StopIteration
        return self.__collection_employer [self.index]


class Employer(ABC):
    def __init__(self, name, age, prenom, date_entree):
        self.__name = name
        self.__prenom = prenom
        self.__age = age
        self.__date_entree = date_entree


    def getNom(self) -> str:
        return f"Employé : {self.__name} {self.__prenom}, type : {type(self)}"
        # print(f"Employé : {self.__name} {self.__prenom}, type : {type(self)}")

    @abstractmethod
    def calculerSalaire():
        pass


class Commercial(Employer, ABC):
    def __init__(self, name, age, prenom, date_entree , chiffre_affaire):
        super().__init__(name, age, prenom, date_entree)
        # self.__name = name
        # self.__prenom = prenom
        # self.__age = age
        # self.__date_entree = date_entree
        self.__chiffre_affaire = chiffre_affaire
    
    def getNom(self) -> str:
        # FIXME: Same here
        return f"Commercial : {self._Employer__name} {self._Employer__name}, type : {type(self)}"


class Vente(Commercial):
    def __init__(self, name, age, prenom, date_entree , chiffre_affaire):
        super().__init__(name, age, prenom, date_entree, chiffre_affaire)
        # self.__name = name
        # self.__prenom = prenom
        # self.__age = age
        # self.__date_entree = date_entree
        # self.__chiffre_affaire = chiffre_affaire

    def calculerSalaire(self) -> float:
        # FIXME: Not working, how could i have the __chiffre_affaire 
        # that is defined in the commercial class
        # I'm guessing that if i define self.__chiffre_affaire in the `__init__`, i could access it here
        # return self.__chiffre_affaire * 20/100 + 400 
        return self._Commercial__chiffre_affaire * 20/100 + 400

    def getNom(self) -> str:
        # FIXME: Same here
        return f"Vendeur : {self._Employer__name} {self._Employer__prenom}, type : {type(self)}"


class Représentation(Commercial):
    def __init__(self, name, age, prenom, date_entree , chiffre_affaire):
        super().__init__(name, age, prenom, date_entree, chiffre_affaire)
    
    def calculerSalaire(self) -> float :
        return self._Commercial__chiffre_affaire * 20/100 + 800
    
    def getNom(self) -> str:
        # FIXME: Same here
        return f"Représentation : {self._Employer__name} {self._Employer__prenom}, type : {type(self)}"




class Technique(Employer):
    def __init__(self, name, age, prenom, date_entree , unit_prod):
        super().__init__(name, age, prenom, date_entree)
        self.__unit_prod = unit_prod
    
    def calculerSalaire(self) -> float:
        return self.__unit_prod * 5

    def getNom(self) -> str:
        # FIXME: Same here
        return f"Technique : {self._Employer__name} {self._Employer__prenom}, type : {type(self)}"

class Manutention(Employer):
    def __init__(self, name, age, prenom, date_entree , nb_heure):
        super().__init__(name, age, prenom, date_entree)
        self.__nb_heure = nb_heure

    def calculerSalaire(self) -> float:
        return self.__nb_heure * 65
    
    def getNom(self) -> str:
        # FIXME: Same here
        return f"Manutention : {self._Employer__name} {self._Employer__prenom}, type : {type(self)}"



if __name__ == "__main__":
    list_personnel = Personnel()

    vendeur = Vente(name="Dupont",age=50,prenom="Pierre", date_entree="10/01/2022", chiffre_affaire=50)
    représentation = Représentation(name="Guyot",age=50,prenom="Arthur",date_entree="10/10/1997",chiffre_affaire=30)
    technique = Technique(name="Petter", age=20, prenom="Mark", date_entree="666" , unit_prod=75)
    manutention = Manutention("Mich", 33, "Mich", "null", 300)




    list_personnel.ajouterEmploye(vendeur)
    list_personnel.ajouterEmploye(représentation)
    list_personnel.ajouterEmploye(technique)
    list_personnel.ajouterEmploye(manutention)

    list_personnel.afficherSalaire()
    # for employer in list_personnel:
    #     print(f"Employer de type : {employer.getNom()}, aillant pour salaire : {employer.calculerSalaire()}")