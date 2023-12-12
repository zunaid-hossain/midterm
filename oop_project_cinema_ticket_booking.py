class star_cinema:
    _hall_list=[]
    
    def entry_hall(self,hall):
        self._hall_list.append(hall)



class Hall(star_cinema):
    def __init__(self,rows,cols,hall_no) -> None:
       self._seats={}
       self._show_list=[]
       self._rows=rows
       self._cols=cols 
       self._hall_no=hall_no
       
       self.entry_hall(self)



    def entry_show(self,id,movie_name,time):

        show=(id,movie_name,time)
        self._show_list.append(show)
        
        seats = []

        for row in range(self._rows):
            row_seats = []
            for col in range(self._cols):
                row_seats.append('0')
            seats.append(row_seats)

        self._seats[id] = seats


    def book_seats(self,id,seatbook):
        if id not in self._seats:
            raise ValueError("Invalid show id")
        
        for seat in seatbook:
            row,col=seat
            if(0>row>self._rows and 0>col>self._cols):
                raise ValueError("Invalid seat")
            
            if(self._seats[id][row][col]=='1'):
                self.view_available_seats(id)
                raise ValueError (f"seat {row } {col} is already booked\nplease try another\n '0'indicate free and '1' indicate booked ")
            
            else :
                self._seats[id][row][col]='1'
                print("Thanks for booking")
            
        
    def view_show_list(self):
        
        for j in  self._show_list:
            print(j)
    

    def view_available_seats(self,id):
        
        if id not in self._seats:
            print("invalid show id")
        
        else:
            for row in self._seats[id]:
                print(" ".join(row))


Hall1=Hall(10,10,1)
Hall2=Hall(20,20,2)

Hall1.entry_show("1001","B","3.00")
Hall1.entry_show("2001","Avengers","7.00")
Hall1.entry_show("3001","KGF","16.00")
Hall1.entry_show("4001","jawan","13.00")
Hall2.entry_show("5001","j","12.00")


while True:
    
    print("1 .View All Show Today")        
    print("2 .View Available Seats")
    print("3 .Book Ticket")
    print("4. Exit")
    print("")
    ch=input("Enter option ")

    if ch=="1":
        print(Hall1.view_show_list())
        print("")
        
    elif ch=="2":

        show=input("Enter show id ")
        print(" ")
        Hall1.view_available_seats(show)


    elif ch=="3":
        
        try:

            show=input("Enter show id")
            row=int(input("enter row"))
            col=int(input("enter column"))
            Hall1.book_seats(show,[(row,col)])

        except ValueError as e:
            print(f"{e}")

    
    elif ch=='4':
        exit()
    else:
        continue