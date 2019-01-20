#extraction de racine carrée par dichotomie
#par Yassine Sahraoui

def dichosqrt(number):
    
    if number < 0:
        return 0 #dans le cas ou l'utilisateur entre un nombre négatif, le programme retournera 0
    else:
        mini = 0.0 #borne inferieure de départ: 0
        maxi = round(number, 4) #borne supérieure de départ: le nombre entré par l'utilisateur
        mid = round(mini+maxi/2.0, 4) #moyenne de la borne sup et inf
        
        while True:
            mid = round((mini+maxi)/2.0, 5) #reévalution de "mid" a chaque iteration 
            diff = mid*mid - round(number, 4) #variable marge de précision
            if abs(diff) <= 0.001:
                return round(mid, 4)  # si la précision atteint 0.001, la boucle s'arrête et le programme renvoie le resultat
            elif mid*mid < number: 
                mini = mid # si le carré de "mid" est inferrieur au nombre, on reduit la zone de recherche à  la moitié supérieur
            else:
                maxi = mid # si le carré de "mid" est superieur au nombre, on reduit la zone de recherche à la moitié inférieure

