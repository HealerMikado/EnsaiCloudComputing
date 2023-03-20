---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: Cloud Computing
nav_order: 1
---

### But du cours
Avec l’avènement des plateforme comme Amazon Web Service (AWS), Google Cloud Platform (GCP), Microsoft Azure ou OVH Cloud les entreprises **abandonnent de plus en plus leurs data centers *on premises* et migrent vers le *cloud***. Cette migration leur apporte de la souplesse car il n'y a plus d'investissement à faire et de la liberté pour innover, à condition d'avoir des équipes formées à utiliser les outils qu'offrent le cloud. **Le but du cours est de vous faire découvrir les outils de base d'un *cloud provider*** pour que vous puissiez dans votre vie professionnelle mettre en place des outils cloud.

À la fin du cours vous saurez :

- 🖥Créer une machine dans le cloud 
- 🧨Créer l’infrastructure pour faire un webservice qui va pouvoir gérer des millions de requêtes en parallèle en pic, mais qui diminuera quand le nombre de requête va diminuer 
- 🪐Automatiser la création de ressource en utilisant Terraform, un logiciel d’infrastructure as code. 
- 🗄Utiliser DynamoDB, une base de données NoSql Serverless qui permet de stocker des To de données et de les requêter en temps réel.
- 🚄Créer une fonction AWS Lambda, le service Function as a Service d'AWS qui permet d'exécuter des milliers de fonctions en parallèle sans se soucier de la partie architecture.
- Et plus encore si on a le temps.

### Pré-requis
Seul les cours du tronc commun sont nécessaire pour se cours. Néanmoins, une **grande autonomie et curiosité** sont attendues pour ce cours. Il sera en grande majorité pratique. La partie cours sera uniquement là pour vous faire comprendre les concepts généraux. Donc vous allez devoir **apprendre à vous débuguer par vous même**. Demandez à vos camarades, stackoverflow ou ChatGPT. Et si vous avez des questions, doutes, idée ne les gardez pas pour vous ! 

**Un ordinateur portable sera nécessaire pendant le cours**. J'ai demandé à la DSI de préparer des ordinateurs sous ubuntu pour vous tous. Vous êtes libre d'aller en chercher un. Les applications suivantes seront nécessaires pendant le cours : git, python, un client ssh, nodejs et npm, aws CLI, docker et Terraform (un outil d'Infrastructure as Code). **Tous ces outils doivent être installés sur vos machines**. Si vous avez une distribution se basant sur ubuntu, je vous ai fait un script d'installation des outils. Pour les autres, l'installation est à votre charge. Et je n'aurais pas le temps en cours de débuguer vos installations, alors pour profiter du cours au maximum je vous encourage à aller prendre un ordinateur à la DSI.

### Notation

Ce cours sera en contrôle continue. Ainsi, vous aurez entre chaque cours à répondre à un petit QCM sur Moodle. Vous disposerez de deux tentatives et il n'y a pas de limite de temps pendant une tentative. Ces QCM n'ont pas pour vocation de vous piéger et ils constitueront une partie de votre note du module. 

Deux TP notés vous seront demandés. Un à la moitié du cours et un autre à la fin du cours. Ces TP seront l'application des concepts vus précédemment mais vous serez moins guidé que dans un TP classique. Ils seront à faire à la maison mais pourront être commencés en cours si vous avez le temps.