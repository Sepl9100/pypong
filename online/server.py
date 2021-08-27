import pickle
import socket
from _thread import *
import sys
from online.server_game import *

server = "10.0.0.14"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except Exception as e:
    print(e)


s.listen()
print("Waiting for a connection. Server started successfully.")

connected = set()
games = {}
id_count = 0


def client(conn, p, gameID):
    global id_count
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(2048).decode()

            if gameID in games:
                game = games[gameID]

                if not data:
                    break
                else:
                    if data != "get":
                        i = data.index("=")
                        if data.count("ready") == 1:
                            game.update_ready(p)
                        elif data.count("x=") == 1:
                            game.update_x(p, data[i+1:])
                        elif data.count("y=") == 1:
                            game.update_y(p, data[i+1:])
                        elif data.count("name=") == 1:
                            game.update_name(p, data[i+1:])
                        elif data.count("pcol=") == 1:
                            game.update_paddle_col(p, data[i+1:])
                    reply = game
                    conn.sendall(pickle.dumps(reply))
            else:
                break
        except:
            break
    print("Lost connection")
    try:
        del games[gameID]
        print(f"Closing game {gameID}")
    except:
        pass
    id_count -= 1
    conn.close()


while True:
    conn, addr = s.accept()
    print(f"Connected to: {addr}")

    id_count += 1
    p = 0
    gameID = (id_count-1)//2
    if id_count % 2 == 1:
        games[gameID] = ServerGame(gameID)
        print("Creating a new game with id "+str(gameID))
    else:
        games[gameID].ready = True
        p = 1

    start_new_thread(client, (conn, p, gameID))


