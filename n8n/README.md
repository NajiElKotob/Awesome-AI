# n8n

## n8n
* [n8n](https://n8n.io/) - n8n.io
* [n8n Learning path](https://docs.n8n.io/learning-path/)
* [n8n Tutorials](https://community.n8n.io/c/tutorials/28)
* [n8n Academy](https://learn.n8n.io/courses)
  
## Trends
* [Google Trends](https://trends.google.com/explore?q=n8n%2CHermes%2520Agent%2COpenClaw%2CZapier&date=2024-01-01%202026-09-08&geo=Worldwide)

## Tutorials
* [n8n Telegram integration: Set up, automate, and scale bots](https://www.hostinger.com/tutorials/n8n-telegram-integration/?REFERRALCODE=JBKLNAJI3OX8)
* [How to integrate WhatsApp with n8n?](https://www.hostinger.com/tutorials/how-to-integrate-n8n-with-whatsapp/?REFERRALCODE=JBKLNAJI3OX8)
* [Practical n8n workflow examples for business automation](https://www.hostinger.com/tutorials/n8n-workflow-examples/?REFERRALCODE=JBKLNAJI3OX8)
* [All n8n tutorials](https://www.hostinger.com/tutorials/page/1?REFERRALCODE=JBKLNAJI3OX8&s=n8n)

----

## My n8n Community Nodes
* [n8n-nodes-random-delay](https://www.npmjs.com/package/n8n-nodes-random-delay) - Pause a workflow for a random duration within a range
* [n8n-nodes-random-number](https://www.npmjs.com/package/n8n-nodes-random-number) - Generate random integers, decimals and booleans in n8n workflows, with optional seeding for repeatable results
* [n8n-nodes-hash](https://www.npmjs.com/package/n8n-nodes-hash) - Hash text, files or JSON in n8n using algorithms the built-in Crypto node does not offer.


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
