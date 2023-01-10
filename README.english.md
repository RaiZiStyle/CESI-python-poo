# Exercice : 
## Step 1

A CEO of chimical product want to handle the salary of his employe with a programme

Employe : 
- First name
- Last name
- Age
- entree date

Define : 
1. An abstraict function "CalculSalary"
2. A function "getNom" that return "Employee 'first_name', 'last_name'"

-----------------------------

## Step 2

4 type of employe : 
- Seller
- Technical
- Material handling
- Commercial


Calcul of salary : 
- Seller  = 20% turnover + 400€
- Technical = unit_product * 5
- Commercial = 20% turnover + 800€
- Material handling = nb_hours * 65

---------------
## Step 3 
Add a class `Personnel` that contain a collection of employe. It should be a polymorphique class. Define those method : 

- addEmploye(Employe) : add an employe to the collection
- showSalary(): Show salary of each employe