class Film(object):

    def __init__(self, id_film, titlu, descriere, gen):
        """
        metoda speciala care atribuie valori campurilor tipului de date Film
        :param id_film: intreg >=0
        :param titlu: string
        :param descriere: string
        :param gen: string
        """
        self.__id_film = id_film
        self.__titlu = titlu
        self.__descriere = descriere
        self.__gen = gen

    def get_id_film(self):
        # functie care returneaza id-ul unui film
        return self.__id_film

    def get_titlu(self):
        # functie care returneaza titlul unui film
        return self.__titlu

    def get_descriere(self):
        # functie care returneaza descrierea unui film
        return self.__descriere

    def get_gen(self):
        # functie care returneaza genul unui film
        return self.__gen

    def set_titlu(self, valoare):
        # functie care schimba titlul unui film cu un alt titlu(valoare)
        self.__titlu = valoare

    def set_descriere(self, valoare):
        # functie care schimba descrierea unui film cu o alta descriere(valoare)
        self.__descriere = valoare

    def set_gen(self, valoare):
        # functie care schimba genul unui film cu un alt gen(valoare)
        self.__gen = valoare

    def __eq__(self, other):
        # functie care supraincara operatorul = (verifica daca id-urile tipului Film sunt egale)
        return self.__id_film == other.__id_film

    def __str__(self):
        # functie care furnizeaza o reprezentare sub forma de string pentru Film
        return '[' + str(self.__id_film) + ',' + self.__titlu + ',' + self.__descriere + ',' + self.__gen + ']'

class Client(object):

    def __init__(self, id_client, nume, prenume, cnp):
        """
        metoda speciala care atribuie valori campurilor tipului de date Client
        :param id_client: intreg >= 0
        :param nume: string
        :param prenume: string
        :param cnp: string
        """
        self.__id_client = id_client
        self.__nume = nume
        self.__prenume = prenume
        self.__cnp = cnp

    def get_id_client(self):
        # functie care returneaza id-ul unui client
        return self.__id_client

    def get_nume(self):
        # functie care returneaza numele unui client
        return self.__nume

    def get_prenume(self):
        # functie care returneaza prenumele unui client
        return self.__prenume

    def get_cnp(self):
        # functie care returneaza cnp-ul unui client
        return self.__cnp

    def set_nume(self, valoare):
        # functie care schimba numele unui client cu un alt nume
        self.__nume = valoare

    def set_prenume(self, valoare):
        # functie care schimba prenumele unui client cu un alt prenume
        self.__prenume = valoare

    def __eq__(self, other):
        # functie care supraincarca operatorul = (verifica daca id-urile sau cnp-urile tipului Client sunt egale)
        return self.__id_client == other.__id_client or self.__cnp == other.__cnp

    def __str__(self):
        # functie care furnizeaza o reprezentare sub forma de string pentru Client
        return f"[{self.__id_client},{self.__nume},{self.__prenume},{self.__cnp}]"

class Inchiriere(object):

    def __init__(self, id_film, titlu, gen, id_client, nume, prenume):
        """
        metoda speciala care atribuie valori campurilor tipului de date Inchiriere
        :param id_film: intreg >= 0
        :param id_client:  intreg >= 0
        """
        self.__id_film = id_film
        self.__titlu = titlu
        self.__gen = gen
        self.__id_client = id_client
        self.__nume = nume
        self.__prenume = prenume

    def get_id_film(self):
        # functie care returneaza id-ul unui film
        return self.__id_film

    def get_titlu(self):
        return self.__titlu

    def get_gen(self):
        return self.__gen

    def get_id_client(self):
        # functie care returneaza id-ul unui client
        return self.__id_client

    def get_nume(self):
        return self.__nume

    def get_prenume(self):
        return self.__prenume

    def set_nume(self, valoare):
        # functie care schimba numele unui client cu un alt nume
        self.__nume = valoare

    def set_prenume(self, valoare):
        # functie care schimba prenumele unui client cu un alt prenume
        self.__prenume = valoare

    def __eq__(self, other):
        # functie care supraincarca operatorul = (verifica daca id-urile tipului Inchiriere sunt egale)
        return self.__id_film == other.__id_film

    def __str__(self):
        # functie care furnizeaza o reprezentare sub forma de string pentru Inchiriere
        return "Clientul " + str(self.__nume) + " " + str(self.__prenume) \
        + " care are id-ul " + str(self.__id_client) + " a inchiriat filmul " + str(self.__titlu) \
        + " care are id-ul " + str(self.__id_film)

