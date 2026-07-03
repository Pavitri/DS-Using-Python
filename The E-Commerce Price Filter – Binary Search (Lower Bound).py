"""You are shopping on Flipkart and apply the filter: "Show me laptops priced ₹50,000 or above." The products are already sorted by price. Flipkart needs to find the first product whose price is greater than or equal to ₹50,000. Write a program using the appropriate searching algorithm to find the first product with price ≥ ₹50,000."""
price = [25000, 30000, 42000, 50000, 55000, 60000, 70000]
find_price = 50000

low = 0
high = len(price) - 1

while low <= high:
    mid = (low + high) // 2
    if price[mid] >= find_price:
        answer = mid
        high = mid - 1
    else:
        low = mid + 1
if answer != -1:
    print("Laptop price >=", find_price, "is", price[answer])
else:
    print("Laptop not found")
