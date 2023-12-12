import socket
import time

PORT = 5050
LOG_PATH = "log.txt"


def main():
    ip = get_priv_ip()
    address = (ip, PORT)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(address)
        server_socket.listen(10)

        log("Starting")

        while True:
            accept_clients(server_socket)


def accept_clients(server_socket: socket.socket):
    client_socket, addr = server_socket.accept()
    client_socket.close()
    log(f"{addr[0]}:{addr[1]}")


def get_priv_ip():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as temp_socket:
        temp_socket.connect(("1.1.1.1", 80))
        local_ip = temp_socket.getsockname()[0]

    return local_ip


def log(msg: str):
    print(msg)
    timestamp = time.strftime("%H:%M:%S", time.localtime())
    with open(LOG_PATH, "a") as file:
        file.write(f"[{timestamp}] | {msg}\n")


if __name__ == "__main__":
    main()
