import socket

def run_client(filename="/"):
    # Buat socket client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 8080))

    # Request HTTP
    request = f"GET {filename} HTTP/1.1\r\n"
    request += "Host: localhost\r\n"
    request += "Connection: close\r\n\r\n"

    client.send(request.encode("utf-8"))

    # Terima response dari server
    response = b""
    while True:
        data = client.recv(4096)
        if not data:
            break
        response += data

    client.close()

    # Pisahkan header dan body
    header, body = response.split(b"\r\n\r\n", 1)

    print("=== RESPONSE HEADER ===")
    print(header.decode("utf-8", errors="ignore"))

    # Simpan body ke file (kalau html / gambar)
    if filename.endswith(".html") or filename == "/":
        with open("hasil.html", "wb") as f:
            f.write(body)
        print("File disimpan sebagai hasil.html")

    elif filename.endswith(".jpg") or filename.endswith(".png"):
        with open("hasil.jpg", "wb") as f:
            f.write(body)
        print("Gambar disimpan sebagai hasil.jpg")

    else:
        print("=== RESPONSE BODY ===")
        print(body.decode("utf-8", errors="ignore"))


if __name__ == "__main__":
    run_client("/index.html")
