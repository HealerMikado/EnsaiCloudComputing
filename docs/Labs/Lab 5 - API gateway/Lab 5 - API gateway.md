---
layout: default
title: "TP5 - Faire une API REST 100% serverless	🧰"
nav_order: 5
parent: Labs
---

# TP5 - Faire une API REST 100% serverless

Le but de ce TP est de faire une API REST en utilisant uniquement des services serverless proposés par AWS. Cela ne va pas être plus compliqué pour vous (voir même cela risque d'être plus facile). Comme votre application sera 100% serverless, vous n'allez plus utiliser Terraform, mais AWS SAM (Serverless Application Model). Comme Terraform, SAM est une solution IaC, et va permettre de définir l'architecture de votre application comme du code. Cette fois-ci ce ne sera pas du code python, mais un simple yaml (YAML Ain't Markup Language), un format clef valeur proche du json, mais où l'indentation est importante.

Le but du TP est de mettre en place une API REST pour gérer des tâches d'une to-do liste. Vous n'allez faire pendant la séance que la partie création d'une tâche. À vous de terminer si vous le souhaitez.

<img src="img/architecture cible.jpg" style="zoom:60%;" />

## Un hello world avec SAM

Placez-vous dans le répertoire où vous souhaitez faire le TP puis exécutez la commande `sam init`. Sélectionnez l'option `AWS Quick Start Templates` puis sélectionnez le premier template. Pour la question suivante validez que vous souhaitez utiliser python, refusez X-ray puis donnez un nom à votre projet. Une fois le projet téléchargez un dossier sera apparu avec arborescences suivante (certaines parties sont omises) :

```
📦test
 ┣ 📂events
 ┃ ┗ 📜event.json
 ┣ 📂hello_world
 ┃ ┣ 📜app.py
 ┃ ┣ 📜requirements.txt
 ┃ ┗ 📜__init__.py
 ┣ 📜template.yaml
 ┗ 📜__init__.py
```

Le fichier `template.yaml` contient l'infrastructure de votre code, le dossier `hello_world` va contenir le code de votre lambda (ce dossier peut être renommé) et `event.json` va contenir un évènement pour tester votre application. 

Le fichier qui nous intéresse particulièrement en ce moment est le fichier `template.yaml`. Voici son contenu (certaines parties sont omises):

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Globals:
  Function:
    Timeout: 3

Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function 
    Properties:
      CodeUri: hello_world/
      Handler: app.lambda_handler
      Runtime: python3.9
      Architectures:
        - x86_64
      Events:
        HelloWorld:
          Type: Api
          Properties:
            Path: /hello
            Method: get

Outputs:
  HelloWorldApi:
    Description: "API Gateway endpoint URL for Prod stage for Hello World function"
    Value: !Sub "https://${ServerlessRestApi}.execute-api.${AWS::Region}.amazonaws.com/Prod/hello/"
  HelloWorldFunction:
    Description: "Hello World Lambda Function ARN"
    Value: !GetAtt HelloWorldFunction.Arn
  HelloWorldFunctionIamRole:
    Description: "Implicit IAM Role created for Hello World function"
    Value: !GetAtt HelloWorldFunctionRole.Arn
```

Vous constatez qu'il y a 3 parties dans votre fichier et évidement chacune à son rôle:

- **Globals** permet de définir des configurations de manière globale. Ici le timeout des fonctions lambda du template est de 3 secondes
- **Ressources** est la partie où infrastructure est défini. Actuellement ce template défini :
  - Une fonction lambda, c'est ce que veut dire la ligne 10. Son code est dans le dossier hello-world, le handler est la fonction lambda_handler du fichier app.py, et la version de python de la fonction est 3.9
  - Une API Gateway. C'est moins clair mais c'est ce que veux dire la ligne 19. Comme la lambda est déclenché par une API Gateway, elle va être créée même si elle n'est pas formellement définie. Le code de la lambda sera déclenché par un appel GET sur le chemin /hello
- **Outputs** permet de récupérer facilement des valeurs qui ne sont connues qu'une fois le template déployé. Ici l'URL pour déclencher la fonction, l'identifiant AWS de la lambda et de son rôle.

Comme vous utilisez des labs AWS academy, ce code ne fonctionne pas tel quel. En effet, ce code crée automatiquement un rôle pour la lambda , sauf que c'est impossible sur un lab. Ajoutez après `Handler` la ligne `Role: !Sub arn:aws:iam::${AWS::AccountId}:role/LabRole` pour mettre le bon rôle à votre lambda.. Supprimez également les 3 dernières lignes du template.

Maintenant cela fait, il est temps de déployer le template ! Faites un `sam deploy --guided` et répondez au question dans le terminal.

- Stack Name : répondez ce que vous souhaitez
- AWS Region : us-east-1
- Confirm changes before deploy  : y
- Allow SAM CLI IAM role creation : n
- Capabilities [['CAPABILITY_IAM']]:  validez avec entrée
- Disable rollback [y/N]: répondez ce que vous souhaitez
- HelloWorldFunction may not have authorization defined, Is this okay? [y/N]: y
- Valider les prompts suivant avec entrée

Après quelques instants, la liste des ressources a déployer va apparaitre dans votre terminal 

| Operation | LogicalResourceId                          | ResourceType                | Replacement |
| --------- | ------------------------------------------ | --------------------------- | ----------- |
| + Add     | HelloWorldFunctionHelloWorldPermissionProd | AWS::Lambda::Permission     | N/A         |
| + Add     | HelloWorldFunction                         | AWS::Lambda::Function       | N/A         |
| + Add     | ServerlessRestApiDeployment47fc2d5f9d      | AWS::ApiGateway::Deployment | N/A         |
| + Add     | ServerlessRestApiProdStage                 | AWS::ApiGateway::Stage      | N/A         |
| + Add     | ServerlessRestApi                          | (AWS::ApiGateway::RestApi)  | N/A         |

Comme c'est un premier déploiement vous avez seulement des opérations `Add`. Votre template tout simple est en train de créer :

- Une fonction lambda (AWS::Lambda::Function) et un politique de sécurité associée (AWS::Lambda::Permission)
- Une API Gateway de type Rest (AWS::Lambda::Function), avec un stage (AWS::ApiGateway::Stage) le tout accessible sur internet (AWS::ApiGateway::Deployment)

Validez les changements et après quelques instants un bloc output va apparaitre dans le terminal. Copiez/collez l'url de l'api et vérifiez qu'elle fonctionne bien.

🎉 Félicitation vous venez de créer votre premier API Rest 100% serverless sur AWS ! Avec un peu de travail, vous pourriez redéployer tout votre projet info de 2A.

## Ajouter une base de données DynamoDB

DynamoDB est une base de données serverless, il est donc possible de l'ajouter dans le template. Dans la partie Resources du template ajoutez :

```yaml
DynamoDBTable:
  Type: AWS::DynamoDB::Table
  Properties: 
    AttributeDefinitions: 
      - AttributeName: user
        AttributeType: S
      - AttributeName: id
        AttributeType: S
    KeySchema: 
      - AttributeName: user
        KeyType: HASH
      - AttributeName: id
        KeyType: RANGE
    ProvisionedThroughput: 
      ReadCapacityUnits: 5
      WriteCapacityUnits: 5
```

Et déployez de nouveau votre template. Vous allez voir que seule la nouvelle ressource va être déployée.

Maintenant il faut arriver à faire le lien entre la base DynamoDB et la fonction lambda. Pour rendre le code le plus souple possible, le nom de la table ne va pas être *harcodé* dans la fonction, mais mis dans ses variables d'environnement. Dans les properties de votre fonction ajoutez les lignes :

```yaml
Environment:
  Variables:
    DYNAMO_TABLE: !Ref DynamoDBTable
```

Ces lignes vont faire que lors du déploiement, une variable d'environnement `DYNAMO_TABLE` va être créée, et qu'elle va avoir pour valeur le nom de la table. Comme le nom est généré dynamiquement, on va passer une référence à la ressource DynamoDB (`!Ref DybamoDBTable`) et SAM va dynamiquement injecter le nom.

Déployez le template, allez sur la page du service AWS Lambda, puis sur la lambda créée par le template, puis `configuration` et `Environment variables` et vérifier que tout est bon.

## Le code de la lambda

Pour le moment vous avez seulement fait la partie infrastructure de l'application, il est temps de regarder un peu le code. Quand AWS SAM a généré le template de base, il a crée un dossier `hello_world`. Ce dossier contient le code de la fonction lambda. Quand AWS SAM va déployer le code de la lambda, il cherche le contenu de la variable `codeUri` et déploie l'intégralité du dossier. Si le dossier contient un fichier `requirements.txt`, SAM va installer les dépendances pour la lambda. Si vous regarder le fichier `app.py`, il contient la méthode `lambda_handler()`, qui pour le moment ne renvoie qu'une réponse prédéfinie.

1. Dans le `template.yml` changez le nom de la ressource `HelloWorldFunction` en `PostTaskFunction` (attention vous devez mettre à jour la dernière ligne du template également)

2. Changez dans l'Events de la fonction le nom de l'API (HelloWorld -> Task), et de sa propriété (/hello -> task, get -> post)

3. Créez un dossier `PostTask` et faites que votre lambda pointe vers se dossier.

4. Implémentez la fonction `lambda_handler()` qui va poster un commentaire dans la base DynamoDB. Une requête http post permet de créer une ressource, les éléments de la ressource seront dans le `body` de la requête. Voici un exemple de body

   ```json
   {
   	"user" : "Rémi",
       "taskTitle" : "Corriger le TP noté",
       "taskBody" : "Tout est dans le titre",
       "taskDueDate" : "18/05/2023"
   }
   ```

Pour vous aider :

- Pour récupérer le contenu du corps de la requête, utilisez `body = json.loads(event['body'])` (pensez à importer le package json, ce package est dans les packages de base de python, pas besoin de l'ajouter dans le requirements.txt). La variable body est un dictionnaire python.

- Chaque task va avoir un identifiant unique générée par avec la fonction `uuid.uuid4()` (il faut importer uuid, c'est un package dans la distribution python de base)

- Voici un code exemple pour écrire un objet dans DynamoDB, ce code n'est pas à reprendre tel quel ! Vous trouvera le nom de la table dans les variables d'environnement de votre lambda.

  ```python
  import boto3
  # Get the service resource.
  dynamodb = boto3.resource('dynamodb')
  # Get the table.
  table = dynamodb.Table('users')
  # Put item to the table.
  table.put_item(
     Item={
          'username': 'janedoe',
          'first_name': 'Jane',
          'last_name': 'Doe',
          'age': 25,
          'account_type': 'standard_user',
      }
  )
  ```

  >  🧙‍♂️Bien que n'étant pas par défaut dans python, boto3 est par défaut dans les lambdas

- Une fois l'ajout fait, faites retourner à votre lambda une dictionnaire s'inspirant de celui ci :

  ```json
  {
      "statusCode": 200,
      "body": votre objet task
  }
  ```

  

