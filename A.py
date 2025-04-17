# distance = 0
# middle_consumption = 0
# mid_fuel_price = 0
# passengers = 0

# full_price = 0
# price_per_passenger = 0

distance = int(input("Дистанція подорожі (км): "))
middle_consumption = int(input("Середня витрата палива (літр/100 км): "))
mid_fuel_price = int(input("Середня ціна на літр палива (грн): "))
passengers = int(input("Кількість пасажирів: "))

fuel_amount = distance/100*middle_consumption
full_price = fuel_amount*mid_fuel_price
price_per_passenger = round(full_price/passengers, 2)

print(f"Для подорожі довжиною {distance} з середньою витратою палива {middle_consumption} на 100 км та ціною {mid_fuel_price} грн за літр,")
print(f"Вартість пального буде {full_price} грн")
print(f"З переоцінкою на пасажира вийде {price_per_passenger} грн з людини")