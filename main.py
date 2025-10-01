menu={
    "pizza":120,
    "burger":70,
    "butter chicken":260,
    "chicken":160,
    "noodles":120,
    "momos":60,
    "pasta":60,
    "cold coffee":210,
    "hot coffee":250,
    "mojito":99,

}

# greek
print("welcome to kaif restaurant")
print("pizza:120\nburger:70\nbutter chicken:260\nchicken:160\nnoodle:120\nmomos:60\npasta:60\ncold coffee:210\nhot coffee:250\nmojito:99")

order_total=0
while True:
    item_1 = input("\nEnter the name of item you want to order (or type 'exit' to finish): ").lower()

    if item_1 == "exit":
        break

    if item_1 in menu:
        order_total+=menu[item_1]
        print(f"your item {item_1} has been added to your order")

    else:
        print(f"sorry,order item {item_1} is not available")

another_order=input("do you want to add another item?(yes/no)")


if another_order=="yes":
    item_2=input("Enter the name of second item you want to order:")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"your item {item_2} has been added to your order")
    else:
        print(f"sorry,order item {item_2} is not available!")

print(f"The total amount of items to pay is : {order_total}")
print("Thankyou for ordering from kaif restaurant!\nEnjoy your meal!")
