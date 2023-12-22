import os
import re
import time

def scan_file(file_path):
    # Zararlı yazılım imzası kontrolü yapılacak işlev
    # Burada bir veritabanı veya imza listesi kullanabilirsiniz
    
    # Örnek olarak, dosya adında "zararli" kelimesi geçtiğinde zararlı olarak işaretleyelim
    if "zararli" in file_path.lower():
        return "Zararli"  # Zararlı dosya tespit edildi
    else:
        return None  # Zararlı dosya tespit edilmedi

def detect_virus(file_path):
    # Dosyanın içeriğindeki virüs türünü tespit etmek için işlev
    # Burada bir veritabanı veya imza listesi kullanabilirsiniz
    
    # Örnek olarak, dosya içinde "Trojan" kelimesini arayalım
    with open(file_path, 'r') as file:
        content = file.read()
        if re.search(r'Trojan', content, re.IGNORECASE):
            return "Trojan"
        elif re.search(r'Worm', content, re.IGNORECASE):
            return "Worm"
        else:
            return None

def scan_directory(directory_path):
    # Dizin içindeki dosyaları tarayalım
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Animasyon için çizgileri tanımlayalım
            animation_chars = ['-', '/', '|', '\\']
            for char in animation_chars:
                time.sleep(0.1)
                print(f"Taraniyor: {char}", end='\r')
            
            virus_type = scan_file(file_path)
            if virus_type:
                print("Potansiyel zararli dosya:", file_path)
                detected_virus = detect_virus(file_path)
                if detected_virus:
                    print(f"Virüs Türü: {detected_virus}")
            else:
                print("Dosya virus icermiyor:", file_path)

# Tarama yapılacak dizini kullanıcıdan alalım
directory_to_scan = input("Tarama yapmak istediğiniz dizini girin: ")

# Dizini tarayalım
scan_directory(directory_to_scan)
