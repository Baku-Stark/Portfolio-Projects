import java.util.*; /* Scanner, ArrayList */

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		List<String> candidatos_aceitos = new ArrayList<String>();
		List<String> candidatos_nova_oferta = new ArrayList<String>();
		List<String> candidatos_espera = new ArrayList<String>();
		
		List<String> candidatos_aprovados = new ArrayList<String>();
		
		for(int num = 1; num <= 5; num++) {
			System.out.println("Registre seu nome: ");
			String candidato = scanner.nextLine();
			System.out.println();
			
			System.out.println("Sálario pretendido: R$");
			double user_salario = scanner.nextDouble();
			scanner.nextLine();
			System.out.println();
			
			switch (checkProcess(user_salario)) {
				case "LIGAR PARA CANDIDATO": {
					candidatos_aceitos.add(candidato);
					break;
				}
				
				case "LIGAR PARA CANDIDATO COM CONTRA PROPOSTA":{
					candidatos_nova_oferta.add(candidato);
					break;
				}
				
				case "AGUARDANDO RESULTADO DOS DEMAIS CANDIDATOS":{
					candidatos_espera.add(candidato);
					break;
				}
			}
			
			System.out.println("Candidato " + num + ": " + checkProcess(user_salario));
		}
		
		System.out.println("=== FIM DO PROCESSO SELETIVO ===");
		System.out.println("Candidatos aceitos: ");
		printLists(candidatos_aceitos);
		System.out.println();
		
		System.out.println("Candidatos para novas propostas: ");
		printLists(candidatos_nova_oferta);
		System.out.println();
		
		System.out.println("Candidatos em espera: ");
		printLists(candidatos_espera);
		System.out.println();
		
		if(candidatos_aceitos.size() > 0) {
			ligarCandidato(candidatos_aceitos, candidatos_aprovados);
		}
		
		else if (candidatos_nova_oferta.size() > 0){
			ligarCandidato(candidatos_nova_oferta, candidatos_aprovados);
		}
		
		else {
			ligarCandidato(candidatos_espera, candidatos_aprovados);
		}
		
		System.out.println();
		
		System.out.println("=== LIGAÇÃO (confirmou vaga) ===");
		printLists(candidatos_aprovados);
		scanner.close();
	}
	
	public static String checkProcess(double user_salario) {
		double base_salario = 2000.00;
		
		if(user_salario < base_salario) {
			return "LIGAR PARA CANDIDATO";
		}
		
		else if(user_salario == base_salario) {
			return "LIGAR PARA CANDIDATO COM CONTRA PROPOSTA";
		}
		
		else {
			return "AGUARDANDO RESULTADO DOS DEMAIS CANDIDATOS";
		}
	}
	
	public static void printLists(List<String> list) {
		// System.out.println(list.size());
		
		for(int index = 0; index < list.size(); index++) {
			System.out.println("- " + list.get(index));
		}
	}
	
	public static void ligarCandidato(List<String> list_candidatos, List<String> list_candidatos_aprovados) {
		Scanner scanner = new Scanner(System.in);
		
		for(int index = 0; index < list_candidatos.size(); index++) {
			int tent = 1;
			
			do {
				System.out.println(tent + " Tentativa de ligação");
				String res = atender(scanner, list_candidatos.get(index));
				
				// System.out.println(res);
				if(res == "LIGAÇÃO ATENDIDA") {
					list_candidatos_aprovados.add(list_candidatos.get(index));
					System.out.println("- CONTATO REALIZADO COM SUCESSO");
					break;
				}
				
				else{
					System.out.println("- CONTATO REALIZADO SEM SUCESSO");
				}
				
				tent ++;
				System.out.println();
				
			} while (tent < 4);
			
			System.out.println("Processo de ligação encerrado");
		}
		scanner.close();
	}
	
	public static String atender(Scanner scanner, String candidato) {
		String situacao = null;

		System.out.println(candidato + " - Atender ligação? [sim/nao]: ");
		String res = scanner.nextLine();
		//System.out.println(res);
		scanner.nextLine();
		
		switch (res) {
			case "sim": {
				situacao = "LIGAÇÃO ATENDIDA";
				break;
			}
			
			case "nao":
				situacao = "LIGAÇÃO NÃO ATENDIDA";
				break;
		}
		
		return situacao;
	}
}
