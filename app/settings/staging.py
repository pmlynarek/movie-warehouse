from .dev import *  # NOQA

logger = logging.getLogger(__name__)  # NOQA
logger.setLevel(logging.DEBUG)  # NOQA
logger.debug("loading settings staging.py")


DEBUG = False

ALLOWED_HOSTS = ["moviewarehouse-app.herokuapp.com"]

if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN, integrations=[DjangoIntegration()], send_default_pii=True
    )
