def get_bandeira(card_number: str) -> str:
    """Detecta a bandeira do cartão de crédito com base no número."""
    if card_number.startswith('4'):
        return 'Visa'
    if (card_number[:2] in [str(i) for i in range(51, 56)] or
        2221 <= int(card_number[:4]) <= 2720):
        return 'MasterCard'
    if (card_number.startswith('4011') or
        card_number.startswith('4312') or
        card_number.startswith('4389')):
        return 'Elo'
    if card_number.startswith('34') or card_number.startswith('37'):
        return 'American Express'
    if (card_number.startswith('6011') or
        card_number.startswith('65') or
        (644 <= int(card_number[:3]) <= 649)):
        return 'Discover'
    if card_number.startswith('6062'):
        return 'Hipercard'
    return 'Unknown'

if __name__ == "__main__":
    while True:
        numero = input("Digite o número do cartão (ou pressione Enter para sair): ")
        if not numero:
            print("Encerrando...")
            break
        print("Bandeira detectada:", get_bandeira(numero))