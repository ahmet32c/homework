from abc import ABC, abstractmethod
class Kaynak(ABC):
    def __init__(self, baslik: str, kayitNo: str):
        self._baslik = baslik
        self._kayitNo = kayitNo

    @property
    def baslik(self):
        return self._baslik

    @baslik.setter
    def baslik(self, value):
        self._baslik = value

    @property
    def kayitNo(self):
        return self._kayitNo

    @kayitNo.setter
    def kayitNo(self, value):
        self._kayitNo = value

    @abstractmethod
    def __str__(self):
        pass

class Kitap(Kaynak):
    def __init__(self, baslik: str, kayitNo: str, yazar: str, sayfa_sayisi: int):
        super().__init__(baslik, kayitNo)
        self._yazar = yazar
        self._sayfa_sayisi = sayfa_sayisi

    @property
    def yazar(self):
        return self._yazar

    @yazar.setter
    def yazar(self, value):
        self._yazar = value

    @property
    def sayfa_sayisi(self):
        return self._sayfa_sayisi

    @sayfa_sayisi.setter
    def sayfa_sayisi(self, value):
        self._sayfa_sayisi = int(value)

    def __str__(self):
        return f"Kitap - Başlık: {self.baslik}, KayıtNo: {self.kayitNo}, Yazar: {self.yazar}, Sayfa: {self.sayfa_sayisi}"

class Dergi(Kaynak):
    def __init__(self, baslik: str, kayitNo: str, yayin_donemi: str, sayi_no: str):
        super().__init__(baslik, kayitNo)
        self._yayin_donemi = yayin_donemi
        self._sayi_no = sayi_no

    @property
    def yayin_donemi(self):
        return self._yayin_donemi

    @yayin_donemi.setter
    def yayin_donemi(self, value):
        self._yayin_donemi = value

    @property
    def sayi_no(self):
        return self._sayi_no

    @sayi_no.setter
    def sayi_no(self, value):
        self._sayi_no = value

    def __str__(self):
        return f"Dergi - Başlık: {self.baslik}, KayıtNo: {self.kayitNo}, Dönem: {self.yayin_donemi}, Sayı: {self.sayi_no}"


class Islem(ABC):
    @abstractmethod
    def ekle(self):
        pass

    @abstractmethod
    def sil(self):
        pass

    @abstractmethod
    def guncelle(self):
        pass

    @abstractmethod
    def listele(self):
        pass


class KitapIslem(Islem):
    def __init__(self):
        self._kitaplar = []

    # Yardımcı: kayitNo ile var mı kontrolü
    def _bul_index_by_kayitno(self, kayitNo):
        for i, k in enumerate(self._kitaplar):
            if k.kayitNo == kayitNo:
                return i
        return None

    def ekle(self):
        baslik = input("Kitabın başlığını girin: ").strip()
        kayitNo = input("Kitabın kayıt numarasını girin: ").strip()
        if self._bul_index_by_kayitno(kayitNo) is not None:
            print("Aynı kayıt numarasına ait bir kitap zaten var. Eklenemedi.")
            return
        yazar = input("Kitabın yazarını girin: ").strip()
        try:
            sayfa = int(input("Kitabın sayfa sayısını girin: ").strip())
        except ValueError:
            print("Sayfa sayısı sayı olmalı. Eklenemedi.")
            return
        kitap = Kitap(baslik, kayitNo, yazar, sayfa)
        self._kitaplar.append(kitap)
        print("Kitap başarıyla eklendi.")
        print(f"Toplam Kitap Sayısı: {len(self._kitaplar)}")

    def sil(self):
        kayitNo = input("Silinecek kitabın kayıt numarasını girin: ").strip()
        idx = self._bul_index_by_kayitno(kayitNo)
        if idx is None:
            print("Kayıt bulunamadı.")
            return
        removed = self._kitaplar.pop(idx)
        print(f"Silindi: {removed.baslik} ({removed.kayitNo})")
        print(f"Toplam Kitap Sayısı: {len(self._kitaplar)}")

    def guncelle(self):
        kayitNo = input("Güncellenecek kitabın kayıt numarasını girin: ").strip()
        idx = self._bul_index_by_kayitno(kayitNo)
        if idx is None:
            print("Kayıt bulunamadı.")
            return
        kitap = self._kitaplar[idx]
        print("Boş bırakılırsa mevcut değer korunur.")
        yeni_baslik = input(f"Yeni başlık ({kitap.baslik}): ").strip()
        yeni_yazar = input(f"Yeni yazar ({kitap.yazar}): ").strip()
        yeni_sayfa = input(f"Yeni sayfa sayısı ({kitap.sayfa_sayisi}): ").strip()
        if yeni_baslik:
            kitap.baslik = yeni_baslik
        if yeni_yazar:
            kitap.yazar = yeni_yazar
        if yeni_sayfa:
            try:
                kitap.sayfa_sayisi = int(yeni_sayfa)
            except ValueError:
                print("Sayfa sayısı sayı olmalı. Güncelleme sırasında atlandı.")
        print("Güncelleme tamamlandı.")

    def listele(self):
        if not self._kitaplar:
            print("Kayıt bulunamadı.")
            return
        for k in self._kitaplar:
            print(k)

    def kitap_sayisi(self):
        return len(self._kitaplar)

class DergiIslem(Islem):
    def __init__(self):
        self._dergiler = []

    def _bul_index_by_kayitno(self, kayitNo):
        for i, d in enumerate(self._dergiler):
            if d.kayitNo == kayitNo:
                return i
        return None

    def ekle(self):
        baslik = input("Derginin başlığını girin: ").strip()
        kayitNo = input("Derginin kayıt numarasını girin: ").strip()
        if self._bul_index_by_kayitno(kayitNo) is not None:
            print("Aynı kayıt numarasına ait bir dergi zaten var. Eklenemedi.")
            return
        yayin_donemi = input("Yayın dönemi (ör: aylık/haftalık) girin: ").strip()
        sayi_no = input("Sayı numarasını girin: ").strip()
        dergi = Dergi(baslik, kayitNo, yayin_donemi, sayi_no)
        self._dergiler.append(dergi)
        print("Dergi başarıyla eklendi.")
        print(f"Toplam Dergi Sayısı: {len(self._dergiler)}")

    def sil(self):
        kayitNo = input("Silinecek derginin kayıt numarasını girin: ").strip()
        idx = self._bul_index_by_kayitno(kayitNo)
        if idx is None:
            print("Kayıt bulunamadı.")
            return
        removed = self._dergiler.pop(idx)
        print(f"Silindi: {removed.baslik} ({removed.kayitNo})")
        print(f"Toplam Dergi Sayısı: {len(self._dergiler)}")

    def guncelle(self):
        kayitNo = input("Güncellenecek derginin kayıt numarasını girin: ").strip()
        idx = self._bul_index_by_kayitno(kayitNo)
        if idx is None:
            print("Kayıt bulunamadı.")
            return
        dergi = self._dergiler[idx]
        print("Boş bırakılırsa mevcut değer korunur.")
        yeni_baslik = input(f"Yeni başlık ({dergi.baslik}): ").strip()
        yeni_donem = input(f"Yeni yayın dönemi ({dergi.yayin_donemi}): ").strip()
        yeni_sayi = input(f"Yeni sayı no ({dergi.sayi_no}): ").strip()
        if yeni_baslik:
            dergi.baslik = yeni_baslik
        if yeni_donem:
            dergi.yayin_donemi = yeni_donem
        if yeni_sayi:
            dergi.sayi_no = yeni_sayi
        print("Güncelleme tamamlandı.")

    def listele(self):
        if not self._dergiler:
            print("Kayıt bulunamadı.")
            return
        for d in self._dergiler:
            print(d)

    def dergi_sayisi(self):
        return len(self._dergiler)


class Menu:
    def __init__(self, kitap_islem: KitapIslem, dergi_islem: DergiIslem):
        self.kitap_islem = kitap_islem
        self.dergi_islem = dergi_islem

    def goster(self):
        print("\n1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Kitap Güncelle")
        print("4. Kitapları Listele")
        print("5. Dergi Ekle")
        print("6. Dergi Sil")
        print("7. Dergi Güncelle")
        print("8. Dergileri Listele")
        print("9. Çıkış")

    def calistir(self):
        while True:
            self.goster()
            secim = input("Yapmak istediğiniz işlemi seçin (1-9): ").strip()
            if secim == "1":
                self.kitap_islem.ekle()
            elif secim == "2":
                self.kitap_islem.sil()
            elif secim == "3":
                self.kitap_islem.guncelle()
            elif secim == "4":
                self.kitap_islem.listele()
            elif secim == "5":
                self.dergi_islem.ekle()
            elif secim == "6":
                self.dergi_islem.sil()
            elif secim == "7":
                self.dergi_islem.guncelle()
            elif secim == "8":
                self.dergi_islem.listele()
            elif secim == "9":
                print("Çıkılıyor...")
                break
            else:
                print("Geçersiz seçim. Tekrar deneyin.")

# Program başlatma
if __name__ == "__main__":
    kitap_islem = KitapIslem()
    dergi_islem = DergiIslem()
    menu = Menu(kitap_islem, dergi_islem)
    menu.calistir()
