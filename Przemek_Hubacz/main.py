def load_decision_system(info_file, type_file):
    with open(info_file, 'r') as info_stream, open(type_file, 'r') as type_stream:
        # Wczytujemy informacje o systemie
        system_info = info_stream.readline().split()
        num_attributes = float(system_info[1])
        num_objects = float(system_info[2])

        # Pomijamy nazwę systemu, ponieważ jesteśmy zainteresowani tylko klasami decyzyjnymi



        # Wczytujemy istniejące symbole klas decyzyjnych
        decision_classes = {class_name: 0 for class_name in info_stream.readline().split()}

        symbols_count = {}
        # Wczytujemy dane obiektów i wyświetlamy wszystkie możliwe symbole z ostatniej kolumny
        symbols = set()
        for line in info_stream:
            attributes = line.split()
            symbols.add(attributes[-1])
            symbol = attributes[-1] # Dodajemy ostatni symbol z każdego wiersza
            symbols_count[symbol] = symbols_count.get(symbol, 0) + 1
    return num_attributes, num_objects, decision_classes, symbols, symbols_count

def count_objects_with_symbol(symbol, symbols_count):
    if symbol in symbols_count:
        return symbols_count[symbol]
    else:
        return 0

if __name__ == "__main__":
    num_attributes, num_objects, decision_classes, symbols, symbols_count = load_decision_system("australian.txt", "australian-type.txt")

    # Wyświetlamy wszystkie możliwe symbole z ostatniej kolumny
    print("All possible symbols in the last column:")
    for symbol in symbols:
        print(symbol)

    symbol_0_objects = count_objects_with_symbol("0", symbols_count)
    print(f"Liczba obiektów z symbolem '0': {symbol_0_objects}")

    # Obliczamy liczbę obiektów dla symbolu "1"
    symbol_1_objects = count_objects_with_symbol("1", symbols_count)
    print(f"Liczba obiektów z symbolem '1': {symbol_1_objects}")



