This script will send an email and send you an alert on the configured notifiers

[![PyPI](https://img.shields.io/pypi/v/autoemailsmtp.svg)](https://pypi.python.org/pypi/autoemailsmtp)
[![PyPI versions](https://img.shields.io/pypi/pyversions/autoemailsmtp.svg)](https://pypi.python.org/pypi/autoemailsmtp)
[![Python test](https://github.com/M0NsTeRRR/autoemailsmtp/actions/workflows/test.yml/badge.svg)](https://github.com/M0NsTeRRR/autoemailsmtp/actions/workflows/test.yml)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# Why ?
When a company wants you to send an email every month to get what you need because they don't want to send it automatically to piss you off.
![meme](https://media3.giphy.com/media/O1xeZ4AgSaNBS/giphy.gif)


# Install
```
pip install autoemailsmtp
```

# Config
Create an `.env` file with this content or create environment variables
```
AUTOEMAILSMTP_SMTP_HOST="smtp.example.com"
AUTOEMAILSMTP_SMTP_PORT=587
AUTOEMAILSMTP_SMTP_USERNAME="toto@example.com"
AUTOEMAILSMTP_SMTP_PASSWORD="mypassword"

Optional:
AUTOEMAILSMTP_LOG_LEVEL="INFO"
AUTOEMAILSMTP_DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/aaaaaa/aaaaa"
```

# Systemd
To send an email each month you can setup a cron or use systemd like (must be adapated).
Service file
```
[Unit]
Description=send an email
After=network-online.target

[Service]
Type=oneshot
ExecStart=/opt/autoemailsmtp/venv/bin/python autoemailsmtp.send_mail.py --to email@example.com --subject "rent" --file rent_receipt --discord

[Install]
WantedBy=multi-user.target
```

Systemd timer file
```
[Unit]
Description=Send an email on the 10th of every month

[Timer]
OnCalendar=*-*-10 08:00:00

[Install]
WantedBy=timers.target
```

# Dev
Install [Poetry](https://python-poetry.org/docs/master/#installing-with-the-official-installer)

Install and setup dependencies
```bash
poetry install
poetry shell
pre-commit install
```

### Run pre-commit
```bash
pre-commit run --all-files
```

# Licence

The code is under CeCILL license.

You can find all details here: https://cecill.info/licences/Licence_CeCILL_V2.1-en.html

# Credits

Copyright © Ludovic Ortega, 2023

Contributor(s):

-Ortega Ludovic - ludovic.ortega@adminafk.fr
