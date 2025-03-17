buy = float(input("Type how much you will pay:"))

if (buy > 200):
    discount = buy * 0.20
    buy = buy - discount
    print(f'The discount is 20%. The price is ${buy}')
elif (buy > 100):
    discount = buy * 0.10
    buy = buy - discount
    print(f'The discount is 10%. The price is ${buy}')
else: 
    discount = buy * 0.05
    buy = buy - discount
    print(f'The discount is 5%. The price is ${buy:.2f}')