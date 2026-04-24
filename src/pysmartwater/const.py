"""Constants for the Smart Water library."""
import logging
from datetime import datetime, timezone

_LOGGER: logging.Logger = logging.getLogger(__package__)


# Note: firebase api keys are safe to check in. See https://firebase.google.com/docs/projects/api-keys
FIREBASE_PUBLIC_API_KEY_SMARTWATER = b'\x00\x8c\xda\x4b\x20\x48\x65\x51\x32\xbb\x5a\xf5\x94\xaf\xf0\x46\x3f\x1d\xd8\x02\x24\xaf\x59\x63\x93\xe4\x6e\x93\x69'
FIRESTORE_PROJECT_NAME_SMARTWATER = 'smartwater-app'
FIREBASE_PUBLIC_API_KEY_GALLAGHER = b'\x00\x8c\xda\x4b\x20\xe1\xea\xd1\xe6\xc3\xef\xb7\xd7\x89\x56\xa1\x5c\x2f\x87\xb5\x09\x4e\x85\xe2\x5c\xc6\x08\x65\xb3'
FIRESTORE_PROJECT_NAME_GALLAGHER = 'ggl-water-app'
FIRESTORE_URL = 'https://firestore.googleapis.com/v1'

GOOGLE_APIS_LOGIN_URL = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword'
GOOGLE_APIS_REFRESH_URL = 'https://securetoken.googleapis.com/v1/token'

ACCESS_TOKEN_EXPIRE_MARGIN = 60 # seconds

CALL_CONTEXT_SYNC = "SYNC"
CALL_CONTEXT_ASYNC = "ASYNC"


# Global helper functions
utcnow_dt = lambda: datetime.now(timezone.utc)
utcnow_ts = lambda: datetime.now(timezone.utc).timestamp()
