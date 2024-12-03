import requests


server_url = "https://my-flask-server.onrender.com/send"

def send_message(message):
    try:
        response = requests.post(server_url, json={"message": message})
        if response.status_code == 200:
            print("Wiadomość wysłana pomyślnie!")
        else:
            print(f"Błąd: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Wyjątek: {e}")

if __name__ == "__main__":
    # Testowe wysłanie wiadomości
    message = "test"
    send_message(message)
