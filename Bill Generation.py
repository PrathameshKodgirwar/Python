def Bill():
    items = {
        "Chai": 20,
        "Bread Pakoda": 25,
        "Samosa": 20,
        "Coffee": 20,
        "Muffins": 30,
        "Kaju katli":70,
        "Malai pedha":45,
    }
    print("-" * 60)
    print("{:^50}".format("Bill"))
    print("-" * 60)
    print("{:^50}".format("Haldirams"))
    print("{:^50}".format("Address: Swargate Pune"))
    print("{:^50}".format("Tel: 020 6775243"))
    print("-" * 60)
    print("{:<10} {:<30} {:>10}".format("Quantity", "Item", "Amount"))
    print("-" * 60)


    total = 0
    for item, price in items.items():
        qty = int(input(f"Enter quantity for {item} (Price: {price}/-): "))
        if qty > 0:
            amount = qty * price
            total += amount
            print("{:<10} {:<30} {:>10.2f}".format(qty, item, amount))
    print("-" * 60)
    print("{:<40} {:>10.2f}".format("Total", total))
    print("{:^50}".format("Thank you!"))


Bill()