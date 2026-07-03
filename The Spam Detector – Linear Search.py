"""A cybersecurity intern at a startup is building a basic spam filter. Incoming emails are checked against a blacklist of known spam sender IDs. The blacklist is not sorted. Write a program to search whether a sender ID exists in the blacklist using the appropriate searching technique."""
blacklist = ["spam123", "abc456", "fake789", "test111"]
id = input("Enter sender's ID: ")
found = False

for i in blacklist:
    if i == id:
        found = True
        break

if found:
    print("Spam sender detected.")
else:
    print("Safe sender.")
