from ast import Try


def prefixes(pre):
    try:
        while True:
            name = (yield)
            print(pre + ":" + name)

    except GeneratorExit:
        print("Done")


coroutine = prefixes("Cool")

#initialization

next(coroutine)

#Sending data and control
coroutine.send("Sudipto")
coroutine.send("prapti")
coroutine.close()


