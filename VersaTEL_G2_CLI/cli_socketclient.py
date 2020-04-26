import pickle
import linstordb
import socket

# ip_port = ('192.168.36.61',12129)
def get_host_ip():
    try:
        obj_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        obj_socket.connect(('8.8.8.8', 80))
        ip = obj_socket.getsockname()[0]
    except Exception:
        return '127.0.0.0'
    finally:
        obj_socket.close()
    return ip

ip_port = (get_host_ip(),12144)


class SocketSend():
    def __init__(self):
        self.client = socket.socket()
        self.client.connect(ip_port)


    def sql_script(self,*args):
        db = linstordb.LINSTORDB()
        return db.data_base_dump()

    def print_sql(self,func,*args):
        func = func()
        print(func.encode())

    def send_result(self,func,*args):
        client = self.client
        func = func(*args)
        func = pickle.dumps(func)
        judge_conn = client.recv(8192).decode()
        print(judge_conn)
        client.send(b'database')
        client.recv(8192)
        client.sendall(func)
        client.recv(8192)
        client.send(b'exit')
        client.close()





