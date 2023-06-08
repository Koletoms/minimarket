def check_payment(number_card: str) -> bool:
    """
    Условный проверщик оплаты. Если карта заканчивается на
    Eсли введённый номер чётный и не заканчивается на ноль - True
    Eсли введённый номер нечётный или заканчивается на ноль - False
    """
    try:
        number = int(number_card[-1])
        if number != 0 and number % 2 == 0:
            return True
        raise BaseException
    except BaseException:
        return False

