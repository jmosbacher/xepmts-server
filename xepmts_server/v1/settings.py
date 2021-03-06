import os

from copy import deepcopy
from xepmts_server.secrets import MONGO_PASSWORD
from xepmts_server.v1.domain import get_domain

DOMAIN = get_domain()

URL_PREFIX = os.getenv("XEPMTS_URL_PREFIX", "")
API_VERSION = "v1"
RESOURCE_METHODS = ["GET", "POST"]
ITEM_METHODS = ["GET", "PUT", "PATCH", "DELETE"]
ALLOWED_READ_ROLES = ["admin", "superuser", "expert", "user", "read", "write"]
ALLOWED_WRITE_ROLES = ["admin", "superuser", "expert", "write"]
EMBEDDING = True
MEDIA_PATH = "files"
PAGINATION_LIMIT = 10000
SCHEMA_ENDPOINT = "schema"
IF_MATCH = True
ENFORCE_IF_MATCH = False
HATEOAS = True
VERSIONS = "_versions"
NORMALIZE_ON_PATCH = False

# ----------------- Mongo config ------------------------------------------ #
MONGO_HOST = os.getenv("XEPMTS_MONGO_HOST", "localhost")
MONGO_PORT = int(os.getenv("XEPMTS_MONGO_PORT", 27017))
MONGO_DBNAME = os.getenv("XEPMTS_MONGO_DB", "pmts")
MONGO_USERNAME = os.getenv("XEPMTS_MONGO_USER", "")
MONGO_AUTH_SOURCE = os.getenv("XEPMTS_MONGO_AUTH_SOURCE", MONGO_DBNAME)

MONGO1T_HOST = MONGO_HOST
MONGO1T_PORT = MONGO_PORT
MONGO1T_DBNAME = MONGO_DBNAME
MONGO1T_AUTH_SOURCE = MONGO_AUTH_SOURCE
MONGO1T_PASSWORD = MONGO_PASSWORD
if os.getenv("XEPMTS_MONGO_REPLICA_SET", ""):
    MONGO_REPLICA_SET = os.getenv("XEPMTS_MONGO_REPLICA_SET", "")
    MONGO1T_REPLICA_SET = MONGO_REPLICA_SET

MONGO1T_USERNAME = MONGO_USERNAME

if os.getenv("XEPMTS_MONGO_URI", ""):
    MONGO_URI = os.getenv("XEPMTS_MONGO_URI", "")
    MONGO1T_URI = MONGO_URI
# -------------------------------------------------------------------------- #

SERVERS = [
    "https://api-dot-xenon-pmts.uc.r.appspot.com",
    "https://api."+os.getenv('XEPMTS_DOMAIN','pmts.xenonnt.org'),        
    ]

X_DOMAINS = ['http://localhost:8000',
            'http://127.0.0.1:8000',
            'http://127.0.0.1:5000',
            'http://editor.swagger.io',
            "https://"+os.getenv('XEPMTS_DOMAIN','pmts.xenonnt.org'),
            "https://api."+os.getenv('XEPMTS_DOMAIN','pmts.xenonnt.org'),
            "https://website."+os.getenv('XEPMTS_DOMAIN','pmts.xenonnt.org'),
            "https://panels."+os.getenv('XEPMTS_DOMAIN','pmts.xenonnt.org'),
            "https://catalog."+os.getenv('XEPMTS_DOMAIN','pmts.xenonnt.org'),
             ]

X_HEADERS = ['Content-Type', 'If-Match', 'Authorization', 'X-HTTP-Method-Override']  # Needed for the "Try it out" buttons

