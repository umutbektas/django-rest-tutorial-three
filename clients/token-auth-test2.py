import requests


def client():
    token_h = "Token <token>"

    headers = {"Authorization": token_h}

    response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)

    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()