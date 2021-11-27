f = open("railwaysdb.txt", 'r')
l = f.readlines()
f.close()

usernames =eval(l[0])
password = eval(l[1])
ticket = eval(l[2])
CPNR = eval(l[3])

f1 = open("Train_details.txt", 'r')
l1 = f1.readlines()
f1.close()

UP = eval(l1[0])
DOWN = eval(l1[1])

f2 = open("passenger_details.txt", 'r')
l11 = f2.readlines()
f2.close()

PASSENGER = eval(l11[0])
AGE = eval(l11[1])
ADH = eval(l11[2])

f4= open('booking_details.txt', 'r')
l10 = f4.readlines()
f4.close()

PNR = eval(l10[0])
Train_Name = eval(l10[1])
Route = eval(l10[2])
DAY= eval(l10[3])
MONTH = eval(l10[4])
YEAR = eval(l10[5])
TIME = eval(l10[6])

f3 = open("bank_details.txt", 'r')
l6 = f3.readlines()
f3.close()

BANKNAME = eval(l6[0])
ACCOUNTNO = eval(l6[1])
IFSCCODE = eval(l6[2])
HOLDERNAME = eval(l6[3])


class Pnr_Enquiry():
    def __init__(self):
        pass

    def pnr_status(self,i):
        cpnr = CPNR[i]
        tic1 = ticket[i]
        epnr = input("Enter the PNR")
        if epnr == CPNR[i]:
            print("Your train is: ", tic1)
        else:
            print("Wrong PNR,TRY AGAIN............")
            self.pnr_status(i)





class My_Bookings():
    def __init__(self):
        pass

    def show_ticket(self, i):
        tic = ticket[i]
        ccpnr = CPNR[i]
        print("Booked Ticked PNR is: ", ccpnr)
        print("Your Booked Ticket is : ", tic)




class Journey():
    def __init__(self):
        pass

    def journey_details(self, i):
        print("Enter the date of journey")
        try:
            day = input("Enter the Day")
            month = input("Enter the Month")
            year = input("Enter the Year")
        except:
            self.journey_details(i)
        else:
            print("Date of Journey is : %s/%s/%s" %(day, month, year))
        try:  
            starting = input("Enter the Source Station in CAPS : ")
            ending = input("Enter the Destination Station in CAPS : ")
        except:
            self.journey_details(i)
        else:
            if starting == 'KOLKATA' and ending == 'DELHI':
                print("%s_ %s_ %s  %s/%s/%s_ %s_ AC-%d_ NON_AC-%d" %(UP[0][0]['1'][0][0], UP[0][0]['1'][1][0], UP[1][0], day, month, year, UP[2][0], UP[3]['AC'][0], UP[3]['NONAC'][0]))
                try:
                    Select1 = int(input("Enter 1 for Confirm and 2 for EXIT"))
                except:
                    self.journey_details(i)
                else:
                    if Select1 == 1:
                         PNR.append(UP[0][0]['1'][0][0])
                         Train_Name.append(UP[0][0]['1'][1][0])
                         Route.append(UP[1][0])
                         DAY.append(day)
                         MONTH.append(month)
                         YEAR.append(year)
                         TIME.append(UP[2][0])
                         print("Ticket you want to select: PNR:%s Train_Name:%s Route:%s Date: %s/%s/%s  Time:%s" %(UP[0][0]['1'][0][0], UP[0][0]['1'][1][0], UP[1][0], day, month, year, UP[2][0]))
                         f4= open('booking_details.txt', 'w')
                         f4.write("%s \n%s \n%s  \n%s \n%s \n%s  \n%s" %(PNR, Train_Name, Route, DAY, MONTH, YEAR, TIME))
                         f4.close()
                         ticket.append(UP[0][0]['1'][1][0])
                         CPNR.append(UP[0][0]['1'][0][0])
                         f = open("railwaysdb.txt", 'w')
                         f.write("%s \n%s \n%s \n%s" %(usernames, password, ticket, CPNR))
                    else:    
                        exit()  
                    self.passenger(i)
            elif starting == 'DELHI' and ending == 'KOLKATA':
                print("%s_ %s_ %s  %s/%s/%s_ %s_ AC-%d_ NON_AC-%d" %(DOWN[0][0]['2'][0][0], DOWN[0][0]['2'][1][0], DOWN[1][0], day, month, year, DOWN[2][0], DOWN[3]['AC'][0], DOWN[3]['NONAC'][0]))
                try:
                    Select2 = int(input("Enter 1 for Confirm and 2 for EXIT"))
                except:
                    self.journey_details(i)
                else:
                    if Select2 == 1:
                        PNR.append(DOWN[0][0]['2'][0][0])
                        Train_Name.append(DOWN[0][0]['2'][1][0])
                        Route.append(DOWN[1][0])
                        DAY.append(day)
                        MONTH.append(month)
                        YEAR.append(year)
                        TIME.append(DOWN[2][0])
                        print("Ticket you want to select: PNR:%s Train_Name:%s Route:%s Date: %s/%s/%s  Time:%s  " %(DOWN[0][0]['2'][0][0], DOWN[0][0]['2'][1][0], DOWN[1][0], day, month, year, DOWN[2][0]))
                        f4= open('booking_details.txt', 'w')
                        f4.write("%s \n%s \n%s  \n%s \n%s \n%s  \n%s" %(PNR, Train_Name, Route, DAY, MONTH, YEAR, TIME))
                        f4.close()
                        ticket.append(DOWN[0][0]['2'][1][0]) 
                        CPNR.append(DOWN[0][0]['2'][0][0])
                        f = open("railwaysdb.txt", 'w')
                        f.write("%s \n%s \n%s \n%s" %(usernames, password, ticket, CPNR))
                    else:    
                        exit()
                    self.passenger(i)
                    

    def passenger(self, i):
        npass = int(input("Enter the No, of passengers MAXIMUM 4 allowed at a time: "))
        sel1 = int(input("Enter 1 for AC and 2 for NON_AC"))
        if npass == 1:
            if sel1 == 1:
                price = 2000 * npass
            else:
                price = 1500 * npass
            psg1 = input("Enter the Name : ")
            try:
                age1 = input("Enter the age : ")
                adh1 = input("Enter the Adhaar number : ")
            except:
                self.passenger(i)
            else:
                PASSENGER.append(psg1)
                AGE.append(age1)
                ADH.append(adh1)
                print("Total Fare : ", price)
                self.payment()
                f2 = open("passenger_details.txt", 'w')
                f2.write("%s   \n%s   \n%s" %(PASSENGER, AGE, ADH))
                f2.close()
                
        elif npass == 2:
            if sel1 == 1:
                price = 2000 * npass
            else:
                price = 1500 * npass
            psg1 = input("Enter the Name : ")
            psg2 = input("Enter the Name : ")
            try:
                age1 = input("Enter the age : ")
                age2 = input("Enter the age : ")
                adh1 = input("Enter the Adhaar number : ")
                adh2 = input("Enter the Adhaar number : ")
            except:
                self.passenger(i)
            else:
                PASSENGER.append(psg1)
                AGE.append(age1)
                ADH.append(adh1)
                PASSENGER.append(psg2)
                AGE.append(age2)
                ADH.append(adh2)
                print("Total Fare : ", price)
                self.payment()
                f2 = open("passenger_details.txt", 'w')
                f2.write("%s   \n%s   \n%s" %(PASSENGER, AGE, ADH))
                f2.write("\n%s \n%s \n%s" %(PASSENGER, AGE, ADH))
                f2.close()
        elif npass == 3:
            if sel1 == 1:
                price = 2000 * npass
            else:
                price = 1500 * npass
            psg1 = input("Enter the Name : ")
            psg2 = input("Enter the Name : ")
            psg3 = input("Enter the Name : ")
            try:
                age1 = input("Enter the age : ")
                age2 = input("Enter the age : ")
                age3 = input("Enter the age : ")
                adh1 = input("Enter the Adhaar number : ")
                adh2 = input("Enter the Adhaar number : ")
                adh3 = input("Enter the Adhaar number : ")
            except:
                self.passenger(i)
            else:
                PASSENGER.append(psg1)
                AGE.append(age1)
                ADH.append(adh1)
                PASSENGER.append(psg2)
                AGE.append(age2)
                ADH.append(adh2)
                PASSENGER.append(psg3)
                AGE.append(age3)
                ADH.append(adh3)
                print("Total Fare : ", price)
                print("Total Fare : ", price)
                self.payment()
                f2 = open("passenger_details.txt", 'w')
                f2.write("%s   \n%s   \n%s" %(PASSENGER, AGE, ADH))
                f2.write("\n%s   \n%s   \n%s" %(PASSENGER, AGE, ADH))
                f2.write("\n%s  \n%s   \n%s" %(PASSENGER, AGE, ADH))
                f2.close()
        elif npass == 4:
            if sel1 == 1:
                price = 2000 * npass
            else:
                price = 1500 * npass
            psg1 = input("Enter the Name : ")
            psg1 = input("Enter the Name : ")
            psg2 = input("Enter the Name : ")
            psg3 = input("Enter the Name : ")
            try:
                age1 = input("Enter the age : ")
                age2 = input("Enter the age : ")
                age3 = input("Enter the age : ")
                age4 = input("Enter the age : ")
                adh1 = input("Enter the Adhaar number : ")
                adh2 = input("Enter the Adhaar number : ")
                adh3 = input("Enter the Adhaar number : ")
                adh4 = input("Enter the Adhaar number : ")
            except:
                self.passenger(i)
            else:
                PASSENGER.append(psg1)
                AGE.append(age1)
                ADH.append(adh1)
                PASSENGER.append(psg2)
                AGE.append(age2)
                ADH.append(adh2)
                PASSENGER.append(psg3)
                AGE.append(age3)
                ADH.append(adh3)
                PASSENGER.append(psg4)
                AGE.append(age4)
                ADH.append(adh4)
                print("Total Fare : ", price)
                self.payment()
                f2 = open("passenger_details.txt", 'w')
                f2.write("%s   \n%s   \n%s" %(PASSENGER, AGE, ADH))
                f2.write("\n%s   \n%s   \n%s" %(PASSENGER, AGE, ADH))
                f2.write("\n%s   \n%s   \n%s" %(PASSENGER, AGE, ADH))
                f2.write("\n%s   \n%s   \n%s" %(PASSENGER, AGE, ADH))
                f2.close()
        else:
            self.passenger(i)

    def payment(self):
        bank_name = input("Enter Bank Name")
        acc_no = input("Enter the Account Number")
        ifsc_code = input("Enter the IFSC_CODE")
        acc_hldr_name = input("Enter the Account Holder Name")
        try:
            pay = int(input("Enter 1 for proceed to pay and 2 for Back"))
        except:
            self.payment()
        else:
            BANKNAME.append(bank_name)
            ACCOUNTNO.append(acc_no)
            IFSCCODE.append(ifsc_code)
            HOLDERNAME.append(acc_hldr_name)
            f3 = open('bank_details.txt', 'w')
            f3.write("%s \n%s \n%s \n%s" %(BANKNAME, ACCOUNTNO, IFSCCODE, HOLDERNAME))
            f3.close()
            if pay == 1:
                print("Booking is Confirmed.....")
            elif pay == 2:
                exit()
                
        
            
            
class Main_menu(Journey, My_Bookings, Pnr_Enquiry):
    def __init__(self):
        Journey.__init__(self)
        My_Bookings.__init__(self)
        Pnr_Enquiry.__init__(self)

    def show_menu(self, i):
        print("Hello ", usernames[i])
        print("|  Press 1 for Ticket Bookings  ||  Press 2 for My Bookings  ||  Press 3 for PNR Enquiry  |")
        print("|  Press 4 for EXIT  |")
        try:
            choice1 = int(input("Enter your Choice"))
        except:
            self.show_menu(i)
        else:
            if choice1 == 1:
                print("Ticket Bookings")
                self.journey_details(i)
                self.cont(i)
            elif choice1 == 2:
                print("My Bookings")
                self.show_ticket(i)
                self.cont(i)
            elif choice1 == 3:
                print("PNR status")
                self.pnr_status(i)
                self.cont(i)
            elif choice1 == 4:
                exit()
            else:
                self.show_menu(i)
        
    def cont(self, i):
        choice2 = input("Press B for Back , Press E for Exit : ")
        if choice2 == "B":
            self.show_menu(i)
        elif choice2 == "E":
            exit()
        else:
            self.cont()
                    
                



class Sign_up():
    def __init__(self):
        pass

    def create_account(self):
        print("SIGN-Up")
        username1 = input("Create Username: ")
        if username1 in usernames:
            print("Username Already Exists.....")
            for j in (1, 100, 1):
                username_given = username1 + "" + str(j)
            usernames.append(username_given)
            print("Your automated username is : ", username_given)
            f = open("railwaysdb.txt", 'w')
            l = f.write("%s" %(usernames))
            f.close()
            self.create_password()
        else:
            usernames.append(username1)
            f = open("railwaysdb.txt", 'w')
            l = f.write("%s" %(usernames))
            f.close()
            self.create_password()
        
    def create_password(self):
        createpassword = input("Create New Password: ")
        confirmpassword = input("Confirm your Password: ")
        if createpassword == confirmpassword:
            password.append(confirmpassword)
            f = open("railwaysdb.txt", 'w')
            l = f.write("%s \n%s" %(usernames, password))
            f.close()
            print("Account Successfully Created...........")
            self.verify_username()
        else:
            self.create_account()

class Log_in(Sign_up, Main_menu):
    def __init__(self):
        Sign_up.__init__(self)
        Main_menu.__init__(self)

    def verify_username(self):
        print("LOG-In")
        username2 = input("Enter the Username: ")
        if username2 in usernames:
            index_no = usernames.index(username2)
            print("Welcome..........")
            self.verify_password(index_no)
        else:
            print("Wrong Username, Try Again...")
            self.verify_username()
            exit()

    def verify_password(self, i):
        c = 0
        while c < 3:
            currentpassword = input("Enter the Password : ")
            if currentpassword == password[i]:
                print("Login Successfull...")
                self.show_menu(i)
                break
            else:
                print("Wrong Password, Try Again...")
            c = c + 1
        if c == 3:
            print("Wrong INPUT many times.....TRY AFTER SOMETIME")
            exit()
            
    def user_choice(self):
        print("------------------------------------")
        print("   Welcome To RAILWAY RESERVATION   ")
        print("------------------------------------")
        try:
            choice = int(input("Enter 1 for SignUp , Enter 2 for LogIn, Enter 0 for Exit : "))
        except:
            self.user_choice()
        else:
            if choice == 1:
                self.create_account()
            elif choice == 2:
                self.verify_username()
            elif choice == 0:
                exit()
            else:
                self.user_choice()
            
            
o = Log_in()
o.user_choice()


        
