from infrastructura.repozitorii import *
from prezentare.ghid import ghid
class Consola(object):

    def __init__(self, srv_filme, srv_clienti, srv_inchiriere):
        self.__srv_filme = srv_filme
        self.__srv_clienti = srv_clienti
        self.__srv_inchiriere = srv_inchiriere

    def _ui_adauga_film(self):
        id_film = int(input("id_film: "))
        titlu = input("titlu_film: ").strip()
        descriere = input("descriere_film: ").strip()
        gen = input("gen_film: ").strip()
        self.__srv_filme.adauga_film(id_film, titlu, descriere, gen)

    def _ui_stergere_film(self):
        id_film = int(input("id_film: "))
        self.__srv_filme.sterge_film(id_film)

    def _ui_modifica_film(self):
        id_film = int(input("id_film: "))
        titlu = input("titlu_film: ").strip()
        descriere = input("descriere_film: ").strip()
        gen = input("gen_film: ").strip()
        self.__srv_filme.modifica_film(id_film, titlu, descriere, gen, 0)

    def _ui_adauga_filme_random(self):
        try:
            nr_filme_de_generat = int(input("nr_filme: "))
        except:
            print("Numarul de filme este de tip intreg")
            return
        self.__srv_filme.adauga_filme_random(nr_filme_de_generat)

    def _ui_cauta_film(self):
        id_film = int(input("id_film: "))
        film = self.__srv_filme.cauta_film(id_film, 0)
        print(film)

    def _ui_toate_filmele(self):
        filme = self.__srv_filme.get_filme()
        if len(filme) == 0:
            print("NU exista filme!\n")
        for film in filme:
            print(film, '\n')

    def _ui_adauga_client(self):
        id_client = int(input("id_client: "))
        nume = input("nume_client: ").strip()
        prenume = input("prenume_client: ").strip()
        cnp = input("cnp_client: ").strip()
        self.__srv_clienti.adauga_client(id_client, nume, prenume, cnp)

    def _ui_stergere_client(self):
        id_client = int(input("id_client: "))
        self.__srv_clienti.sterge_client(id_client)

    def _ui_modifica_client(self):
        id_client = int(input("id_client: "))
        nume = input("nume_client: ")
        prenume = input("prenume_client: ")
        cnp = input("cnp_client: ")
        self.__srv_clienti.modifica_client(id_client, nume, prenume, cnp)

    def _ui_cauta_client(self):
        id_client = int(input("id_client: "))
        client = self.__srv_clienti.cauta_client(id_client)
        print(client)

    def _ui_toti_clientii(self):
        clienti = self.__srv_clienti.get_clienti()
        if len(clienti) == 0:
            print("NU exista clienti!\n")
        for client in clienti:
            print(client, '\n')

    def _ui_adauga_inchiriere(self):
        id_client = int(input("id_client: "))
        id_film = int(input("id_film: "))
        self.__srv_inchiriere.adauga_inchiriere(id_client, id_film)

    def _ui_modifica_inchiriere(self):
        id_client = int(input("id_client: "))
        self.__srv_inchiriere.modifica_inchiriere_dupa_client(id_client)

    def _ui_sterge_inchiriere(self):
        id_client = int(input("id_client: "))
        id_film = int(input("id_film: "))
        self.__srv_inchiriere.sterge_inchiriere(id_client, id_film)

    def _ui_ordoneaza_inchirieri_dupa_client(self):
        inchirieri = self.__srv_inchiriere.get_inchirieri()
        if len(inchirieri) == 0:
            print("NU exista inchirieri!\n")
            return
        copie_lista_inchirieri = self.__srv_inchiriere.ordoneaza_inchirieri_dupa_client()
        aparitii_client_in_lista = {}
        self.__srv_inchiriere.aparitii_client_in_lista_de_inchirieri(copie_lista_inchirieri, aparitii_client_in_lista)
        i = 0
        while i < len(copie_lista_inchirieri):
            print(copie_lista_inchirieri[i].get_nume() + ' ' + copie_lista_inchirieri[i].get_prenume() + ':')
            ap_client = aparitii_client_in_lista[copie_lista_inchirieri[i].get_id_client()]
            for j in range(i, i + ap_client):
                print('\t' + copie_lista_inchirieri[j].get_titlu() + ' ' + '[' + copie_lista_inchirieri[j].get_gen() + ']')
            i = i + ap_client

    def _ui_ordoneaza_inchirieri_dupa_nr_de_filme(self):
        inchirieri = self.__srv_inchiriere.get_inchirieri()
        if len(inchirieri) == 0:
            print("NU exista inchirieri!\n")
            return
        dictionar = {}
        copie_lista_inchirieri = self.__srv_inchiriere.ordoneaza_inchirieri_dupa_nr_de_filme(dictionar)
        for i in copie_lista_inchirieri:
            print(i, '\n')

    def _ui_ordoneaza_inchirieri_dupa_aparitia_filmelor(self):
        inchirieri = self.__srv_inchiriere.get_inchirieri()
        if len(inchirieri) == 0:
            print("NU exista inchirieri!\n")
            return
        dictionar = {}
        copie_lista_inchirieri = self.__srv_inchiriere.ordoneaza_inchirieri_dupa_aparitia_filmelor(dictionar)
        i = 0
        while i < len(copie_lista_inchirieri):
            if dictionar[copie_lista_inchirieri[i].get_titlu()] > 1:
             print("Filmul", copie_lista_inchirieri[i].get_titlu(), "a fost inchiriat de", dictionar[copie_lista_inchirieri[i].get_titlu()], "ori")
            else:
                print("Filmul", copie_lista_inchirieri[i].get_titlu(), "a fost inchiriat o singura data")
            i = i + dictionar[copie_lista_inchirieri[i].get_titlu()]

    def _ui_ordoneaza_inchirieri_dupa_aparitia_genului_de_filme(self):
        inchirieri = self.__srv_inchiriere.get_inchirieri()
        if len(inchirieri) == 0:
            print("NU exista inchirieri!\n")
            return
        dictionar = {}
        copie_lista_inchirieri = self.__srv_inchiriere.ordoneaza_inchirieri_dupa_aparitia_genului_de_filme(dictionar)
        cnt = 0
        top_3_filme = 3
        i = 0
        while i < len(copie_lista_inchirieri):
            if cnt == top_3_filme:
                break
            if dictionar[copie_lista_inchirieri[i].get_gen()] == 1:
                print("Filmele de", copie_lista_inchirieri[i].get_gen(), "au o singura inchiriere")
            elif dictionar[copie_lista_inchirieri[i].get_gen()] == 2:
                print("Filmele de", copie_lista_inchirieri[i].get_gen(), "au doua inchirieri")
            else:
             print("Filmele de", copie_lista_inchirieri[i].get_gen(), "au", dictionar[copie_lista_inchirieri[i].get_gen()], "inchirieri")
            i = i + dictionar[copie_lista_inchirieri[i].get_gen()]
            cnt += 1

    def _ui_primii_clienti(self):
        inchirieri = self.__srv_inchiriere.get_inchirieri()
        if len(inchirieri) == 0:
            print("NU exista inchirieri!\n")
            return
        dictionar = {}
        copie_lista_inchirieri = self.__srv_inchiriere.ordoneaza_inchirieri_dupa_nr_de_filme(dictionar)
        cnt = 0
        nr_clienti = int((3/10)*len(dictionar)) # primii 30% clienti
        i = 0
        while i < len(copie_lista_inchirieri):
            if nr_clienti == cnt:
                break
            if dictionar[copie_lista_inchirieri[i].get_id_client()] > 1:
                print("Clientul", copie_lista_inchirieri[i].get_nume(), copie_lista_inchirieri[i].get_prenume(), "a inchiriat", dictionar[copie_lista_inchirieri[i].get_id_client()], "filme")
            else:
                print("Clientul", copie_lista_inchirieri[i].get_nume(), copie_lista_inchirieri[i].get_prenume(), "a inchiriat un singur film")
            cnt += 1
            i = i + dictionar[copie_lista_inchirieri[i].get_id_client()]


    def _ui_toate_inchirierile(self):
        inchirieri = self.__srv_inchiriere.get_inchirieri()
        if len(inchirieri) == 0:
            print("NU exista inchirieri!\n")
        copie_lista_inchirieri = self.__srv_inchiriere.ordoneaza_inchirieri_dupa_client()
        aparitii_client_in_lista = {}
        self.__srv_inchiriere.aparitii_client_in_lista_de_inchirieri(copie_lista_inchirieri, aparitii_client_in_lista)
        for i in range(len(inchirieri)):
            if aparitii_client_in_lista[inchirieri[i].get_id_client()] != 0:
                poz = 0
                for j in range(len(copie_lista_inchirieri)):
                    if copie_lista_inchirieri[j].get_id_client() == inchirieri[i].get_id_client():
                        poz = j
                        break
                print(inchirieri[i].get_nume() + ' ' + inchirieri[i].get_prenume() + ':')
                capat = poz + aparitii_client_in_lista[inchirieri[i].get_id_client()]
                while poz < capat and poz < len(copie_lista_inchirieri):
                    print('\t' + copie_lista_inchirieri[poz].get_titlu() + ' ' + '[' + copie_lista_inchirieri[poz].get_gen() + ']')
                    poz += 1
                aparitii_client_in_lista[inchirieri[i].get_id_client()] = 0

    # def _ui_toate_inchirierile(self):
    #     inchirieri = self.__srv_inchiriere.get_inchirieri()
    #     for date in inchirieri:
    #         print(inchirieri)

    def run(self):
        # functie care executa comenzile introduse de catre utilizator
        ghid()
        while True:
            comanda = input(">>>").strip()
            if comanda == "exit":
                return
            if comanda == "":
                continue
            try:
                if comanda == "adauga_film":
                    self._ui_adauga_film()
                elif comanda == "sterge_film":
                    self._ui_stergere_film()
                elif comanda == "modifica_film":
                    self._ui_modifica_film()
                elif comanda == "cauta_film":
                    self._ui_cauta_film()
                elif comanda == "filme":
                    self._ui_toate_filmele()
                elif comanda == "adauga_client":
                    self._ui_adauga_client()
                elif comanda == "sterge_client":
                    self._ui_stergere_client()
                elif comanda == "modifica_client":
                    self._ui_modifica_client()
                elif comanda == "cauta_client":
                    self._ui_cauta_client()
                elif comanda == "clienti":
                    self._ui_toti_clientii()
                elif comanda == "inchiriaza_film":
                    self._ui_adauga_inchiriere()
                elif comanda == "ordoneaza_inchirieri_dupa_nume":
                    self._ui_ordoneaza_inchirieri_dupa_client()
                elif comanda == "ordoneaza_inchirieri_dupa_filme":
                    self._ui_ordoneaza_inchirieri_dupa_nr_de_filme()
                elif comanda == "ordoneaza_inchirieri_dupa_aparitii":
                    self._ui_ordoneaza_inchirieri_dupa_aparitia_filmelor()
                elif comanda == "top_3_filme_dupa_gen":
                    self._ui_ordoneaza_inchirieri_dupa_aparitia_genului_de_filme()
                elif comanda == "primii_clienti":
                    self._ui_primii_clienti()
                elif comanda == "returneaza_film":
                    self._ui_sterge_inchiriere()
                elif comanda == "modifica_inchiriere":
                    self._ui_modifica_inchiriere()
                elif comanda == "inchirieri":
                    self._ui_toate_inchirierile()
                elif comanda == "genereaza_filme":
                    self._ui_adauga_filme_random()
                elif comanda == "exit":
                    exit()
                else:
                    print("comanda invalida")
            except ValidationError as ve:
                print(ve)
            except RepositoryError as re:
                print(re)
            except ValueError:
                print("Id-ul trebuie sa fie intreg!\n")
