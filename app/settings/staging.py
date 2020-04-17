from .dev import *  # NOQA

logger = logging.getLogger(__name__)  # NOQA
logger.setLevel(logging.DEBUG)  # NOQA
logger.debug("loading settings staging.py")


DEBUG = False

ALLOWED_HOSTS = ["moviewarehouse-app.herokuapp.com"]

# Sentry

if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN, integrations=[DjangoIntegration()], send_default_pii=True
    )

# Storage
DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
STATICFILES_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
GS_BUCKET_NAME = "media-movie-warehouse"
