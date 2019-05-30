import requests


def client():
    credential = {"username": "demo", "password": "Passw0rd1-+"}

    response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", data=credential)

    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()