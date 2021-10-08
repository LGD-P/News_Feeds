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

question = input('entrez une recherche : ')

print(""
      "")


def fonction_filtrage(question):

    #création d'un compteur d'article
    compteur_article = 0

    # création du filtre des clefs requêtées
    filtrage = list(filter(lambda x: question.lower() in x, titre))

    # si aucun retour message de retour négatif
    if not filtrage:
        print("Aucune recherche correspondante")

    else:
        # sinon le compteur rentre en jeu, pour chaque élement filtré:

        for element in filtrage:
            compteur_article += 1

            # grace au clef du dictionnaire on ajoute les url à un liste
            # pour le mécanise d'ouverture des url qui suivra

            url_browser.append(dictionnaire_titre_et_lien[element])

            # on imprime le résultat
            print(f'{compteur_article} :  {element} : {dictionnaire_titre_et_lien[element]}\n')


        # On propose l'ouverture de liens.

        ouverture = input("Voulez vous ouvrir les liens ? : O/N ")

        if ouverture == "o" or ouverture == "O":
            for element in url_browser:
                    webbrowser.open(element)



    # si on ne veut pas ouvrir c'est la fin de la recherche:'
        else:
            resultat_nul = "FIN DE RECHERCHE"
            print(resultat_nul)

    # un navigateur ou de convertir les articles en pdf.


    return question


fonction_filtrage(question)



