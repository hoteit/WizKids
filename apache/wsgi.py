import os
import sys
import site
from wizkids.settings import PROJECT_ROOT

site.addsitedir(PROJECT_ROOT+'/env/lib/python3.5/site-packages')
sys.path.append(PROJECT_ROOT+'/')

# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_wsgi process. To fix this, use
# mod_wsgi daemon mode with each site in its own daemon process, or use
# os.environ["DJANGO_SETTINGS_MODULE"] = "qlstimesheet.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "winkids.settings")


activate_env=os.path.expanduser(PROJECT_ROOT+'/env/bin/activate_this.py')
with open(activate_env) as activate_file:
    exec (activate_file.read())
#xecfile(activate_env, dict(__file__=activate_env))


# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)