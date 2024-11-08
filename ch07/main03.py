import json
def main():
    with open("todos.json","r") as f:
        data = json.load(f)
        print(data[0])
        print(data[0]['title'])
if __name__=='__main__':
    main()
