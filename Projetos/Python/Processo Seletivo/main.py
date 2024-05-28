from style import Colors

class CodeStatus:
    def error(self, error : str):
        print(Colors.BACK_GRAY + f"[{error}] O programa foi encerrado pelo usuário" + Colors.END)

    def success(self, success : str, message : str):
        badget = Colors.BACK_GREEN + f" {success} " + Colors.END
        sys_message = Colors.GREEN + f" {message} " + Colors.END
        print(f"{badget} {sys_message}")

class Candidato:
    def atender(self, chamada : str) -> bool:
        print(f"'{chamada}' está ligando")
        res = str(input("Deseja atender [s/n]? ")).strip().lower()
        return True if res == "s" else False

class ProcessoSeletivo(CodeStatus, Candidato):
    _lista_candidatos : list[object]
    _lista_candidatos_aprovados : list[object]

    def __init__(self) -> None:
        self.panel("PROCESSO SELETIVO")

        # === REGISTRAR CANDIDATOS AO PROCESSO SELETIVO ===
        try:
            for num in range(1, 3):
                candidato = str(input(f"{num}° Candidato - Digite o seu nome\nr: ")).strip().capitalize()
                print('')

                salario_candidato = float(input("Sálario pretendido R$"))
                print('')
                #print(self.checar_processo(salario_candidato))
                    
                self._lista_candidatos.append({'nome': candidato, 'salario_pretendido': salario_candidato, 'sit': self.checar_processo(salario_candidato)})

                self.success("INSERT NEW USER", "Um novo candidato foi registrado")

        except ValueError:
            self.error("ValueError")

        finally:
            print("=== Processo de candidatura encerrado! ===")
            print("Candidatos Registrados")
            for candidato in self._lista_candidatos:
                print(f"- Nome : {candidato['nome']}")

        # === REALIZAR LIGAÇÕES PARA OS CANDIDATOS ===
        self.panel("FASE DE CONFIRMAÇÃO DA BOLSA DE ESTUDOS")
        self.ligar_para_candidatos(self._lista_candidatos)
        print("=== Processo de ligação encerrado! ===")
        print("Candidatos Aprovados")
        for candidato in self._lista_candidatos_aprovados:
            print(f"- Nome : {candidato['nome']}")

    def panel(self, text : str):
        print("-=" * 30)
        print(Colors.BLUE + f"=== {text.upper()} ===".center(50) + Colors.END)
        print("-=" * 30)
        print('\n' * 3)

    def checar_processo(self, salario_candidato : float) -> str:
        _resultado : str
        _salario_base = 2000

        if salario_candidato < _salario_base:
            _resultado = "LIGAR PARA CANDIDATO"

        elif salario_candidato == _salario_base:
            _resultado = "LIGAR PARA CANDIDATO COM CONTRA PROPOSTA"

        else:
            _resultado = "AGUARDANDO RESULTADO DOS DEMAIS CANDIDATOS"

        return _resultado
    
    def ligar_para_candidatos(self, lista_candidatos: list[object]):
        tent = 1

        for candidato in lista_candidatos:
            while tent < 4:
                print(f"Tentativa {tent} de ligação para '{candidato['nome']}'...")
                res = self.atender("Processo Seletivo - Vivo")

                if res:
                    self._lista_candidatos_aprovados.append(candidato)
                    self.success("OK", "CONTATO REALIZADO COM SUCESSO")

                else:
                    self.error("CONTATO REALIZADO SEM SUCESSO")

                tent += 1

try:
    ProcessoSeletivo() if __name__ == '__main__' else None

except KeyboardInterrupt:
    print(f"[App Interrupt] {KeyboardInterrupt}")

finally:
    print("=== ADEUS! ===")