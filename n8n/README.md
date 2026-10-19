# n8n

## n8n
* [n8n](https://n8n.io/) - n8n.io
* [n8n Learning path](https://docs.n8n.io/learning-path/)
* [n8n Tutorials](https://community.n8n.io/c/tutorials/28)
  
## Trends
* [Google Trends](https://trends.google.com/explore?q=n8n%2CHermes%2520Agent%2COpenClaw%2CZapier&date=2024-01-01%202026-09-08&geo=Worldwide)

## Tutorials
* [n8n Telegram integration: Set up, automate, and scale bots](https://www.hostinger.com/tutorials/n8n-telegram-integration/?REFERRALCODE=JBKLNAJI3OX8)
* [How to integrate WhatsApp with n8n?](https://www.hostinger.com/tutorials/how-to-integrate-n8n-with-whatsapp/?REFERRALCODE=JBKLNAJI3OX8)
* [Practical n8n workflow examples for business automation](https://www.hostinger.com/tutorials/n8n-workflow-examples/?REFERRALCODE=JBKLNAJI3OX8)
* [All n8n tutorials](https://www.hostinger.com/tutorials/page/1?REFERRALCODE=JBKLNAJI3OX8&s=n8n)

----

## Setup and Config
### winget
* winget install --id Cloudflare.cloudflared
  - cloudflared tunnel --url http://localhost:5678
  - Copy the https://....trycloudflare.com line (new-url)
  - set WEBHOOK_URL=https://<new-url>/
  - n8n start
### Docker
* [Install with Docker](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-docker) - docs.n8n.io
  - [n8n Images](https://hub.docker.com/u/n8nio)
  - %USERPROFILE%\.n8n
### npm
* npm install -g n8n
  
### Help
* n8n --help
* n8n export:workflow --help

### Backup
* n8n export:workflow --backup --output=X:\n8n\backup\workflows\
* n8n export:credentials --backup --decrypted --output=X:\n8n\backup\credentials\ ⚠️
* n8n export:entities --outputDir=X:\n8n\backup\entities
