def process_bids(num_bids, bids):
    products = {}
    winners = {}

    for i in range(num_bids):
        bid_type, *rest = bids[i]
        if bid_type == "B":
            bidder, product, value = rest
            if product not in products:
                products[product] = {}
            products[product][bidder] = [int(value), i]
            winners[bidder] = []
        elif bid_type == "W":
            bidder, product = rest
            if product in products and bidder in products[product]:
                del products[product][bidder]

    for product, bidders in products.items():
        tmp = []
        for bidder, (value, index) in bidders.items():
            tmp.append((value, -index, bidder))
        if tmp:
            max_value, _, max_bidder = max(tmp)
            winners[max_bidder].append([max_value, product])

    return winners

def print_results(winners):
    for bidder in sorted(winners.keys()):
        total = 0
        products = []
        for value, product in winners[bidder]:
            total += value
            products.append(product)
        if total == 0:
            print(bidder + ": $0")
        else:
            print(bidder + ": $" + str(total) + " -> " + " ".join(sorted(products)))

num_bids = int(input())
bids = [input().split() for i in range(num_bids)]
winners = process_bids(num_bids, bids)
print_results(winners)
