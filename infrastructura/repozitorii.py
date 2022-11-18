import random
import string
# from domain.entitati import Film, Client, Inchiriere
from erori.exceptii import *
from business.servicii import *

class RepoFilme(object):

    def __init__(self):
        # metoda speciala care creeaza lista de filme (constructor)
        self._filme = []

    def __len__(self):
        # functie care supraincarca lungimea listei de filme
        return len(self._filme)

    def adauga_film(self, film):
        """
        :param film: Film
        functie care adauga un film in lista de filme sau arunca o exceptie
        in cazul in care filmul care se doreste a fi adaugat exista deja in lista (se verifica existenta filmului in lista
        in functie de id)
        """
        for f in self._filme:
            if f == film:
                raise RepositoryError("id-ul filmului este existent\n")
        self._filme.append(film)



    def gaseste_dupa_id_film(self, id_film, poz):
        """
        FUNCTIE RECURSIVA
        :param id_film: intreg >= 0
        :return: film
        sau se arunca o exceptie(repoexception) daca id-ul introdus nu se regaseste in lista de filme
        """
        if poz == len(self._filme):
            raise RepositoryError("id-ul filmului este inexistent\n")
        if self._filme[poz].get_id_film() == id_film:
            return self._filme[poz]
        return self.gaseste_dupa_id_film(id_film, poz + 1)

    def sterge_film(self, id_film):
        """
        :param id_film: intreg >= 0
        :return: None
        sau se arunca o exceptie (repoexception) daca filmul care se vrea a fi sters nu exista in lista de filme
        """
        for i in range(len(self._filme)):
            if self._filme[i].get_id_film() == id_film:
                del self._filme[i]
                return
        raise RepositoryError("filmul de sters nu exista")

    def modifica_film(self, film, poz):
        """
        FUNCTIE RECURSIVA
        functie care modifica un film care se regaseste in lista cu un alt film sau care arunca o exceptie
        in cazul in care filmul care se doreste a fi modificat nu exista in lista de filme
        :param film: Film
        :return: None
        sau se arunca o exceptie
        """
        if poz == len(self._filme):
            raise RepositoryError("filmul pe care doriti sa il modificati nu exista")
        if self._filme[poz] == film:
            self._filme[poz] = film
            return
        return self.modifica_film(film, poz + 1)


    def genereaza_filme(self, nr_filme_de_generat):
            """
            functie care genereaza campuri random pentru un Film (titlu random, descriere random, gen random)
            si creeaza o lista formata din 3 elemente care va contine acele campuri
            :return: lista
            """
            if nr_filme_de_generat > 1001:
                raise RepositoryError("Nu se pot genera " + str(nr_filme_de_generat) + " filme")

            for j in range(nr_filme_de_generat):
                lista = []
                while True:
                    cnt = 0
                    for film in self._filme:
                        if film.get_id_film() >= 0 and film.get_id_film() <= 1000:
                            cnt += 1
                    if cnt == 1001:
                       print("Toate id-urile din interval au fost generate si se afla in lista")
                       return

                    nu_exista_id_in_lista = True
                    id_film = random.randint(0, 1000)
                    for film in self._filme:
                        if film.get_id_film() == id_film:
                            nu_exista_id_in_lista = False
                            break
                    if nu_exista_id_in_lista == True:
                        lista.append(id_film)
                        break

                for i in range(3):
                    lungime_string = random.randint(1, 5)
                    # lungimea sirului generat va di determinata de lungimea numarului generat random
                    cifre = string.digits + string.ascii_lowercase  # se vor genera caractere random
                    random_string = ""  # acesta va fi sirul format din cifre random
                    for i in range(lungime_string):
                        random_string += random.choice(cifre)  # se construieste sirul
                    if i == 0:
                        titlu = random_string
                        lista.append(titlu)
                    elif i == 1:
                        descriere = random_string
                        lista.append(descriere)
                    else:
                        gen = random_string
                        lista.append(gen)

                film = Film(lista[0], str(lista[1]), str(lista[2]), str(lista[3]))
                self._filme.append(film)


    def get_all_filme(self):
        # functie care returneaza lista de filme
        return self._filme


class FileRepoFilme(RepoFilme):
    def __init__(self, file_path):
        """
        metoda speciala care apeleaza metoda de pe clasa RepoFilme si salveaza locatia fisierului
        intr-o variabila privata
        :param file_path: filme.txt
        """
        RepoFilme.__init__(self)
        self.__file_path = file_path


    def __read_all_from_file_filme(self):
        """
        functie care citeste filme din fisier, sparge campurile filmelor dupa ','
        si adauga filme in lista de filme
        :return: None
        """
        with(open(self.__file_path, 'r')) as f:
            self._filme = []
            linii = f.readlines()
            for linie in linii:
                linie = linie.strip()
                if len(linie) > 0:
                    parts = linie.split(',')
                    id_film = int(parts[0])
                    titlu = parts[1]
                    descriere = parts[2]
                    gen = parts[3]
                    film = Film(id_film, titlu, descriere, gen)
                    self._filme.append(film)


    def __write_all_to_file_filme(self):
        """
        functie care parcurge lista de filme din memorie si suprascrie filmele care se afla in fisier
        cu filmele care se afla la momentul actual in lista de filme din memorie
        :return: None
        """
        with(open(self.__file_path, 'w')) as f:
            for film in self._filme:
                f.write(f"{film.get_id_film()},{film.get_titlu()},{film.get_descriere()},{film.get_gen()}\n")

    def __append_to_file_filme(self, film):
        """
        functie care adauga la finalul fisierului un nou film
        :param film: Film
        :return: None
        """
        with(open(self.__file_path, 'a')) as f:
            f.write(f"{film.get_id_film()},{film.get_titlu()},{film.get_descriere()},{film.get_gen()}\n")



    def __len__(self):
        self.__read_all_from_file_filme()
        return len(self._filme)

    def adauga_film(self, film):
        self.__read_all_from_file_filme()
        RepoFilme.adauga_film(self, film)
        self.__append_to_file_filme(film)

    def genereaza_filme(self, nr_filme_de_generat):
        self.__read_all_from_file_filme()
        RepoFilme.genereaza_filme(self, nr_filme_de_generat)
        self.__write_all_to_file_filme()

    def sterge_film(self, id_film):
        self.__read_all_from_file_filme()
        RepoFilme.sterge_film(self, id_film)
        self.__write_all_to_file_filme()

    def modifica_film(self, film, poz):
        self.__read_all_from_file_filme()
        RepoFilme.modifica_film(self, film, poz)
        self.__write_all_to_file_filme()

    def gaseste_dupa_id_film(self, id_film, poz):
        self.__read_all_from_file_filme()
        return RepoFilme.gaseste_dupa_id_film(self, id_film, poz)

    def get_all_filme(self):
        self.__read_all_from_file_filme()
        return RepoFilme.get_all_filme(self)


class RepoClienti(object):

    def __init__(self):
        # metoda speciala care creeaza lista de clienti (constructor)
        self._clienti = []

    def __len__(self):
        # functie care supraincarca lungimea listei de clienti
        return len(self._clienti)

    def adauga_client(self, client):
        """
        functie care adauga un client in lista de clienti daca id-ul si cnp-ul clientului care se vrea adaugat nu exista
        deja in lista, sau care arunca o exceptie in caz contrar
        :param client: Client
        :return: None
        """
        for c in self._clienti:
            if c == client:
                exceptii = ""
                if c.get_id_client() == client.get_id_client():
                    exceptii += "id-ul clientului este existent\n"
                if c.get_cnp() == client.get_cnp():
                    exceptii += "cnp-ul clientului este existent\n"
                raise RepositoryError(exceptii)
        self._clienti.append(client)

    def gaseste_dupa_id_client(self, id_client):
        """
        :param id_client: intreg >= 0
        :return: id_client sau None daca s-a aruncat o exceptie
        """

        for client in self._clienti:
            if client.get_id_client() == id_client:
                return client
        raise RepositoryError("id-ul clientului este inexistent\n")

    def sterge_client(self, id_client):
        """
        functie care cauta in lista un client dupa un id
        daca id-ul introdus corespunde unui client din lista clientul va fi sters, iar in caz
        contrar se va arunca o exceptie
        :param id_client: intreg >= 0
        :return:
        """
        for i in range(len(self._clienti)):
            if self._clienti[i].get_id_client() == id_client:
                del self._clienti[i]
                return
        raise RepositoryError("clientul de sters nu exista")

    def modifica_client(self, client):
        """
        functie care modifica un client care se regaseste in lista cu un alt client sau care arunca o exceptie
        in cazul in care clientul care se doreste a fi modificat nu exista in lista de clienti
        :param client: Client
        :return: None
        sau se arunca o exceptie
        """
        for i in range(len(self._clienti)):
            if self._clienti[i] == client:
                if self._clienti[i].get_id_client() == client.get_id_client() and self._clienti[i].get_cnp() == client.get_cnp():
                    self._clienti[i] = client
                    return
        raise RepositoryError("clientul pe care doriti sa il modificati nu exista")

    def get_all_clienti(self):
        # functie care returneaza lista de clienti
        return self._clienti


class FileRepoClienti(RepoClienti):
    def __init__(self, file_path):
        """
        metoda speciala care apeleaza metoda de pe clasa RepoClienti si salveaza locatia fisierului
        intr-o variabila privata
        :param file_path: clienti.txt
        """
        RepoClienti.__init__(self)
        self.__file_path = file_path


    def __read_all_from_file_clienti(self):
        """
        functie care citeste clienti din fisier, sparge campurile clientilor dupa ','
        si adauga clienti in lista de clienti
        :return: None
        """
        with(open(self.__file_path, 'r')) as f:
            self._clienti = []
            linii = f.readlines()
            for linie in linii:
                linie = linie.strip()
                if len(linie) > 0:
                    parts = linie.split(',')
                    id_client = int(parts[0])
                    nume = parts[1]
                    prenume = parts[2]
                    cnp = parts[3]
                    client = Client(id_client, nume, prenume, cnp)
                    self._clienti.append(client)


    def __write_all_to_file_clienti(self):
        """
        functie care parcurge lista de clienti din memorie si suprascrie clientii care se afla in fisier
        cu clientii care se afla la momentul actual in lista de clienti din memorie
        :return: None
        """
        with(open(self.__file_path, 'w')) as f:
            for client in self._clienti:
                f.write(f"{client.get_id_client()},{client.get_nume()},{client.get_prenume()},{client.get_cnp()}\n")

    def __append_to_file_clienti(self, client):
        """
        functie care adauga la finalul fisierului un nou client
        :param client: Client
        :return: None
        """
        with(open(self.__file_path, 'a')) as f:
            f.write(f"{client.get_id_client()},{client.get_nume()},{client.get_prenume()},{client.get_cnp()}\n")

    def __len__(self):
        self.__read_all_from_file_clienti()
        return len(self._clienti)

    def adauga_client(self, client):
        self.__read_all_from_file_clienti()
        RepoClienti.adauga_client(self, client)
        self.__append_to_file_clienti(client)


    def sterge_client(self, id_client):
        self.__read_all_from_file_clienti()
        RepoClienti.sterge_client(self, id_client)
        self.__write_all_to_file_clienti()

    def modifica_client(self, client):
        self.__read_all_from_file_clienti()
        RepoClienti.modifica_client(self, client)
        self.__write_all_to_file_clienti()

    def gaseste_dupa_id_client(self, id_client):
        self.__read_all_from_file_clienti()
        return RepoClienti.gaseste_dupa_id_client(self, id_client)


    def get_all_clienti(self):
        self.__read_all_from_file_clienti()
        return RepoClienti.get_all_clienti(self)


class RepoInchirieri(object):

    def __init__(self):
        # metoda speciala care creeaza lista de inchirieri(constructor)
        self._inchirieri = []

    def __len__(self):
        # functie care supraincarca lungimea listei de inchirieri
        return len(self._inchirieri)

    def sterge_inchiriere(self, id_client, id_film):
        """
        :param id_client: intreg >= 0
        :param id_film: intreg >= 0
        :return: None
        functie care sterge o inchiriere din lista de inchirieri in cazul in care id-ul clientului si id-ul filmului
        introduse de catre utilizator coincid cu unul dintre acelea din lista de inchirieri
        """
        for i in range(len(self._inchirieri)):
            if self._inchirieri[i].get_id_film() == id_film and self._inchirieri[i].get_id_client() == id_client:
                # de la linia 383 la 387 am modificat
                repo = RepoFilme()
                filme = repo.get_all_filme()
                for film in filme:
                    if film.get_id_film() == self._inchirieri[i]:
                        all_filme.remove(film)
                del self._inchirieri[i]
                return
        for i in range(len(self._inchirieri)):
            if self._inchirieri[i].get_id_film() == id_film and self._inchirieri[i].get_id_client() != id_client:
                    raise RepositoryError("id-ul clientului este inexistent")
            elif self._inchirieri[i].get_id_film() != id_film and self._inchirieri[i].get_id_client() == id_client:
                    raise RepositoryError("id-ul filmului este inexistent")
        raise RepositoryError("id-ul clientului este inexistent\nid-ul filmului este inexistent")

    def inchiriaza_film(self, inchiriere):
        """
        :param inchiriere: Inchiriere
        :return: None
        functie care adauga o inchiriere in lista de inchirieri
        """
        # de la linia 404 pana la 409 am modificat
        repo = RepoFilme()
        filme = repo.get_all_filme()
        for film in filme:
            if film.get_id_film() == inchiriere.get_id_film():
                all_filme.append(film)
                break
        self._inchirieri.append(inchiriere)

    def gaseste_inchiriere_dupa_id_film(self, id_film):
        """
        functie care arunca o exceptie in cazul in care id-ul filmului introdus exista deja in lista de inchirieri
        sau returneaza None in caz contrar
        :param id_film: intreg >= 0
        :return: None
        """
        for i in self._inchirieri:
           if i.get_id_film() == id_film:
                raise RepositoryError("id-ul filmului pe care doriti sa il inchiriati este existent in lista de inchirieri\n")

    def modifica_inchiriere_dupa_client(self, id_client, client):
        """
        functie care modifica o inchiriere dupa client in cazul in care clientul si-a schimbat cel putin unul dintre
        campurile nume, prenume
        :param id_client: intreg >= 0
        :param client: Client
        :return: None
        """
        ok = 0
        for i in range(len(self._inchirieri)):
            if self._inchirieri[i].get_id_client() == id_client:
                self._inchirieri[i].set_nume(client.get_nume())
                self._inchirieri[i].set_prenume(client.get_prenume())
                ok = 1
        if ok == 0:
            raise RepositoryError("clientul pe care doriti sa il modificati nu exista in lista de inchirieri")

    def get_all_inchirieri(self):
        """
        functie care returneaza lista de inchirieri
        :return: self.__inchirieri
        """
        return self._inchirieri

class FileRepoInchirieri(RepoInchirieri):
    def __init__(self, file_path_inchirieri):
        """
        metoda speciala care apeleaza metoda de pe clasa RepoInchirieri si salveaza locatia fisierului
        intr-o variabila privata
        :param file_path_inchirieri: inchirieri.txt
        """
        RepoInchirieri.__init__(self)
        self.__file_path_inchirieri = file_path_inchirieri

    def __read_all_from_file_inchirieri(self):
        """
        functie care citeste inchirieri din fisier, sparge campurile inchirierilor dupa ','
        si adauga inchirieri in lista de inchirieri
        :return: None
        """
        with(open(self.__file_path_inchirieri, 'r')) as f:
            self._inchirieri = []
            linii = f.readlines()
            for linie in linii:
                linie = linie.strip()
                if len(linie) > 0:
                    parts = linie.split(',')
                    id_film = int(parts[0])
                    id_client = int(parts[1])
                    titlu_film = parts[2]
                    gen_film = parts[3]
                    nume_client = parts[4]
                    prenume_client = parts[5]
                    inchiriere = Inchiriere(id_film, titlu_film, gen_film, id_client, nume_client, prenume_client)
                    self._inchirieri.append(inchiriere)

    def __write_all_to_file_inchirieri(self):
        """
        functie care parcurge lista de inchirieri din memorie si suprascrie inchirierile care se afla in fisier
        cu inchirierile care se afla la momentul actual in lista de inchirieri din memorie
        :return: None
        """
        with(open(self.__file_path_inchirieri, 'w')) as f:
            for inchiriere in self._inchirieri:
                f.write(f"{inchiriere.get_id_film()},{inchiriere.get_id_client()},{inchiriere.get_titlu()},{inchiriere.get_gen()},{inchiriere.get_nume()},{inchiriere.get_prenume()}\n")

    def __append_to_file_inchirieri(self, inchiriere):
        """
        functie care adauga la finalul fisierului o noua inchiriere
        :param inchiriere: Inchiriere
        :return: None
        """
        with(open(self.__file_path_inchirieri, 'a')) as f:
            f.write(f"{inchiriere.get_id_film()},{inchiriere.get_id_client()},{inchiriere.get_titlu()},{inchiriere.get_gen()},{inchiriere.get_nume()},{inchiriere.get_prenume()}\n")

    def __len__(self):
        self.__read_all_from_file_inchirieri()
        return len(self._inchirieri)

    def inchiriaza_film(self, inchiriere):
        self.__read_all_from_file_inchirieri()
        RepoInchirieri.inchiriaza_film(self, inchiriere)
        self.__append_to_file_inchirieri(inchiriere)


    def sterge_inchiriere(self, id_client, id_film):
        self.__read_all_from_file_inchirieri()
        RepoInchirieri.sterge_inchiriere(self, id_client, id_film)
        self.__write_all_to_file_inchirieri()

    def modifica_inchiriere_dupa_client(self, id_client, client):
        self.__read_all_from_file_inchirieri()
        RepoInchirieri.modifica_inchiriere_dupa_client(self, id_client, client)
        self.__write_all_to_file_inchirieri()

    def gaseste_inchiriere_dupa_id_film(self, id_film):
        self.__read_all_from_file_inchirieri()
        return RepoInchirieri.gaseste_inchiriere_dupa_id_film(self, id_film)


    def get_all_inchirieri(self):
        self.__read_all_from_file_inchirieri()
        return RepoInchirieri.get_all_inchirieri(self)

