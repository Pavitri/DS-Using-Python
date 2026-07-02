"""A toll plaza has a fixed capacity of 5 vehicles. If full, new vehicles must wait. Implement a circular queue to simulate this, since it reuses empty slots without wasting memory."""
# Circular Queue for Toll Plaza

class CircularQueue:

    def __init__(self):
        self.size = 5
        self.queue = [""] * self.size
        self.front = -1
        self.rear = -1

    # Add vehicle
    def enqueue(self, vehicle):

        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full. Vehicle has to wait.")
            return

        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = vehicle
        print(vehicle, "entered the toll plaza.")

    # Remove vehicle
    def dequeue(self):

        if self.front == -1:
            print("Queue is Empty.")
            return

        print(self.queue[self.front], "has crossed the toll plaza.")

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    # Display queue
    def display(self):

        if self.front == -1:
            print("Queue is Empty.")
            return

        print("Vehicles in Queue:")

        i = self.front

        while True:
            print(self.queue[i])

            if i == self.rear:
                break

            i = (i + 1) % self.size


# Main Program

obj = CircularQueue()

obj.enqueue("Car")
obj.enqueue("Bus")
obj.enqueue("Truck")
obj.enqueue("Bike")
obj.enqueue("Van")

obj.display()

obj.enqueue("Taxi")    # Queue Full

obj.dequeue()
obj.dequeue()

obj.enqueue("Taxi")
obj.enqueue("Auto")

obj.display()