from threading import Thread
import socket
from home_works.lesson_7.utils.messages import SocketMessage
from home_works.lesson_7._library.library import Library


class SocketServer(Thread):
    def __init__(self, host='127.0.0.1', port=9090, socket_listen=10, library: Library = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__host = host
        self.__port = port
        self.__sock = socket.socket()
        self.__sock.bind((self.__host, self.__port))
        self.__sock.listen(socket_listen)
        self.__library = library
        self.__message = SocketMessage()
        self.__available_commands = {'1': self.__library.get_available_books,
                                     '2': self.__library.get_unavailable_books,
                                     '3': self.__library.get_all_books,
                                     '4': self.__library.get_member_list,
                                     }
        self.__terminal_options = "1 - get available books\n2 - get unavailable books\n3 - get all books\n" \
                                  "4 - get members list\nclose - close terminal"
        self.start()

    def __in_conn_handler(self, conn, addr):
        try:
            self.__message.send(conn, f'Welcome to Library terminal!\n'
                                      f'Please, choose options:\n{self.__terminal_options}')
            requested_option = self.__message.receive(conn)
            while True:
                if requested_option == 'close':
                    self.__message.send(conn, 'Bye!')
                    print(f'Host: {addr} has been disconnected!')
                    break
                if requested_option in self.__available_commands:
                    request = self.__available_commands[requested_option]()
                    self.__message.send(conn, str(request))
                else:
                    self.__message.send(conn, f'Wrong option! Should choose one from:\n{self.__terminal_options}')
                requested_option = self.__message.receive(conn)
        except ConnectionError:
            print(f'Connection was interrupted unexpectedly!')

    def run(self):
        print(f'Server started! host: {self.__host}, port: {self.__port}')
        while True:
            conn, addr = self.__sock.accept()
            print(f'Host: {addr} has been connected!')
            Thread(target=self.__in_conn_handler, args=(conn, addr)).start()
