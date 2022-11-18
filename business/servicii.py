from domain.entitati import *
class ServiceFilme(object):

    def __init__(self, valid_film, repo_filme):
        """
        constructor al clasei ServiceFilm
        :param valid_film:
        :param repo_filme:
        """
        self.__valid_film = valid_film
        self.__repo_filme = repo_filme

    def get_nr_filme(self):
        # functie care returneaza lungimea listei de filme
        return len(self.__repo_filme)

    def adauga_film(self, id_film, titlu, descriere, gen):
        """
        functie care creeaza un film de tipul Film, il valideaza, iar daca campurile filmului sunt corecte
        filmul va fi introdus in lista de filme
        :param id_film: intreg >= 0
        :param titlu: string
        :param descriere: string
        :param gen: string
        :return: None
        """
        film = Film(id_film, titlu, descriere, gen)
        self.__valid_film.valideaza(film)
        self.__repo_filme.adauga_film(film)

    def adauga_filme_random(self, nr_filme_de_generat):
        """
        functie care adauga filme cu campuri random in lista de filme
        :param nr_filme_de_generat: intreg >= 0
        :return: None
        """
        self.__repo_filme.genereaza_filme(nr_filme_de_generat)

    def sterge_film(self, id_film):
        """
        functie care apeleaza metoda sterge_film din RepoFilme si sterge un film dupa id daca acesta exista in lista
        :param id_film: intreg >= 0
        """
        self.__repo_filme.sterge_film(id_film)

    def modifica_film(self, id_film, titlu, descriere, gen, poz):
        """
        functie care creeaza un film de tipul Film, valideaza campurile, iar daca toate campurile
        sunt valide se vor putea modifica acele campuri corespunzatoare id-ului introdus
        :param id_film: intreg >= 0
        :param titlu: string
        :param descriere: string
        :param gen: gen
        """
        film = Film(id_film, titlu, descriere, gen)
        self.__valid_film.valideaza(film)
        self.__repo_filme.modifica_film(film, 0)

    def cauta_film(self, id_film, poz):
        """
        functie care returneaza filmul din lista al carui id coincide cu id-ul introdus de catre utilizator
        sau care arunca o exceptie in cazul in care id-ul nu se regaseste in lista de filme
        :param id_film: intreg >= 0
        """
        return self.__repo_filme.gaseste_dupa_id_film(id_film, poz)

    def get_filme(self):
        # functie care returneaza lista de filme
        return self.__repo_filme.get_all_filme()

class ServiceClienti(object):

    def __init__(self, valid_client, repo_clienti):
        """
        constructor al clasei ServiceFilm
        :param valid_client:
        :param repo_clienti:
        """
        self.__valid_client = valid_client
        self.__repo_clienti = repo_clienti

    def get_nr_clienti(self):
        # functie care returneaza lungimea listei de clienti
        return len(self.__repo_clienti)

    def adauga_client(self, id_client, nume, prenume, cnp):
        """
        functie care creeaza un client de tipul Client, il valideaza, iar daca campurile clientului sunt corecte
        clientul va fi introdus in lista de clienti
        :param id_client: intreg >= 0
        :param nume: string
        :param prenume: string
        :param cnp: string
        :return: None
        """
        client = Client(id_client, nume, prenume, cnp)
        self.__valid_client.valideaza(client)
        self.__repo_clienti.adauga_client(client)

    def sterge_client(self, id_client):
        """
        functie care apeleaza metoda sterge_client din RepoClienti si sterge un client dupa id daca acesta exista in lista
        :param id_client: intreg >= 0
        """
        self.__repo_clienti.sterge_client(id_client)

    def modifica_client(self, id_client, nume, prenume, cnp):
        """
        functie care creeaza un client de tipul Client, valideaza campurile, iar daca toate campurile
        sunt valide se vor putea modifica acele campuri corespunzatoare id-ului introdus
        :param id_client: intreg >= 0
        :param nume: string
        :param prenume: string
        :param cnp: string
        """
        client = Client(id_client, nume, prenume, cnp)
        self.__valid_client.valideaza(client)
        self.__repo_clienti.modifica_client(client)

    def cauta_client(self, id_client):
        """
        functie care returneaza clientul din lista al carui id coincide cu id-ul introdus de catre utilizator
        sau care arunca o exceptie in cazul in care id-ul nu se regaseste in lista de clienti
        :param id_client: intreg >= 0
        """
        return self.__repo_clienti.gaseste_dupa_id_client(id_client)

    def get_clienti(self):
        # functie care returneaza lista de clienti
        return self.__repo_clienti.get_all_clienti()

all_filme = []
class ServiceInchirieri(object):

    def __init__(self, valid_id_uri, repo_filme, repo_clienti, repo_inchirieri):
        """
        constructor al clasei ServiceInchirieri
        :param valid_id_uri:
        :param repo_filme:
        :param repo_clienti:
        :param repo_inchirieri:
        """
        self.__valid_id_uri = valid_id_uri
        self.__repo_filme = repo_filme
        self.__repo_clienti = repo_clienti
        self.__repo_inchirieri = repo_inchirieri

    def get_nr_inchirieri(self):
        # functie care returneaza lungimea listei de inchirieri
        return len(self.__repo_inchirieri)

    def adauga_inchiriere(self, id_client, id_film):
        """
        :param id_client: intreg >= 0
        :param id_film: intreg >= 0
        :return: None
        functie care creeaza o inchiriere de tipul Inchiriere, o valideaza, verifica daca id-ul clientului
        se afla in lista de clienti si daca id-ul filmului se afla in lista de filme. in cazul in care se afla atunci
        se adauga o noua inchiriere, iar in caz contrar se arunca o exceptie.
        in cazul in care s-a adaugat o noua inchiriere, se creeaza o noua lista in care se adauga filmul care a fost
        inchiriat, respectivul film stergandu-se la final din lista de filme.
        """
        self.__valid_id_uri.valideaza_id_uri(id_film, id_client)
        self.__repo_inchirieri.gaseste_inchiriere_dupa_id_film(id_film)
        client = self.__repo_clienti.gaseste_dupa_id_client(id_client)
        film = self.__repo_filme.gaseste_dupa_id_film(id_film, 0)
        inchiriere = Inchiriere(id_film, film.get_titlu(), film.get_gen(), id_client, client.get_nume(), client.get_prenume())
        self.__repo_inchirieri.inchiriaza_film(inchiriere)
        global all_filme
        all_filme.append(self.__repo_filme.gaseste_dupa_id_film(id_film, 0))
        self.__repo_filme.sterge_film(id_film)

    def sterge_inchiriere(self, id_client, id_film):
        """
        :param id_client: intreg >= 0
        :param id_film: intreg >= 0
        :return: None
        functie care sterge o inchiriere din lista de inchirieri si adauga inapoi in lista de filme
        filmul care s-a dorit a fi returnat
        """
        t = self.__repo_inchirieri.sterge_inchiriere(id_client, id_film)
        for i in range(len(all_filme)):
            if all_filme[i].get_id_film() == id_film:
                self.__repo_filme.adauga_film(all_filme[i])
                del all_filme[i]
                break
        return t

    def modifica_inchiriere_dupa_client(self, id_client):
        """
        functie care modifica lista de inchirieri in cazul in care id-ul introdus este corespunzator unui client care
        exista in lista de inchirieri si care si-a modificat cel putin unul dintre campurile nume, prenume
        in lista de clienti
        :param id_client: intreg >= 0
        :return: None
        """
        self.__valid_id_uri.valideaza_id_uri(0, id_client)
        client = self.__repo_clienti.gaseste_dupa_id_client(id_client)
        self.__repo_inchirieri.modifica_inchiriere_dupa_client(id_client, client)

    def cmp_client(self, a, b):
        """
        functie de comparare a doi clienti dupa nume, prenume si id
        :param a: Client
        :param b: Client
        :return: boolean
        """
        if a.get_nume() < b.get_nume():
            return True
        if a.get_nume() == b.get_nume() and a.get_prenume() < b.get_prenume():
            return True
        if a.get_nume() == b.get_nume() and a.get_prenume() == b.get_prenume() and a.get_id_client() < b.get_id_client():
            return True
        return False

    def cmp_ap_id_client(self, a, b):
        """
        functie de comparare a doua numere care reprezinta aparitiile a doua id-uri a
        doi clienti din lista de inchirieri
        :param a: intreg >= 0
        :param b: intreg >= 0
        :return: boolean
        """
        if a < b:
            return True
        return False

    def cmp_ap_titlu(self, a, b):
        """
        functie de comparare a doua numere care reprezinta aparitiile a doua titluri
        a doua filme din lista de inchirieri
        :param a: intreg >= 0
        :param b: intreg >= 0
        :return: boolean
        """
        if a < b:
            return True
        return False

    def cmp_ap_gen(self, a, b):
        """
        functie de comparare a doua numere care reprezinta aparitiile a doua genuri
        a doua filme din lista de inchirieri
        :param a: intreg >= 0
        :param b: intreg >= 0
        :return: boolean
        """
        if a < b:
            return True
        return False


    def identitate(self, x):
        """
        :param x: boolean
        functie care returneaza rezultatul functiei de comparare
        :return: boolean
        """
        return x

    def negare(self, x):
        """
        :param x: boolean
        functie care returneaza rezultatul negat al functiei de comparare
        :return: boolean
        """
        return not x


    def insertion_sort(self, lista, key=lambda x: x, reverse=False, cmp=lambda x, y: x < y):
        """
        :param lista: lista
        :param key: elementul dupa care se face sortarea
        :param reverse: False -> sortarea se face crescator
                         True  -> sortarea se face descrescator
        :param cmp: functie care ne indica criteriul dupa care se face compararea
        :return: lista
        """
        if reverse is True:
            operatie = self.negare
        else:
            operatie = self.identitate

        for i in range(1, len(lista)):
            ind = i - 1
            a = lista[i]
            while ind >= 0 and operatie(cmp(key(a), key(lista[ind]))):
                  lista[ind + 1] = lista[ind]
                  ind = ind - 1
            lista[ind + 1] = a
        return lista



    def getNextGap(self, gap):
        gap = int((gap * 10) / 13)
        if gap < 1:
            return 1
        return gap

    def combSort(self, lista, key=lambda x: x, reverse=False, cmp=lambda x, y: x < y):
        if reverse is False:
            operatie = self.negare
        else:
            operatie = self.identitate
        n = len(lista)
        gap = n
        swapped = True
        while gap != 1 or swapped is True:
            gap = self.getNextGap(gap)
            swapped = False
            for i in range(0, n - gap):
                if operatie(cmp(key(lista[i]), key(lista[i+gap]))):
                    lista[i], lista[i + gap] = lista[i + gap], lista[i]
                    swapped = True
        return lista


    def ordoneaza_inchirieri_dupa_client(self):
        """
        functie care creeaza o copie a listei de inchirieri si o sorteaza crescator dupa numele clientilor. In cazul
        in care numele coincid, se sorteaza crescator dupa prenumele clientilor.
        In cazul in care si prenumele coincid, se sorteaza crescator dupa id-urile clientilor
        functia returneaza noua lista sortata
        :return: copie_lista
        """
        all_inchirieri = self.__repo_inchirieri.get_all_inchirieri()
        copie_lista_inchirieri = []
        for i in range(len(all_inchirieri)):
            copie_lista_inchirieri.append(all_inchirieri[i])
        copie_lista = self.insertion_sort(copie_lista_inchirieri, key=lambda x: x, reverse=False, cmp=self.cmp_client)
        return copie_lista


    def aparitii_client_in_lista_de_inchirieri(self, lista_inchirieri, dictionar):
        """
        functie care retine intr-un dictionar numarul de aparitii al id-urilor clientilor in lista de inchirieri
        :param lista_inchirieri: []
        :param dictionar: {}
        :return: None
        """
        for inchiriere in lista_inchirieri:
            dictionar[inchiriere.get_id_client()] = 0
        for inchiriere in lista_inchirieri:
            dictionar[inchiriere.get_id_client()] += 1


    def ordoneaza_inchirieri_dupa_nr_de_filme(self, dictionar):
        """
        functie care creeaza o copie a listei de inchirieri si un dictionar care contine numarul de aparitii al fiecarui
        client din lista de inchirieri in functie de id-ul clientului.
        functia sorteaza descrescator copia listei de inchirieri dupa numarul de aparitii al fiecarui client in lista
        respectiva
        functia returneaza noua lista sortata
        :param dictionar: dictionar
        :return: lista_inchirieri
        """
        all_inchirieri = self.__repo_inchirieri.get_all_inchirieri()
        copie_lista_inchirieri = []
        for i in range(len(all_inchirieri)):
            dictionar[all_inchirieri[i].get_id_client()] = 0
            copie_lista_inchirieri.append(all_inchirieri[i])
        for i in range(len(all_inchirieri)):
            dictionar[all_inchirieri[i].get_id_client()] += 1

        lista_inchirieri = self.insertion_sort(copie_lista_inchirieri, key=lambda x: dictionar[x.get_id_client()], reverse=True, cmp=self.cmp_ap_id_client)
        return lista_inchirieri

    def ordoneaza_inchirieri_dupa_aparitia_filmelor(self, dictionar):
        """
        functie care creeaza o copie a listei de inchirieri si un dictionar care contine numarul de aparitii al fiecarui
        film din copia listei de inchirieri in functie de titlul filmului
        functia sorteaza descrescator copia listei de inchirieri dupa titlul filmului
        functia returneaza noua lista sortata
        :param dictionar: dictionar
        :return: lista_inchirieri
        """
        all_inchirieri = self.__repo_inchirieri.get_all_inchirieri()
        copie_lista_inchirieri = []
        for i in range(len(all_inchirieri)):
            dictionar[all_inchirieri[i].get_titlu()] = 0
            copie_lista_inchirieri.append(all_inchirieri[i])
        for i in range(len(all_inchirieri)):
            dictionar[all_inchirieri[i].get_titlu()] += 1
        lista_inchirieri = self.combSort(copie_lista_inchirieri, key=lambda x: dictionar[x.get_titlu()], reverse=True, cmp=self.cmp_ap_titlu)
        return lista_inchirieri

    def ordoneaza_inchirieri_dupa_aparitia_genului_de_filme(self, dictionar):
        """
        functie care creeaza o copie a listei de inchirieri si un dictionar care contine numarul de aparitii al fiecarui
        film din copia listei de inchirieri in functie de genul filmului
        functia sorteaza descrescator copia listei de inchirieri dupa genul filmului
        functia returneaza noua lista sortata
        :param dictionar: dictionar
        :return: lista_inchirieri
        """
        all_inchirieri = self.__repo_inchirieri.get_all_inchirieri()
        copie_lista_inchirieri = []
        for i in range(len(all_inchirieri)):
            dictionar[all_inchirieri[i].get_gen()] = 0
            copie_lista_inchirieri.append(all_inchirieri[i])
        for i in range(len(all_inchirieri)):
            dictionar[all_inchirieri[i].get_gen()] += 1
        lista_inchirieri = self.combSort(copie_lista_inchirieri, key=lambda x: dictionar[x.get_gen()], reverse=True, cmp=self.cmp_ap_gen)
        return lista_inchirieri


    def get_inchirieri(self):
        # functie care returneaza lista de inchirieri
        return self.__repo_inchirieri.get_all_inchirieri()

    # def get_inchirieri(self):
    #     inchirieri_dtos = self.__repo_inchirieri.get_all_inchirieri()
    #     dictionar_inchirieri = {}
    #     for inchiriere_dto in inchirieri_dtos:
    #         film = self.__repo_filme.gaseste_dupa_id_film(inchiriere_dto.get_id_film())
    #         client = self.__repo_clienti.gaseste_dupa_id_client(inchiriere_dto.get_id_client())
    #         inchiriere_dto.set_film(film)
    #         inchiriere_dto.set_client(client)
    #         if client.get_id_client() not in dictionar_inchirieri:
    #             dictionar_inchirieri[client.get_id_client()] = []
    #         dictionar_inchirieri[client.get_id_client()].append(inchiriere_dto)
    #     rezultat = []
    #     for dictionar_inchiriere in dictionar_inchirieri:
    #         id_client = dictionar_inchiriere
    #         client = self.__repo_clienti.gaseste_dupa_id_client(id_client)
    #         filme = dictionar_inchirieri[dictionar_inchiriere]
    #         inchiriere_dto = DTO_Inchirieri(client.get_nume(), client.get_prenume(), filme)
    #         rezultat.append(inchiriere_dto)
    #     return rezultat


