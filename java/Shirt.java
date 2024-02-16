class Shirt extends Clothing{
    private String color;
    private String sleeveType;

    // Konstruktor default untuk membuat objek Kemeja dengan nilai awal
    Shirt()
    {
        
    }

    // Konstruktor untuk membuat objek Kemeja baru dengan detail yang diberikan
    public Shirt( String color, String sleveType) {
        this.color = color;
        this.sleeveType = sleveType;
    }

    // Getter dan setter untuk atribut color
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    // Getter dan setter untuk atribut sleeveType
    public String getSleeveType() {
        return sleeveType;
    }

    public void setSleeveType(String sleeveType) {
        this.sleeveType = sleeveType;
    }

}
