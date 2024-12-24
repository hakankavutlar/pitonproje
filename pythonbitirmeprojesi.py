def duzenliListe(girdi):
    cikti = []  # Düzleştirilmiş elemanları saklamak için bir liste
    for item in girdi:  # Girdi listesindeki her elemanı sırayla işle
        if isinstance(item, list):  # Eğer eleman bir liste ise
            cikti.extend(duzenliListe(item))  # Özyineleme yaparak düzleştirilen elemanları ekle
        else:  # Eğer eleman bir liste değilse
            cikti.append(item)  # Doğrudan son listeye ekle
    return cikti


girdi = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
sonuc = duzenliListe(girdi)
print(sonuc)