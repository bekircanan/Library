complexite_ajout_fin = 0
complexite_ajouter_debut = 0
complexite_est_vide = 0
complexite_taille = 0
complexite_get_dernier_maillon = 0
complexite_get_maillon_indice = 0
complexite_inserer_apres = 0
complexite_supprimer = 0
complexite_recherche = 0
complexite_tri_insertion = 0
complexite_tri_selection = 0
complexite_tri_fusion = 0
complexite_tri_bulle = 0


class Maillon():
    def __init__(self, valeur):
        self.valeur = valeur
        self.suivant = None


class ListeChainée():
    def __init__(self):
        self.tete = None

    def ajouter_fin(self, valeur):
        """
        Ajoute un maillon avec la valeur donnée à la fin de la liste chaînée.
        Args:
            valeur: La valeur à ajouter à la fin de la liste.
        """
        global complexite_ajout_fin
        complexite_ajout_fin+= 1  # Initialisation de maillon
        maillon = Maillon(valeur)
        complexite_ajout_fin+= 1  # Test if(self.tete == None)
        if(self.tete == None):
            self.tete = maillon
            complexite_ajout_fin+= 1  # Affectation self.tete = maillon
        else:
            courant = self.tete
            complexite_ajout_fin+= 1  # Initialisation de courant
            while (courant.suivant != None):
                courant = courant.suivant
                complexite_ajout_fin+= 2  # Test while et affectation courant = courant.suivant
            courant.suivant = maillon
            complexite_ajout_fin+= 1  # Affectation courant.suivant = maillon

    def ajouter_debut(self, valeur):
        """
        Ajoute un maillon avec la valeur donnée au début de la liste chaînée.
        Args:
            valeur: La valeur à ajouter au début de la liste.
        """
        global complexite_ajouter_debut
        complexite_ajouter_debut = 0
        complexite_ajouter_debut += 1  # Initialisation de maillon
        maillon = Maillon(valeur)
        complexite_ajouter_debut += 1  # Test if(self.tete == None)
        if(self.tete == None):
            self.tete = maillon
            complexite_ajouter_debut += 1  # Affectation self.tete = maillon
        else:
            maillon.suivant = self.tete
            self.tete = maillon
            complexite_ajouter_debut += 2  # Affectations maillon.suivant et self.tete

    def est_vide(self):
        """
        Vérifie si la liste chaînée est vide.
        Returns:
            bool: True si la liste est vide, sinon False.
        """
        global complexite_est_vide
        complexite_est_vide = 0
        complexite_est_vide += 1  # Test if(self.tete == None)
        if(self.tete == None):
            return True
        else:
            return False
        
    def taille(self):
        """
        Calcule la taille de la liste chaînée.
        Returns:
            int: Le nombre de maillons dans la liste.
        """
        global complexite_taille
        complexite_taille = 0
        if self.tete is None:
            return 0
        else:
            cpt = 0
            courant = self.tete
            complexite_taille += 1  # Initialisation de courant
            while courant.suivant is not None:
                cpt += 1
                courant = courant.suivant
                complexite_taille += 2  # Test while et affectation courant = courant.suivant
            return cpt

    def get_dernier_maillon(self):
        """
        Récupère le dernier maillon de la liste chaînée.
        Returns:
            Maillon: Le dernier maillon de la liste, ou None si la liste est vide.
        """
        global complexite_get_dernier_maillon
        complexite_get_dernier_maillon = 0
        if self.tete is None:
            return None
        else:
            courant = self.tete
            complexite_get_dernier_maillon += 1  # Initialisation de courant
            while courant.suivant is not None:
                courant = courant.suivant
                complexite_get_dernier_maillon += 2  # Test while et affectation courant = courant.suivant
            return courant

    def get_maillon_indice(self, i):
        """
        Récupère le maillon à l'indice donné dans la liste chaînée.
        Args:
            i (int): L'indice du maillon à récupérer.
        Returns:
            Maillon: Le maillon à l'indice donné, ou None si l'indice est hors limites.
        """
        global complexite_get_maillon_indice
        complexite_get_maillon_indice = 0
        if self.taille() >= i:
            if self.tete is None:
                return None
            else:
                courant = self.tete
                cpt = 0
                complexite_get_maillon_indice += 1  # Initialisation de courant
                while cpt != i:
                    cpt += 1
                    courant = courant.suivant
                    complexite_get_maillon_indice += 2  # Test while et affectation courant = courant.suivant
                return courant

    def inserer_apres(self, valeur, indice):
        """
        Insère un maillon avec la valeur donnée après le maillon à l'indice spécifié.
        Args:
            valeur: La valeur du nouveau maillon.
            indice (int): L'indice après lequel insérer le nouveau maillon.
        """
        global complexite_inserer_apres
        complexite_inserer_apres = 0
        if self.taille() >= indice:
            if not self.est_vide():
                maillon = Maillon(valeur)
                courant = self.tete
                cpt = 0
                complexite_inserer_apres += 1  # Initialisation de courant
                while cpt != indice:
                    cpt += 1
                    courant = courant.suivant
                    complexite_inserer_apres += 2  # Test while et affectation courant = courant.suivant
                maillon.suivant = courant.suivant
                courant.suivant = maillon
                complexite_inserer_apres += 2  # Affectations maillon.suivant et courant.suivant

    def inserer_après(self, valeur, indice):
        """
        Supprime le maillon à l'indice donné de la liste chaînée.
        Args:
            indice (int): L'indice du maillon à supprimer.
        """
        if(self.taille() >= indice):
            if(not self.est_vide()):
                maillon = Maillon(valeur)
                courant = self.tete
                cpt = 0
                while (cpt != indice):
                    cpt += 1
                    courant = courant.suivant
                maillon.suivant = courant.suivant
                courant.suivant = maillon

    def supprimer(self, indice):
        """
        Recherche la première occurrence de la valeur donnée dans la liste chaînée.
        Args:
            valeur: La valeur à rechercher.
        Returns:
            int: L'indice du maillon contenant la valeur, ou -1 si la valeur n'est pas trouvée.
        """
        global complexite_supprimer
        complexite_supprimer = 0
        if self.taille() >= indice:
            if not self.est_vide():
                courant = self.tete
                cpt = 0
                complexite_supprimer += 1  # Initialisation de courant
                while cpt + 1 != indice and courant.suivant is not None:
                    cpt += 1
                    courant = courant.suivant
                    complexite_supprimer += 2  # Test while et affectation courant = courant.suivant
                maillon = courant.suivant
                courant.suivant = maillon.suivant
                del maillon
                complexite_supprimer += 1  # Affectation courant.suivant

    def recherche(self, valeur):
        """
        Trie la liste chaînée en utilisant l'algorithme de tri par insertion.
        Args:
            key (str, optional): La clé à utiliser pour le tri si les valeurs sont des dictionnaires.
        """
        global complexite_recherche
        complexite_recherche = 0
        if not self.est_vide():
            courant = self.tete
            indice = 0
            complexite_recherche += 1  # Initialisation de courant
            while courant.suivant is not None and courant.valeur != valeur:
                courant = courant.suivant
                complexite_recherche += 2  # Test while et affectation courant = courant.suivant
            if courant.valeur == valeur:
                return indice
            else:
                return -1
            
    def triInsertion(self, key = None):
        """
        Trie la liste chaînée en utilisant l'algorithme de tri par sélection.
        Args:
            key (str, optional): La clé à utiliser pour le tri si les valeurs sont des dictionnaires.
        """
        global complexite_tri_insertion
        complexite_tri_insertion = 0
        for i in range(1, self.taille()):
            key_value = self.get_maillon_indice(i).valeur
            complexite_tri_insertion += 1  # Affectation de key_value
            j = i - 1
            complexite_tri_insertion += 1  # Initialisation de j
            while j >= 0 and (self.get_maillon_indice(j).valeur[key] if key is not None else self.get_maillon_indice(j).valeur["titre"]) > (key_value[key] if key is not None else key_value["titre"]):
                self.get_maillon_indice(j + 1).valeur = self.get_maillon_indice(j).valeur
                complexite_tri_insertion += 2  # Affectation et appel de fonction get_maillon_indice
                j -= 1
                complexite_tri_insertion += 1  # Décrémentation de j
            self.get_maillon_indice(j + 1).valeur = key_value
            complexite_tri_insertion += 1  # Affectation de key_value

    def triSelection(self, key = None):
        """
        Trie la liste chaînée en utilisant l'algorithme de tri par fusion.
        Args:
            key (str, optional): La clé à utiliser pour le tri si les valeurs sont des dictionnaires.
        """
        global complexite_tri_selection
        complexite_tri_selection = 0
        for i in range(self.taille() - 1):
            min_index = i
            complexite_tri_selection += 1  # Initialisation de min_index
            for j in range(i + 1, self.taille()):
                complexite_tri_selection += 1  # Initialisation de j
                if (self.get_maillon_indice(j).valeur[key] if key is not None else self.get_maillon_indice(j).valeur["titre"]) < (self.get_maillon_indice(min_index).valeur[key] if key is not None else self.get_maillon_indice(min_index).valeur["titre"]):
                    min_index = j
                    complexite_tri_selection += 1  # Affectation de min_index
                complexite_tri_selection += 1  # Test if
            if min_index != i:
                self.get_maillon_indice(i).valeur, self.get_maillon_indice(min_index).valeur = self.get_maillon_indice(min_index).valeur, self.get_maillon_indice(i).valeur
                complexite_tri_selection += 3  # Affectation de valeurs et test if
            complexite_tri_selection += 1  # Test if

    def triFusion(self, key = None):
        """
        Trie la liste chaînée en utilisant l'algorithme de tri à bulles.
        Args:
            key (str, optional): La clé à utiliser pour le tri si les valeurs sont des dictionnaires.
        """
        global complexite_tri_fusion
        complexite_tri_fusion = 0

        if self.taille() <= 1:
            return self

        # Helper function to split the list into two halves
        def split(head):
            """
            Divise une liste chaînée en deux moitiés.
            Cette fonction prend la tête d'une liste chaînée et la divise en deux moitiés
            en utilisant l'algorithme du lièvre et de la tortue. La première moitié est 
            retournée à partir de la tête d'origine, et la seconde moitié commence à partir 
            du milieu de la liste.
            Args:
                head (Node): La tête de la liste chaînée à diviser.
            Retours:
                tuple: Un tuple contenant les têtes des deux moitiés de la liste chaînée.
            Variables globales:
                complexite_tri_fusion (int): Compteur global pour suivre la complexité du tri par fusion.
            """
            global complexite_tri_fusion
            slow = head
            fast = head
            prev = None
            complexite_tri_fusion += 3  # Initialisation de slow, fast et prev
            while fast and fast.suivant:
                prev = slow
                slow = slow.suivant
                fast = fast.suivant.suivant
                complexite_tri_fusion += 4  # Affectations de prev, slow, fast et test while
            prev.suivant = None
            complexite_tri_fusion += 1  # Affectation de prev.suivant
            return head, slow

        # Helper function to merge two sorted lists
        def fusionner(gauche, droite, key = None):
            """
            Fusionne deux listes chaînées triées en une seule liste triée.
            Cette fonction prend les têtes de deux listes chaînées triées et les fusionne
            en une seule liste triée. La fusion est effectuée en comparant les valeurs des
            deux listes et en les fusionnant dans l'ordre croissant.
            Args:
                gauche (Node): La tête de la première liste chaînée triée.
                droite (Node): La tête de la seconde liste chaînée triée.
                key (str, optionnel): La clé à utiliser pour la comparaison des valeurs.
            Retours:
                Node: La tête de la liste chaînée fusionnée.
            Variables globales:
                complexite_tri_fusion (int): Compteur global pour suivre la complexité du tri par fusion.
            """
            global complexite_tri_fusion
            tmp = Maillon(None)
            courant = tmp
            complexite_tri_fusion += 2  # Initialisation de tmp et courant
            while gauche and droite:
                if (gauche.valeur[key] if key is not None else gauche.valeur["titre"]) <= (droite.valeur[key] if key is not None else droite.valeur["titre"]):
                    courant.suivant = gauche
                    gauche = gauche.suivant
                    complexite_tri_fusion += 3  # Test if et affectations de courant.suivant et gauche
                else:
                    courant.suivant = droite
                    droite = droite.suivant
                    complexite_tri_fusion += 3  # Test else et affectations de courant.suivant et droite
                courant = courant.suivant
                complexite_tri_fusion += 1  # Affectation de courant
            courant.suivant = gauche or droite
            complexite_tri_fusion += 1  # Affectation de courant.suivant
            return tmp.suivant

        # Recursive function to perform merge sort
        def fusion_trier(head):
            """
            Trie une liste chaînée en utilisant l'algorithme de tri par fusion.
            Cette fonction trie une liste chaînée en utilisant l'algorithme de tri par fusion.
            La liste est divisée en deux moitiés, puis les deux moitiés sont triées récursivement
            avant d'être fusionnées ensemble.
            Args:
                head (Node): La tête de la liste chaînée à trier.
            Retours:
                Node: La tête de la liste chaînée triée.
            Variables globales:
                complexite_tri_fusion (int): Compteur global pour suivre la complexité du tri par fusion.
            """
            global complexite_tri_fusion
            if not head or not head.suivant:
                return head
            gauche, droite = split(head)
            complexite_tri_fusion += 1  # Appel de fonction split
            gauche = fusion_trier(gauche)
            droite = fusion_trier(droite)
            complexite_tri_fusion += 2  # Appels de fonctions fusion_trier
            if key is None:
                return fusionner(gauche, droite)
            else:
                return fusionner(gauche, droite, key)

        self.tete = fusion_trier(self.tete)
        complexite_tri_fusion += 1  # Affectation de self.tete

    def triBulle(self, key = None):
        """
        Trie la liste chaînée en utilisant l'algorithme de tri à bulles.
        Args:
            key (str, optional): La clé à utiliser pour le tri si les valeurs sont des dictionnaires.
        Variables globales:
            complexite_tri_bulle (int): Compteur global pour suivre la complexité du tri à bulles.
        """
        global complexite_tri_bulle
        complexite_tri_bulle = 0
        n = self.taille()
        complexite_tri_bulle += 1  # Initialisation de n
        for i in range(n):
            test = False
            complexite_tri_bulle += 1  # Initialisation de test
            for j in range(0, n - i - 1):
                complexite_tri_bulle += 1  # Initialisation de j
                if (self.get_maillon_indice(j).valeur[key] if key is not None else self.get_maillon_indice(j).valeur["titre"]) > (self.get_maillon_indice(j + 1).valeur[key] if key is not None else self.get_maillon_indice(j + 1).valeur["titre"]):
                    complexite_tri_bulle += 1  # Test if
                    self.get_maillon_indice(j).valeur, self.get_maillon_indice(j + 1).valeur = self.get_maillon_indice(j + 1).valeur, self.get_maillon_indice(j).valeur
                    complexite_tri_bulle += 3  # Affectation et appel de fonction get_maillon_indice
                    test = True
                    complexite_tri_bulle += 1  # Affectation de test
            if not test:
                complexite_tri_bulle += 1  # Test if
                break
            
    def tri_optimise(self, key=None):
        """
        Trie la liste chaînée en utilisant l'algorithme de tri le plus optimisé.
        Args:
            key (str, optional): La clé à utiliser pour le tri si les valeurs sont des dictionnaires.
        """
        global complexite_tri_insertion, complexite_tri_selection, complexite_tri_fusion, complexite_tri_bulle
        complexite_tri_insertion = 0
        complexite_tri_selection = 0
        complexite_tri_fusion = 0
        complexite_tri_bulle = 0
        copie_insertion = ListeChainée()
        copie_selection = ListeChainée()
        copie_fusion = ListeChainée()
        copie_bulle = ListeChainée()

        courant = self.tete
        while courant:
            copie_insertion.ajouter_fin(courant.valeur)
            copie_selection.ajouter_fin(courant.valeur)
            copie_fusion.ajouter_fin(courant.valeur)
            copie_bulle.ajouter_fin(courant.valeur)
            courant = courant.suivant
        copie_insertion.triInsertion(key)
        copie_selection.triSelection(key)
        copie_fusion.triFusion(key)
        copie_bulle.triBulle(key)
        complexites = {
            'insertion': complexite_tri_insertion,
            'selection': complexite_tri_selection,
            'fusion': complexite_tri_fusion,
            'bulle': complexite_tri_bulle
        }
        tri_optimal = min(complexites, key=complexites.get)
        if tri_optimal == 'insertion':
            self.triInsertion(key)
        elif tri_optimal == 'selection':
            self.triSelection(key)
        elif tri_optimal == 'fusion':
            self.triFusion(key)
        elif tri_optimal == 'bulle':
            self.triBulle(key)




class MaPile():
    def __init__(self):
        self.liste = ListeChainée()

    def empiler(self, valeur):
        """
        Ajoute une valeur au sommet de la pile.
        Args:
            valeur: La valeur à ajouter à la pile.
        """
        self.liste.ajouter_debut(valeur)

    def depiler(self):
        """
        Retire et retourne la valeur au sommet de la pile.
        Returns:
            La valeur au sommet de la pile, ou None si la pile est vide.
        """
        if not self.liste.est_vide():
            valeur = self.liste.tete.valeur
            self.liste.tete = self.liste.tete.suivant
            return valeur
        return None

    def est_vide(self):
        """
        Vérifie si la pile est vide.
        Returns:
            bool: True si la pile est vide, sinon False.
        """
        return self.liste.est_vide()

class MaFile():
    def __init__(self):
        self.liste = ListeChainée()

    def enfiler(self, valeur):
        """
        Ajoute une valeur à la fin de la file.
        Args:
            valeur: La valeur à ajouter à la file.
        """
        self.liste.ajouter_fin(valeur)

    def defiler(self):
        """
        Retire la valeur au début de la file.
        """
        self.liste.supprimer(0)

    def est_vide(self):
        """
        Vérifie si la pile est vide.
        Returns:
            bool: True si la pile est vide, sinon False.
        """
        return self.liste.est_vide()