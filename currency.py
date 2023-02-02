def how_to_pay(amount: int, currency: list):
    num_of_notes = []
    currency.reverse()
    for note in currency:
        quotient = amount//note
        if quotient:
            num_of_notes.append(quotient)
            amount -= quotient
        else:
            num_of_notes.append(0)
    
    num_of_notes.reverse()
    currency.reverse()

    ammount_to_pay = {x:y for (x, y) in zip(num_of_notes, currency)}
    return ammount_to_pay
