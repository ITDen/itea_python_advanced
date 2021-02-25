import threading
import socket
from home_works.lesson_7.utils.messages import SocketMessage


class SocketClient2(threading.Thread):
    def __init__(self, host='127.0.0.1', port=9090, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__host = host
        self.__port = port
        self.__message = SocketMessage()
        self.start()

    def run(self):
        try:
            sock = socket.socket()
            sock.connect((self.__host, self.__port))
            print(f'Connected to {self.__host}:{self.__port}')
            answer = self.__message.receive(sock)
            if answer:
                print(answer)
        except ConnectionError:
            print('Server not found!')
            exit(0)
        else:
            while True:
                option = input()
                self.__message.send(sock, option)
                print(self.__message.receive(sock))
                if option == 'close':
                    sock.close()
                    exit(0)


SocketClient2()
