import pytest
import decorateur_fonction_exemple
# ----------------------------------- EXO 2 -----------------------------------
def exo2():
    print(" ----------------------------------- EXO 2 -----------------------------------")

    a = [8, 1, 4, 6]
    b = [8, 1, 4, 6]
    c = b

    a is b #  False
    a == b  #  True
    c is b  #  True
    p, *m, d = a  #  8 ,  1 4 ,  6
    len(a)  #  4
    a[-1]  #  6
    a[0]  #  8
    x = 'a'
    s = str(x)  #  a
    r = repr(x)  #  'a'

    print("a is b # " ,a is b)
    print("a == b  # " ,a == b)
    print("c is b  # " ,c is b)
    print("p, *m, d = a  # " ,p, ', ', *m, ', ', d)
    print("len(a)  # " ,len(a))
    print("a[-1]  # " ,a[-1])
    print("a[0]  # " ,a[0])
    print("s = str(x)  # " ,s)
    print("r = repr(x)  # " ,r)

# ----------------------------------- EXO 3 -----------------------------------
def exo3():
    print(" ----------------------------------- EXO 3 -----------------------------------")
    l1 = []
    for i in range(2, 10):
        l1.append(2 * i + 5)
    print("# l1 ",l1)

    l2 = [2 * i + 5 for i in range(2, 10)]
    print("# l2 ",l2)

    print("l1 == l2  #", l1 == l2)

    # l1  [9, 11, 13, 15, 17, 19, 21, 23]
    # l2  [9, 11, 13, 15, 17, 19, 21, 23]

# ----------------------------------- EXO 4 -----------------------------------
def exo4():
    print(" ----------------------------------- EXO 4 -----------------------------------")

    a = { 1, 2, 3, 4, 3, 2, 1}
    b = { 'fr': 'France', 'de': 'Allemagne' }
    len(a)  #  4
    len(b)  #  1
    b[5] = 'fr'  # b =  {'de': 'Allemagne'}
    x = b['fr']  #  France
    y = b.get('it', -1)  #  -1 # Renvoie -1 si la clé 'it' n'existe pas
    del b[5]  # b =  {'de': 'Allemagne'}
    b.items()  #  dict_items([('de', 'Allemagne')]) # Renvoie les items de b
    b.values()  #  dict_values(['Allemagne']) # Renvoie les valeurs de b
    b.keys()  #  dict_keys(['de']) # Renvoie les clés de b
    p = b.pop('fr')  #  France # p récupère la valeur à 'fr' et l'enlève du dictionnaire


    print("len(a)  # ", len(a))
    print("len(b)  # ", len(b))
    print("b[5] = 'fr'  # b = ", b)
    print("x = b['fr']  # ", x)
    print("y = b.get('it', -1)  # ", y, "# Renvoie -1 si la clé 'it' n'existe pas")
    print("del b[5]  # b = ", b)
    print("b.items()  # ", b.items(), "# Renvoie les items de b")
    print("b.values()  # ", b.values(), "# Renvoie les valeurs de b")
    print("b.keys()  # ", b.keys(), "# Renvoie les clés de b")
    print("p = b.pop('fr')  # ", p, "# p récupère la valeur à 'fr' et l'enlève du dictionnaire")

# ----------------------------------- EXO 5 -----------------------------------
def exo5():
    print(" ----------------------------------- EXO 5 -----------------------------------")
    pytest.main(["index_test.py"])

# ----------------------------------- EXO 6 -----------------------------------

def f(a=4, *p, x, **kw):
    print('a =', a)
    print('p =', p)
    print('kw =', kw)
    print(*p, sep='... ', end=' !\n')

def exo6():
    print(" ----------------------------------- EXO 6 -----------------------------------")
    # 1 et 2 vont dans *p
    # x, y et z vont dans kw
    print("Quand il y a une '*' dans les paramètres, les paramètres qui suivent doivent être écrit explicitement")
    print("Exemple : x = 5, y = 6, z = 4")
    print(f(1,2,3,x=5,y=6,z=4))

# ----------------------------------- EXO 7 -----------------------------------
def zero(f, a, b, *, precision=10e-5):
    '''Retourner une abscisse où la fonction f s'annule entre a et b'''
    assert f(a) * f(b) <= 0
    if a > b:
        a, b = b, a
    while b - a > precision:
        milieu = (a + b) / 2
        if f(a) * f(milieu) > 0:
            a = milieu
        else:
            b = milieu
    return (a + b) / 2

def exo7():
    print("Le paramètre f est une fonction")
    print("On donne une valeur au paramètre appelé précision en l'écrivant explicitement car il y a une '*' dans les paramètres")
    # TODO : appeler la fonction zero avec la fonction f (x) = x2 − 2x − 15 sur l’intervalle [0, 15] avec une précision de 0.01.


# ----------------------------------- EXO 8 -----------------------------------
def fn_bavard(f):
    def f_interne(*p, **k):
        print('debut de f_interne()')
        f(*p, **k)
        print('fin de f_interne()')
    print('dans fn_bavard')
    return f_interne

@fn_bavard
def exemple(x, y='ok'):
    print('exemple:', y, x)

def exo8():
    print('Appel à exemple')
    exemple('?')
    print(exemple.__qualname__)


#exo2()
#exo3()
#exo4()
#exo5()
#exo6()
#exo7()
#exo8()