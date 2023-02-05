class Flight():
    def __init__(self,capacity) :
        self.capacity=capacity
        self.passengers=[]
    
    def addPassenger(self,name):

        if not self.open_seats():
            return False;

        self.passengers.append(name);
        return True;

    def open_seats(self):
        return self.capacity-len(self.passengers);


flight=Flight(3);

people=['liam','Damon','noel','freddy'];

for person in people:
   
    if flight.addPassenger(person):
        print(f"The passenger {person} has been added");
    else: 
        print(f"The passenger {person} cannot been added");


