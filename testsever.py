from pymongo import MongoClient
import socket


MONGO_URL = "mongodb+srv://hdrproject:50230@cluster0.ktm1unb.mongodb.net/?retryWrites=true&w=majority"
HOST = '0.0.0.0'  # IP ของเครื่องเซิร์ฟเวอร์
PORT = 9090

client = MongoClient(MONGO_URL)
db = client.HDRProjecct
collection = db.histories

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)


print("Waiting for connection...")
client_socket, client_address = server_socket.accept()
print("Connected to:", client_address)


while True:
    data = client_socket.recv(1024).decode()
    if not data:
        break
    datadb = collection.find_one({"StudentNumber":int(data)})
    print("Received:", datadb)

client_socket.close()
server_socket.close()