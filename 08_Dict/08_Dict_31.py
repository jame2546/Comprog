def total(pocket):
    return sum([k*v for k,v in pocket.items()])

def take(pocket, money_in):
    for b in money_in :
        if b in pocket :
            pocket[b] += money_in[b]
        else :
            pocket[b] = money_in[b]
    return pocket

def pay(pocket, amt):
    paid = {}
    for bank in sorted(pocket.keys(), reverse=True) :
        while bank <= amt and pocket[bank] > 0 :
            if bank in paid :
                paid[bank] += 1
            else :
                paid[bank] = 1
            amt -= bank
            pocket[bank] -= 1
    if amt != 0 :
        pocket = take(pocket,paid)
        return {}
    else :
        return paid
exec(input().strip()) 