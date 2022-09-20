import logging
from django.db import models

logger = logging.getLogger(__name__)


class UserSocialAuthManager(models.Manager):
    """Manager for the UserSocialAuth django model."""

    class Meta:
        app_label = "social_django"

    def get_social_auth(self, provider, uid):
        try:
            logger.info("#### Social Manager ####")
            logger.info(type(uid))
            logger.info(provider)
            logger.info(uid)
            return self.select_related('user').get(provider=provider,
                                                   uid=uid)
        except self.model.DoesNotExist:
            return None
