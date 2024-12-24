def donusturucu(girdi):
    cikti = []  
    for item in reversed(girdi):  # Girdi listesindeki her elemanı sırayla işle
        if isinstance(item, list):  # Eğer eleman bir liste ise
            cikti.append(donusturucu(item))  # Özyineleme yaparak düzleştirilen elemanları ekle
        else:  # Eğer eleman bir liste değilse
            cikti.append(item)  # Doğrudan son listeye ekle
    return cikti

# Örnek kullanım
girdi = [[1, 2], [3, 4], [5, 6, 7]]
sonuc = donusturucu(girdi)
print(sonuc)