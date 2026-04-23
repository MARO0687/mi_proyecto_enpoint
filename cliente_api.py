import os
import requests

BASE_URL = "http://127.0.0.1:7000"
ORG_NAME = "iseu-desarrollo-maro"

def test_info():
    r = requests.get(f"{BASE_URL}/info")
    print("INFO:", r.json())

def test_datos_usuario(token):
    r = requests.get(f"{BASE_URL}/datosUsuario", params={"token": token})
    print("DATOS USUARIO:", r.json())

def test_usuarios(token):
    r = requests.get(f"{BASE_URL}/usuarios", params={"token": token})
    print(f"USUARIOS ({ORG_NAME}):", r.json())

if __name__ == "__main__":
    test_info()

    github_token = os.environ.get("GITHUB_TOKEN")
    if not github_token:
        raise ValueError("La variable de entorno GITHUB_TOKEN no está definida")

    test_datos_usuario(github_token)
    test_usuarios(github_token)
