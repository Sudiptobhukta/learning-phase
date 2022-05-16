import json
with open("E:\learning-phase_git_github\__pycache__\hello.txt", "r") as file:
    print(file.read())
    print(file.seek(5))
    print(file.read())

with open("E:\learning-phase_git_github\__pycache__\checkJason.jason","r") as files:
    data = files.read()
    print(data)

    d = json.loads(data)
    print(d)

    string = json.dumps(d)
    print(string)

    json.dump(d,file)


