#include <bits/stdc++.h>
using namespace std;

class Product
{
    private:
        int idProduct;
        string name;
        string brand;
        string price;
    public:
    Product()
    {
        this->idProduct= '-';
        this->name = "";
        this->brand = "";
        this->price = "";

    }

    Product(int idProduct, string name, string brand, string price)
    {
        this->idProduct = idProduct;
        this->name = name;
        this->brand = brand;
        this->price = price;
    }

    int getIdProduct()
    {
        return this->idProduct;
    }

    void setIdProduct(int idProduct)
    {
        this->idProduct = idProduct;
    }

    string getName()
    {
        return this->name;
    }

    void setName(string name)
    {
        this->name = name;
    }

    string getBrand()
    {
        return this->brand;
    }

    void setBrand(string brand)
    {
        this->brand = brand;
    }

    string getPrice()
    {
        return this->price;
    }

    void setPrice(string price)
    {
        this->price = price;
    }
    
    ~Product()
    {

    }
};

