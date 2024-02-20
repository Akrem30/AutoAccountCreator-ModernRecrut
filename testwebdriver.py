from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random
import string

driver = webdriver.Chrome()
#aller sur la page de création de compte
driver.get("https://localhost:7001/Identity/Account/Register")

#récupérer tous les éléments du formulaire et les remplir
driver.find_element(by=By.ID,value="Input_Prenom").send_keys("Jack")
driver.find_element(by=By.ID,value="Input_Nom").send_keys("Jack")

# on génére à chaque fois l'adresse email pour garantir l'unicité
chaine = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))  
# Construire l'adresse e-mail complète
email = chaine + "@gmail.com"
driver.find_element(by=By.ID, value="Input_Email").send_keys(email)

#afficher l'adresse email générée
print("email : " +email)

select = driver.find_element(by=By.ID,value="Input_Type")
candidat = Select(select).select_by_index(2)

#on définit une fonction pour générer un mot de passe fort aléatoire
def generer_mot_de_passe():

    caracteres= string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
  
    while len(mot_de_passe) < 10:
        mot_de_passe.append(random.choice(caracteres))
   
    random.shuffle(mot_de_passe)

    mot_de_passe = ''.join(mot_de_passe)
    return mot_de_passe

#générer le mot de passe en utilisant la fonction
mot_de_passe = generer_mot_de_passe()

driver.find_element(by=By.ID,value="Input_Password").send_keys(mot_de_passe)
driver.find_element(by=By.ID,value="Input_ConfirmPassword").send_keys(mot_de_passe)
#afficher le mot de passe
print("mot de passe : " + mot_de_passe)

driver.find_element(by=By.CLASS_NAME,value="form-check-input").click()
# cliquer sur le bouton pour s'enregistrer
driver.find_element(by=By.ID,value="registerSubmit").click()

driver.find_element(by=By.ID,value="confirm-link").click()
#aller à la page de connexion pour se connecter
driver.get("https://localhost:7001/Identity/Account/Login")
driver.find_element(by=By.ID,value="Input_Email").send_keys(email)
mdp = driver.find_element(by=By.ID,value="Input_Password")
mdp.clear()
mdp.send_keys(mot_de_passe)
driver.find_element(by=By.ID,value="login-submit").click()
#fermer le navigateur
driver.quit()



