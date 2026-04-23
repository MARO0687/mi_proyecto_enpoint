import requests
import json

BASE_URL = "http://127.0.0.1:7000"

def get_info():
    r = requests.get(f"{BASE_URL}/info")
    print("\n--- INFO ---")
    print(json.dumps(r.json(), indent=2))

def get_datos_usuario(token):
    r = requests.get(f"{BASE_URL}/datosUsuario", params={"token": token})
    print("\n--- DATOS USUARIO ---")
    print(json.dumps(r.json(), indent=2))

def get_usuarios(token):
    r = requests.get(f"{BASE_URL}/usuarios", params={"token": token})
    print("\n--- USUARIOS Y REPOS ---")
    print(json.dumps(r.json(), indent=2))

def main():
    while True:
        print("\n=== Frontend API - mi-proyecto-enpoint ===")
        print("1. Ver Info")
        print("2. Ver Datos Usuario (requiere token)")
        print("3. Ver Usuarios y Repos (requiere token)")
        print("4. Salir")

        choice = input("Selecciona una opción: ")

        if choice == "1":
            get_info()
        elif choice == "2":
            token = input("Introduce tu GitHub Token: ")
            get_datos_usuario(token)
        elif choice == "3":
            token = input("Introduce tu GitHub Token: ")
            get_usuarios(token)
        elif choice == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
