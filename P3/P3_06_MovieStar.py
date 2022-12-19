def Printout(actor) :
    actor = actor.strip()
    if actor not in Dictactor :
        return actor + " -> " + "Not found"
    else :
        return actor + " -> " + ", ".join(Dictactor[actor])
n = int(input())
Dictactor = {}
for i in range(n) :
    movie,actor1,actor2 = input().split(",")
    actor1 = actor1.strip()
    actor2 = actor2.strip()
    if actor1 not in Dictactor :
        Dictactor[actor1] = [movie]
    else :
        Dictactor[actor1].append(movie)
    if actor2 not in Dictactor :
        Dictactor[actor2] = [movie]
    else :
        Dictactor[actor2].append(movie)
actors = input().split(",")
for actor in actors :
    print(Printout(actor))