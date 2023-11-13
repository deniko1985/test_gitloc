from os import path

from flask import Flask, render_template

from i18n import config
from i18n.translator import t

RESOURCE_FOLDER = path.join(path.dirname(__file__), "static")
config.set('filename_format', '{namespace}.{format}')
config.set('file_format', 'json')
config.set('skip_locale_root_data', True)

def renderHello(lang):
  config.set('locale', lang)
  config.set("load_path", [path.join(RESOURCE_FOLDER, "locales", lang)])
  return render_template('hello.html', title=t('welcome.title'))

app = Flask(__name__)

@app.route('/')
def index():
  return renderHello('en')

@app.route('/en')
def en():
  return renderHello('en')

@app.route('/de')
def de():
  return renderHello('de')


if __name__ == "__main__":

    app.run(host='0.0.0.0', port=6000)