import feedparser
from bs4 import BeautifulSoup

# on défini le flux rss a parser

Urls_de_ressources = ["https://www.lefigaro.fr/rss/figaro_actualites.xml"
                     ,"https://feeds.leparisien.fr/leparisien/rss/"
                      ]

# la liste titre contiendra tout les titres
titre = []

# la liste link contientra tout les liens
lien = []


# on créer un dictionnaire  à partir des précédentes listes
dictionnaire_titre_et_lien = []


# cette liste contiendra les titres obtenus suite à la recherche demandée, ces titres seront les clefs du dictionnaire
#pour permettre de retrouver les valeurs.
titres_obtenus = []


# on parler les liens souhaités pour alimenter nos listes puis notre dictionnaire.
for rss in Urls_de_ressources:
    feed = feedparser.parse(rss)

    # On boucle sur le flux pour récolter les titre et les liens
    for entry in feed.entries:

        # On collecte tous les titres et on les ajoute à la liste concernée
        title = entry.title
        titre.append(title)



        # On collecte tous les liens et on les ajoute à la liste concerncée
        link = entry.link
        lien.append(link)



        # on crée un dictionnaire avec les information collectées.
        dictionnaire_titre_et_lien.append(dict(zip(title, lien)))

print("***************************************************"
      "")
print("              DICTIONNAIRE CREE                    ")
print("***************************************************"
      "")



# on demande la recherche souhaité

question = input('entrez une recherche : ')

print(""
      "")

# on filtre la recherche dans la liste de titre qu'on a préalablement obtenu.

filtrage_question = list(filter( lambda x: question in x, titre))


# on boucle pour obtenir chaque élément de la liste de titre correspondant à la recherche.
# on ajoute les résultats dans une liste qui nous servira à obtenir toutes la valeurs du dico correspondant.

for element in filtrage_question:
    titres_obtenus.append(element)
    print(titres_obtenus)

# les cas qui me génèrent des erreurs quand je cherche à obtenir les urls du dico.
  #  print(dictionnaire_titre_et_lien[titres_obtenus])  # erreur type ne doit pas être list
   # print(dictionnaire_titre_et_lien[element]) # erreur type, ne doit pas être str



