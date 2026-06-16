pokedex = {}
capture_history = []
pokemon_types = ["Fogo", "Água", "Planta", "Elétrico", "Gelo", "Lutador", "Voador", "Psíquico", "Inseto", "Pedra", "Fantasma", "Dragão", "Noturno", "Aço", "Fada"]


def add_pokemon():
    """Adicionar um novo Pokémon à Pokedex."""
    name = input("Digite o nome do Pokémon: ").strip()
    if name in pokedex:
        print(f"Erro: {name} já está cadastrado na Pokedex.\n")
        return
    
    while True:
        pokemon_type = input("Digite o tipo do Pokémon: ").strip()
        if pokemon_type in pokemon_types:
            break
        else:
            print(f"Erro: Tipo inválido. Tipos válidos: {', '.join(pokemon_types)}")
    
    while True:
        try:
            level = int(input("Digite o nível (1-100): ").strip())
            if 1 <= level <= 100:
                break
            else:
                print("Erro: O nível deve estar entre 1 e 100.")
        except ValueError:
            print("Erro: Digite um número válido.")
    
    pokedex[name] = {"type": pokemon_type, "level": level, "captures": 0}
    print(f"{name} foi adicionado à Pokedex!\n")


def list_pokemon():
    """Listar todos os Pokémon cadastrados em ordem alfabética."""
    if not pokedex:
        print("A Pokedex está vazia.\n")
        return
    
    print("\n--- Pokémon Cadastrados ---")
    for name in sorted(pokedex.keys()):
        pokemon = pokedex[name]
        print(f"{name} - {pokemon['type']} - Nível {pokemon['level']}")
    print()


def remove_pokemon():
    """Remover um Pokémon da Pokedex."""
    name = input("Digite o nome do Pokémon a remover: ").strip()
    if name in pokedex:
        del pokedex[name]
        print(f"{name} foi removido da Pokedex!\n")
    else:
        print(f"Erro: {name} não encontrado na Pokedex.\n")


def update_level():
    """Atualizar o nível de um Pokémon."""
    name = input("Digite o nome do Pokémon: ").strip()
    if name not in pokedex:
        print(f"Erro: {name} não encontrado na Pokedex.\n")
        return
    
    while True:
        try:
            new_level = int(input("Digite o novo nível (1-100): ").strip())
            if 1 <= new_level <= 100:
                break
            else:
                print("Erro: O nível deve estar entre 1 e 100.")
        except ValueError:
            print("Erro: Digite um número válido.")
    
    pokedex[name]["level"] = new_level
    print(f"Nível de {name} atualizado para {new_level}!\n")


def register_capture():
    """Registrar a captura de um Pokémon."""
    name = input("Digite o nome do Pokémon capturado: ").strip()
    if name not in pokedex:
        print(f"Erro: {name} não encontrado na Pokedex.\n")
        return
    
    while True:
        try:
            quantity = int(input("Quantas vezes foi capturado? ").strip())
            if quantity > 0:
                break
            else:
                print("Erro: A quantidade deve ser maior que 0.")
        except ValueError:
            print("Erro: Digite um número válido.")
    
    pokedex[name]["captures"] += quantity
    capture_history.append({"name": name, "quantity": quantity})
    print(f"Captura(s) de {name} registrada(s)!\n")


def show_capture_history():
    """Exibir o histórico de capturas."""
    if not capture_history:
        print("Nenhuma captura registrada.\n")
        return
    
    print("\n--- Histórico de Capturas ---")
    for entry in capture_history:
        print(f"{entry['name']} - {entry['quantity']} captura(s)")
    print()


def main():
    """Menu principal da Pokedex."""
    while True:
        print("=== Pokedex ===")
        print("1. Adicionar Pokémon")
        print("2. Listar Pokémon")
        print("3. Remover Pokémon")
        print("4. Atualizar nível do Pokémon")
        print("5. Registrar captura")
        print("6. Exibir histórico de capturas")
        print("7. Sair")
        
        choice = input("Escolha uma opção (1-7): ").strip()
        
        if choice == "1":
            add_pokemon()
        elif choice == "2":
            list_pokemon()
        elif choice == "3":
            remove_pokemon()
        elif choice == "4":
            update_level()
        elif choice == "5":
            register_capture()
        elif choice == "6":
            show_capture_history()
        elif choice == "7":
            print("Saindo da Pokedex. Até logo!")
            break
        else:
            print("Erro: Opção inválida. Escolha entre 1 e 7.\n")


if __name__ == "__main__":
    main()
