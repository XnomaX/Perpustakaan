import os 
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name

match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

print("SELAMAT DATANG DI PERPUSTAKAAN DIGITAL")
print("===========SELAMAT MENCOBA============")
print("="*38)    

#mengecek database

CRUD.init_console()
    
while True:
    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print("SELAMAT DATANG DI PERPUSTAKAAN DIGITAL")
    print("===========SELAMAT MENCOBA============")
    print("="*38)
    print(f"1. Read Data")
    print(f"2. Create Data")
    print(f"3. Update Data")
    print(f"4. Delete Data\n")
    
    user_option = input("Masukan Opsi : ")
    
    match user_option :
        case "1" : CRUD.read_console()
        case "2" : CRUD.create_console()
        case "3" : CRUD.update_console()
        case "4" : CRUD.delete_console()
        
    is_done = input("Apakah Sudah Selesai (y/n) : ")
    if is_done == "Y" or is_done == "y":
        break

print("Program Berakhir KAKAK!!!!!!!!!!!")