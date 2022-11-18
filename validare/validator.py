from erori.exceptii import *
class ValidatorFilm(object):

    def valideaza(self, film):
        """"
        :param film: Film
        metoda care valideaza filmul dupa campuri(id,titlu,descriere,gen)
        se arunca exceptii in cazul in care campurile nu respecta constrangerile
        """
        erori = ""
        if film.get_id_film() < 0:
            erori += "id-ul este invalid\n"
        if film.get_titlu() == "":
            erori += "titlul este invalid\n"
        if film.get_descriere() == "":
            erori += "descrierea este invalida\n"
        if film.get_gen() == "":
            erori += "genul este invalid\n"
        if len(erori) > 0:
            raise ValidationError(erori)


class ValidatorClient(object):

    def valideaza(self, client):
        """
        metoda care valideaza clientul dupa campuri(id,nume,prenume,cnp)
        se arunca exceptii in cazul in care campurile introduse nu respecta constrangerile
        :param client: Client
        :return:
        """
        erori = ""
        if client.get_id_client() < 0:
            erori += "id-ul este invalid\n"
        if client.get_nume() == "":
            erori += "numele este invalid\n"
        if client.get_prenume() == "":
            erori += "prenumele este invalid\n"
        cnp = client.get_cnp()
        if len(cnp) == 0:
            erori += "cnp-ul este invalid\n"
        for i in range(len(cnp)):
           if not (cnp[i] >= '0' and cnp[i] <= '9') or len(cnp) != 13:
               erori += "cnp-ul este invalid\n"
               break
        if len(erori) > 0:
            raise ValidationError(erori)

class ValidatorID(object):

    def valideaza_id_uri(self, id_film, id_client):
        """
        :param id_film: intreg >= 0
        :param id_client: intreg >= 0
        :return: None
        metoda care valideaza pe id_film si id_client
        sau care arunca exceptii in cazul in care campurile nu respecta constrangerile
        """
        erori = ""
        if id_film < 0:
            erori += "id-ul filmului este invalid\n"
        if id_client < 0:
            erori += "id-ul clientului este invalid\n"
        if len(erori) > 0:
            raise ValidationError(erori)
