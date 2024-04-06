from mendeleev import element

class Python_Quimica():
    def __init__(self):
        elem_num = int(input("Escolha o número do elemento [1 até 118]: "))
        print('')
        self.elemento_info(elem_num)

    def elemento_info(self, elem_num: int) -> None:
        elem = element(elem_num)

        print('-' * 30)
        print(f"""
        === { elem.atomic_number } | { elem.name }({ elem.symbol }) ===
        |
        `-> { elem.name_origin }

        =+ Infomações do átomo de { elem.name } +=
            * Massa: { elem.mass }
            * N° atômico: { elem.atomic_number }
            * Raio atômico: { elem.atomic_radius } pm
            * Peso atômico: { elem.atomic_weight }
            * Massa atômica: { elem.mass_number } u
            * Volume atômico: { elem.atomic_volume } cm³/mol
            ( - Elétrons: { elem.electrons } | Prótons: { elem.protons } | Neutrons: { elem.neutrons } - )

        =+ Ficha do elemento +=
            * Grupo: { elem.group_id }A | { elem.group.name }
            * Descobridor: { elem.discoverers }
            * Ano de descoberta: { elem.discovery_year }
            * Local de descoberta: { elem.discovery_location }
        """)
        print(f"* Descrição do { elem.name }: { elem.description }")
        print('-' * 30)

if __name__ == '__main__':
    Python_Quimica()