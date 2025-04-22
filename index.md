---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: Cloud Computing
nav_order: 1
---

### But du cours

Avec l’avènement des plateformes comme Amazon Web Services (AWS), Google Cloud Platform (GCP), Microsoft Azure ou OVH Cloud, les entreprises **abandonnent de plus en plus leurs data centers \*on-premises\* pour migrer vers le \*cloud\***. Cette migration leur apporte de la souplesse (plus besoin d’investissement initial) et de la liberté pour innover, à condition d’avoir des équipes formées aux outils proposés par le cloud.
 **Le but du cours est de vous faire découvrir les outils de base d’un \*cloud provider\***, pour que vous puissiez, dans votre vie professionnelle, mettre en place des solutions cloud.

À la fin du cours, vous saurez :

- 🖥 Créer une machine dans le cloud
- 🧨 Créer une infrastructure capable d’héberger un webservice pouvant gérer des millions de requêtes simultanément, tout en s’adaptant à la charge
- 🪐 Automatiser la création de ressources en utilisant Terraform, un outil d’Infrastructure as Code
- 🗄 Utiliser DynamoDB, une base de données NoSQL serverless qui permet de stocker des To de données et de les requêter en temps réel
- 🚄 Créer une fonction AWS Lambda, le service Function as a Service d’AWS, qui permet d’exécuter des milliers de fonctions en parallèle sans se soucier de l’infrastructure
- Et plus encore, si le temps le permet

------

### Pré-requis

Seuls les cours du tronc commun sont nécessaires pour ce cours. Néanmoins, une **grande autonomie et curiosité** sont attendues. Le cours sera majoritairement pratique. La partie théorique servira uniquement à introduire les concepts généraux.
 Vous devrez donc **apprendre à vous déboguer par vous-même**. Demandez à vos camarades, consultez StackOverflow ou utilisez ChatGPT. Et si vous avez des questions, des doutes, des idées : **ne les gardez pas pour vous !**

**Un ordinateur portable sera nécessaire pendant le cours.** J’ai demandé à la DSI de préparer des ordinateurs sous Ubuntu pour vous tous. Vous êtes libres d’en emprunter un.
 Les applications suivantes seront nécessaires : Git, Python, un client SSH, Node.js et npm, AWS CLI, Docker et Terraform.
 **Tous ces outils doivent être installés sur vos machines.**
 Si vous avez une distribution basée sur Ubuntu, un script d’installation vous sera fourni. Pour les autres distributions, l’installation est à votre charge.
 ⚠️ Je n’aurai pas le temps en cours de déboguer vos installations, alors pour profiter pleinement des séances, **je vous encourage à emprunter un ordinateur à la DSI.**

### Notation

Ce cours sera en contrôle continu. Ainsi, vous aurez entre certains cours à répondre à un petit QCM sur Moodle. Vous disposerez de deux tentatives et il n'y a pas de limite de temps pendant une tentative. Ces QCM n'ont pas pour vocation de vous piéger et ils constitueront une partie de votre note du module. 

Deux rendus notés vous seront demandés. Un à la moitié du cours et un autre à la fin du cours. Ces TP seront l'application des concepts vus précédemment mais vous serez moins guidés que dans un TP classique. Ils seront à faire à la maison mais pourront être commencés en cours si vous avez le temps.