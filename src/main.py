import json
import os
from getpass import getpass

FILE_USER = "database/users.json"

def load_users():
    if not os.path.exists(FILE_USER):
        print("❌ File users.json tidak ditemukan!")
        return []
    with open(FILE_USER, "r") as file:
        return json.load(file)["users"]

def cek_login(username, password):
    users = load_users()
    for user in users:
        if user["username"] == username and user["password"] == password:
            return True
    return False

def login():
    print("=== LOGIN SISTEM SMKNX ===")
    username = input("Username: ")
    password = getpass("Password: ")
    
    if cek_login(username, password):
        print(f"\n✅ Login berhasil! Halo, {username}")
        return True, username
    else:
        print("\n❌ Username atau password salah!")
        return False, None

def tambah_user():
    users = load_users()
    print("\n--- TAMBAH USER BARU ---")
    username_baru = input("Username baru: ")
    
    if any(user["username"] == username_baru for user in users):
        print("❌ Username sudah ada!")
        return
        
    password_baru = getpass("Password baru: ")
    users.append({"username": username_baru, "password": password_baru})
    
    with open(FILE_USER, "w") as f:
        json.dump({"users": users}, f, indent=2)
    print(f"✅ User '{username_baru}' berhasil ditambah!")

def jendela_utama(username):
    while True:
        print(f"\n=== MENU UTAMA | User: {username} ===")
        print("1. Lihat Data Siswa")
        print("2. Tambah User Baru") 
        print("3. Logout")
        
        pilihan = input("Pilih 1-3: ")
        if pilihan == "1":
            print(">> Menampilkan data siswa SMKNX...")
        elif pilihan == "2":
            tambah_user()
        elif pilihan == "3":
            print(">> Logout berhasil")
            break
        else:
            print(">> Menu tidak valid")
