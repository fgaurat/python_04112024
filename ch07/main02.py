import json

def main():
    # f = open('mon_fichier.txt',"a")
    # f.write('Bonjour\n')
    # f.close()

    # context manager
    with open('mon_fichier.txt', "a") as f:
        f.write('Bonjour\n')

    # with open('mon_fichier.txt',"r") as f:
    #     s = f.read() # lit la totalité du fichier
    #     lines = s.splitlines()
    #     print(lines)

    with open('mon_fichier.txt', "r") as f:
        # lit la totalité du fichier dans une liste
        lines = [line.strip() for line in f.readlines()]
        print(lines)

    with open('mon_fichier.txt', "r") as f:
        for line in f:
            # print(line.strip())
            print(line, end="")

    data = [
        {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": False
        },
        {
            "userId": 1,
            "id": 2,
            "title": "quis ut nam facilis et officia qui",
            "completed": False
        },
        {
            "userId": 1,
            "id": 3,
            "title": "fugiat veniam minus",
            "completed": False
        }]

    with open("todos.json","w") as f:
        json.dump(data,f,indent=4)
if __name__ == '__main__':
    main()
