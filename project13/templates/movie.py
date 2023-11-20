def single_ton(cls):
    L = []
    def inner():
        if(len(L) == 0):
            obj = cls()
            L.append(obj)
        return L[0]
    return inner


'''Creating red_bus'''


@single_ton
class red_bus:
    def __init__(self):
        self.seats = 150

    def bookings(self):
        print('WELCOME TO RED_BUSSSS......')
        self.name = input('Enter Your Name: ')
        self.age  = int(input('Enter Your Age: '))
        self.gender = input('Enter Your Gender : ')
        self.mobile = int(input('Enter Your Mobile Number: '))

        
        tickets = int(input('Enter required tickets : '))
        if(self.seats >= tickets ):
            self.seats -= tickets
            if(self.gender == 'Male' or 'male'):
                print(f'Mr.{self.name} you have booked {tickets} ticket successfully in red_bus')
                print('THANK YOU')
            elif(self.gender == 'Female' or 'female'):
                print(f'Mrs.{self.name} you have booked {tickets} ticket successfully in red_bus')
                print('THANK YOU')
            else:
                print('Choose Proper Gender.....')
                
        else:
            print(f'{tickets} tickets are not available')
            print(f'only {self.seats} are left...')


'''Creating Green_bus'''

@single_ton
class green_bus:
    def __init__(self):
        self.seats = 150

    def bookings(self):
        print('WELCOME TO GREEN_BUSSSS......')
        self.name = input('Enter Your Name: ')
        self.age  = int(input('Enter Your Age: '))
        self.gender = input('Enter Your Gender : ')
        self.mobile = int(input('Enter Your Mobile Number: '))

        
        tickets = int(input('Enter required tickets : '))
        if(self.seats >= tickets ):
            self.seats -= tickets
            if(self.gender == 'Male' or 'male'):
                print(f'Mr.{self.name} you have booked {tickets} ticket successfully in red_bus')
                print('THANK YOU')
            elif(self.gender == 'Female' or 'female'):
                print(f'Mrs.{self.name} you have booked {tickets} ticket successfully in red_bus')
                print('THANK YOU')
            else:
                print('Choose Proper Gender.....')
                
        else:
            print(f'{tickets} tickets are not available')
            print(f'only {self.seats} are left...')


'''Creating Abhi_bus'''

@single_ton

class abhi_bus:
    def __init__(self):
        self.seats = 150

    def bookings(self):
        print('WELCOME TO ABHI_BUSSSS......')
        self.name = input('Enter Your Name: ')
        self.age  = int(input('Enter Your Age: '))
        self.gender = input('Enter Your Gender : ')
        self.mobile = int(input('Enter Your Mobile Number: '))

        
        tickets = int(input('Enter required tickets : '))
        if(self.seats >= tickets ):
            self.seats -= tickets
            if(self.gender == 'Male' or 'male'):
                print(f'Mr.{self.name} you have booked {tickets} ticket successfully in red_bus')
                print('THANK YOU')
            elif(self.gender == 'Female' or 'female'):
                print(f'Mrs.{self.name} you have booked {tickets} ticket successfully in red_bus')
                print('THANK YOU')
            else:
                print('Choose Proper Gender.....')
                
        else:
            print(f'{tickets} tickets are not available')
            print(f'only {self.seats} are left...')



'''Creating Orange_bus'''

@single_ton

class orange_bus:
    def __init__(self):
        self.seats = 150

    def bookings(self):
        print('WELCOME TO ORANGE_BUSSSS......')
        self.name = input('Enter Your Name: ')
        self.age  = int(input('Enter Your Age: '))
        self.gender = input('Enter Your Gender : ')
        self.mobile = int(input('Enter Your Mobile Number: '))

        
        tickets = int(input('Enter required tickets : '))
        if(self.seats >= tickets ):
            self.seats -= tickets
            if(self.gender == 'Male' or 'male'):
                print(f'Mr.{self.name} you have booked {tickets} ticket successfully in red_bus')
                print('THANK YOU')
            elif(self.gender == 'Female' or 'female'):
                print(f'Mrs.{self.name} you have booked {tickets} ticket successfully in red_bus')
                print('THANK YOU')
            else:
                print('Choose Proper Gender.....')
                
        else:
            print(f'{tickets} tickets are not available')
            print(f'only {self.seats} are left...')



def book_ticket():
    print('1.red_bus\n2.green_bus\n3.abhi_bus\n4.Orange_bus')
    option = int(input('Choose a service to book the tickets: '))
    if(option == 1):
        r1 = red_bus()
        r1.bookings()
    elif(option == 2):
        g1 = green_bus()
        g1.bookings()
    elif(option == 3):
        a1 = abhi_bus()
        a1.bookings()
    elif(option == 4):
        o1 = orange_bus()
        o1.bookings()
    else:
        print('choose valid option!!!!!')

while True:
    book_ticket()
    

























            
