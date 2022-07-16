from audioop import avg
from collections import Counter

################
# DATA
################

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3),
                    (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


interests = {
    (0, "Hdoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy")
    (2, "numpy"), (2, "statsmodel"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability")
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learnig"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "BigData")
}
################
# FUNCTIONS
################


def number_of_friends(user):
    """Quantos amigos tem o _user_?"""
    user_id = user["id"]
    friends_ids = friendships[user_id]
    return len(friends_ids)


def foaf_ids_bad(user):
    """fof sognifica "friend of friend" """
    return [foaf_id
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]]


def friends_of_friends(user):
    """Calcula os amigos de amigos sem repetição"""
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendship_pairs[user_id]
        for foaf_id in friendships[friend_id]
        if foaf_id != user_id
        and foaf_id not in friendships[user_id]
    )

################
# LOGIC
################


# Criando dict
friendships = {user["id"]: [] for user in users}

# Preencendo dict
for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

total_connections = sum(number_of_friends(user) for user in users)
print("Total de conexões", total_connections)

num_users = len(users)
print("Total de amigos", num_users)

avg_connections = total_connections / num_users
print("Média de conexões", avg_connections)

# Ordena e imprime dos que mais possuem conexões
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

num_friends_by_id.sort(
    key=lambda id_and_friends: id_and_friends[1],
    reverse=True
)
print("Ordenação de mais conexões\n", num_friends_by_id)

print("Encontrado os amigos de amigos de forma crua\n",
      "Buscando foaf de Thor", foaf_ids_bad(users[0]))

print("Encontrado os amigos de amigos com exclusão de repetidos\n",
      "Buscando foaf de Thor", friends_of_friends(users[0]))

print("Encontrado os amigos de amigos com exclusão de repetidos\n",
      "Buscando foaf de Chi", friends_of_friends(users[4]))