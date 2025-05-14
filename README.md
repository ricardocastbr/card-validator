# Validador de Bandeira de Cartão de Crédito

Este projeto identifica a bandeira (Visa, MasterCard, Elo, etc.) de um cartão de crédito a partir do número digitado pelo usuário.

## Como funciona
O programa pede para o usuário digitar o número do cartão e, com base nos primeiros dígitos, informa qual é a bandeira do cartão.

## Como executar
1. Certifique-se de ter o Python instalado (versão 3.x).
2. No terminal, navegue até a pasta do projeto.
3. Execute o arquivo principal:

```bash
python scr/index.py
```

4. Digite o número do cartão quando solicitado. Para sair, basta pressionar Enter sem digitar nada.

## Exemplo de uso
```
Digite o número do cartão (ou pressione Enter para sair): 4111111111111111
Bandeira detectada: Visa

Digite o número do cartão (ou pressione Enter para sair): 6011000990139424
Bandeira detectada: Discover
```

## Explicação detalhada do código

O código principal está no arquivo `scr/index.py`. Veja abaixo o que cada linha faz:

```python
def get_bandeira(card_number: str) -> str:
    """Detecta a bandeira do cartão de crédito com base no número."""
    # Verifica se o número começa com 4 (Visa)
    if card_number.startswith('4'):
        return 'Visa'
    # Verifica se começa com 51-55 ou 2221-2720 (MasterCard)
    if (card_number[:2] in [str(i) for i in range(51, 56)] or
        2221 <= int(card_number[:4]) <= 2720):
        return 'MasterCard'
    # Verifica se começa com 4011, 4312 ou 4389 (Elo)
    if (card_number.startswith('4011') or
        card_number.startswith('4312') or
        card_number.startswith('4389')):
        return 'Elo'
    # Verifica se começa com 34 ou 37 (American Express)
    if card_number.startswith('34') or card_number.startswith('37'):
        return 'American Express'
    # Verifica se começa com 6011, 65 ou entre 644 e 649 (Discover)
    if (card_number.startswith('6011') or
        card_number.startswith('65') or
        (644 <= int(card_number[:3]) <= 649)):
        return 'Discover'
    # Verifica se começa com 6062 (Hipercard)
    if card_number.startswith('6062'):
        return 'Hipercard'
    # Se não for nenhum dos casos acima, retorna 'Unknown'
    return 'Unknown'

if __name__ == "__main__":
    # Laço para permitir várias tentativas
    while True:
        # Pede o número do cartão ao usuário
        numero = input("Digite o número do cartão (ou pressione Enter para sair): ")
        # Se o usuário não digitar nada, encerra o programa
        if not numero:
            print("Encerrando...")
            break
        # Mostra a bandeira detectada
        print("Bandeira detectada:", get_bandeira(numero))
```

### Resumo das principais funções e comandos:
- `def get_bandeira(card_number: str) -> str:` Cria uma função que recebe o número do cartão e retorna a bandeira.
- `startswith()` Verifica se o número começa com determinados dígitos.
- `input()` Pede uma informação ao usuário.
- `print()` Mostra uma mensagem na tela.
- `while True:` Cria um laço para repetir o processo até o usuário decidir sair.
- `break` Sai do laço quando o usuário não digita nada.

## Observações
- O projeto foi desenvolvido em Python, enquanto o exemplo do curso foi feito em JavaScript.
- As regras de identificação das bandeiras seguem os padrões mais comuns do mercado.
