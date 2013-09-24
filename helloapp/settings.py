SECRET_KEY = 'tic233k_tra8c2ggk_hd4KO34=-+#$'
CSRF_ENABLED = False
CSRF_SESSION_LKEY = "testsf-sfsd_key_h8asSNJ9s9dfsdf+"
DEBUG = True

import os
PRODUCTION = os.environ.get("SERVER_SOFTWARE", "").startswith("Google")
DEVELOPMENT = not PRODUCTION
DEBUG = DEVELOPMENT

if DEVELOPMENT:
    # Development related settings
    pass
else:
    # Production related settings
    pass

