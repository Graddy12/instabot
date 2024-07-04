from instabot import Bot
import json

def load_config():
    with open('config.json') as f:
        return json.load(f)

def main():
    config = load_config()
    
    bot = Bot()
    bot.login(username=config["username"], password=config["password"])

    # Suivre une liste d'utilisateurs
    utilisateurs_a_suivre = config["utilisateurs_a_suivre"]
    for utilisateur in utilisateurs_a_suivre:
        bot.follow(utilisateur)

    # Liker les photos des utilisateurs
    for utilisateur in utilisateurs_a_suivre:
        bot.like_user(utilisateur, amount=3)

    bot.logout()

if __name__ == "__main__":
    main()￼Enter
