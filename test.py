import feedparser
import webbrowser



Urls_de_ressources = ["https://feeds.leparisien.fr/leparisien/rss/",
                      "https://www.lefigaro.fr/rss/figaro_actualites.xml",
                      "https://www.lemonde.fr/rss/une.xml",
                      "https://www.lemonde.fr/international/rss_full.xml",
                      "https://www.mediapart.fr/articles/feed",
                      "https://www.lemonde.fr/politique/rss_full.xml",
                      "https://korben.info/feed",
                      "https://www.francebleu.fr/rss/rcfm/a-la-une.xml",
                      "https://www.francebleu.fr/rss/rcfm/rubrique/vie-quotidienne.xml",
                      "https://www.courrierinternational.com/feed/category/6678/rss.xml"
                      ",https://www.courrierinternational.com/feed/category/6678/rss.xml"
                      "https://www.courrierinternational.com/feed/category/6679/rss.xml",
                      "https://www.courrierinternational.com/feed/category/6681/rss.xml",
                      "https://www.courrierinternational.com/feed/category/6263/rss.xml",
                      "https://www.courrierinternational.com/feed/category/6260/rss.xml",
                      "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
                      "http://www.lepoint.fr/politique/rss.xml",
                      "https://reflets.info/feeds/public",
                      "https://www.afp.com/fr/actus/afp_actualite/792,31,9,7,33/feed"
                      "https://news.google.com/rss/search?q=source:bloomberg&um=1&ie=UTF-8&num=100&hl=en-US&gl=US&ceid=US:en",

                      ]


titre = []


lien = []


dictionnaire_titre_et_lien = []


titres_obtenus = []


url_browser = []

print("Patientez ça mouline....")


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
print("          BASE DE RECHERCHE CONSTITUTEE           ")
print("***************************************************"
      "")


print(""
      "")


def fonction_filtrage(question):
    reponse = {}
    compteur_article = 0
    filtrage = list(filter(lambda x: question.lower() in x, titre))
    if not filtrage:
        print("Aucune recherche correspondante"
              ""
              "")
        resultat_nul = ("FIN DE RECHERCHE")
        print(resultat_nul)
        exit()  # exit évite que la boucle while pour l'ouverture se déclenche ligne 99


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
        resultat_nul = (" "
                        "")
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


def in_or_out(stay):
    if stay == "o" or stay == "O":
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

    else:
        resultat_nul = (""
                        "")
        print(resultat_nul)
        exit()


end_or_not = False

while end_or_not == False:
    new_search = input("Voulez vous effectuer une nouvelle recherche: O/N ")

    if new_search:
        in_or_out(new_search)
        end_or_not = True
    else:
        exit()
