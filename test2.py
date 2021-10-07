import feedparser
import webbrowser

# on défini le flux rss a parser

Urls_de_ressources = ["https://feeds.leparisien.fr/leparisien/rss/",
                      "https://www.lefigaro.fr/rss/figaro_actualites.xml"]

# la liste titre contiendra tout les titres
titre = []
# la liste link contientra tout les liens
lien = []

# on créer un dictionnaire  à partir des précédentes listes
dictionnaire_titre_et_lien = []

# cette liste contiendra les titres obtenus suite à la recherche demandée, ces titres seront les clefs du dictionnaire
# pour permettre de retrouver les valeurs.
titres_obtenus = []

# cette liste contiendra les urls retournés par la recherche afin qu'ils puissent être ouvert sur demande.
url_browser = []

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
        dictionnaire_titre_et_lien = dict(zip(titre, lien))

print("***************************************************"
      "")
print("              DICTIONNAIRE CREE                    ")
print("***************************************************"
      "")

# on demande la recherche souhaité

question = input('entrez une recherche : ')

print(""
      "")

# création d'un compteur d'article

compteur_article = 0

# on filtre la recherche dans la liste de titre qu'on a préalablement obtenu. on applique les methodes de casse
# pour être sur que tous titres soient bien retournés.

filtrage_normal = list(filter(lambda x: question in x, titre))
filtrage_upper = list(filter(lambda x: question.upper() in x, titre))
filtrage_lower = list(filter(lambda x: question.lower() in x, titre))
filtrage_capitalize = list(filter(lambda x: question.capitalize() in x, titre))

# on boucle pour obtenir chaque élément de la liste de titre correspondant à la recherche. s'il n'y a pas de retour dans
# les trois première boucles c'est que qu'il n'y a pas d'article correspondant à la recherche.


# boucle 0

for element in filtrage_normal:
    compteur_article += 1
    url_browser.append(dictionnaire_titre_et_lien[element])
    print(f'{compteur_article} :  {element} : {dictionnaire_titre_et_lien[element]}\n')


# boucle 1

for element_lower in filtrage_lower:
    compteur_article += 1
    url_browser.append(dictionnaire_titre_et_lien[element_lower])
    print(f'{compteur_article} :  {element_lower} : {dictionnaire_titre_et_lien[element_lower]}\n')

# boucle 2

for element_upper in filtrage_upper:
    compteur_article += 1
    url_browser.append(dictionnaire_titre_et_lien[element_upper])
    print(f'{compteur_article} : {element_upper} : {dictionnaire_titre_et_lien[element_upper]} \n')

# boucle 3

for element_capitalize in filtrage_capitalize:
    compteur_article += 1
    url_browser.append(dictionnaire_titre_et_lien[element_capitalize])
    print(f'{compteur_article} : {element_capitalize} : {dictionnaire_titre_et_lien[element_capitalize]}\n')

# Absence d'article

if not filtrage_normal and filtrage_lower and not filtrage_upper and not filtrage_capitalize:
    print("Aucune recherche correspondante")

# S'il y a un article on propose l'ouverture de liens.

if filtrage_normal or filtrage_lower or filtrage_upper or filtrage_capitalize == True:
    ouverture = input("Voulez vous ouvrir les liens ? : O/N ")

    if ouverture == "o" or ouverture == "O":
        for element in url_browser:
            webbrowser.open(element)

# si on ne veut pas ouvrir c'est la fin de la recherche:'
    else:
        print("FIN DE RECHERCHE")

