import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from decouple import config

SENTRY_DSN = config("SENTRY_DSN", default="")

if SENTRY_DSN:  # Only initialize if DSN is provided
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration()],
        traces_sample_rate=1.0,
        send_default_pii=True,
    )
else:
    print("Sentry DSN not configured. Skipping Sentry initialization.")
