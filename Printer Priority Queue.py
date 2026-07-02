"""There is a Printer. Write a priority queue program for urgent jobs and normal jobs and treat them by priority."""    
# Priority Queue for Printer

class Printer:

    def __init__(self):
        self.urgent = []
        self.normal = []

    # Add a print job
    def add_job(self, job, priority):

        if priority == "urgent":
            self.urgent.append(job)
        else:
            self.normal.append(job)

        print("Job added successfully.")

    # Print next job
    def print_job(self):

        if len(self.urgent) > 0:
            print("Printing Urgent Job:", self.urgent.pop(0))

        elif len(self.normal) > 0:
            print("Printing Normal Job:", self.normal.pop(0))

        else:
            print("No jobs to print.")

    # Display all pending jobs
    def display(self):
        print("Urgent Jobs:", self.urgent)
        print("Normal Jobs:", self.normal)


# Main Program

obj = Printer()

obj.add_job("Project Report", "normal")
obj.add_job("Exam Paper", "urgent")
obj.add_job("Assignment", "normal")
obj.add_job("Office Letter", "urgent")

obj.display()

obj.print_job()
obj.print_job()
obj.print_job()

obj.display()