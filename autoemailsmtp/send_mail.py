import logging
import smtplib
from argparse import ArgumentParser

from jinja2 import Template

from .config import get_settings
from .notifiers.discord import notify as discord_notify

cfg = get_settings()

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s:%(message)s")
logger = logging.getLogger(__name__)

parser = ArgumentParser()
parser.add_argument(
    "--to",
    action="store",
    dest="to",
    help="Email recipient",
)
parser.add_argument(
    "--template",
    action="store",
    dest="template",
    help="Jinja template that contain text to send as email",
)
parser.add_argument(
    "--discord",
    action="store_true",
    dest="discord",
    help="Enable discord notifier if discord is configured",
)
args = parser.parse_args()

status = False

try:
    s = smtplib.SMTP(cfg.SMTP_HOST, cfg.SMTP_PORT)
    s.ehlo("localhost")
    s.starttls()
    s.ehlo("localhost")
    s.login(cfg.SMTP_USERNAME, cfg.SMTP_PASSWORD)
    message = Template(open(args.template, encoding="utf-8").read()).render(
        {"to": args.to, "from": cfg.SMTP_USERNAME}
    )
    s.sendmail(cfg.SMTP_USERNAME, args.to, message.encode("utf-8"))
    s.quit()
    status = True
    logger.info(
        f"Email {'' if status else 'not '}sended to {args.to} with template {args.template}"
    )
except Exception as e:
    logger.error(e)

if args.discord:
    discord_notify(status, args.template, args.to)
