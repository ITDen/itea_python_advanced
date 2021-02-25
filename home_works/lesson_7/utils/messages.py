import socket


class SocketMessage:
    def __init__(self, header_size=10, size_pack=1024, encoding='866'):
        self.header_size = header_size
        self.size_pack = size_pack
        self.encoding = encoding

    def send(self, conn: socket, msg: str) -> bool:
        size_msg = f'{len(msg):{self.header_size}}'

        # отправляем размер последующего сообщения
        if conn.send(size_msg.encode(encoding=self.encoding)) != self.header_size:
            print("ERROR: can't send size message")
            return False

        if conn.send(bytearray(msg, encoding='utf8')) != len(msg):
            print("ERROR: can't send message")
            return False
        return True

    def receive(self, conn: socket) -> bytearray or bool:
        data = conn.recv(self.header_size)
        if not data:
            return False

        size_msg = int(data.decode(encoding=self.encoding))
        msg = b''

        while True:
            if size_msg <= self.size_pack:
                data = conn.recv(size_msg)
                if not data:
                    return False

                msg += data
                break

            data = conn.recv(self.size_pack)
            if not data:
                return False

            size_msg -= self.size_pack
            msg += data
        return msg.decode('utf8')
