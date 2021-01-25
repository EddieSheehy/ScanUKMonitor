import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from scanuk-monitor import MyWSGIApp


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "py_mrp.settings")

application = get_wsgi_application()
application = MyWSGIApp()
application = WhiteNoise(application, root='/path/to/static/files')
application.add_files('/path/to/more/static/files', prefix='more-files/')
