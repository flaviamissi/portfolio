from flask import render_template, Blueprint, abort
# from jinja2 import TemplateNotFound

from api.site_info import site

single_page = Blueprint('single_page', __name__,
                        template_folder='../templates',
                        url_prefix='/',
                        )

@single_page.route('/')
def index():
    return render_template('index.html', page={}, site=site)
