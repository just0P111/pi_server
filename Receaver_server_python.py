import requests

# Adres serwera na Render (podmień na Twój)
server_url = "https://my-flask-server.onrender.com/receive"

def receive_messages():
    try:
        response = requests.get(server_url)
        if response.status_code == 200:
            messages = response.json().get("messages", [])
            if "test" in messages:
                print("Otrzymałem wiadomość: test")
            else:
                print("Brak wiadomości 'test'. Otrzymane wiadomości:", messages)
        else:
            print(f"Błąd: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Wyjątek: {e}")

if __name__ == "__main__":
    # Testowe odbieranie wiadomości
    receive_messages()
