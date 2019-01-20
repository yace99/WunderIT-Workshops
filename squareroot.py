#extraction de racine carr�e par dichotomie
#par Yassine Sahraoui

def dichosqrt(number):
    
    if number < 0:
        return 0 #dans le cas ou l'utilisateur entre un nombre n�gatif, le programme retournera 0
    else:
        mini = 0.0 #borne inferieure de d�part: 0
        maxi = round(number, 4) #borne sup�rieure de d�part: le nombre entr� par l'utilisateur
        mid = round(mini+maxi/2.0, 4) #moyenne de la borne sup et inf
        
        while True:
            mid = round((mini+maxi)/2.0, 5) #re�valution de "mid" a chaque iteration 
            diff = mid*mid - round(number, 4) #variable marge de pr�cision
            if abs(diff) <= 0.001:
                return round(mid, 4)  # si la pr�cision atteint 0.001, la boucle s'arr�te et le programme renvoie le resultat
            elif mid*mid < number: 
                mini = mid # si le carr� de "mid" est inferrieur au nombre, on reduit la zone de recherche �  la moiti� sup�rieur
                print("1", mid)
            else:
                maxi = mid # si le carr� de "mid" est superieur au nombre, on reduit la zone de recherche � la moiti� inf�rieure
                print("2", mid)

