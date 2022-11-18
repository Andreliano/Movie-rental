from prezentare.user_interface import Consola
# from business.servicii import ServiceFilme, ServiceClienti, ServiceInchirieri
from infrastructura.repozitorii import *
from validare.validator import ValidatorFilm, ValidatorClient, ValidatorID
from testare.teste import Teste
if __name__ == '__main__':
    valid_film = ValidatorFilm()
    valid_client = ValidatorClient()
    valid_inchiriere = ValidatorID()

    repo_filme = FileRepoFilme("filme.txt")
    repo_clienti = FileRepoClienti("clienti.txt")
    repo_inchirieri = FileRepoInchirieri("inchirieri.txt")

    # repo_filme = RepoFilme()
    # repo_clienti = RepoClienti()
    # repo_inchirieri = RepoInchirieri()

    srv_filme = ServiceFilme(valid_film, repo_filme)
    srv_clienti = ServiceClienti(valid_client, repo_clienti)
    srv_inchirieri = ServiceInchirieri(valid_inchiriere, repo_filme, repo_clienti, repo_inchirieri)

    ui = Consola(srv_filme, srv_clienti, srv_inchirieri)
    teste = Teste()
    teste.run_all_tests()
    ui.run()
