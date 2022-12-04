def double(x):
    return x * 2


def apply_to_one(f):
    return f(2)


my_double = double

x = apply_to_one(my_double)

print(x)

print(apply_to_one(lambda x: x + 8))


def print_default(message="Default Message"):
    print(message)


print_default("Hellow")
print_default()


def full_name(first="Firt-name", last="Last-name"):
    print(first + " " + last)


full_name()
full_name(first="David")
full_name("robso")
full_name(last="Robson")

first_name = "David"
last_name = "Forn"

# forma tradicional de contateção
print(first_name + " " + last_name)

# nova forma
print("{0} {1}".format(first_name, last_name))

# realizando stride(fatia) no list

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

every_third = x[::3]
print(every_third)
five_to_three = x[5:2:-1]
print(five_to_three)
print(1 in [1, 2, 3])
print("ameda" in [1, 2.4, "julia", "ameda"])
print(90 in [1, 2.4, "julia", "ameda"])

# dicionários

dicty = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}

if "asdsadE" in dicty:
    print("Exists")
else:
    print("Not exists")

# A_value
print(dicty.get("A", False))
# B_value
print(dicty.get("B", False))
# ABC_value
print(dicty.get("ABC", False))

# forma melhorada de utilização de dicionários
# como exemplo vamos pegar um tweet

tweet = {
    "user": "fornazierr",
    "text": "Data science is awesome",
    "retweet_count": 0,
    "hashtags": ["data", "science", "datascience", "awesome", "yolo"]
}

# Aqui vem a forma bacana de pegá-las

tweet_keys = tweet.keys()
tweet_values = tweet.values()
tweet_items = tweet.items()

if "fornazierr" in tweet_values:
    print("Oia tu aqui rapaz")


if "#datascience" in tweet_values:
    print("Tu tá estudando isso???")


if "retweet_count" in tweet:
    qtd = tweet["retweet_count"]
    if qtd > 1:
        print("Já é famoso, pode pedir recebidinhos")
    else:
        print("Sozinho mas bem =)")

# Classificacao

minha_lista_x = [23,22,109,1,67,29,3,6,7,32,34,31,78,5]
print("Minha lista X: ", x)
y = sorted(x)
print("Sorteando e gravando em variável: ", y)

# Compreensões de listas
valores_pares = [x for x in range(13) if x % 2 == 0]
print("Valores pares de X:", valores_pares)
ao_quadrado = [x * x for x in range(13)]
print("Valores ao quadrado de X: ", ao_quadrado)
valores_impares = [x for x in range(13) if x % 2 != 0]
print("Valores impares de X:", valores_impares)

# Transformando em dicionarios
ao_quadrado_dict = {x: x * x for x in range (10)}
print("Dicionário de X:", ao_quadrado_dict)

# Teste automatizados e asserção
#uma boa pratica é adicionar à funções como abaixo

def menor_numero(xs):
    return min(xs)

assert menor_numero([10,20,4,40]) == 4
assert menor_numero([-1,-5,0,2,3]) == -5

#POO
class CountingClicker:
    """Classe contadora de Cliques"""
    
    count = 0
    
    def __init__(self, count = 0):
        self.count = count
    
    def _repr_(self):
        return f"CountingClicker(count={self.count})"
    
    def click(self, cliques=1):
        """Clique no contador"""
        self.count += cliques
    
    def read(self):
        return self.count
    
    def reset(self):
        self.count = 0

#Iniciando as variaveis
clicker1 = CountingClicker()
clicker2 = CountingClicker(100)
clicker3 = CountingClicker(count=100)

#Usando o assert
clicker = CountingClicker()
assert clicker.read() == 0, "clicker should start with count 0"
clicker.click()
clicker.click()
assert clicker.read() == 2, "clicker should have count 2"
clicker.reset()
assert clicker.read() == 0, "clicker should have count 0"