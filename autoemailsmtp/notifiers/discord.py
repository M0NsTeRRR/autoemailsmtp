import logging

import requests

from ..config import get_settings

logger = logging.getLogger()


def notify(status: bool, template: str, email: str):
    headers = {"Content-Type": "application/json"}
    webhook_url = get_settings().DISCORD_WEBHOOK_URL
    r = requests.post(
        webhook_url,
        json={
            "embeds": [
                {
                    "title": "autoemailsmtp",
                    "description": f"""Email {'' if status else 'not '}sended to {email}
                    with template {template} {':white_check_mark:' if status else ':x:'}""",
                    "color": 1376000 if status else 16711680,
                }
            ],
            "attachments": [],
        },
        headers=headers,
        allow_redirects=False,
    )
    if not r.ok:
        logger.error(f"Can't send Discord webhook http status code {r.status_code}")
        logger.debug(r.content)
    else:
        logger.debug(f"Discord notification sended to {webhook_url}")
