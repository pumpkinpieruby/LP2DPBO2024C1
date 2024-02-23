#include <bits/stdc++.h>
#include <iomanip>
#include <vector>
#include "Shirt.cpp"
using namespace std;

int main()
{
    vector<Shirt> listShirt;
    Shirt shirts;
    int id;
    string name, brand, price, size, material, gender, color, sleeveType;

    int n;
    cout << "Masukkan berapa banyak produk yang ingin ditambah: \n";
    cin >> n;

    cout << "Masukkan detail untuk produk:\n";
    for(int i = 0; i < n; i++)
    {
        cin >> id >> name >> brand >> price >> size >> material >> gender >> color >> sleeveType;
        shirts.setIdProduct(id);
        shirts.setName(name);
        shirts.setBrand(brand);
        shirts.setPrice(price);
        shirts.setSize(size);
        shirts.setMaterial(material);
        shirts.setGender(gender);
        shirts.setColor(color);
        shirts.setSleeveType(sleeveType);

        listShirt.push_back(shirts);
    }
    // Menampilkan header
    cout << "\n+------+---------------+---------------+----------+------+---------------+----------+----------+---------------+\n";
    cout << "|  ID  |     Name      |     Brand     |  Price   | Size |   Material    |  Gender  |  Color   |  Sleeve Type  |\n";
    cout << "+------+---------------+---------------+----------+------+---------------+----------+----------+---------------+\n";

    // Menampilkan data
    for (const auto &shirt : listShirt) {
        cout << "|" << left << setw(6) << shirts.getIdProduct()
             << "|" << left << setw(15) << shirts.getName()
             << "|" << left << setw(15) << shirts.getBrand()
             << "|" << right << setw(10) << shirts.getPrice() // Menggunakan manipulator right untuk harga
             << "|" << left << setw(6) << shirts.getSize()
             << "|" << left << setw(15) << shirts.getMaterial()
             << "|" << left << setw(10) << shirts.getGender()
             << "|" << left << setw(10) << shirts.getColor()
             << "|" << left << setw(15) << shirts.getSleeveType() << "|\n";
    }

    // Menampilkan footer
    cout << "+------+---------------+---------------+----------+------+---------------+----------+----------+---------------+\n";

    return 0;
}