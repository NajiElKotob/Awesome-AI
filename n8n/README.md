# n8n

## Trends
* [Google Trends](https://trends.google.com/explore?q=n8n%2CHermes%2520Agent%2COpenClaw%2CZapier&date=2024-01-01%202026-09-08&geo=Worldwide)

## Tutorials
* [n8n Telegram integration: Set up, automate, and scale bots](https://www.hostinger.com/tutorials/n8n-telegram-integration/?REFERRALCODE=JBKLNAJI3OX8)


----

## Backup
* n8n export:workflow --backup --output=X:\n8n\backup\workflows\
* n8n export:credentials --backup --decrypted --output=X:\n8n\backup\credentials\ ⚠️
* n8n export:entities --outputDir=X:\n8n\backup\entities

## Help
* n8n --help
* n8n export:workflow --help

## Setup
### npm
* winget install --id Cloudflare.cloudflared
  - cloudflared tunnel --url http://localhost:5678
  - Copy the https://....trycloudflare.com line (new-url)
  - set WEBHOOK_URL=https://<new-url>/
  - n8n start
