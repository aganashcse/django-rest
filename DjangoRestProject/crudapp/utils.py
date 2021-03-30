from .models import Reporter, Article, Place, Restaurant, Publication1, Article1

def createReporter(first_name, last_name, email):
    r = Reporter(first_name= first_name, last_name=last_name, email=email)
    r.save()

def getReporter(first_name=None, last_name=None, email=None):
    r = Reporter.objects.filter(first_name=first_name, last_name=last_name, email=email)
    return r

def getAllReporters():
    return Reporter.objects.all()

def getAllReportersSortedFirstname():
    return Reporter.objects.order_by('first_name')

def createArticle(headline, pub_date, reporter):
    a = Article(headline=headline, pub_date=pub_date, reporter=reporter)
    a.save()

def getArticle(headline=None, pub_date=None, reporter= None):
    #reporter can be a Reporter object (OR) can be an id of a reporter
    if reporter:
        return Article.objects.filter(reporter=reporter)
    return Article.objects.get(headline=headline, pub_date=pub_date)

def getArticleWithReporterFirstName(reporter_first_name):
    # return Article.objects.filter(reporter__in=Reporter.objects.filter(first_name=reporter_name)).distinct()
    # OR
    return Article.objects.filter(reporter__first_name=reporter_first_name)

def getArticleCountOfReporter(reporter_obj):
    return Article.objects.filter(reporter=reporter_obj).distinct().count()
