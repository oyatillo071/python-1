print("=== TOPSHIRIQLAR RO'YXATI ===")
print("1. Valyuta konvertori")
print("2. Aylana uzunligi va yuzi")
print("3. Vaqtni sekundlarga o'tkazish")
print("4. Kassa cheki hisoblagichi")
print("5. Raqamlar yig'indisini topish (2 xonali son)")
print("6. Haroratni o'girish (Selsiy -> Farengeyt)")
print("=============================\n")

which_code_run = int(input("Qaysi kodni ishga tushirishni xohlaysiz? (1-6): "))

match which_code_run:
    case 1:
        # 1-topshiriq uchun versiyalar ro'yxati
        print("\n--- Valyuta konvertori versiyalari ---")
        print("1. USD -> UZS (Dollardan so'mga)")
        print("2. UZS -> USD (So'mdan dollarga)")
        print("3. Moslashuvchan kurs bilan (USD -> UZS kursni foydalanuvchi kiritadi)")
        
        version = int(input("Qaysi versiyani tanlaysiz? (1-3): "))
        
        match version:
            case 1:
                # 1-versiya: USD -> UZS (12 800 so'm deb olingan)
                user_sum = float(input("USD valyutasida qiymat kiriting: "))
                user_uzs_value = user_sum * 12800
                print(f"Kiritilgan USD qiymati: {user_sum}")
                print(f"Konvertatsiya natijasi (UZS): {user_uzs_value} so'm")
            case 2:
                # 2-versiya: UZS -> USD
                user_sum = float(input("UZS valyutasida qiymat kiriting: "))
                user_dollar_value = user_sum / 12800
                print(f"Kiritilgan UZS qiymati: {user_sum}")
                print(f"Konvertatsiya natijasi (USD): {user_dollar_value} $")
            case 3:
                # 3-versiya: Kurs foydalanuvchi tomonidan kiritiladi
                user_sum = float(input("USD valyutasida qiymat kiriting: "))
                custom_rate = float(input("Hozirgi USD kursini kiriting (masalan, 12800): "))
                user_uzs_value = user_sum * custom_rate
                print(f"Kiritilgan USD qiymati: {user_sum}")
                print(f"Konvertatsiya natijasi (UZS, kurs {custom_rate}): {user_uzs_value} so'm")
            case _:
                print("Noto'g'ri versiya tanlandi!")

    case 2:
        # 2. Aylana uzunligi va yuzi
        r = float(input("Aylananing radiusini (r) kiriting: "))
        pi = 3.14
        L = 2 * pi * r
        S = pi * (r ** 2)
        print(f"Aylana uzunligi (L): {L}")
        print(f"Aylana yuzi (S): {S}")

    case 3:
        # 3-topshiriq uchun versiyalar ro'yxati
        print("\n--- Vaqtni o'girish versiyalari ---")
        print("1. Soat va minut -> Sekundlarga")
        print("2. Sekundlar -> Soat, minut va sekundlarga (Reverse)")
        print("3. Sekundlar -> Faqat minutlarga (float)")
        
        version = int(input("Qaysi versiyani tanlaysiz? (1-3): "))

        match version:
            case 1:
                # 1-versiya: Soat va minutdan sekundga
                hours = int(input("Soatni kiriting: "))
                minutes = int(input("Minutni kiriting: "))
                total_seconds = (hours * 3600) + (minutes * 60)
                print(f"Kiritilgan vaqt: {hours} soat, {minutes} minut")
                print(f"Umumiy sekundlar: {total_seconds} sekund")

            case 2:
                # 2-versiya: Sekunddan soat, minut va qoldiq sekundlarga (Reverse)
                seconds = int(input("Sekundlar miqdorini kiriting: "))
                hours = seconds // 3600
                remaining_seconds = seconds % 3600
                minutes = remaining_seconds // 60
                final_seconds = remaining_seconds % 60
                
                print(f"Kiritilgan sekundlar: {seconds}")
                print(f"Natija: {hours} soat, {minutes} minut, {final_seconds} sekund")

            case 3:
                # 3-versiya: Sekundlarni daqiqalarga (minut) o'girish
                seconds = int(input("Sekundlar miqdorini kiriting: "))
                total_minutes = seconds / 60
                print(f"Kiritilgan sekundlar: {seconds}")
                print(f"Daqiqalardagi qiymati: {total_minutes} minut")

            case _:
                print("Noto'g'ri versiya tanlandi!")

    case 4:
        # 4. Kassa cheki hisoblagichi
        price1 = float(input("1-mahsulot narxini kiriting: "))
        count1 = int(input("1-mahsulot miqdorini kiriting: "))

        price2 = float(input("2-mahsulot narxini kiriting: "))
        count2 = int(input("2-mahsulot miqdorini kiriting: "))

        price3 = float(input("3-mahsulot narxini kiriting: "))
        count3 = int(input("3-mahsulot miqdorini kiriting: "))

        total_sum = (price1 * count1) + (price2 * count2) + (price3 * count3)
        print(f"Umumiy to'lanishi kerak bo'lgan summa: {total_sum} so'm")

    case 5:
        # 5. Raqamlar yig'indisini topish (2 xonali son)
        number = int(input("2 xonali son kiriting (masalan: 47): "))
        tens = number // 10
        units = number % 10
        digits_sum = tens + units
        print(f"Kiritilgan son: {number}")
        print(f"Raqamlar yig'indisi ({tens} + {units}): {digits_sum}")

    case 6:
        # 6. Haroratni o'girish (Selsiy -> Farengeyt)
        celsius = float(input("Selsiy bo'yicha haroratni kiriting: "))
        fahrenheit = celsius * (9 / 5) + 32
        print(f"Kiritilgan harorat (Selsiy): {celsius}°C")
        print(f"Farengeyt shkalasidagi qiymat: {fahrenheit}°F")

    case _:
        print("Noto'g'ri topshiriq tanlandi! 1 dan 6 gacha bo'lgan raqamni kiriting.")
