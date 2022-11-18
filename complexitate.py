# def sterge_client(self, id_client):
#     """
#     functie care cauta in lista un client dupa un id
#     daca id-ul introdus corespunde unui client din lista clientul va fi sters, iar in caz
#     contrar se va arunca o exceptie
#     :param id_client: intreg >= 0
#     :return: None
#     """
#     for i in range(len(self._clienti)):
#         if self._clienti[i].get_id_client() == id_client:
#             del self._clienti[i]
#             return
#     raise RepositoryError("clientul de sters nu exista")

"""
Caz favorabil: clientul care se doreste a fi sters se afla pe prima pozitie in lista : 𝑇(𝑛) = 1 ∈ 𝛩(1)
Caz defavorabil: clientul care se doreste a fi sters nu se afla in lista : 𝑇(𝑛) = 𝑛 ∈ 𝛩(𝑛)
Caz mediu: for-ul se poate executa de 1,2,..n ori : T(n) = (1 + 2 + ... + n) / n = n * (n+1) / 2 * n = (n + 1) / 2
-> T(n) ∈ 𝛩(𝑛)
Complexitate 𝑂(𝑛)
"""
# def k_element(lista, st, dr, k):
#     if st == dr:
#         if k == st + 1:
#             return lista[k - 1]
#         return 0
#     mij = st + (dr - st) // 2
#     x1 = k_element(lista, st, mij, k)
#     x2 = k_element(lista, mij + 1, dr, k)
#     return x1 + x2






# def consistent(lista):
#     for i in range(len(lista) - 1):
#         if lista[i] == 1 and lista[i] == lista[i + 1]:
#             return False
#     return True
#
# def e_solutie(lista, n):
#     return len(lista) == n
#
# def solutie_gasita(lista):
#     for i in range(len(lista)):
#         print(lista[i], end=' ')
#     print()
#
# def back_recursiv(lista, n):
#     if e_solutie(lista, n) is True:
#         solutie_gasita(lista)
#         return
#     lista.append(0)
#     for i in range(2):
#         lista[-1] = i
#         if consistent(lista) is True:
#             back_recursiv(lista, n)
#     lista.pop()

"""
SOLUTIE CANDIDAT

x = (x0, x1, x2, ... ,xk) , k < n
xi apartine {0,1}

CONDITIE CONSISTENT
x = (x0, x1, x2, ..., xk) e consistent daca oricare ar fi i apartine {0, ... , k - 1}, j = i + 1 si xi = 1 xi != xj

CONDITIE SOLUTIE
    x e solutie daca x e consistent si k + 1 = n
"""

def fact_var(num):
    a, b, i = 1,2,2 # base cases and our i counter.
    while i < num: # if i is equal to num, we're done, last product will be at return.
        c = a * b # start to multiply and save in c.
        i+=1 # add 1 to i because we want to multiply next number with c (in the next iteration).
        a, b = c, i # update variables to the next iteration.
    return a * b if num > 1 else 1 # last product occurs here is num is greater than 1.

print(fact_var(3))






