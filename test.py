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
        titre.append(title.lower())

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


print(""
      "")


def fonction_filtrage(question):
    reponse = {}
    compteur_article = 0
    filtrage = list(filter(lambda x: question.lower() in x, titre))

    # for question in filtrage:     était inutile et empéchait le print 'aucune recherche"

    if not filtrage:
        print("Aucune recherche correspondante"
              ""
              "")
        resultat_nul = ("FIN DE RECHERCHE")
        print(resultat_nul)
        exit() # exit évite que la boucle while pour l'ouverture se déclenche ligne 99


    else:
        for element in filtrage:
            compteur_article += 1
            url_browser.append(dictionnaire_titre_et_lien[element])
            reponse[compteur_article] = (f"{element} : {dictionnaire_titre_et_lien[element]}")

    for k, v in reponse.items():
        print(f'{k} -> {v}')
        print('')

    return reponse


def open_url(ouverture):
    if ouverture == "o" or ouverture == "O":
        for element in url_browser:
            webbrowser.open(element)
    else:
        resultat_nul = ("FIN DE RECHERCHE")
        print(resultat_nul)


question = input('entrez une recherche : ')
reponse_filtrage = fonction_filtrage(question)



choice_open_urls = False

while choice_open_urls == False:

    ouverture = input("Voulez vous ouvrir les liens ? : O/N ")

    if ouverture:
        open_url(ouverture)
        choice_open_urls = True
    else:
        exit()


