from blog.models import Article
def run():
    for i in range(5,15):
        article=Article()
        article.title="Article N #%d" %i
        article.desc="Description d'article N #%d" %i
        article.image="http://default"
        article.save()
print("Operation est reussie")