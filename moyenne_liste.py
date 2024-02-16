def calculer_moyenne(liste):
    somme = 0
    for i in range(len(liste)):
        somme = somme + liste[i]
    return somme/len(liste)