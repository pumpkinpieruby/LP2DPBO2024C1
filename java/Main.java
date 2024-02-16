import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Shirt> listProducts = new ArrayList<>();

        System.out.print("masukan berapa banyak produk yang ingin ditambah: \n");
        int numProducts = scanner.nextInt();
        scanner.nextLine();

        for(int i = 0; i < numProducts; i++) {
            System.out.println("masukan detail untuk produk" + (i + 1) + ":");
            int id = scanner.nextInt();
            String name = scanner.next();
            String brand = scanner.next();
            double price = scanner.nextDouble();
            String size = scanner.next();
            String material = scanner.next();
            String gender = scanner.next();
            String color = scanner.next();
            String sleeveType = scanner.next();

            // Membuat objek Shirt baru untuk setiap produk
            Shirt shirt = new Shirt();
            shirt.setIdProduct(id);
            shirt.setName(name);
            shirt.setBrand(brand);
            shirt.setPrice(price);
            shirt.setSize(size);
            shirt.setMaterial(material);
            shirt.setGender(gender);
            shirt.setColor(color);
            shirt.setSleeveType(sleeveType);

            listProducts.add(shirt);
        }

        for (int i = 0; i < listProducts.size(); i++) {
            System.out.println("Detail Produk ke-" + (i + 1) + ":");
            System.out.println("ID Product : " + listProducts.get(i).getIdProduct());
            System.out.println("Name : " + listProducts.get(i).getName());
            System.out.println("Brand : " + listProducts.get(i).getBrand());
            System.out.println("Price : " + listProducts.get(i).getPrice());
            System.out.println("Size : " + listProducts.get(i).getSize());
            System.out.println("Material : " + listProducts.get(i).getMaterial());
            System.out.println("Gender : " + listProducts.get(i).getGender());
            System.out.println("Color : " + listProducts.get(i).getColor());
            System.out.println("Sleeve Type : " + listProducts.get(i).getSleeveType());
            System.out.println();
        }

        scanner.close();
    }
}
