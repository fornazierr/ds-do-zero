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
