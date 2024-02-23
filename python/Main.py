from Shirt import Shirt
from tabulate import tabulate # library untuk tabel

if __name__ == "__main__":
    listProducts = []
    
    numProducts = int(input("Masukkan berapa banyak produk yang ingin ditambah: \n"))

    print("Masukkan detail untuk produk:")
    for i in range(numProducts):
        # Meminta input untuk setiap atribut produk
        id, name, brand, price, size, material, gender, color, sleeveType = input().split()

        # Membuat objek Kemeja
        shirt = Shirt()
        
        # Mengatur atribut-atribut produk
        shirt.setIdProduct(id)
        shirt.setName(name)
        shirt.setBrand(brand)
        shirt.setPrice(price)
        shirt.setSize(size)
        shirt.setMaterial(material)
        shirt.setGender(gender)
        shirt.setColor(color)
        shirt.setSleeveType(sleeveType)

        # Menambahkan produk ke dalam list produk
        listProducts.append(shirt)

    # Membuat data untuk tabel
    table_data = []
    for p in listProducts:
        table_data.append([p.getIdProduct(), p.getName(), p.getBrand(), p.getPrice(), p.getSize(), p.getMaterial(), p.getGender(), p.getColor(), p.getSleeveType()])

    # Menampilkan tabel dengan menggunakan tabulate
    headers = ["Product", "Name", "Brand", "Price", "Size", "Material", "Gender", "Color", "Sleeve Type"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
