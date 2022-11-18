import unittest
from validare.validator import *
from infrastructura.repozitorii import *
from business.servicii import *
class Teste(unittest.TestCase):

    def test_creeaza_film(self):
        id_film = 15
        titlu = "predators"
        descriere = "18+"
        gen = "actiune"
        film = Film(id_film, titlu, descriere, gen)
        self.assertEqual(film.get_id_film(), id_film)
        self.assertEqual(film.get_titlu(), titlu)
        self.assertEqual(film.get_descriere(), descriere)
        self.assertEqual(film.get_gen(), gen)
        alta_descriere = "15+"
        alt_gen = "aventura"
        alt_film = Film(id_film, titlu, alta_descriere, alt_gen)
        self.assertEqual(film, alt_film)
        self.assertTrue(film.__eq__(alt_film))
        self.assertEqual(str(film), "[15,predators,18+,actiune]")
        self.assertEqual(film.__str__(), "[15,predators,18+,actiune]")


    def test_valideaza_film(self):
        id_film = 15
        titlu = "predators"
        descriere = "18+"
        gen = "actiune"
        film = Film(id_film, titlu, descriere, gen)
        valid = ValidatorFilm()
        valid.valideaza(film)
        id_invalid = -3
        titlu_invalid = ""
        descriere_invalida = ""
        gen_invalid = ""
        id_film_invalid = Film(id_invalid, titlu, descriere, gen)
        film_invalid = Film(id_invalid, titlu_invalid, descriere_invalida, gen_invalid)
        with self.assertRaises(ValidationError) as ve:
            valid.valideaza(id_film_invalid)
        self.assertEqual(str(ve.exception), "id-ul este invalid\n")
        with self.assertRaises(ValidationError) as ve:
            valid.valideaza(film_invalid)
        self.assertEqual(str(ve.exception), "id-ul este invalid\ntitlul este invalid\ndescrierea este invalida\ngenul este invalid\n")

    def test_adauga_film_repo(self):
        with open("test_filme.txt", 'w') as f:
            f.write("")
        repo = FileRepoFilme("test_filme.txt")
        self.assertEqual(len(repo), 0)
        self.assertEqual(repo.__len__(), 0)
        id_film = 15
        titlu = "predators"
        descriere = "18+"
        gen = "actiune"
        film = Film(id_film, titlu, descriere, gen)
        repo.adauga_film(film)
        self.assertEqual(len(repo), 1)
        film_gasit = repo.gaseste_dupa_id_film(id_film, 0)
        self.assertEqual(film_gasit, film)
        self.assertEqual(film_gasit.get_titlu(), film.get_titlu())
        self.assertEqual(film_gasit.get_descriere(), film.get_descriere())
        self.assertEqual(film_gasit.get_gen(), film.get_gen())
        all = repo.get_all_filme()
        self.assertEqual(all[0], film)
        self.assertEqual(all[0].get_titlu(), film.get_titlu())
        self.assertEqual(all[0].get_descriere(), film.get_descriere())
        self.assertEqual(all[0].get_gen(), film.get_gen())
        id_film_inexistent = 35
        with self.assertRaises(RepositoryError) as re:
            repo.gaseste_dupa_id_film(id_film_inexistent, 0)
        self.assertEqual(str(re.exception), "id-ul filmului este inexistent\n")
        alt_titlu = "hobbit"
        alta_descriere = "12"
        alt_gen = "aventura"
        same_id_film = Film(id_film, alt_titlu, alta_descriere, alt_gen)
        with self.assertRaises(RepositoryError) as re:
            repo.adauga_film(same_id_film)
        self.assertEqual(str(re.exception), "id-ul filmului este existent\n")

    def test_adauga_film_service(self):
        repo_filme = RepoFilme()
        valid = ValidatorFilm()
        srv = ServiceFilme(valid, repo_filme)
        id_film = 15
        titlu = "predators"
        descriere = "18+"
        gen = "actiune"
        self.assertEqual(srv.get_nr_filme(), 0)
        srv.adauga_film(id_film, titlu, descriere, gen)
        self.assertEqual(srv.get_nr_filme(), 1)
        alt_titlu = "titanic"
        alta_descriere = "15"
        alt_gen = "drama"
        with self.assertRaises(RepositoryError) as re:
            srv.adauga_film(id_film, alt_titlu, alta_descriere, alt_gen)
        self.assertEqual(str(re.exception), "id-ul filmului este existent\n")
        id_invalid = -3
        titlu_invalid = ""
        descriere_invalida = ""
        gen_invalid = ""
        with self.assertRaises(ValidationError) as ve:
            srv.adauga_film(id_invalid, titlu_invalid, descriere_invalida, gen_invalid)
        self.assertEqual(str(ve.exception), "id-ul este invalid\ntitlul este invalid\ndescrierea este invalida\ngenul este invalid\n")

    def test_sterge_film_repo(self):
        # black box testing - testele se fac dupa specificatiile din metoda de stergere din repo
        with open("test_filme.txt", 'w') as f:
            f.write("")
        repo = FileRepoFilme("test_filme.txt")
        self.assertEqual(len(repo), 0)
        self.assertEqual(repo.__len__(), 0)
        id_film = 2
        titlu = "f1"
        descriere = "super"
        gen = "aventura"
        film = Film(id_film, titlu, descriere, gen)
        repo.adauga_film(film)
        self.assertEqual(len(repo), 1)
        self.assertEqual(repo.__len__(), 1)
        id_inexistent = 3
        with self.assertRaises(RepositoryError) as re:
            repo.sterge_film(id_inexistent)
        self.assertEqual(str(re.exception), "filmul de sters nu exista")
        id_invalid = -5
        film = Film(id_invalid, titlu, descriere, gen)
        valid = ValidatorFilm()
        with self.assertRaises(ValidationError) as ve:
            valid.valideaza(film)
        self.assertEqual(str(ve.exception), "id-ul este invalid\n")
        self.assertIsNone(repo.sterge_film(id_film))
        self.assertEqual(len(repo), 0)
        self.assertEqual(repo.__len__(), 0)
        with self.assertRaises(RepositoryError) as re:
            repo.sterge_film(id_film)
        self.assertEqual(str(re.exception), "filmul de sters nu exista")

    def test_sterge_film_service(self):
        repo = RepoFilme()
        valid = ValidatorFilm()
        srv = ServiceFilme(valid, repo)
        id_film = 1
        with self.assertRaises(RepositoryError) as re:
            srv.sterge_film(id_film)
        self.assertEqual(str(re.exception), "filmul de sters nu exista")
        id_film = 2
        titlu = "add"
        descriere = "interesant"
        gen = "documentar"
        self.assertEqual(srv.get_nr_filme(), 0)
        srv.adauga_film(id_film, titlu, descriere, gen)
        self.assertEqual(srv.get_nr_filme(), 1)
        srv.sterge_film(id_film)
        self.assertEqual(srv.get_nr_filme(), 0)

    def test_modifica_film_repo(self):
        with open("test_filme.txt", 'w') as f:
            f.write("")
        repo = FileRepoFilme("test_filme.txt")
        self.assertEqual(len(repo), 0)
        self.assertEqual(repo.__len__(), 0)
        id_film = 2
        titlu = "home"
        descriere = "dragut"
        gen = "comedie"
        film = Film(id_film, titlu, descriere, gen)
        repo.adauga_film(film)
        alt_titlu = "platoon"
        alta_descriere = "superb"
        alt_gen = "drama"
        alt_film = Film(id_film, alt_titlu, alta_descriere, alt_gen)
        repo.modifica_film(alt_film, 0)
        all = repo.get_all_filme()
        self.assertEqual(all[0], alt_film)
        self.assertEqual(all[0].get_titlu(), alt_titlu)
        self.assertEqual(all[0].get_descriere(), alta_descriere)
        self.assertEqual(all[0].get_gen(), alt_gen)
        alt_id = 3
        film_cu_alt_id = Film(alt_id, titlu, descriere, gen)
        with self.assertRaises(RepositoryError) as re:
            repo.modifica_film(film_cu_alt_id, 0)
        self.assertEqual(str(re.exception), "filmul pe care doriti sa il modificati nu exista")

    def test_modifica_film_service(self):
        repo = RepoFilme()
        valid = ValidatorFilm()
        srv = ServiceFilme(valid, repo)
        id_film = 3
        titlu_film = "4dd"
        descriere_film = "sdd"
        gen_film = "actiune"
        self.assertEqual(srv.get_nr_filme(), 0)
        with self.assertRaises(RepositoryError) as re:
            srv.modifica_film(id_film, titlu_film, descriere_film, gen_film, 0)
        self.assertEqual(str(re.exception), "filmul pe care doriti sa il modificati nu exista")
        srv.adauga_film(id_film, titlu_film, descriere_film, gen_film)
        self.assertEqual(srv.get_nr_filme(), 1)
        alt_titlu_film = "once"
        alta_descriere_film = "frumos"
        alt_gen_film = "actiune"
        srv.modifica_film(id_film, alt_titlu_film, alta_descriere_film, alt_gen_film, 0)
        self.assertEqual(srv.get_nr_filme(), 1)
        all = srv.get_filme()
        self.assertEqual(all[0].get_id_film(), id_film)
        self.assertEqual(all[0].get_titlu(), alt_titlu_film)
        self.assertEqual(all[0].get_descriere(), alta_descriere_film)
        self.assertEqual(all[0].get_gen(), alt_gen_film)

    def test_cauta_film(self):
        with open("test_filme.txt", 'w') as f:
            f.write("")
        repo = FileRepoFilme("test_filme.txt")
        id_film = 3
        titlu = "win"
        descriere = "frumos"
        gen = "aventura"
        film = Film(id_film, titlu, descriere, gen)
        repo.adauga_film(film)
        self.assertEqual(repo.gaseste_dupa_id_film(id_film, 0), film)
        alt_id = 6
        with self.assertRaises(RepositoryError) as re:
            repo.gaseste_dupa_id_film(alt_id, 0)
        self.assertEqual(str(re.exception), "id-ul filmului este inexistent\n")

    def test_inchiriaza_film_repo(self):
        with open("test_inchirieri.txt", 'w') as f:
            f.write("")
        repo = FileRepoInchirieri("test_inchirieri.txt")
        self.assertEqual(len(repo), 0)
        id_film = 1
        titlu = "home"
        gen = "comedie"
        id_client = 10
        nume = "moise"
        prenume = "marius"
        inchiriere = Inchiriere(id_film, titlu, gen, id_client, nume, prenume)
        repo.inchiriaza_film(inchiriere)
        self.assertEqual(inchiriere.__str__(), "Clientul moise marius care are id-ul 10 a inchiriat filmul home care are id-ul 1")
        self.assertEqual(len(repo), 1)
        id_film = 2
        titlu = "taz"
        gen = "actiune"
        id_client = 11
        nume = "vincetiu"
        prenume = "ionut"
        inchiriere = Inchiriere(id_film, titlu, gen, id_client, nume, prenume)
        repo.inchiriaza_film(inchiriere)
        self.assertEqual(len(repo), 2)
        titlu = "titanic"
        gen = "actiune"
        id_client = 12
        nume = "mihaila"
        prenume = "andrei"
        inchiriere = Inchiriere(id_film, titlu, gen, id_client, nume, prenume)
        with self.assertRaises(RepositoryError) as re:
            repo.gaseste_inchiriere_dupa_id_film(id_film)
            repo.inchiriaza_film(inchiriere)
        self.assertEqual(str(re.exception), "id-ul filmului pe care doriti sa il inchiriati este existent in lista de inchirieri\n")

    def test_adauga_inchiriere_service(self):
        repo_f = RepoFilme()
        repo_c = RepoClienti()
        repo_i = RepoInchirieri()
        valid_f = ValidatorFilm()
        valid_c = ValidatorClient()
        valid_i = ValidatorID()
        srv_f = ServiceFilme(valid_f, repo_f)
        srv_c = ServiceClienti(valid_c, repo_c)
        srv_i = ServiceInchirieri(valid_i, repo_f, repo_c, repo_i)
        id_film = 1
        titlu = "daf"
        descriere = "frumos"
        gen = "comedie"
        self.assertEqual(srv_f.get_nr_filme(), 0)
        srv_f.adauga_film(id_film, titlu, descriere, gen)
        self.assertEqual(srv_f.get_nr_filme(), 1)
        alt_id_film = 3
        alt_titlu = "terra"
        alta_descriere = "interesant"
        alt_gen = "documentar"
        srv_f.adauga_film(alt_id_film, alt_titlu, alta_descriere, alt_gen)
        self.assertEqual(srv_f.get_nr_filme(), 2)
        id_client = 10
        nume = "ionel"
        prenume = "bogdan"
        cnp = "1234567890123"
        self.assertEqual(srv_c.get_nr_clienti(), 0)
        srv_c.adauga_client(id_client, nume, prenume, cnp)
        self.assertEqual(srv_c.get_nr_clienti(), 1)
        self.assertEqual(srv_i.get_nr_inchirieri(), 0)
        srv_i.adauga_inchiriere(id_client, id_film)
        self.assertEqual(srv_i.get_nr_inchirieri(), 1)
        self.assertEqual(srv_f.get_nr_filme(), 1)
        id_film_existent = 1
        with self.assertRaises(RepositoryError) as re:
            srv_i.adauga_inchiriere(id_client, id_film_existent)
        self.assertEqual(str(re.exception), "id-ul filmului pe care doriti sa il inchiriati este existent in lista de inchirieri\n")
        srv_i.adauga_inchiriere(id_client, alt_id_film)
        self.assertEqual(srv_i.get_nr_inchirieri(), 2)
        self.assertEqual(srv_f.get_nr_filme(), 0)

    def test_sterge_inchiriere_repo(self):
        with open("test_inchirieri.txt", 'w') as f:
            f.write("")
        repo_i = FileRepoInchirieri("test_inchirieri.txt")
        id_film = 2
        titlu = "taz"
        gen = "aventura"
        id_client = 10
        nume = "vincetiu"
        prenume = "ionut"
        inchiriere = Inchiriere(id_film, titlu, gen, id_client, nume, prenume)
        repo_i.inchiriaza_film(inchiriere)
        alt_id_film = 1
        alt_titlu = "home"
        alt_gen = "actiune"
        alt_id_client = 10
        alt_nume = "moise"
        alt_prenume = "marius"
        inchiriere = Inchiriere(alt_id_film, alt_titlu, alt_gen, alt_id_client, alt_nume, alt_prenume)
        repo_i.inchiriaza_film(inchiriere)
        self.assertEqual(len(repo_i), 2)
        repo_i.sterge_inchiriere(id_client, id_film)
        self.assertEqual(len(repo_i), 1)

    def test_sterge_inchiriere_service(self):
        repo_f = RepoFilme()
        repo_c = RepoClienti()
        repo_i = RepoInchirieri()
        valid_f = ValidatorFilm()
        valid_c = ValidatorClient()
        valid_i = ValidatorID()
        srv_f = ServiceFilme(valid_f, repo_f)
        srv_c = ServiceClienti(valid_c, repo_c)
        srv_i = ServiceInchirieri(valid_i, repo_f, repo_c, repo_i)
        id_film = 1
        titlu = "daf"
        descriere = "frumos"
        gen = "comedie"
        self.assertEqual(srv_f.get_nr_filme(), 0)
        srv_f.adauga_film(id_film, titlu, descriere, gen)
        self.assertEqual(srv_f.get_nr_filme(), 1)
        alt_id_film = 2
        alt_titlu = "time"
        alta_descriere = "captivant"
        alt_gen = "aventura"
        srv_f.adauga_film(alt_id_film, alt_titlu, alta_descriere, alt_gen)
        self.assertEqual(srv_f.get_nr_filme(), 2)
        id_client = 10
        nume = "andi"
        prenume = "dobrin"
        cnp = "1230894560123"
        self.assertEqual(srv_c.get_nr_clienti(), 0)
        srv_c.adauga_client(id_client, nume, prenume, cnp)
        self.assertEqual(srv_c.get_nr_clienti(), 1)
        self.assertEqual(srv_i.get_nr_inchirieri(), 0)
        srv_i.adauga_inchiriere(id_client, alt_id_film)
        self.assertEqual(srv_i.get_nr_inchirieri(), 1)
        self.assertEqual(srv_f.get_nr_filme(), 1)
        srv_i.adauga_inchiriere(id_client, id_film)
        self.assertEqual(srv_i.get_nr_inchirieri(), 2)
        self.assertEqual(srv_f.get_nr_filme(), 0)
        srv_i.sterge_inchiriere(id_client, id_film)
        self.assertEqual(srv_i.get_nr_inchirieri(), 1)
        self.assertEqual(srv_f.get_nr_filme(), 1)
        id_client_inexistent_in_inchirieri = 12
        with self.assertRaises(RepositoryError) as re:
            srv_i.sterge_inchiriere(id_client_inexistent_in_inchirieri, alt_id_film)
        self.assertEqual(str(re.exception), "id-ul clientului este inexistent")
        id_film_inexistent_in_inchirieri = 25
        with self.assertRaises(RepositoryError) as re:
            srv_i.sterge_inchiriere(id_client_inexistent_in_inchirieri, id_film_inexistent_in_inchirieri)
        self.assertEqual(str(re.exception), "id-ul clientului este inexistent\nid-ul filmului este inexistent")
    all_filme = []

    def test_ordoneaza_inchirieri_dupa_client_service(self):
        repo_f = RepoFilme()
        repo_c = RepoClienti()
        repo_i = RepoInchirieri()
        valid_i = ValidatorID()
        srv_i = ServiceInchirieri(valid_i, repo_f, repo_c, repo_i)
        copie_lista_goala_inchirieri = srv_i.ordoneaza_inchirieri_dupa_client()
        self.assertEqual(copie_lista_goala_inchirieri, [])
        self.assertEqual(srv_i.get_nr_inchirieri(), 0)
        inchiriere = Inchiriere(1, "prison", "actiune", 10, "andi", "marian")
        repo_i.inchiriaza_film(inchiriere)
        self.assertEqual(srv_i.get_nr_inchirieri(), 1)
        inchiriere = Inchiriere(2, "home", "aventura", 11, "marius", "ionut")
        repo_i.inchiriaza_film(inchiriere)
        self.assertEqual(srv_i.get_nr_inchirieri(), 2)
        inchiriere = Inchiriere(3, "asc", "actiune", 10, "andi", "marian")
        repo_i.inchiriaza_film(inchiriere)
        self.assertEqual(srv_i.get_nr_inchirieri(), 3)
        inchiriere = Inchiriere(4, "da", "comedie", 11, "marius", "ionut")
        repo_i.inchiriaza_film(inchiriere)
        self.assertEqual(srv_i.get_nr_inchirieri(), 4)
        inchiriere = Inchiriere(5, "alone", "aventura", 11, "marius", "ionut")
        repo_i.inchiriaza_film(inchiriere)
        self.assertEqual(srv_i.get_nr_inchirieri(), 5)
        inchiriere = Inchiriere(6, "titanic", "show", 12, "alex", "stoian")
        repo_i.inchiriaza_film(inchiriere)
        lista_inchirieri = srv_i.get_inchirieri()
        copie_lista_inchirieri = srv_i.ordoneaza_inchirieri_dupa_client()
        self.assertEqual(copie_lista_inchirieri[0].get_id_client(), lista_inchirieri[5].get_id_client())
        self.assertEqual(copie_lista_inchirieri[1].get_id_client(), lista_inchirieri[0].get_id_client())
        self.assertEqual(copie_lista_inchirieri[2].get_id_client(), lista_inchirieri[2].get_id_client())
        self.assertEqual(copie_lista_inchirieri[3].get_id_client(), lista_inchirieri[1].get_id_client())
        self.assertEqual(copie_lista_inchirieri[4].get_id_client(), lista_inchirieri[3].get_id_client())
        self.assertEqual(copie_lista_inchirieri[5].get_id_client(), lista_inchirieri[4].get_id_client())


    def test_ordoneaza_inchirieri_dupa_nr_de_filme(self):
        repo_f = RepoFilme()
        repo_c = RepoClienti()
        repo_i = RepoInchirieri()
        valid_i = ValidatorID()
        srv_i = ServiceInchirieri(valid_i, repo_f, repo_c, repo_i)
        copie_lista_goala_inchirieri = srv_i.ordoneaza_inchirieri_dupa_client()
        self.assertEqual(copie_lista_goala_inchirieri, [])
        self.assertEqual(srv_i.get_nr_inchirieri(), 0)
        inchiriere = Inchiriere(1, "prison", "actiune", 10, "andi", "marian")
        repo_i.inchiriaza_film(inchiriere)
        self.assertEqual(srv_i.get_nr_inchirieri(), 1)
        inchiriere = Inchiriere(2, "home", "aventura", 11, "marius", "ionut")
        repo_i.inchiriaza_film(inchiriere)
        self.assertEqual(srv_i.get_nr_inchirieri(), 2)
        inchiriere = Inchiriere(3, "asc", "actiune", 10, "andi", "marian")
        repo_i.inchiriaza_film(inchiriere)
        self.assertEqual(srv_i.get_nr_inchirieri(), 3)
        inchiriere = Inchiriere(4, "da", "comedie", 11, "marius", "ionut")
        repo_i.inchiriaza_film(inchiriere)
        self.assertEqual(srv_i.get_nr_inchirieri(), 4)
        inchiriere = Inchiriere(5, "alone", "aventura", 11, "marius", "ionut")
        repo_i.inchiriaza_film(inchiriere)
        self.assertEqual(srv_i.get_nr_inchirieri(), 5)
        inchiriere = Inchiriere(6, "titanic", "actiune", 12, "alex", "stoian")
        repo_i.inchiriaza_film(inchiriere)
        lista_inchirieri = srv_i.get_inchirieri()
        dictionar = {}
        copie_lista_inchirieri = srv_i.ordoneaza_inchirieri_dupa_nr_de_filme(dictionar)
        self.assertEqual(dictionar[10], 2)
        self.assertEqual(dictionar[11], 3)
        self.assertEqual(dictionar[12], 1)
        self.assertEqual(copie_lista_inchirieri[0].get_id_client(), lista_inchirieri[1].get_id_client())
        self.assertEqual(copie_lista_inchirieri[1].get_id_client(), lista_inchirieri[3].get_id_client())
        self.assertEqual(copie_lista_inchirieri[2].get_id_client(), lista_inchirieri[4].get_id_client())
        self.assertEqual(copie_lista_inchirieri[3].get_id_client(), lista_inchirieri[0].get_id_client())
        self.assertEqual(copie_lista_inchirieri[4].get_id_client(), lista_inchirieri[2].get_id_client())
        self.assertEqual(copie_lista_inchirieri[5].get_id_client(), lista_inchirieri[5].get_id_client())

    def test_ordoneaza_inchirieri_dupa_aparitia_filmelor(self):
        repo_f = RepoFilme()
        repo_c = RepoClienti()
        repo_i = RepoInchirieri()
        valid_i = ValidatorID()
        srv_i = ServiceInchirieri(valid_i, repo_f, repo_c, repo_i)
        copie_lista_goala_inchirieri = srv_i.ordoneaza_inchirieri_dupa_client()
        self.assertEqual(copie_lista_goala_inchirieri, [])
        self.assertEqual(srv_i.get_nr_inchirieri(), 0)
        inchiriere = Inchiriere(1, "home", "aventura", 10, "andi", "marian")
        repo_i.inchiriaza_film(inchiriere)
        self.assertEqual(srv_i.get_nr_inchirieri(), 1)
        inchiriere = Inchiriere(2, "home", "aventura", 11, "marius", "ionut")
        repo_i.inchiriaza_film(inchiriere)
        self.assertEqual(srv_i.get_nr_inchirieri(), 2)
        inchiriere = Inchiriere(3, "asc", "actiune", 10, "andi", "marian")
        repo_i.inchiriaza_film(inchiriere)
        self.assertEqual(srv_i.get_nr_inchirieri(), 3)
        inchiriere = Inchiriere(4, "da", "comedie", 11, "marius", "ionut")
        repo_i.inchiriaza_film(inchiriere)
        self.assertEqual(srv_i.get_nr_inchirieri(), 4)
        inchiriere = Inchiriere(5, "asc", "actiune", 11, "marius", "ionut")
        repo_i.inchiriaza_film(inchiriere)
        self.assertEqual(srv_i.get_nr_inchirieri(), 5)
        inchiriere = Inchiriere(6, "asc", "show", 12, "alex", "stoian")
        repo_i.inchiriaza_film(inchiriere)
        lista_inchirieri = srv_i.get_inchirieri()
        dictionar = {}
        copie_lista_inchirieri = srv_i.ordoneaza_inchirieri_dupa_aparitia_filmelor(dictionar)
        self.assertEqual(dictionar["asc"], 3)
        self.assertEqual(dictionar["home"], 2)
        self.assertEqual(dictionar["da"], 1)
        self.assertEqual(copie_lista_inchirieri[0].get_titlu(), lista_inchirieri[2].get_titlu())
        self.assertEqual(copie_lista_inchirieri[1].get_titlu(), lista_inchirieri[4].get_titlu())
        self.assertEqual(copie_lista_inchirieri[2].get_titlu(), lista_inchirieri[5].get_titlu())
        self.assertEqual(copie_lista_inchirieri[3].get_titlu(), lista_inchirieri[0].get_titlu())
        self.assertEqual(copie_lista_inchirieri[4].get_titlu(), lista_inchirieri[1].get_titlu())
        self.assertEqual(copie_lista_inchirieri[5].get_titlu(), lista_inchirieri[3].get_titlu())



    def test_creeaza_client(self):
        id_client = 1
        nume = "popescu"
        prenume = "andrei"
        cnp = "1235921245671"
        client = Client(id_client, nume, prenume, cnp)
        self.assertEqual(client.get_id_client(), id_client)
        self.assertEqual(client.get_nume(), nume)
        self.assertEqual(client.get_prenume(), prenume)
        self.assertEqual(client.get_cnp(), cnp)
        alt_nume = "danci"
        alt_prenume = "ionut"
        alt_client = Client(id_client, alt_nume, alt_prenume, cnp)
        self.assertEqual(client, alt_client)
        self.assertTrue(client.__eq__(alt_client))
        self.assertEqual(str(client), "[1,popescu,andrei,1235921245671]")
        self.assertEqual(client.__str__(), "[1,popescu,andrei,1235921245671]")

    def test_valideaza_client(self):
        id_client = 34
        nume = "moise"
        prenume = "george"
        cnp = "4563214789012"
        client = Client(id_client, nume, prenume, cnp)
        valid = ValidatorClient()
        valid.valideaza(client)
        id_invalid = -5
        nume = "gherasim"
        prenume = "mihai"
        cnp_invalid = "123456"
        id_cnp_client_invalide = Client(id_invalid, nume, prenume, cnp_invalid)
        with self.assertRaises(ValidationError) as ve:
            valid.valideaza(id_cnp_client_invalide)
        self.assertEqual(str(ve.exception), "id-ul este invalid\ncnp-ul este invalid\n")
        id_invalid = -4
        nume_invalid = ""
        prenume_invalid = ""
        cnp_invalid = "123456789012r"
        client_invalid = Client(id_invalid, nume_invalid, prenume_invalid, cnp_invalid)
        with self.assertRaises(ValidationError) as ve:
            valid.valideaza(client_invalid)
        self.assertEqual(str(ve.exception), "id-ul este invalid\nnumele este invalid\nprenumele este invalid\ncnp-ul este invalid\n")


    def test_adauga_client_repo(self):
        with open("test_clienti.txt", 'w') as f:
            f.write("")
        repo = FileRepoClienti("test_clienti.txt")
        self.assertEqual(len(repo), 0)
        self.assertEqual(repo.__len__(), 0)
        id_client = 3
        nume = "pop"
        prenume = "marius"
        cnp = "2341567890123"
        client = Client(id_client, nume, prenume, cnp)
        repo.adauga_client(client)
        self.assertEqual(len(repo), 1)
        client_gasit = repo.gaseste_dupa_id_client(id_client)
        self.assertEqual(client_gasit, client)
        self.assertEqual(client_gasit.get_nume(), client.get_nume())
        self.assertEqual(client_gasit.get_prenume(), client.get_prenume())
        self.assertEqual(client_gasit.get_cnp(), client.get_cnp())
        all = repo.get_all_clienti()
        self.assertEqual(all[0], client)
        self.assertEqual(all[0].get_nume(), client.get_nume())
        self.assertEqual(all[0].get_prenume(), client.get_prenume())
        self.assertEqual(all[0].get_cnp(), client.get_cnp())
        self.assertEqual(len(all), 1)
        id_client_inexistent = 7
        with self.assertRaises(RepositoryError) as re:
            repo.gaseste_dupa_id_client(id_client_inexistent)
        self.assertEqual(str(re.exception), "id-ul clientului este inexistent\n")
        alt_id = 25
        alt_nume = "zancu"
        alt_prenume = "denis"
        alt_cnp = "1234097453219"
        same_id_client = Client(id_client, alt_nume, alt_prenume, alt_cnp)
        with self.assertRaises(RepositoryError) as re:
            repo.adauga_client(same_id_client)
        self.assertEqual(str(re.exception), "id-ul clientului este existent\n")
        same_id_cnp_client = Client(id_client, alt_nume, alt_prenume, cnp)
        with self.assertRaises(RepositoryError) as re:
            repo.adauga_client(same_id_cnp_client)
        self.assertEqual(str(re.exception), "id-ul clientului este existent\ncnp-ul clientului este existent\n")
        same_cnp_client = Client(alt_id, alt_nume, alt_prenume, cnp)
        with self.assertRaises(RepositoryError) as re:
            repo.adauga_client(same_cnp_client)
        self.assertEqual(str(re.exception), "cnp-ul clientului este existent\n")

    def test_adauga_client_service(self):
        repo = RepoClienti()
        valid = ValidatorClient()
        srv = ServiceClienti(valid, repo)
        id_client = 12
        nume = "marin"
        prenume = "zalos"
        cnp = "5612345109123"
        self.assertEqual(srv.get_nr_clienti(), 0)
        srv.adauga_client(id_client, nume, prenume, cnp)
        self.assertEqual(srv.get_nr_clienti(), 1)
        id_invalid = -1
        nume_invalid = ""
        prenume_invalid = ""
        cnp_invalid = "2443556"
        with self.assertRaises(ValidationError) as ve:
            srv.adauga_client(id_invalid, nume_invalid, prenume_invalid, cnp_invalid)
        self.assertEqual(str(ve.exception), "id-ul este invalid\nnumele este invalid\nprenumele este invalid\ncnp-ul este invalid\n")

    def test_sterge_client_repo(self):
        with open("test_clienti.txt", 'w') as f:
            f.write("")
        repo = FileRepoClienti("test_clienti.txt")
        self.assertEqual(len(repo), 0)
        self.assertEqual(repo.__len__(), 0)
        id_client = 5
        nume = "vrab"
        prenume = "andreea"
        cnp = "1209234152589"
        client = Client(id_client, nume, prenume, cnp)
        repo.adauga_client(client)
        self.assertEqual(len(repo), 1)
        self.assertEqual(repo.__len__(), 1)
        id_inexistent = 8
        with self.assertRaises(RepositoryError) as re:
            repo.sterge_client(id_inexistent)
        self.assertEqual(str(re.exception), "clientul de sters nu exista")
        repo.sterge_client(id_client)
        self.assertEqual(len(repo), 0)
        self.assertEqual(repo.__len__(), 0)
        with self.assertRaises(RepositoryError) as re:
            repo.sterge_client(id_client)
        self.assertEqual(str(re.exception), "clientul de sters nu exista")
        with self.assertRaises(RepositoryError) as re:
            repo.sterge_client(id_client)
        self.assertEqual(str(re.exception), "clientul de sters nu exista")

    def test_sterge_client_service(self):
        repo = RepoClienti()
        valid = ValidatorClient()
        srv = ServiceClienti(valid, repo)
        id_client = 34
        with self.assertRaises(RepositoryError) as re:
            srv.sterge_client(id_client)
        self.assertEqual(str(re.exception), "clientul de sters nu exista")
        nume = "daniel"
        prenume = "marin"
        cnp = "4321567890123"
        self.assertEqual(srv.get_nr_clienti(), 0)
        srv.adauga_client(id_client, nume, prenume, cnp)
        self.assertEqual(srv.get_nr_clienti(), 1)
        srv.sterge_client(id_client)
        self.assertEqual(srv.get_nr_clienti(), 0)

    def test_modifica_client_repo(self):
        with open("test_clienti.txt", 'w') as f:
            f.write("")
        repo = FileRepoClienti("test_clienti.txt")
        self.assertEqual(len(repo), 0)
        self.assertEqual(repo.__len__(), 0)
        id_client = 253
        nume = "vali"
        prenume = "raul"
        cnp = "1209224561231"
        client = Client(id_client, nume, prenume, cnp)
        repo.adauga_client(client)
        alt_nume = "iban"
        alt_prenume = "dragos"
        alt_client = Client(id_client, alt_nume, alt_prenume, cnp)
        repo.modifica_client(alt_client)
        all = repo.get_all_clienti()
        self.assertEqual(all[0], alt_client)
        self.assertEqual(all[0].get_nume(), alt_nume)
        self.assertEqual(all[0].get_prenume(), alt_prenume)
        self.assertEqual(all[0].get_cnp(), cnp)
        alt_id = 250
        alt_cnp = "1234567012345"
        client_cu_alt_id = Client(alt_id, nume, prenume, alt_cnp)
        with self.assertRaises(RepositoryError) as re:
            repo.modifica_client(client_cu_alt_id)
        self.assertEqual(str(re.exception), "clientul pe care doriti sa il modificati nu exista")

    def test_modifica_client_service(self):
        repo = RepoClienti()
        valid = ValidatorClient()
        srv = ServiceClienti(valid, repo)
        id_client = 2
        nume = "daniel"
        prenume = "ionut"
        cnp = "2341081056734"
        self.assertEqual(srv.get_nr_clienti(), 0)
        with self.assertRaises(RepositoryError) as re:
            srv.modifica_client(id_client, nume, prenume, cnp)
        self.assertEqual(str(re.exception), "clientul pe care doriti sa il modificati nu exista")
        srv.adauga_client(id_client, nume, prenume, cnp)
        self.assertEqual(srv.get_nr_clienti(), 1)
        alt_nume = "morar"
        alt_prenume = "vasile"
        srv.modifica_client(id_client, alt_nume, alt_prenume, cnp)
        self.assertEqual(srv.get_nr_clienti(), 1)
        all = srv.get_clienti()
        self.assertEqual(all[0].get_id_client(), id_client)
        self.assertEqual(all[0].get_nume(), alt_nume)
        self.assertEqual(all[0].get_prenume(), alt_prenume)
        self.assertEqual(all[0].get_cnp(), cnp)

    def test_cauta_client(self):
        with open("test_clienti.txt", 'w') as f:
            f.write("")
        repo = FileRepoClienti("test_clienti.txt")
        id_client = 50
        nume = "dascalu"
        prenume = "andrei"
        cnp = "8902314568201"
        client = Client(id_client, nume, prenume, cnp)
        repo.adauga_client(client)
        self.assertEqual(repo.gaseste_dupa_id_client(id_client), client)
        alt_id_client = 20
        with self.assertRaises(RepositoryError) as re:
            repo.gaseste_dupa_id_client(alt_id_client)
        self.assertEqual(str(re.exception), "id-ul clientului este inexistent\n")

    def run_all_tests(self):
        # print("testele au inceput")
        self.test_creeaza_film()
        self.test_valideaza_film()
        self.test_adauga_film_repo()
        self.test_adauga_film_service()
        self.test_sterge_film_repo()
        self.test_sterge_film_service()
        self.test_modifica_film_repo()
        self.test_modifica_film_service()
        self.test_cauta_film()

        self.test_creeaza_client()
        self.test_valideaza_client()
        self.test_adauga_client_repo()
        self.test_adauga_client_service()
        self.test_sterge_client_repo()
        self.test_sterge_client_service()
        self.test_modifica_client_repo()
        self.test_modifica_client_service()
        self.test_cauta_client()

        self.test_inchiriaza_film_repo()
        self.test_adauga_inchiriere_service()
        self.test_sterge_inchiriere_repo()
        self.test_sterge_inchiriere_service()
        self.test_ordoneaza_inchirieri_dupa_client_service()
        self.test_ordoneaza_inchirieri_dupa_nr_de_filme()
        self.test_ordoneaza_inchirieri_dupa_aparitia_filmelor()
        # print("testele s-au incheiat cu succes")