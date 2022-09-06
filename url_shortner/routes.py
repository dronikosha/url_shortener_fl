
from urllib.parse import urlparse

from flask import redirect, render_template, request, url_for

from url_shortner import app, db, domain

from .models import URL


@app.route('/', methods=['GET', 'POST'])
def short_url():
    if request.method == 'POST':
        url = request.form.get('url')
        parsed = urlparse(url)
        if parsed.netloc and parsed.scheme:
            new_url = URL(url=url, short_url=URL.generate_short_url())
            if db.session.query(URL).filter_by(url=url).first():
                return render_template('index.html', shorted_url=db.session.query(URL).filter_by(url=url).first().short_url)
            db.session.add(new_url)
            db.session.commit()
            return render_template('index.html', shorted_url=new_url.short_url)
        elif not parsed.netloc and not parsed.scheme:
            return render_template('index.html', shorted_url="Wrong URL")
    if request.method == 'GET':
        return render_template('index.html', shorted_url=None)


@app.route('/<short_url>')
def redirect_to_url(short_url):
    print(short_url)
    url = db.session.query(URL).filter_by(
        short_url=domain + "/" + short_url).first()
    print(url)
    if url:
        return redirect(url.url)
    return f'<h1>URL not found</h1>'


@app.route('/all', methods=['POST', 'GET'])
def all_urls():
    urls = db.session.query(URL).all()
    return render_template('allUrls.html', urls=urls)
