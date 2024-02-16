class Product {
    private int idProduct;
    private String name;
    private String brand;
    private double price;

    Product()
    {

    }
    public Product(int id, String name, String brand, double price)
    {
        this.idProduct = id;
        this.name = name;
        this.brand = brand;
        this.price = price;
    }

    public int getIdProduct()
    {
        return idProduct;
    }

    public void setIdProduct(int idProduct)
    {
        this.idProduct = idProduct;
    }

    public String getName()
    {
        return name;
    }

    public void setName(String name)
    {
        this.name = name;
    }

    public String getBrand()
    {
        return brand;
    }

    public void setBrand(String brand)
    {
        this.brand = brand;
    }

    public double getPrice()
    {
        return price;
    }

    public void setPrice(double price)
    {
        this.price = price;
    }

}
