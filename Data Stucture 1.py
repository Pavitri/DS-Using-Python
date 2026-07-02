"""An Amazon fulfillment centre has a conveyor belt with exactly 8 slots numbered 0-7. Each slot holds one product. The warehouse manager needs to : Check what's at a slot, Find a product, Update a slot and check if the belt is full. The conveyor belt has 8 slots (fixed)."""
# Amazon Fulfillment Center

class Conveyor:

    def __init__(self):
        # Conveyor belt with 8 slots
        self.belt = [""] * 8

    # Update a slot
    def update(self, slot, product):
        self.belt[slot] = product
        print("Product added.")

    # Check product at a slot
    def check(self, slot):
        print("Product at slot", slot, "is", self.belt[slot])

    # Find a product
    def find(self, product):
        for i in range(8):
            if self.belt[i] == product:
                print(product, "found at slot", i)
                return
        print("Product not found.")

    # Check if conveyor belt is full
    def full(self):
        if "" in self.belt:
            print("Conveyor belt is not full.")
        else:
            print("Conveyor belt is full.")

    # Display all slots
    def display(self):
        print(self.belt)


# Main Program

obj = Conveyor()

obj.update(0, "Laptop")
obj.update(1, "Mobile")
obj.update(2, "Shoes")

obj.display()

obj.check(1)

obj.find("Mobile")

obj.full()