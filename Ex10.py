#When Joe purchased stock
no_of_shares = 1000
buy_price = 32.87
buy_amount = no_of_shares * buy_price
buy_commission = (buy_amount * 2)/100

new_amount = buy_amount + buy_commission

#When he sold,
sell_price = 33.92
sell_amount = sell_price * no_of_shares

sell_commission = (new_amount * 2)/100

total_commission = buy_commission + sell_commission
final_amount = sell_amount - buy_amount
profit_or_loss = final_amount - total_commission

print("Amount Joe paid for the stock: ", buy_amount)
print("Commission paid to broker when he bought :", buy_commission)
print("Amount at he sold :", sell_amount)
print("Commission paid to his broker when he sold :", sell_commission)
print("Total commission Joe paid to his broker : ", round(total_commission,2))


if profit_or_loss > 0:
    print(f"Joe made a profit of {round(profit_or_loss,2)}")
else:
    print(f"Joe loss by : {round(profit_or_loss,2)}")
