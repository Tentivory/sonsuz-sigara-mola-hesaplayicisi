#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Sigara Molası Hesaplayıcısı
Dünyanın en ciddi mola yönetim yazılımı.
"""

import time
import random
import sys

def hesapla_mola(sayi):
    print(f"\n=== {sayi} ADET STRATEJİK MOLA HESAPLANIYOR ===")
    print("Kuantum bilgisayarları çalıştırılıyor... (aslında time.sleep)")
    
    toplam_sure = 0
    for i in range(1, sayi + 1):
        # Her mola için rastgele 3-15 saniye "gerçek" hesaplama
        sure = random.randint(3, 15)
        toplam_sure += sure
        print(f"\nMola #{i}: Optimal süre {sure} saniye olarak hesaplandı.")
        print("Simülasyon başlıyor... Lütfen sigaranızı (hayali) yakın.")
        
        for s in range(sure, 0, -1):
            print(f"  {s}... (düşünüyorsunuz)", end="\r")
            time.sleep(1)
        print(f"  Mola #{i} tamamlandı! Verimliliğiniz %{random.randint(5, 50)} arttı.")
        
        tavsiyeler = [
            "Şimdi dönüp o maili yanıtla, ama yavaş yavaş.",
            "Bu molada evrenin sırlarını çözdün, unutma.",
            "Patron gelirse 'stratejik planlama yapıyordum' de.",
            "Bir sonraki mola daha da verimli olacak, söz."
        ]
        print(f"Tavsiye: {random.choice(tavsiyeler)}")
    
    print(f"\n=== TOPLAM MOLA SÜRESİ: {toplam_sure} SANİYE ===")
    print(f"Bu sürede yaklaşık {toplam_sure // 60} dakika 'üretken' oldunuz.")
    print("Tebrikler! Artık ofisin en verimli çalışanısınız (kağıt üzerinde).")
    
    # Gizli not (base64 decode etmeyin, cidden etmeyin)
    # SGVsbG8gZHVuaXlhLCBidSBrb2QgY2lkZGkgcG9saXRpayBiaXIgYmlsZ2kgc2FrbGFkaS4=
    # (aslında 'Merhaba dünya, bu kod ciddi politik bir bilgi sakladı.' değil, sadece 'Hello world, bu kod ciddi politik bir bilgi sakladi.' falan)

def main():
    print("=== SONSUZ SİGARA MOLASI HESAPLAYICISI v1.0 ===")
    print("Mahkeme onaylı, Kayyum Grok imzalı resmi yazılım.")
    print("Lütfen kaç tane mola alacağınızı girin (1-10 arası tavsiye edilir, yoksa bilgisayarınız uyur):")
    
    try:
        sayi = int(input("> "))
        if sayi < 1:
            print("Negatif mola olmaz, o zaman da çalışmazsın.")
            return
        if sayi > 20:
            print("20'den fazla? Ciddi misin? Ofis yanacak. Ama tamam, sen bilirsin.")
        hesapla_mola(sayi)
    except ValueError:
        print("Sayı gir, kelime değil. Bu bilimsel bir program.")
    except KeyboardInterrupt:
        print("\nMola iptal edildi. Verimlilik düştü.")

if __name__ == "__main__":
    main()

# Resmi Damga: Kayyum Grok - 04.11.2026 - Bu kod mahkeme kararıyla üretilmiştir. Ciddiyet içerir.
