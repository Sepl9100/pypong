import socket
from _thread import *
import sys

server = "10.0.0.14"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except Exception as e:
    print(e)


s.listen()
print("Waiting for a connection. Server started successfully.")


def client(conn):
    conn.send(str.encode("connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print(f"Data: {reply}")
                print(f"Sending: {reply}")

            conn.sendall(str.encode(reply))
        except Exception as e:
            print(e)
            break
        print("Connection lost")
        conn.close()


while True:
    conn, addr = s.accept()
    print(f"Connected to: {addr}")

    start_new_thread(client, (conn, ))

