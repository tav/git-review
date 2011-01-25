# Public Domain (-) 2009-2011 The Ampify Authors.
# See the Ampify UNLICENSE file for details.

"""A handler that exports various App Engine services over HTTP."""

import logging
import os

from urllib import unquote

from google.appengine.ext.webapp import WSGIApplication
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.remote_api.handler import ApiCallHandler

from config import REMOTE_KEY
from pyutil.crypto import validate_tamper_proof_string

# ------------------------------------------------------------------------------
# Some Constants
# ------------------------------------------------------------------------------

SSL_ENABLED_FLAGS = frozenset(['yes', 'on', '1'])

if os.environ.get('SERVER_SOFTWARE', '').startswith('Google'):
    RUNNING_ON_GOOGLE_SERVERS = True
else:
    RUNNING_ON_GOOGLE_SERVERS = False

# ------------------------------------------------------------------------------
# Request Handler
# ------------------------------------------------------------------------------

class RemoteAPIHandler(ApiCallHandler):
    """Remote API handler."""

    def get(self):
        """Handle GET requests with a 404."""
        self.response.set_status(404)

    def post(self):
        """Handle POST requests by executing the API call."""

        verifier = unquote(self.request.path.rsplit('/', 1)[1])

        if not validate_tamper_proof_string('remote', verifier, REMOTE_KEY):
            logging.info("Unauthorised Remote Access Attempt: %r", verifier)
            self.response.set_status(401)
            return

        # we skip the SSL check for local dev instances
        if (RUNNING_ON_GOOGLE_SERVERS and
            os.environ.get('HTTPS') not in SSL_ENABLED_FLAGS
            ):
            logging.info("Insecure Remote Access Attempt")
            self.response.set_status(401)
            return

        ApiCallHandler.post(self)

    def CheckIsAdmin(self):
        """Dummy for parent class since we don't depend on this for security."""
        return True

# ------------------------------------------------------------------------------
# Main Function
# ------------------------------------------------------------------------------

application = WSGIApplication([('.*', RemoteAPIHandler)])

def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
