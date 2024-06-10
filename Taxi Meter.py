while True:
    kilo = int(input("ป้อนระยะทาง(กิโลเมตร) : "))
    price = 0

    if kilo > 80:
        x_kilo = (kilo - 80)
        price += x_kilo * 10.50
        kilo -= x_kilo

    if kilo > 60:
        x_kilo = (kilo - 60)
        price += x_kilo * 9
        kilo -= x_kilo

    if kilo > 40:
        x_kilo = (kilo - 40)
        price += x_kilo * 8
        kilo -= x_kilo

    if kilo > 20:
        x_kilo = (kilo - 20)
        price += x_kilo * 7.50
        kilo -= x_kilo

    if kilo > 10:
        x_kilo = (kilo - 10)
        price += x_kilo * 6.50
        kilo -= x_kilo

    if kilo > 1:
        x_kilo = (kilo - 1)
        price += x_kilo * 5.50
        kilo -= x_kilo

    if kilo == 1:
        price += 35

    if round(price) % 2 == 0:
        price += 1

    print("ค่าแท็กซี่ทั้งหมด %.0f บาท" % price)
    print("\n")

    again = input("ต้องการคำนวนค่าแท็กซี่อีกหรือไม่ ? (ถ้าใช่ให้พิมพ์ 'y') : ")
    if again.lower() != 'y':
        break

    print("\n")