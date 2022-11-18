class InchiriereDTO:
    def __init__(self, id_film, id_client, gen_film):
        self.__id_film = id_film
        self.__film = None
        self.__id_client = id_client
        self.__client = None
        self.__gen_film = gen_film

    def get_id_film(self):
        return self.__id_film

    def get_film(self):
        return self.__film

    def set_film(self, valoare):
        self.__film = valoare

    def get_id_client(self):
        return self.__id_client

    def get_client(self):
        return self.__client

    def set_client(self, valoare):
        self.__client = valoare

    def get_gen_film(self):
        return self.__gen_film

    def __str__(self):
        return self.__film.get_titlu() + ' ' + '[' + self.__gen_film + ']'


class DTO_Inchirieri:
    def __init__(self, nume_client, prenume_client, lista_filme):
        self.__nume_client = nume_client
        self.__prenume_client = prenume_client
        self.__lista_filme = lista_filme

    def __str__(self):
        reprezentare = ""
        reprezentare = reprezentare + self.__nume_client + ' ' + self.__prenume_client + ":\n"
        for film in self.__lista_filme:
            reprezentare = reprezentare + '\t' + str(film) + '\n'

