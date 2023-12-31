# PasswordManager

Ce projet est un gestionnaire de mots de passe simple réalisé en utilisant Python et la bibliothèque Tkinter pour l'interface graphique. Il stocke les informations des sites Web, noms d'utilisateur et mots de passe dans une base de données SQLite. Vous pouvez ajouter, afficher, modifier et supprimer des entrées de mot de passe à l'aide de cette application.

## Prérequis

- Python 3.x doit être installé sur votre système.
- Assurez-vous d'avoir la bibliothèque Tkinter, qui est généralement incluse dans les installations Python standard.

## Comment exécuter l'application

1. Téléchargez ou clonez le code source dans votre répertoire local.
2. Assurez-vous que le fichier `icon.ico` est présent dans le même répertoire que le script Python.
3. Exécutez l'application en exécutant le fichier Python `password_manager.py`.

## Fonctionnalités

### Ajouter un mot de passe

1. Ouvrez l'application Password Manager.
2. Saisissez le site Web, le nom d'utilisateur et le mot de passe dans les champs appropriés.
3. Cliquez sur le bouton "Add Password" pour ajouter les informations à la base de données.

### Afficher les mots de passe

1. Cliquez sur le bouton "Show Passwords" pour afficher tous les mots de passe enregistrés dans la base de données.
2. Une fenêtre s'ouvrira avec une liste des sites Web, noms d'utilisateur et mots de passe.

### Modifier un mot de passe

1. Dans la fenêtre affichant les mots de passe, cliquez sur le bouton "Edit" correspondant à l'entrée que vous souhaitez modifier.
2. Une nouvelle fenêtre s'ouvrira, vous permettant de modifier les informations du site Web, du nom d'utilisateur et du mot de passe.
3. Cliquez sur le bouton "Enregistrer les modifications" pour sauvegarder les changements.

### Supprimer un mot de passe

1. Dans la fenêtre affichant les mots de passe, cliquez sur le bouton "Delete" correspondant à l'entrée que vous souhaitez supprimer.
2. Une boîte de dialogue de confirmation apparaîtra pour confirmer la suppression.
3. Cliquez sur "Yes" pour supprimer le mot de passe de la base de données.

## Remarques

- Les mots de passe sont stockés localement dans une base de données SQLite appelée `passwords.db`.
- Assurez-vous de sauvegarder vos mots de passe en toute sécurité, car ils ne sont pas récupérables en cas de perte de la base de données.

