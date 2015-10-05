import threading


def sucesor(a):
    while True:
        print(a + 1, 'sucesor de', a)
        a += 1

miPrimerThread = threading.Thread(target=sucesor, args=(1,))
miPrimerThread.daemon = True
miPrimerThread.start()
