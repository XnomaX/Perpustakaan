from . import Database
from .Util import random_string
import time
import os

def delete(no_buku):
    try:
        with open("data_temp.txt", 'w', encoding="utf-8") as temp_file:
            with open(Database.DB_NAME, 'r', encoding="utf-8") as file:
                for counter, content in enumerate(file):
                    if counter != no_buku - 1:
                        temp_file.write(content)

    except FileNotFoundError:
        print("File tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
    
    try:
        os.replace("data_temp.txt", Database.DB_NAME)
    except FileNotFoundError:
        print("File tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
    

def update(no_buku, pk, data_add, tahun, judul, penulis):
    data = {
        "pk": pk,
        "date_add": data_add,
        "penulis": penulis,
        "judul": judul,
        "tahun": tahun
    }

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    panjang_data = len(data_str)

    try:
        with open(Database.DB_NAME, 'r+', encoding="utf-8") as file:
            file.seek(panjang_data * (no_buku - 1))
            file.write(data_str)
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
        

def create(penulis,judul,tahun):
    
    data = Database.TEMPLATE.copy()
    
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)
    
    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    
    try:
        with open(Database.DB_NAME,'a',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Udah gabisa nambah data lagi coy")
    
    

def create_first_data():
    penulis = input("Penulis :")
    judul = input("Judul : ")
    while True :
        try:
            tahun = int(input("Tahun\t  :"))
            if len(str(tahun)) == 4 :
                break
            else :
                print("Tahun Harus Memakai Angka Dengan Formaat (yyyy)")
        except:
            print("Tahun Harus Memakai Angka Dengan Formaat (yyyy)")
    
    data = Database.TEMPLATE.copy()
    
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)
    
    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Udah gagal coyyyyy")

def read(**kwargs):
    try:
        with open(Database.DB_NAME,'r') as file :
            content = file.readlines()
            jumlah_buku = len(content)
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else : 
                    return content[index_buku]
            else :
                return content
    except:
        print("database errorr")
        return False