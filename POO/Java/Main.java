import javax.swing.text.Document;

class Main{
    public static void main(String[] args) {
        System.out.println("Hola Mundo!");
        Car car = new Car("AMQ123", new Account("Andres Herrera", "AND123"));
        car.passenger = 4;
        car.printDataCar(); //Se manda a llamar del objeto coshe xd

        Car car2 = new Car("QWE567", new Account("Andrea Herrera", "ANA667"));
        car2.passenger = 3;
        car2.printDataCar();
    }
}