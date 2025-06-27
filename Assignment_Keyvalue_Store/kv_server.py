import gevent
from gevent.server import StreamServer
from gevent import monkey

monkey.patch_all()  # Patches standard libraries for non-blocking I/O

class KeyValueServer:
    def __init__(self):
        self.data_store = {}  # In-memory dictionary to store key-value pairs

    def handle_client(self, socket, address):
        print(f"New connection from {address}")
        file_obj = socket.makefile('rwb')  # Binary mode for reading and writing

        while True:
            try:
                line = file_obj.readline()
                if not line:
                    break

                # Decode the incoming command and split into parts
                command, *args = line.strip().split()
                command = command.decode('utf-8').upper()

                if command == 'SET':
                    self.handle_set(file_obj, *args)
                elif command == 'GET':
                    self.handle_get(file_obj, *args)
                elif command == 'DELETE':
                    self.handle_delete(file_obj, *args)
                elif command == 'FLUSH':
                    self.handle_flush(file_obj)
                elif command == 'MGET':
                    self.handle_mget(file_obj, *args)
                elif command == 'MSET':
                    self.handle_mset(file_obj, *args)
                else:
                    file_obj.write(b"-ERROR: Unknown command\r\n")

                file_obj.flush()
            except Exception as e:
                file_obj.write(b"-ERROR: " + str(e).encode('utf-8') + b"\r\n")
                file_obj.flush()
                break

        print(f"Connection closed from {address}")

    def handle_set(self, file_obj, key, value):
        key = key.decode('utf-8')
        value = value.decode('utf-8')
        self.data_store[key] = value
        file_obj.write(b"+OK\r\n")

    def handle_get(self, file_obj, key):
        key = key.decode('utf-8')
        value = self.data_store.get(key)
        if value is not None:
            response = f"${len(value)}\r\n{value}\r\n"
            file_obj.write(response.encode('utf-8'))
        else:
            file_obj.write(b"$-1\r\n")  # Indicates key not found

    def handle_delete(self, file_obj, key):
        key = key.decode('utf-8')
        if key in self.data_store:
            del self.data_store[key]
            file_obj.write(b":1\r\n")  # Indicates one key deleted
        else:
            file_obj.write(b":0\r\n")  # Indicates no keys deleted

    def handle_flush(self, file_obj):
        self.data_store.clear()
        file_obj.write(b"+OK\r\n")  # Indicates all keys cleared

    def handle_mget(self, file_obj, *keys):
        keys = [key.decode('utf-8') for key in keys]
        values = [self.data_store.get(key, None) for key in keys]
        response = f"*{len(values)}\r\n"
        for value in values:
            if value is None:
                response += "$-1\r\n"
            else:
                response += f"${len(value)}\r\n{value}\r\n"
        file_obj.write(response.encode('utf-8'))

    def handle_mset(self, file_obj, *kv_pairs):
        for i in range(0, len(kv_pairs), 2):
            key = kv_pairs[i].decode('utf-8')
            value = kv_pairs[i + 1].decode('utf-8')
            self.data_store[key] = value
        file_obj.write(b"+OK\r\n")

    def start_server(self, host='127.0.0.1', port=1234):
        server = StreamServer((host, port), self.handle_client)
        print(f"Server started on {host}:{port}")
        server.serve_forever()

if __name__ == "__main__":
    kv_server = KeyValueServer()
    kv_server.start_server()
