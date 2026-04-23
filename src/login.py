from login import login, jendela_utama

def main():
    berhasil, username = login()
    if berhasil:
        jendela_utama(username)

if __name__ == "__main__":
    main()
