EXCHANGE_RATE = {
    'USD': 1,
    'EUR': 0.91,
    'UZS': 12787.03,
    'GBP': 0.7634,
    'RUB': 96.5561,
    'JPY': 148.072
}
CURRENCIES = list(EXCHANGE_RATE.keys())
CURRENCIES.sort()
CURRENCIES_TEXT = f"({'/'.join(CURRENCIES).upper()})"

def get_amount():
    while True:
        try:
            amount = float(input('Enter the amount: '))
            if amount > 0:
                return amount
        except ValueError:
            pass
        print('Invalid amount')


def get_currency(label):
    currency = input(F'{label} currency {CURRENCIES_TEXT}: ').upper()
    while currency not in CURRENCIES:
        print('Invalid currency')
        currency = input(F'{label} currency {CURRENCIES_TEXT}: ').upper()
    return currency

def convert(amount, source_currency, target_currency):
    return EXCHANGE_RATE[target_currency] / EXCHANGE_RATE[source_currency] * amount
    
def main():
    amount = get_amount()
    source_currency = get_currency('Source')
    target_currency = get_currency('Target')

    result = convert(amount, source_currency, target_currency)

    print(f"\n{amount} {source_currency} is equal to {result:.2f} {target_currency}\n")

    for curr in CURRENCIES:
        if curr in (target_currency, source_currency):
            continue
        result = convert(amount, source_currency, curr)
        print(f"{amount} {source_currency} = {result:.2f} {curr}")

if __name__ == "__main__":
    main()