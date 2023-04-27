from flask import Flask
from flask_flatpages import FlatPages
from flask import render_template, send_from_directory
import os 

app = Flask(__name__)
app.config['APPLICATION_ROOT'] = '/Flask'
FLATPAGES_EXTENSION = '.md'
FLATPAGES_MARKDOWN_EXTENSIONS = ['extra']
FLATPAGES_AUTO_RELOAD = True 

app.config.from_object(__name__)
application = app
pages = FlatPages(app)


def Liste_cat():
    articles = (p for p in pages if 'published' in p.meta)
    catList = []
    for a in articles:
        catList.append(a.meta['cat'])
    catList = list(dict.fromkeys(catList))
    return catList 


def imagelist(articlename):
    dir_path = os.path.dirname(os.path.realpath(articlename))+'/pages/'
    gallery_path = os.path.join(dir_path, articlename)
    if os.path.exists(gallery_path):
        images = [f for f in os.listdir(gallery_path) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png') or f.endswith('.gif') or f.endswith('.JPG') or f.endswith('.pdf') ]
        return gallery_path ,images
    else:
        return None, None

@app.route('/pages/<path:path>')
def serve_pages(path):
    return send_from_directory('pages', path)


@app.route('/')
def index():
    # Articles are pages with a publication date
    articles = (p for p in pages if 'published' in p.meta)
    # Show the 10 most recent articles, most recent first.
    latest = sorted(articles, reverse=True,
                    key=lambda p: p.meta['published'])
    catList = Liste_cat()
    return render_template('base.html', latest=latest[:10] ,  catList=catList )

@app.route('/<path:path>')
def page(path):
    g_path, imgs = imagelist(path)
    page = pages.get_or_404(path)
    if imgs:
        return render_template('single.html', page=page , g_path=g_path, imgs = imgs)
    else :
        return render_template('single.html', page=page)


@app.route('/s/<path:path>')
def statPage(path):
    page = pages.get_or_404(path)
    return render_template('statPage.html', page=page)



@app.route('/cat/<catname>')
def catPage(catname):
    articles = (p for p in pages if 'published' in p.meta and 'cat' in p.meta and p.meta['cat']==catname )
    latest = sorted(articles, reverse=True,
                    key=lambda p: p.meta['published'])
    catList = Liste_cat()
    return render_template('base.html', latest=latest , catList=catList  )


