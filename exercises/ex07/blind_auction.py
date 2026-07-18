name = input("What is your name?: ")
price = float(input("What's your bid: $"))

# add name and price to dictionary
auction_dictionary= {}
auction_dictionary[name] = price

price_list = []
highest_price = 0
questions = True

while questions:
    answer = input("Do we have other users who want to bid? 'No or Yes': ").lower()

    if answer == 'no':
        questions = False
        # create a list of bids
        for key in auction_dictionary:
            price = auction_dictionary[key]
            price_list.append(price)

        # find the highest bid
        highest_price = max(price_list)

        # find the winner
        for name, price in auction_dictionary.items():
            if price == highest_price:
                print(f"The winner of the auction is {name.upper()} 🏆.")
    else: 
        print("\n" *20)
        name = input("What is your name?: ")
        price = float(input("What's your bid: $"))
        auction_dictionary[name] = price
       