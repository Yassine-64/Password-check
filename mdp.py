tentatives = 0

le_MDP_correct = "DEV@2023"
tentative_max = 3
question_secrete = "Le nom de votre film préféré ?"
reponse_vrai = "imitation game"
while tentatives < tentative_max:
    mot_de_passe = input("Entrez le mot de passe : ")
    if mot_de_passe == le_MDP_correct:
        print("Bonjour!")
        break  
    tentatives += 1

    if tentatives == tentative_max:
        print("Vous avez épuisé toutes les tentatives.")
        print("Répondez à la question secrète.")

        reponse_secrete = input(question_secrete)

        if reponse_secrete == reponse_vrai:
            print("Bonjour!")
            break  
        else:
            print("Réponse incorrecte. Accès refusé.")
            break  