import feedparser
from bs4 import BeautifulSoup

# on défini le flux rss a parser

Urls_de_ressources = ["https://feeds.leparisien.fr/leparisien/rss/","https://www.lefigaro.fr/rss/figaro_actualites.xml"]

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
        dictionnaire_titre_et_lien = dict(zip(titre,lien))


print(dictionnaire_titre_et_lien)


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

    print(f'{element} : {dictionnaire_titre_et_lien[element]}')

