# Membuat Struktur Data Dictionary
userLogin = {"name":"Abdi malika putra", "age":17,"role":"pelajar"}
print(type(userLogin))

# Mengakses Data
print(f"Nama Akun: {userLogin['name']}")
print(f"Umur Akun: {userLogin['age']}")
print(f"Role Akun: {userLogin['role']}")

#Akses Data Seluruh
print(userLogin.items())
print(userLogin.keys())
print(userLogin.values())

# Menambah data kedalam dictionary big-0 0(1)
userLogin["email"] = "abdimalikaputra@example.com"
print(userLogin)

# menghapus data pada dictionary big-0 0(1)
del userLogin["email"]
print(userLogin)

# mengubah data pada dictionary big-0 0(1)
userLogin["role"] = "mahasiswa"
print(userLogin)

# nested dictionary
dbUser = {
    "user1": {"name":"Abdi malika putra", "age":17,"role":"pelajar"},
    "user2": {"name":"andi saputra", "age":18,"role":"pelajar"},
    "user3": {"name":"budi sartono", "age":19,"role":"pelajar"}
}   
print(dbUser)

# akses value base key
print(dbUser["user1"])

# melakukan pencarian data pada dictionary big-0 0(1)
findWord = input("Masukkan kata yang ingin dicari: ")
if findWord in dbUser:
    print("Data ditemukan: ")
    print(dbUser[findWord])
else:
    print("Data tidak ditemukan")
    


