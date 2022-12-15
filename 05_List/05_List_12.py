Name = ['Robert', 'William', 'James', 'John', 'Margaret', 'Edward', 'Sarah', 'Andrew', 'Anthony', 'Deborah']
Nickname = ['Dick', 'Bill', 'Jim', 'Jack', 'Peggy', 'Ed','Sally', 'Andy', 'Tony', 'Debbie']
for i in range(int(input())) :
    find = input()
    if find in Name :
        print(Nickname[Name.index(find)])
    elif find in Nickname :
        print(Name[Nickname.index(find)])
    else :
        print("Not found")