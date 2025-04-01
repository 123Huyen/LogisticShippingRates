# Shipping cost calculator
## Input package weight and shipping rate
weight = float(input"Enter the package weight in kilogorams: ")
rate = float(input("ENter the shipping rate perkilogram: "))

##Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping cost: {shipping_cost} USD")
