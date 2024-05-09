import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("Informe o número do banco: ");
		int numero = scanner.nextInt();
		System.out.println();
		
		System.out.println("Valor do saldo R$");
		double saldo = scanner.nextDouble();
		System.out.println();
		
		scanner.nextLine();
		System.out.println("Informe o nome da agência\nr: ");
		String agencia = scanner.nextLine();
		System.out.println();
		
		System.out.println("Nome do cliente\nr: ");
		String nomeCliente = scanner.nextLine();
		System.out.println();
		
		System.out.println("Olá " + nomeCliente + ", obrigado por criar uma conta em nosso banco, \nSua agência é: " + agencia + "\nConta: " + numero + "\nSaldo(Cliente) <R$" + saldo + "> já está disponível");
		
		scanner.close();
	}
}
