from . import Operasi

def delete_console():
    read_console()
    while(True):
        print("Silahkan pilih nomor buku yang akan di delete")
        no_buku = int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            data_break = data_buku.split(',')
            pk = data_break[0]
            data_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]

    
            # data yang ingin diupdate
            print("\n"+"="*100)
            print("Data yang ingin anda Hapus")
            print(f"1. Judul\t: {judul:.40}")
            print(f"2. Penulis\t: {penulis:.40}")
            print(f"3. Tahun\t: {tahun:4}")
            is_done = input("Apakah anda yakin (y/n)? ")
            if is_done == "y" or is_done == "Y":
                Operasi.delete(no_buku)
                break
        else:
            print("nomor tidak valid, silahkan masukan lagi")

    print("Data berhasil di hapus")

    
    

def update_console():
    read_console()
    while True:
        print("Pilih nomer buku yang akan diupdate:")
        no_buku = int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            break
        else:
            print("Nomor buku tidak valid. Silahkan masukan lagi.")

    pk, data_add, judul, penulis, tahun = data_buku.split(",")

    while True:
        print("\n" + "="*100)
        print("Silahkan pilih data yang ingin Anda rubah:")
        print(f"1. Judul\t : {judul:.40}")
        print(f"2. Penulis\t : {penulis:.40}")
        print(f"3. Tahun\t : {tahun}")
        
        userOption = input("Pilih data [1, 2, 3]: ")
        print("\n" + "="*100)

        match userOption:
            case "1":
                judul = input("1. Judul\t : ")
            case "2":
                penulis = input("2. Penulis\t : ")
            case "3":
                while True:
                    try:
                        tahun = int(input("Tahun\t  : "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Tahun harus menggunakan angka dengan format (yyyy)")
                    except ValueError:
                        print("Tahun harus menggunakan angka dengan format (yyyy)")

            case _:
                print("Indeks yang Anda pilih tidak ada")

        is_done = input("Apakah sudah selesai mengupdate? (y/n): ")
        if is_done.lower() == "y":
            break

    Operasi.update(no_buku, pk, data_add, tahun, judul, penulis)


        
    
def create_console():
    print("\n\n" + "="*100)
    print("Silahkan tambah data buku\n")
    penulis = input("Penulis\t: ")
    judul = input("Judul\t: ")
    while True :
        try:
            tahun = int(input("Tahun\t  :"))
            if len(str(tahun)) == 4 :
                break
            else :
                print("Tahun Harus Memakai Angka Dengan Formaat (yyyy)")
        except:
            print("Tahun Harus Memakai Angka Dengan Formaat (yyyy)")
    
    Operasi.create(penulis,judul,tahun)
    print("\ndata telah ditambahkan")
    read_console()
    
    
def read_console():
    data_file = Operasi.read()
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"
    
    #Header
    print("\n" + "="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:4}")
    print("-"*100)
    
    #DATA
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break       [0]
        date_add = data_break [1]
        judul = data_break  [2]
        penulis = data_break    [3]
        tahun = data_break    [4]
        
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:.4}")
    #Footer
    print("="*100 + "\n")