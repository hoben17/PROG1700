#Author- Adam Hoben 
# Student ID- w0184019
# Version: 1.0

{"A1": {
    "name": "water",
    "pricee": 1.50,
    "quantity": 5   
        }
}

{
    "A2": {
        "name": "pop",
        "price": 2.00,
        "quantity": 8
    }
}

{
    "A3": {
        "name": "Chocolate",
        "price": 2.50,
        "quantity": 3
    }
}

{
    "A4": {
        "name": "Chips",
        "price": 1.75,
        "quantity": 6
    }
}



while True:
    print("\nAvailable Products")
    print("\n------------------")

for product_id, p in products.items():
    # Testing my unpacking of the nested dictionaries
    #print (product_id , p["name"], p["price"], p["quantity"])
    selection = input("Select a product or type EXIT:").upper().strip(

)
    
    
    print(f"product_id")






    # Select a product
    selection = input("select and product or type EXIT:")

    if selection == "EXIT":
        break

    if selection not in products:
        print("Error: Invalid product ID.")
        continue

    quantity = products[selection]["quantity"]

    if quantity == 0:
        print("Product unavailable, Make another choice")
        continue

    print(f"\nSelected Product: {name}")
    print(f"\nPrice ${price:.2f}")

    while True:
        try:
            payment = float(input("Enter Payment: $"))
            
            if not 0 <= payment < float("inf"):
                print("Error: Enter a valid posotive amount.")
            elif payment < price:
                print("Error: Insufficent payment.")
            else:
                break

        except ValueError:
            print("Error:Enter a valid numerical amount.")

        

          
