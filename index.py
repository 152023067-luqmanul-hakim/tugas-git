data_panen = {
    'lokasi1' : {
        'nama_lokasi' : 'Kebun A',
        'hasil_panen' : {
            'padi' : 1200,
            'jagung' : 800,
            'kedelai' : 500
        }
    },
    'lokasi2' : {
        'nama_lokasi' : 'Kebun B',
        'hasil_panen' : {
            'padi' : 1500,
            'jagung' : 900,
            'kedelai' : 450
        }
    },
    'lokasi3' : {
        'nama_lokasi' : 'Kebun C',
        'hasil_panen' : {
            'padi' : 1100,
            'jagung' : 750,
            'kedelai' : 600
        }
    },
    'lokasi4' : {
        'nama_lokasi' : 'Kebun D',
        'hasil_panen' : {
            'padi' : 1300,
            'jagung' : 850,
            'kedelai' : 550
        }
    },
    'lokasi5' : {
        'nama_lokasi' : 'Kebun E',
        'hasil_panen' : {
            'padi' : 1400,
            'jagung' : 950,
            'kedelai' : 480
        }
    },
}

padi_kedelai = {}

print("Data hasil panen :")
for a,b in data_panen.items():
    padi = b['hasil_panen']['padi']
    jagung = b['hasil_panen']['jagung']
    kedelai = b['hasil_panen']['kedelai']
    print(f"Lokasi : {a}")
    print(f"Nama Lokasi : {b['nama_lokasi']}")
    print("Hasil Panen : ")
    print(f"- Padi   : {padi}")
    print(f"- Jagung : {jagung}")
    print(f"- Kedelai: {kedelai}")

    if padi > 1300 or jagung > 800 :
        print("Kondisi : Memerlukan perhatian khusus\n")
    else:
        print("Kondisi : Dalam kondisi baik\n")

    padi_kedelai[a] = {
        'padi' : b['hasil_panen']['padi'],
        'kedelai' : b['hasil_panen']['kedelai']
    }

print("Data spesifik lokasi : ")
jagungLok2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"Hasil panen jagung di lokasi2 adalah {jagungLok2}")

namaLok3 = data_panen['lokasi3']['nama_lokasi']
print(f"Nama lokasi dari lokasi 3 adalah {namaLok3}\n")


