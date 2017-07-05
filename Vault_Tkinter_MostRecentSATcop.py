
#from Tkinter import *
import Tkinter as tk
# Random chars for the encryption
import random
import string


# def global_Vars():
#def set_globals():
global file_lines
global glo_U_P_Str  # The original user password
global Encrypted_Password  # Password that has been encrypted
global choice  # 3 part: Encrypt, Decrypt, Exit
global glo_UID_Str  # Initial Id password number
global glo_2Dkey_Int  # Length of the user password
global glo_location_Str
global glo_Username_Str


class PassWord_Vault(tk.Frame, tk.Text, tk.Scrollbar):
    # ============================================================================
    # ============================================================================
    # ============================================================================
    # ============================================================================
    # ============================================================================
    # ============================================================================
    # ============================================================================
    # ============================================================================
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        tk.Text.__init__(self, parent)
        # Want a scrollbar in the text, box, but cannot find solution without using .pack()
        # Currently we have the program set with .grid()
        #Scrollbar.__init__(self, master)

        self.grid()
        self.master = parent

        self.close_button = tk.Button(parent, text="Close", command=parent.quit)
        self.close_button.grid()
        self.deleteConfirm = False
        self.linecount = 0

        # This will be part of the dropdown box.
        # The dropdown was decided against.
        #self.studFiles = StringVar()  # Files will contain a string variable
        #self.studFiles.set('Choose')  # The files will be set empty by default.
        #options = ['Encrypt', 'Decrypt', 'Exit']  # List with The 2 options that we want in the drop down box.
        #self.choice = StringVar()
        #self.studDropDown = OptionMenu(parent, self.studFiles, *options, command=self.openFiles).grid(row=2)

        # Menu Labels
        # The primary labels for the program title
        #menuLabel1 = StringVar()
        menuLabel2 = tk.StringVar()
        menuLabel3 = tk.StringVar()
        menuLabel4 = tk.StringVar()
        menuLabel5 = tk.StringVar()
        # ==============================
        #menuLabel1.set("-----------------")
        # Set The primary labels for the program title
        menuLabel2.set("CyberNate")
        menuLabel3.set(" Password Encryption")
        #menuLabel4.set("")
        #menuLabel5.set("-----------")
        # ====================================================================================
        # This sets, and organizes the 4 LABEL titles There is one that is not needed currently. Top Line
        #menuLabel1x = Label(self, textvariable=menuLabel1, height=1)  # Create a label object
        #menuLabel1x.grid(row=1, column=0, columnspan=1, sticky=W)
        # -----------
        menuLabel2x = tk.Label(self, textvariable=menuLabel2, height=1)  # Create a label object
        menuLabel2x.config(font=("Cambria", 36, 'bold'))
        menuLabel2x.grid(row=2, column=0, columnspan=1, sticky=tk.W)
        # -----------
        menuLabel3x = tk.Label(self, textvariable=menuLabel3, height=1)  # Create a label object
        menuLabel3x.config(font=("Cambria", 36, 'bold'))
        menuLabel3x.grid(row=2, column=1, columnspan=1, sticky=tk.W)
        # -----------
        #menuLabel4x = Label(self, textvariable=menuLabel4, height=1)  # Create a label object
        #menuLabel4x.config(font=("Cambria", 36))
        #menuLabel4x.grid(row=4, column=0, columnspan=1, sticky=W)
        # -----------
        #menuLabel5x = Label(self, textvariable=menuLabel5, height=1)  # Create a label object
        #menuLabel5x.config(font=("Cambria", 36))
        #menuLabel5x.grid(row=4, column=0, columnspan=1, sticky=W)
        # ====================================================================================
        # The 6 primary labels
        userIDVAR = tk.StringVar()
        idRulesVAR = tk.StringVar()
        locationVAR = tk.StringVar()
        locationExVAR = tk.StringVar()
        usernameVAR = tk.StringVar()
        passwordVAR = tk.StringVar()
        passwordRULESVAR = tk.StringVar()
        deleteVAR = tk.StringVar()
        # -----------------------
        # Set The 6 primary labels
        userIDVAR.set('Enter ID Number :')
        idRulesVAR.set('1-7 Numbers, If NO ID, leave at 0')
        locationVAR.set('Enter Location     :')
        locationExVAR.set('              Example. Gmail.com')
        usernameVAR.set('Enter Username :')
        passwordVAR.set('Enter Password  :')
        passwordRULESVAR.set('              6 - 30 Characters')
        deleteVAR.set('Delete Password #')
        # -----------------------
        # Primary label, locations and detail for the 6 above
        userIDVARx = tk.Label(self, textvariable=userIDVAR, height=1)  # Create a label object
        userIDVARx.config(font=("Cambria", 18))
        userIDVARx.grid(row=11, column=0, columnspan=1, sticky=tk.W)
        # =========
        idRulesVARx = tk.Label(self, textvariable=idRulesVAR, height=1)  # Create a label object
        idRulesVARx.config(font=("Cambria", 10))
        idRulesVARx.grid(row=12, column=0, columnspan=1, sticky=tk.W)
        # =========
        locationVARx = tk.Label(self, textvariable=locationVAR, height=1)  # Create a label object
        locationVARx.config(font=("Cambria", 18))
        locationVARx.grid(row=13, column=0, columnspan=1, sticky=tk.W)
        # =========
        locationExVARx = tk.Label(self, textvariable=locationExVAR, height=1)  # Create a label object
        locationExVARx.config(font=("Cambria", 10))
        locationExVARx.grid(row=14, column=0, columnspan=1, sticky=tk.W)
        # =========
        usernameVARx = tk.Label(self, textvariable=usernameVAR, height=1)  # Create a label object
        usernameVARx.config(font=("Cambria", 18))
        usernameVARx.grid(row=15, column=0, columnspan=1, sticky=tk.W)
        # =========
        passwordVARx = tk.Label(self, textvariable=passwordVAR, height=1)  # Create a label object
        passwordVARx.config(font=("Cambria", 18))
        passwordVARx.grid(row=16, column=0, columnspan=1, sticky=tk.W)
        # =========
        passwordRULESVARx = tk.Label(self, textvariable=passwordRULESVAR, height=1)  # Create a label object
        passwordRULESVARx.config(font=("Cambria", 10))
        passwordRULESVARx.grid(row=17, column=0, columnspan=1, sticky=tk.W)
        # =========
        deleteVARx = tk.Label(self, textvariable=deleteVAR, height=1)  # Create a label object
        deleteVARx.config(font=("Cambria", 18))
        deleteVARx.grid(row=24, column=0, columnspan=1, sticky=tk.W)
        # =========
        # ===========================================================================
        # Variables to hold the user input for the main menu.
        # ID  # , Location, UserName, Password
        self.userIDVAR_input = tk.StringVar(None)
        self.userIDVAR_input.set('0')
        self.locationVAR_input = tk.StringVar(None)
        self.usernameVAR_input = tk.StringVar(None)
        self.passwordVAR_input = tk.StringVar(None)
        self.deleteVar_input = tk.StringVar(None)
        # There is a new line
        # We need to push through
        # ===========================================================================
        # ------------------------
        # 4 Entry boxes for the ID#, Location, UserName, Password
        self.userIDVAR_inputx = tk.Entry(self, textvariable=self.userIDVAR_input, width=40)
        self.userIDVAR_inputx.grid(row=11, column=1, sticky=tk.W)
        # return text if not valid input
        #if type(self.userIDVAR_input.get()) is not int:                 # Make sure we have a number
        #    self.userIDVAR_inputx.delete(0, END)
        #    self.userIDVAR_inputx.insert(0, "That is not a number!")
        # ------------------------
        self.locationVAR_inputx = tk.Entry(self, textvariable=self.locationVAR_input, width=40)
        self.locationVAR_inputx.grid(row=13, column=1, sticky=tk.W)
        # ------------------------
        self.usernameVAR_inputx = tk.Entry(self, textvariable=self.usernameVAR_input, width=40)
        self.usernameVAR_inputx.grid(row=15, column=1, sticky=tk.W)
        # ------------------------
        self.passwordVAR_inputx = tk.Entry(self, textvariable=self.passwordVAR_input, width=40)
        self.passwordVAR_inputx.grid(row=16, column=1, sticky=tk.W)
        # ------------------------
        self.deleteVar_inputx = tk.Entry(self, textvariable=self.deleteVar_input, width=20)
        self.deleteVar_inputx.grid(row=25, column=0, sticky=tk.W)
        # ====================================================================================
        # 3 Primary Buttons

        button1 = tk.Button(self, text="Encrypt Information", width=15, command=lambda: self.openFiles("Encrypt"))
        button1.grid(column=1, sticky=tk.W, padx=15, pady=5)
        # --------
        button2 = tk.Button(self, text="Decrypt Password List", width=15, command=lambda: self.openFiles("Decrypt"))
        button2.grid(column=1, sticky=tk.W, padx=15, pady=5)
        # --------
        button3 = tk.Button(self, text="View Encrypted List", width=15, command=lambda: self.openFiles("View"))
        button3.grid(column=1, sticky=tk.W, padx=15, pady=5)
        # --------
        button4 = tk.Button(self, text="Delete Password", width=15, command=lambda: self.openFiles("Delete"))
        button4.grid(row=26, column=0, sticky=tk.W, padx=15, pady=5)
        # --------
        # ====================================================================================
        # Used for setup, not needed anymore
        self.createWidgets()
        # ====================================================================================
        # The primary text box that will display passwords and encrypted list
        self.text_widget = tk.Text(parent)
        self.text_widget.grid()
        self.text_widget.insert(tk.END, '--------------------------------------\n')
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # ============================================================================
    # ============================================================================
    # ============================================================================
    # ============================================================================
    # ============================================================================
    # ============================================================================
        # =========================================================================
        # =========================================================================
        # =========================================================================
        # =========================================================================
        # =========================================================================
        # =========================================================================
        # =========================================================================
        # =========================================================================
        # =========================================================================
        # =========================================================================
        # =========================================================================
        # =========================================================================
        # =========================================================================
        # =========================================================================
        # =========================================================================
        # =========================================================================
        # =========================================================================
        # =========================================================================
        # =========================================================================
        # =========================================================================
        # =========================================================================
        # =========================================================================
        # =========================================================================
        # =========================================================================
        # =========================================================================
        # =========================================================================
        # =========================================================================
        # ============================================================================
        # ============================================================================
        # ============================================================================
        # ============================================================================
        # ============================================================================
        # ============================================================================
# DECRYPTION SECTION
    # DECRYPTION SECTION
    # DECRYPTION SECTION
    # DECRYPTION SECTION
    # DECRYPTION SECTION

    def openFiles(self, selection):  # There are two selections in our dropdown box.
        # If they select "Student Grades" then we will call in the openGrades function,
        # or else it must be to call in the rank instead.
        if (self.userIDVAR_input.get() == ''):
            self.userIDVAR_input.set('0')


        confirm = self.Ask_For_PassWord_ID_Number(self.userIDVAR_input.get())
        # True for confirm, now check password length
        if confirm == True:
            confirm = self.check_Password_Length(self.passwordVAR_input.get())

        print "confirm in openfiles 1 = ", confirm

            # Remember this must match what we have in our dropdown list.
        if ( selection == "Encrypt" and confirm == True) :
            # Clear the current text box
            print 'made it to Encrypt 1'

            self.text_widget.delete('1.0', tk.END)
            print self.userIDVAR_input.get()
            print self.locationVAR_input.get()
            print self.usernameVAR_input.get()
            print self.passwordVAR_input.get()
            print 'made it to Encrypt 2'

            self.encrypt_in_Main()
            self.openFiles('Decrypt')
        elif selection == "Decrypt":
            self.greet()
            # Clear the current text box
            self.text_widget.delete('1.0', END)
            # Start decryption process
            self.decrypt_in_Main()
        elif selection == "View":
            # Clear the current text box
            self.text_widget.delete('1.0', END)
            # View what the encrypted list looks like.
            self.View_Encrypted_List()
        elif selection == "Exit":
            print "selected Exit"

        elif selection == "Delete":
            self.deleteConfirm = True
            print "selected Delete"
            print self.deleteVar_input.get()
            self.deleteAPassword()


    # ============================================================================
    # ============================================================================
    # ============================================================================
    # ============================================================================
    # ============================================================================

    def say_hi(self):
        print "hi there, everyone!"
        print "chose Encrypt"

    # ============================================================================
    # ============================================================================
    # ============================================================================
    # ============================================================================
    # ============================================================================

    def greet(self):

        print "Greetings!"
        print "chose D23ecrypt"

    # ============================================================================
    # ============================================================================
    # ============================================================================
    # ============================================================================
    # ============================================================================

    def createWidgets(self):
        pass
        #self.QUIT = Button(self)
        #self.QUIT["text"] = "QUIT"
        #self.QUIT["fg"]   = "red"
        #self.QUIT["command"] = self.quit
        #self.QUIT.grid(row=0, column=0)


        #self.hi_there = Button(self)
        #self.hi_there["text"] = "Hello",
        #self.hi_there["command"] = self.say_hi

        #self.hi_there.grid(row=16)

# ============================================================================
# ============================================================================
# ============================================================================
# ============================================================================
# ============================================================================

    def decrypt_in_Main(self):

        password_List = self.de_100()
        final_list = []

        for x in range(len(password_List)):
            f_contents = []

            transfer = password_List[x]
            for i in range(len(password_List[x])):
                f_contents.extend(transfer[i])

            key, encrypted_send = self.Convert_Password_Number(f_contents)
            key, Number_ID, Encrypted_List = self.Use_Key_to_Decrypt_Num_ID(key, encrypted_send)
            glo_2Dkey_Int, glo_UID_Str, glo_U_P_Str, glo_Username_Str, glo_location_Str = self.now_decrypt_Password(key,
                                                                                                               Number_ID, Encrypted_List)

            final_list.append(glo_UID_Str)
            final_list.append(glo_location_Str)
            final_list.append(glo_Username_Str)
            final_list.append(glo_U_P_Str)

        finalString = str('')
        finalString += '--------------------------------------\n'
        # Insert into the text widget
        self.text_widget.grid()

        self.text_widget.insert(tk.END, '--------------------------------------\n')



        print "--------------------------------------"
        for x in range(len(final_list)):
            print x+1,  '[ User ID# ]\t' + final_list[4*x]
            finalString += (str(x+1) + '[ User ID# ]\t' + final_list[4*x] + '\n')
            self.text_widget.insert(tk.END, str(x+1) + '[ User ID# ]\t' + final_list[4*x] + '\n')

            print x+1,  '[ Location ]\t' + final_list[4*x+1]
            finalString += (str(x+1) + '[ Location ]\t' + final_list[4*x+1] + '\n')
            self.text_widget.insert(tk.END, str(x+1) + '[ Location ]\t' + final_list[4*x+1] + '\n')

            print x+1,  '[ Username ]\t' + final_list[4*x+2]
            finalString += (str(x+1) + '[ Username ]\t' + final_list[4*x+2] + '\n')
            self.text_widget.insert(tk.END, str(x+1) + '[ Username ]\t' + final_list[4*x+2] + '\n')

            print x+1,  '[ Password ]\t' + final_list[4*x+3]
            finalString += (str(x+1) + '[ Password ]\t' + final_list[4*x+3] + '\n')
            self.text_widget.insert(tk.END, str(x+1) + '[ Password ]\t' + final_list[4*x+3] + '\n')
            self.text_widget.insert(tk.END, '--------------------------------------\n')

            finalString += '--------------------------------------\n'
            print "--------------------------------------"

            # Insert into the text widget
            #text_widget = Text(self)
            #text_widget.insert(END, finalString)
            #text_widget.grid()

            if (x == (len(final_list)/4 - 1)):
                self.text_widget.insert(tk.END, '--------------------------------------\n')

                #print 'final_string = ', finalString
                break

# ============================================================================
# ============================================================================
# ============================================================================
# ============================================================================
# ============================================================================
# =========================================================================
    def de_100(self):

        Full_Encrypted_List = []
        self.linecount = 0
        with open("Vault.txt", 'r+') as fp:
            for line in fp:

                # This is the full line as a string.
                filler = line.rstrip()
                # Pull the first 2 chars.
                # If the first 2 chars are 'FI' then the previous line is the encrypted line
                verify_Char = filler[0] + filler[1]

                # If the first two char are 'FI' then store the previous line.
                if verify_Char == 'FI':
                    Full_Encrypted_List.append(filler2)

                # place filler2 at the end. This won't change until confirmed not FI above
                filler2 = filler
        print 'self.linecount =', self.linecount
        return Full_Encrypted_List

        # End Full_Encrypted_List =================================================
# ============================================================================
# ============================================================================
# ============================================================================
# ============================================================================
# ============================================================================
    # Convert_Password_Number =================================================

    def Convert_Password_Number(self, lines):

        # lines is the full Encrypted password LIST coming in.
        # This is just to get the key value from the first 2 digits.

        # Now have full encrypted list
        # First 2 chars are key
        # First 2 chars will be the key subtract 20 from ascii
        # Will be 2 digit char
        # Convert 2 digits to int
        # Subtract 25 from int
        # Will be the key.

        for x in range(2):
            changer = lines[x]  # Switch first char to changer
            changer = self.Decrypt_2Digit_Front_Key(changer)
            lines[x] = changer  # set char back into Encrpted it is a number but not right yet

        # Need to convert first two digits to int and subtract 25
        key = ''.join(lines[0] + lines[1])
        Encrypted_Send = ''.join(lines)

        # Change key back into int
        key = int(key)
        # Subtract 25 from 1
        # key int
        key = key - 25

        # We have the key, now set it global
        global_2d_key = key

        return (key, Encrypted_Send)

        # End Convert_Password_Number  ============================================
# ============================================================================
# ============================================================================
    def deleteAPassword(self):

        self.linecount =0
        f = open("Vault.txt", "r")
        lines = f.readlines()
        f.close()
        #f = open("Vault.txt", "w")

        for line in lines:

            if line[0] == 'F' and line[1] == 'I':
                self.linecount = self.linecount + 1
                print line[0]
                print line[1]
            elif line[0] != 'F' and line[1] != 'I' and self.linecount != self.deleteVar_input:
                pass#f.write(line)
                #print line[0]
                #print line[1]

        print 'We just deleted the line hopefully'


                # ============================================================================
# ============================================================================
# ============================================================================
    # Use Key to Decrypt UserID================================================

    def Use_Key_to_Decrypt_Num_ID(self, key, Encrypted_Password):

        Encrypted_List = []
        Number_ID = []
        # Turn string into a list.
        for x in range(len(Encrypted_Password)):
            Encrypted_List.extend(Encrypted_Password[x])

        # Run the length of the password but stop at the space
        # changer = changer + (9 * x + key // 5)  # multiply ascii value by the key/5
        for x in range(len(Encrypted_Password)):
            changer = Encrypted_List[x+2]
            changer = self.Decrypt_the_NumberID(changer, key, x)
            Encrypted_List[x+2] = changer
            if (changer == " "):
                break;
            Number_ID.extend(changer)


        # join to send as string
        #Encrypted_Password = "".join(Encrypted_List)

        # Decrypted user id in list. Turn into global string.
        global_UserID_STRING = ''.join(Number_ID)

        return (key, Number_ID, Encrypted_List)


    # End Use Key to Decrypt User ID ==========================================
# =========================================================================
# =========================================================================
    # Decrypt the password Function ===========================================
    def Decrypt_the_NumberID(self, changer, key, x):

        # Sending just the UserID char's from the function below.
        changer = ord(changer)
        changer = changer - (9 * x + key // 5)
        changer = chr(changer)

        return changer

    # End Decrypt_the_password ================================================
# =========================================================================
# =========================================================================
# =========================================================================
# Use Key to Decrypt UserID================================================
# =========================================================================
# =========================================================================
    # Decrypt password ========================================================
    def now_decrypt_Password(self, key, numberID, password):
        userID_STRING = ''.join(numberID)
        just_password = []

        username = []
        location = []
        space1 = int(0)
        space2 = int(0)

        # --------------------------------------------------------------------
        # Cycle through encrypted password, pull out space locations.
        # There are only 2 spaces after the userID number
        for x in range(10, len(password)):
            if password[x] == ' ':
                space2 = x
                if space1 != 0:
                    break
            if password[x] == ' ':
                space1 = x
        # We now have the username and location spaces

        # --------------------------------------------------------------------
        # After the first space, pull the encrypted username out
        for x in range(space1+1, len(password)):
            # The 2nd space indicates the location. Break out
            if password[x] == ' ':
                break
            username.extend(password[x])

        # --------------------------------------------------------------------
        # We just pulled the encrypted username. Now decrypt
        username2 = []
        for x in range(len(username)):
            changer = username[x]  # Grab the char
            changer = self.Decrypt_The_Password(changer, len(username))
            username2.extend(changer)
        # Turn decrypted username list into a string.
        username = ''.join(username2)

        # --------------------------------------------------------------------
        # --------------------------------------------------------------------
        # After the first space, pull the encrypted location out
        for x in range(space2 + 1, len(password)):
            # The location is the end of the line
            location.extend(password[x])

        # --------------------------------------------------------------------
        # We just pulled the encrypted location. Now decrypt
        location2 = []

        for x in range(len(location)):
            changer = location[x]  # Grab the char
            changer = self.Decrypt_The_Password(changer, len(location))
            location2.extend(changer)
        # Turn decrypted location list into a string.
        location = ''.join(location2)

        # --------------------------------------------------------------------


        # We pulling out the key, USerID and Space here
        # Just_Password will be just that, the encrypted password, nothing else.
        # Now we hop to the start of the password and decrypt
        for x in range((3+len(numberID)), len(password)):
            just_password.extend(password[x])

        # now we have just the Encrypted password in "just_password", pull selections and decrypt
        user_password = []
        for x in range(key):
            changer = just_password[x * 3]  # Grab the char
            changer = self.Decrypt_The_Password(changer, key)
            user_password.extend(changer)

        user_password_STRING = ''.join(user_password)


        return (key, userID_STRING, user_password_STRING, username, location )


    # End Decrypt password ====================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
    # Decrypt the Password Function ===========================================

    def Decrypt_The_Password(self, changer, key):

        changer = ord(changer)  # change to ascii value
        changer = changer - (5 + key // 5)  # Add to value based on password length
        changer = chr(changer)  # Change new value back to a char

        return changer

    # Decrypt password ========================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
    # Convert_2Digit Front_Key ================================================

    def Decrypt_2Digit_Front_Key(self, changer):

        # Will send First 2 chars.
        # First 2 chars will be the key subtract 20 from ascii
        # Will be 2 digit char
        # Convert 2 digits to int
        # Subtract 25 from int
        # Will be the key.

        changer = ord(changer)  # Switch char to ascii value
        changer = changer - 20  # sub 20 from ascii value
        changer = chr(changer)  # convert back into char

        return changer

    # End Convert_2Digit Front_Key ============================================
# =========================================================================
# =========================================================================
    def View_Encrypted_List(self):
        Full_Encrypted_List = []

        with open("Vault.txt", 'r+') as fp:
            for line in fp:

                # This is the full line as a string.
                filler = line.rstrip()
                # Pull the first 2 chars.
                Full_Encrypted_List.append(filler)

        self.text_widget.insert(tk.END, Full_Encrypted_List)
    # DECRYPTION SECTION
    # DECRYPTION SECTION
    # DECRYPTION SECTION
    # DECRYPTION SECTION End

# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # ============================================================================
    # ============================================================================
    # ============================================================================
    # ============================================================================
    # ============================================================================
    # ============================================================================
    # =========================================================================
    # =========================================================================
    # Final Encrypt
    # Final Encrypt
    # Final Encrypt
    # Final Encrypt

    def encrypt_in_Main(self):

        # Write to file, uses the returned Encryption string.
        glo_UID_Str, glo_U_P_Str, glo_2Dkey_Int, glo_Username_Str, glo_location_Str = self.encryption()

        self.Write_to_File(glo_UID_Str, glo_U_P_Str, glo_2Dkey_Int, glo_Username_Str, glo_location_Str)

        spare_key = 00
        for x in range(99):
            self.filler_lines(spare_key)
            while (spare_key < 100):
                spare_key = spare_key + 1 * 3
                spare_key = spare_key * 3
            if (spare_key > 100):
                spare_key = spare_key - 99

                # End Encrypt in Main Func=================================================
                # =========================================================================
                # =========================================================================
    # =========================================================================
    # =========================================================================
    # Encrypt Main ============================================================

    def encryption(self):

        # Bring in the user ID safety number
        #Password_ID = self.Ask_For_PassWord_ID_Number()
        Password_ID = self.userIDVAR_input.get()


        # ---------------------------------------------------------------------------
        # We Need a location for this password
        # The ask_for_PW_Location is for standard python, not Tkinter
        #PW_Location = self.ask_for_PW_location()
        PW_Location = self.locationVAR_input.get()

        Location_Encrypt = []

        for x in range(len(PW_Location)):
            changer = PW_Location[x]
            changer = self.encrypt_the_password(changer, len(PW_Location))
            Location_Encrypt.extend(changer)  # Enter in to encryption locaiton.
            # --------------------------------------------------------------------
        #   Password[key * 3] = '\0'; line 62 in xcode? not working here.
        PW_Location = ''.join(Location_Encrypt)  # convert to a string

        # Now we have a password web Location as a string that is encrypted and ready to send.

        # ---------------------------------------------------------------------------
        # ---------------------------------------------------------------------------
        # Bring in initial user password to encrypt.
        # ask for username is for in house python, not Tkinter
        #Username = self.ask_for_Username()
        Username = self.usernameVAR_input.get()

        Username_Encrypt = []

        for x in range(len(Username)):
            changer = Username[x]
            changer = self.encrypt_the_password(changer, len(Username))
            Username_Encrypt.extend(changer)  # Enter in to encryption locaiton.
            # --------------------------------------------------------------------
        #   Password[key * 3] = '\0'; line 62 in xcode? not working here.
        Username = ''.join(Username_Encrypt)  # convert to a string

        # Now we have a Username as a string that is encrypted and ready to send.
        # ---------------------------------------------------------------------------
        # ---------------------------------------------------------------------------
        # This part is to Encrypt the Password
        #User_Password = str(self.Ask_For_User_Password())
        # Remember the confirm is for Tkinter
        User_Password = self.passwordVAR_input.get()

        # Set the key to the original password length.
        key = len(User_Password)

        # We have Encrypted as a global, declared it a list here
        Encrypted_Password = []

        # For the next loop we need Encrypted to be 3 times the length of the user password
        # We extend the Encrpyted 3 times the length with rnadom chars
        Encrypted_Password.extend(random.choice(
            string.ascii_lowercase + string.ascii_uppercase + string.digits + '!' + '@' + '#' + '%' +
            '^' + '&' + '*' + ',' + '.' + '/' + '?' + ';' + ':' + '[' + ']' + '{' + '}' + '-' + '_')
                                  for i in range(key * 3))

        for x in range(key):
            changer = User_Password[x]  # Grab the char
            changer = self.encrypt_the_password(changer, key)
            Encrypted_Password[x * 3] = changer  # Enter in to encryption locaiton.
            # --------------------------------------------------------------------
        #   Password[key * 3] = '\0'; line 62 in xcode? not working here.
        Encrypted_Password = ''.join(Encrypted_Password)  # convert to a string

        return (Password_ID, Encrypted_Password, key, Username, PW_Location)

        # End Encrypt  ============================================================
        # =========================================================================
        # =========================================================================

    # =========================================================================
    # Write to file ===========================================================

    def Write_to_File(self, Password_ID, Encrypted_Password, key, username, PW_location):

        # 2 digit size,    <= 8digits User ID,   single-space,   password
        # Add a space onto the <= 8digits user ID
        # The only space in the ecrypted will be the divider
        Number_Space = Password_ID + ' '

        # Turn into list so we can adjust char by char
        Number_Space = list(Number_Space)

        # Encrypt the UserID + space. Use a function
        for x in range(len(Number_Space)):  # Will be up to 9.   -> <= 8Digits User Id + 1 space
            changer = Number_Space[x]  # create the change char
            changer = self.encrypt_NumberSpace(changer, key, x)  # Send to function for ascii conversion.
            Number_Space[x] = changer  # place back into list

        Number_Space = ''.join(Number_Space)  # change list back to solid string

        # Set key to double digit after 10 before encryption
        # Will need key for decryption, will always be the first 2 digits.
        # If first digit is 6,7,8,9     after -25 on decrypt, then it must be single.
        # If first digit is 1,2,3,4,5   after -25 on decrypt, then it must be a double.
        # 25 + 6 = 31
        # 31 - 25 = 6   [6][0] we would know the length is 6 can be more than 30
        # 35 - 25 = 10  [1][0] we know it must be 10 since we cant be less than 6
        key = int(key + 25)  # Still an 2 digit int
        key = str(key)  # Change int to string
        key = list(key)  # Change str into list

        for x in range(len(key)):
            changer = key[x]  # Set first list char to changer
            changer = self.encrypt_2D_Key(changer)
            key[x] = changer  # Set new char to key0

        key = ''.join(key)  # Convert from list back to string

        # First 2 chars will be the key subtract 20 from ascii
        # Will be 2 digit char
        # Convert 2 digits to int
        # Subtract 25 from int
        # Will be the key.

        # We are appending to current file
        f = open('Vault.txt', 'a')
        # Writing to file:
        # 1st 2 char = password length.
        # Next set is the User ID number until you hit a space.
        # The space is the only in the entire password.
        # Then the password encrypted is after. We need a \n to write to a new line after each password.

        f.write(key + Number_Space + Encrypted_Password + ' ' + username + ' ' + PW_location + '\n')  # Write numb +
        # space +
        # password
        # to file after
        # encryption
        f.close()

    # End Write to File =======================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    def filler_lines(self, filler_key):

        filler_password = []
        filler_ID = []
        filler_username = []
        filler_location = []
        # -------------------

        filler_ID.extend(random.choice(
            string.ascii_lowercase + string.ascii_uppercase + string.digits + '!' + '@' + '#' + '%' +
            '^' + '&' + '*' + ',' + '.' + '/' + '?' + ';' + ':' + '[' + ']' + '{' + '}' + '-' + '_')
                         for x in range(8))
        filler_ID = ''.join(filler_ID)

        # -------------------

        filler_password.extend(random.choice(
            string.ascii_lowercase + string.ascii_uppercase + string.digits + '!' + '@' + '#' + '%' +
            '^' + '&' + '*' + ',' + '.' + '/' + '?' + ';' + ':' + '[' + ']' + '{' + '}' + '-' + '_')
                               for i in range(random.randrange(10, 128, 2)))
        filler_password = ''.join(filler_password)

        # -------------------

        filler_username.extend(random.choice(
            string.ascii_lowercase + string.ascii_uppercase + string.digits + '!' + '@' + '#' + '%' +
            '^' + '&' + '*' + ',' + '.' + '/' + '?' + ';' + ':' + '[' + ']' + '{' + '}' + '-' + '_')
                               for i in range(10))
        filler_username = ''.join(filler_username)

        # -------------------

        filler_location.extend(random.choice(
            string.ascii_lowercase + string.ascii_uppercase + string.digits + '!' + '@' + '#' + '%' +
            '^' + '&' + '*' + ',' + '.' + '/' + '?' + ';' + ':' + '[' + ']' + '{' + '}' + '-' + '_')
                               for i in range(10))
        filler_location = ''.join(filler_location)

        self.Write_to_File(filler_ID, filler_password, filler_key, filler_username, filler_location)

        # =========================================================================
        # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # Encrypt Password Function ===============================================

    def encrypt_the_password(self, changer, key):

        changer = ord(changer)              # change to ascii value
        changer = changer + (5 + key // 5)  # Add to value based on password length
        changer = chr(changer)              # Change new value back to a char

        return changer

    # End Encrypt Password ====================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # Require Password for location

    def gather_Password_Location(self, password_str):
        print "What is the password [' " + password_str + " '] for?  "
        location = str(raw_input("Enter [1-3]: "))
        print "location = ", location


    # End Require Password for location
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # User Confirmation =======================================================

    def User_Location_Confirmation(self, PW_Location, confirm):

        print "\nIs this what the password is for? \nY or N?"
        print "--------------------------------------"
        print '\t\t', PW_Location
        print "--------------------------------------"

        confirm = str(raw_input())

        return confirm

    # End User Confirmation ===================================================
    # =========================================================================
    # =========================================================================
    # Ask for PW Location =====================================================

    def ask_for_PW_location(self):

        PW_Location = " "

        confirm = 'No' # confirm is created here, also passed to confirm function.
        # ---------------------------------------------
        # confirm is pre set to not pass the while loop
        while (confirm != "Y" and confirm != "y" and confirm != "Yes" and confirm != "yes"):

            # We first check for length, will not get Local password back if length is not 6-30
            PW_Location = str(raw_input("What is this password for?  ex. Gmail.com "))

            # password can be 6-30 but not be what the user wanted. confirm again.
            confirm = self.User_Location_Confirmation(PW_Location, confirm)

            # If the confirm does not pass, we reset the password
            if (confirm != "Y" and confirm != "y" and confirm != "Yes" and confirm != "yes"):
                PW_Location = " "

        return PW_Location

    # End Ask for PW Location =================================================
    # =========================================================================
    # Username Confirmation =======================================================

    def Username_Confirmation(self, Username, confirm):

        print "\nIs this the actual Username? \nY or N?"
        print "--------------------------------------"
        print '\t\t', Username
        print "--------------------------------------"

        confirm = str(raw_input())

        return confirm

    # End User Confirmation ===================================================
    # =========================================================================
    # =========================================================================
    # Ask for Username

    def ask_for_Username(self):

        Username = ""

        confirm = 'No' # confirm is created here, also passed to confirm function.
        # ---------------------------------------------
        # confirm is pre set to not pass the while loop
        while (confirm != "Y" and confirm != "y" and confirm != "Yes" and confirm != "yes"):

            # We first check for length, will not get Local password back if length is not 6-30
            Username = str(raw_input("What is this Username ?   "))

            # password can be 6-30 but not be what the user wanted. confirm again.
            confirm = self.Username_Confirmation(Username, confirm)

            # If the confirm does not pass, we reset the password
            if (confirm != "Y" and confirm != "y" and confirm != "Yes" and confirm != "yes"):
                Username = " "

        return Username

    # End Ask for PW Location =================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # encrypt_NumberSpace =====================================================

    def encrypt_NumberSpace(self, changer, key, x):
        changer = ord(changer)  # adjust to the ascii value

        # The number and space are changed 9*x plus the whole num of div by 5
        changer = changer + (9 * x + key // 5)  # multiply ascii value by the key//5

        changer = chr(changer)  # convert new ascii back to char

        return changer

        # End encrypt_NumberSpace(================================================
        # =========================================================================
        # =========================================================================
        # =========================================================================
    # =========================================================================
    # =========================================================================
    # encrypt_2D_Key Function ================================================

    def encrypt_2D_Key(self, changer):

        changer = ord(changer)  # Change to ascii values
        changer = changer + 20  # Add 20 to ascii value
        changer = chr(changer)  # Change ascii value into char

        return changer

    # End encrypt_2D_Key ======================================================
    # =========================================================================
# =========================================================================
# =========================================================================
    # =========================================================================
    # Ask for Password ID Number==============================================

    def Ask_For_PassWord_ID_Number(self, password_ID):
        # We are sending in the password gathered from the entry box.
        # Check it, if it does not pass return a false
        confirm = False

        password_ID = self.userIDVAR_input.get()
        try:
            int(password_ID)
            confirm = True
            password_ID = int(password_ID)
            print 'No ValueError'

        except ValueError:
            confirm = False
            self.userIDVAR_inputx.delete(0, END)
            self.userIDVAR_inputx.insert(0, 'ID# = 7 Numbers or less. Numbers Only')
            print 'ValueError = False'

        print "PID in ask for password id = ", password_ID

        if type(password_ID) is int:                 # Make sure we have a number
            confirm = True
        else:
            # This was not a number, mark entry box
            print "Please enter a number!"
            self.userIDVAR_inputx.delete(0, tk.END)
            self.userIDVAR_inputx.insert(0, 'ID# = 7 Numbers or less. Numbers Only')

        # Accept IDnumber as an int for numerical verification.
        if password_ID < 0:            # Make sure we have a positive int.
            print "Password ID cannot be less than 0"
            self.userIDVAR_inputx.delete(0, tk.END)
            self.userIDVAR_inputx.insert(0, 'ID# = 7 Numbers or less. Numbers Only')
            confirm = False

        elif password_ID > 9999999:    # Check for less than 9 digits
            print "Password ID NUMBER must be 7-Digits or less."
            confirm = False
            self.userIDVAR_inputx.delete(0, tk.END)
            self.userIDVAR_inputx.insert(0, 'ID# = 7 Numbers or less. Numbers Only')
            # ---------------------------------------------------------------

        # ---------------------------------------------------------------

        print "--------------------------------------"
        print "The returned user id number = ", password_ID
        print "--------------------------------------"

        Password_ID = str(password_ID)          #conver to string for later file write.
        return confirm
        # We now have a positive password ID number.
        # Ask for a password.

    # End Ask for Password ID Number ==========================================
    # =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
    # =========================================================================
    # Ask for User Password: 6 - 30 char ======================================

    def Ask_For_User_Password(self):
        # Most of this is built for normal python.
        # We only need to check the length here

        #Local_Password = "xxx"  # Starts in ask for password
        Local_Password = self.passwordVAR_input.get()
        #confirm = 'No' # confirm is created here, also passed to confirm function.
        confirm = False
        # ---------------------------------------------
        # confirm is pre set to not pass the while loop
        #while (confirm != "Y" and confirm != "y" and confirm != "Yes" and confirm != "yes"):

            # We first check for length, will not get Local password back if length is not 6-30
            #Local_Password = self.check_Password_Length(Local_Password)
        confirm = self.check_Password_Length(self.passwordVAR_input.get())
            # password can be 6-30 but not be what the user wanted. confirm again.
            #confirm = self.User_Password_Confirmation(Local_Password, confirm)

            # If the confirm does not pass, we reset the password
            #if (confirm != "Y" and confirm != "y" and confirm != "Yes" and confirm != "yes"):
                #Local_Password = " "


        # If they Create a faulty initial password.
        # If the input is <6 or >30 characters then repeat.

        print "The  password = ", Local_Password
        print "--------------------------------------"

        # User input and confirmed their password. Set it globally
        # Reset it after it is decrpyted.
        #global_User_Password_STRING = Local_Password

        #return Local_Password
        return confirm


    # End Ask for User Password================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
    # Password Length Check 6 - 30 char =======================================
    # Remember this is very different for standard python or Tkinter
    def check_Password_Length(self, Local_Password):
        confirm = False

        #while (len(Local_Password) < 6 or len(Local_Password) > 30):
        if (len(Local_Password) >= 6 and len(Local_Password) <= 30):
            confirm = True
            #Local_Password = str(raw_input("Enter your password. Must be 6-30 characters: "))
            print "--------------------------------------"
        else:
            self.passwordVAR_inputx.delete(0, tk.END)
            self.passwordVAR_inputx.insert(0, 'Password must be 6 --> 30 Characters')
            confirm = False

        #return Local_Password
        return confirm

    # End Password Length Check ===============================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
    # User Confirmation =======================================================

    def User_Password_Confirmation(self, Local_Password, confirm):

        print "\nIs this what you would like for your personal password? \nYes or No?"
        print "--------------------------------------"
        print '\t\t', Local_Password
        print "--------------------------------------"

        confirm = str(raw_input())

        return confirm

    # End User Confirmation ===================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================

root = tk.Tk()
app = PassWord_Vault(parent=root)
root.title('The Password Vault')
root.geometry('600x800+1+1')

app.mainloop()
root.destroy()

# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================