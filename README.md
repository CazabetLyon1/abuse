# Projet Walletexplorer : 


* Projet réalisé dans le cadre de l'UE POM pour l'extraction des informations relatives aux bitcoins sur les réseaux sociaux 


## Authors 


* POITEVIN Louis & SAKKA AMINI Khaled

* Encadrant : CAZABET Remy


## Required 


* python sur linux : <code>sudo apt-get install python</code>

* python sur macos : <code>brew install python3</code>

* scrapy : <code>pip3 install scrapy</code>

* jupyter : <code> pip3 install jupyter</code>

* pandas : <code>pip3 install pandas</code>


## Objectif


* Associer les adresses bitcoins a des noms de service et leurs catégories


## Avancement


* Possibilité de récupérer toutes les adresses bitcoin dans site

* reduction des redoublant


## How to 


* <code>git clone https://forge.univ-lyon1.fr/p1411478/abuse.git</code>

* <code>cd abuse/abuse/abuse</code> 

* <code>scrapy crawl abuse -o keys.csv </code>

* La dernière commande va extraire les données et créer des fichers csv suivants :  
    * keys.csv contient tous les clés avoir un report sur site

⚠️ ️️please delete keys.csv before doing this  ⚠️
thank you, kindly 😘

finally 

* <code> jupyter notebook  </code>

and open pandas_dublicate.ipynb in web browser



    





