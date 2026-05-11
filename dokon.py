# ============================================
#      DO'KON VA MAHSULOTLAR - OOP (Python)
# ============================================

class Mahsulot:
    """Asosiy mahsulot sinfi"""

    def __init__(self, nomi, narxi, miqdori):
        self.nomi = nomi
        self.__narxi = narxi      # Private (inkapsulatsiya)
        self.__miqdori = miqdori  # Private (inkapsulatsiya)

    @property
    def narxi(self):
        return self.__narxi

    @narxi.setter
    def narxi(self, yangi_narx):
        if yangi_narx <= 0:
            print("❌ Narx musbat bo'lishi kerak!")
        else:
            self.__narxi = yangi_narx

    @property
    def miqdori(self):
        return self.__miqdori

    def qoshish(self, son):
        if son <= 0:
            print("❌ Miqdor musbat bo'lishi kerak!")
            return
        self.__miqdori += son
        print(f"📦 {self.nomi}: {son} ta qo'shildi. Jami: {self.__miqdori} ta")

    def kamaytirish(self, son):
        if son > self.__miqdori:
            print(f"❌ Omborda yetarli {self.nomi} yo'q! Mavjud: {self.__miqdori} ta")
            return False
        self.__miqdori -= son
        return True

    def malumot(self):
        print(f"🛒 {self.nomi} | Narx: {self.__narxi:,.0f} so'm | Miqdor: {self.__miqdori} ta")

    def __str__(self):
        return f"{self.nomi} ({self.__narxi:,.0f} so'm)"


# ─────────────────────────────────────────────
# Meros (Inheritance)
# ─────────────────────────────────────────────

class OziqqovqatMahsulot(Mahsulot):
    """Oziq-ovqat mahsuloti - muddati bor"""

    def __init__(self, nomi, narxi, miqdori, yaroqlilik_kuni):
        super().__init__(nomi, narxi, miqdori)
        self.yaroqlilik_kuni = yaroqlilik_kuni  # kun

    def malumot(self):
        super().malumot()
        print(f"   ⏳ Yaroqlilik muddati: {self.yaroqlilik_kuni} kun")

    def __str__(self):
        return super().__str__() + f" [Oziq-ovqat, {self.yaroqlilik_kuni} kun]"


class ElektronikaMahsulot(Mahsulot):
    """Elektronika mahsuloti - kafolat bor"""

    def __init__(self, nomi, narxi, miqdori, kafolat_oy):
        super().__init__(nomi, narxi, miqdori)
        self.kafolat_oy = kafolat_oy

    def malumot(self):
        super().malumot()
        print(f"   🔧 Kafolat muddati: {self.kafolat_oy} oy")

    def __str__(self):
        return super().__str__() + f" [Elektronika, {self.kafolat_oy} oy kafolat]"


class KiyimMahsulot(Mahsulot):
    """Kiyim mahsuloti - o'lchami bor"""

    def __init__(self, nomi, narxi, miqdori, olcham):
        super().__init__(nomi, narxi, miqdori)
        self.olcham = olcham  # S, M, L, XL

    def malumot(self):
        super().malumot()
        print(f"   👕 O'lcham: {self.olcham}")

    def __str__(self):
        return super().__str__() + f" [Kiyim, {self.olcham}]"


# ─────────────────────────────────────────────
# Savat sinfi
# ─────────────────────────────────────────────

class Savat:
    def __init__(self):
        self.mahsulotlar = {}  # {mahsulot: son}

    def qoshish(self, mahsulot: Mahsulot, son=1):
        if mahsulot.kamaytirish(son):
            if mahsulot in self.mahsulotlar:
                self.mahsulotlar[mahsulot] += son
            else:
                self.mahsulotlar[mahsulot] = son
            print(f"✅ {mahsulot.nomi} savatga qo'shildi ({son} ta)")

    def olib_tashlash(self, mahsulot: Mahsulot):
        if mahsulot in self.mahsulotlar:
            son = self.mahsulotlar.pop(mahsulot)
            mahsulot.qoshish(son)
            print(f"🗑️ {mahsulot.nomi} savatdan olib tashlandi")
        else:
            print("❌ Bu mahsulot savatda yo'q!")

    def jami_narx(self):
        return sum(m.narxi * son for m, son in self.mahsulotlar.items())

    def korsatish(self):
        print("\n🛒 Savat tarkibi:")
        if not self.mahsulotlar:
            print("  Savat bo'sh.")
            return
        for m, son in self.mahsulotlar.items():
            print(f"  - {m.nomi}: {son} ta x {m.narxi:,.0f} so'm = {son * m.narxi:,.0f} so'm")
        print(f"  {'─'*40}")
        print(f"  💵 Jami: {self.jami_narx():,.0f} so'm")


# ─────────────────────────────────────────────
# Do'kon sinfi
# ─────────────────────────────────────────────

class Dokon:
    def __init__(self, nomi):
        self.nomi = nomi
        self.mahsulotlar = []
        self.sotuv_tarixi = []

    def mahsulot_qoshish(self, mahsulot: Mahsulot):
        self.mahsulotlar.append(mahsulot)
        print(f"🏪 Do'konga qo'shildi: {mahsulot}")

    def assortiment(self):
        print(f"\n🏪 {self.nomi} - Barcha mahsulotlar:")
        print("=" * 45)
        for m in self.mahsulotlar:
            m.malumot()
        print("=" * 45)

    def sotib_olish(self, savat: Savat, mijoz_ismi):
        jami = savat.jami_narx()
        if jami == 0:
            print("❌ Savat bo'sh!")
            return
        savat.korsatish()
        print(f"\n🎉 {mijoz_ismi}, xaridingiz uchun rahmat!")
        print(f"💳 To'langan summa: {jami:,.0f} so'm")
        self.sotuv_tarixi.append({
            "mijoz": mijoz_ismi,
            "summa": jami
        })
        savat.mahsulotlar.clear()

    def sotuv_hisobot(self):
        print(f"\n📊 {self.nomi} - Sotuv hisoboti:")
        if not self.sotuv_tarixi:
            print("  Hali sotuv amalga oshirilmagan.")
            return
        jami = 0
        for i, s in enumerate(self.sotuv_tarixi, 1):
            print(f"  {i}. {s['mijoz']}: {s['summa']:,.0f} so'm")
            jami += s['summa']
        print(f"  {'─'*35}")
        print(f"  💰 Umumiy daromad: {jami:,.0f} so'm")


# ============================================
#              DEMO - Sinov
# ============================================

if __name__ == "__main__":
    print("=" * 50)
    print("       SmartShop Do'kon Tizimi!")
    print("=" * 50)

    # Do'kon yaratish
    dokon = Dokon("SmartShop")

    # Mahsulotlar yaratish
    non     = OziqqovqatMahsulot("Non", 8_000, 50, yaroqlilik_kuni=3)
    sut     = OziqqovqatMahsulot("Sut (1L)", 15_000, 30, yaroqlilik_kuni=7)
    telefon = ElektronikaMahsulot("Samsung A55", 7_500_000, 10, kafolat_oy=24)
    noutbuk = ElektronikaMahsulot("Lenovo IdeaPad", 12_000_000, 5, kafolat_oy=12)
    futbolka= KiyimMahsulot("Futbolka", 85_000, 20, olcham="L")
    shim    = KiyimMahsulot("Shim", 250_000, 15, olcham="M")

    # Do'konga qo'shish
    for m in [non, sut, telefon, noutbuk, futbolka, shim]:
        dokon.mahsulot_qoshish(m)

    # Assortimentni ko'rish
    dokon.assortiment()

    # 1-mijoz xaridi
    print("\n--- Alining xaridi ---")
    ali_savat = Savat()
    ali_savat.qoshish(non, 2)
    ali_savat.qoshish(sut, 1)
    ali_savat.qoshish(futbolka, 1)
    dokon.sotib_olish(ali_savat, "Ali Valiyev")

    # 2-mijoz xaridi
    print("\n--- Malikning xaridi ---")
    malik_savat = Savat()
    malik_savat.qoshish(telefon, 1)
    malik_savat.qoshish(shim, 2)
    dokon.sotib_olish(malik_savat, "Malik Rahimov")

    # Narxni o'zgartirish (inkapsulatsiya orqali)
    print("\n--- Narx yangilash ---")
    non.narxi = 9_000
    non.malumot()

    # Sotuv hisoboti
    dokon.sotuv_hisobot()