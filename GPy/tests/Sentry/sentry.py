import sentry_sdk
import policy_sentry
import sentry_webhooks

sentry_sdk.init(release="GPy@1.0.0")
