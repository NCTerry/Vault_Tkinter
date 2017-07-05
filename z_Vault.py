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

# ========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# Start Menu =============================================================

# Simple menu asking for user choice, will return an in value 1, 2, 3
def Menu():
    choice = str('4')  # Starts in menu
    while (choice != '1' and choice != '2' and choice != '3'):
        print "-----------------"
        print "1) Encrypt"
        print "2) Decrypt"
        print "3) Exit"
        print "-----------------"

        choice = str(raw_input("Enter [1-3]: "))

    return choice

# End Menu ===============================================================
# =========================================================================
# =========================================================================
# =========================================================================
# Ask for Password ID Number==============================================

def Ask_For_PassWord_ID_Number():
    Password_ID = int(-1)  # Starts in ask for ID

    while True:
        try:
            # Accept IDnumber as an int for numerical verification.
            Password_ID = int(raw_input("\nEnter an encryption ID number for this password: "))
            if Password_ID <= 0:            # Make sure we have a positive int.
                print "Password ID number must be greater than 0"
                continue
            elif Password_ID > 99999999:    # Check for less than 9 digits
                print "Password ID NUMBER must be 8-Digits or less."
                continue
        # ---------------------------------------------------------------
        except ValueError:                  # Make sure we have a number
            print "Please enter a number!"
            continue
        # ---------------------------------------------------------------
        else:
            break

    print "--------------------------------------"
    print "The returned user id number = ", Password_ID
    print "--------------------------------------"

    Password_ID = str(Password_ID)          #conver to string for later file write.
    return Password_ID
    # We now have a positive password ID number.
    # Ask for a password.

# End Ask for Password ID Number ==========================================
# =========================================================================
# =========================================================================
# =========================================================================
# Password Length Check 6 - 30 char =======================================

def check_Password_Length(Local_Password):

    while (len(Local_Password) < 6 or len(Local_Password) > 30):

        Local_Password = str(raw_input("Enter your password. Must be 6-30 characters: "))
        print "--------------------------------------"

    return Local_Password

# End Password Length Check ===============================================
# =========================================================================
# =========================================================================
# =========================================================================
# User Confirmation =======================================================

def User_Password_Confirmation(Local_Password, confirm):

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
# Ask for User Password: 6 - 30 char ======================================

def Ask_For_User_Password():

    Local_Password = "xxx"  # Starts in ask for password

    confirm = 'No' # confirm is created here, also passed to confirm function.
    # ---------------------------------------------
    # confirm is pre set to not pass the while loop
    while (confirm != "Y" and confirm != "y" and confirm != "Yes" and confirm != "yes"):

        # We first check for length, will not get Local password back if length is not 6-30
        Local_Password = check_Password_Length(Local_Password)

        # password can be 6-30 but not be what the user wanted. confirm again.
        confirm = User_Password_Confirmation(Local_Password, confirm)

        # If the confirm does not pass, we reset the password
        if (confirm != "Y" and confirm != "y" and confirm != "Yes" and confirm != "yes"):
            Local_Password = " "


    # If they Create a faulty initial password.
    # If the input is <6 or >30 characters then repeat.

    print "The  password = ", Local_Password
    print "--------------------------------------"

    # User input and confirmed their password. Set it globally
    # Reset it after it is decrpyted.
    global_User_Password_STRING = Local_Password

    return Local_Password

# End Ask for User Password================================================
# =========================================================================
# =========================================================================
# =========================================================================
# encrypt_NumberSpace =====================================================

def encrypt_NumberSpace(changer, key, x):
    changer = ord(changer)  # adjust to the ascii value

    # The number and space are changed 9*x plus the whole num of div by 5
    changer = changer + (9 * x + key // 5)  # multiply ascii value by the key//5

    changer = chr(changer)  # convert new ascii back to char

    return changer

# End encrypt_NumberSpace(================================================
# =========================================================================
# =========================================================================
# =========================================================================
# encrypt_2D_Key Function ================================================

def encrypt_2D_Key(changer):

    changer = ord(changer)  # Change to ascii values
    changer = changer + 20  # Add 20 to ascii value
    changer = chr(changer)  # Change ascii value into char

    return changer

# End encrypt_2D_Key ======================================================
# =========================================================================
# Write to file ===========================================================

def Write_to_File(Password_ID, Encrypted_Password, key, username, PW_location):

    # 2 digit size,    <= 8digits User ID,   single-space,   password
    # Add a space onto the <= 8digits user ID
    # The only space in the ecrypted will be the divider
    Number_Space = Password_ID + ' '

    # Turn into list so we can adjust char by char
    Number_Space = list(Number_Space)

    # Encrypt the UserID + space. Use a function
    for x in range(len(Number_Space)):                  # Will be up to 9.   -> <= 8Digits User Id + 1 space
        changer = Number_Space[x]                       # create the change char
        changer = encrypt_NumberSpace(changer, key, x)  # Send to function for ascii conversion.
        Number_Space[x] = changer                       # place back into list


    Number_Space = ''.join(Number_Space)                # change list back to solid string

    # Set key to double digit after 10 before encryption
    # Will need key for decryption, will always be the first 2 digits.
    # If first digit is 6,7,8,9     after -25 on decrypt, then it must be single.
    # If first digit is 1,2,3,4,5   after -25 on decrypt, then it must be a double.
    # 25 + 6 = 31
    # 31 - 25 = 6   [6][0] we would know the length is 6 can be more than 30
    # 35 - 25 = 10  [1][0] we know it must be 10 since we cant be less than 6
    key = int(key + 25)         # Still an 2 digit int
    key = str(key)              # Change int to string
    key = list(key)             # Change str into list

    for x in range(len(key)):
        changer = key[x]            # Set first list char to changer
        changer = encrypt_2D_Key(changer)
        key[x] = changer            # Set new char to key0

    key = ''.join(key)              # Convert from list back to string

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
# Encrypt Password Function ===============================================

def encrypt_the_password(changer, key):

    changer = ord(changer)              # change to ascii value
    changer = changer + (5 + key // 5)  # Add to value based on password length
    changer = chr(changer)              # Change new value back to a char

    return changer

# End Encrypt Password ====================================================
# =========================================================================
# =========================================================================
# =========================================================================
# Require Password for location

def gather_Password_Location(password_str):
    print "What is the password [' " + password_str + " '] for?  "
    location = str(raw_input("Enter [1-3]: "))
    print "location = ", location


# End Require Password for location
# =========================================================================
# =========================================================================
# =========================================================================
# User Confirmation =======================================================

def User_Location_Confirmation(PW_Location, confirm):

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

def ask_for_PW_location():

    PW_Location = " "

    confirm = 'No' # confirm is created here, also passed to confirm function.
    # ---------------------------------------------
    # confirm is pre set to not pass the while loop
    while (confirm != "Y" and confirm != "y" and confirm != "Yes" and confirm != "yes"):

        # We first check for length, will not get Local password back if length is not 6-30
        PW_Location = str(raw_input("What is this password for?  ex. Gmail.com "))

        # password can be 6-30 but not be what the user wanted. confirm again.
        confirm = User_Location_Confirmation(PW_Location, confirm)

        # If the confirm does not pass, we reset the password
        if (confirm != "Y" and confirm != "y" and confirm != "Yes" and confirm != "yes"):
            PW_Location = " "

    return PW_Location

# End Ask for PW Location =================================================
# =========================================================================
# Username Confirmation =======================================================

def Username_Confirmation(Username, confirm):

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

def ask_for_Username():

    Username = " "

    confirm = 'No' # confirm is created here, also passed to confirm function.
    # ---------------------------------------------
    # confirm is pre set to not pass the while loop
    while (confirm != "Y" and confirm != "y" and confirm != "Yes" and confirm != "yes"):

        # We first check for length, will not get Local password back if length is not 6-30
        Username = str(raw_input("What is this Username ?   "))

        # password can be 6-30 but not be what the user wanted. confirm again.
        confirm = Username_Confirmation(Username, confirm)

        # If the confirm does not pass, we reset the password
        if (confirm != "Y" and confirm != "y" and confirm != "Yes" and confirm != "yes"):
            Username = " "

    return Username

# End Ask for PW Location =================================================
# =========================================================================
# =========================================================================
# Encrypt Main ============================================================

def encryption():

    # Bring in the user ID safety number
    Password_ID = Ask_For_PassWord_ID_Number()

    # ---------------------------------------------------------------------------
    # We Need a location for this password
    PW_Location = ask_for_PW_location()
    Location_Encrypt = []

    for x in range(len(PW_Location)):
        changer = PW_Location[x]
        changer = encrypt_the_password(changer, len(PW_Location))
        Location_Encrypt.extend(changer)  # Enter in to encryption locaiton.
        # --------------------------------------------------------------------
    #   Password[key * 3] = '\0'; line 62 in xcode? not working here.
    PW_Location = ''.join(Location_Encrypt)  #convert to a string

    # Now we have a password web Location as a string that is encrypted and ready to send.

    # ---------------------------------------------------------------------------
    # ---------------------------------------------------------------------------
    # Bring in initial user password to encrypt.
    Username = ask_for_Username()
    Username_Encrypt = []

    for x in range(len(Username)):
        changer = Username[x]
        changer = encrypt_the_password(changer, len(Username))
        Username_Encrypt.extend(changer)  # Enter in to encryption locaiton.
        # --------------------------------------------------------------------
    #   Password[key * 3] = '\0'; line 62 in xcode? not working here.
    Username = ''.join(Username_Encrypt)  #convert to a string

    # Now we have a Username as a string that is encrypted and ready to send.
    # ---------------------------------------------------------------------------
    # ---------------------------------------------------------------------------
    # This part is to Encrypt the Password
    User_Password = str(Ask_For_User_Password())
    # Set the key to the original password length.
    key = len(User_Password)

    # We have Encrypted as a global, declared it a list here
    Encrypted_Password = []

    # For the next loop we need Encrypted to be 3 times the length of the user password
    # We extend the Encrpyted 3 times the length with rnadom chars
    Encrypted_Password.extend(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '!'+'@'+'#'+'%'+'^'+'&'+'*'+','+'.'+'/'+'?'+';'+':'+'['+']'+'{'+'}'+'-'+'_') for i in range(key*3))

    for x in range(key):
        changer = User_Password[x]          # Grab the char
        changer = encrypt_the_password(changer, key)
        Encrypted_Password[x*3] = changer   # Enter in to encryption locaiton.
        # --------------------------------------------------------------------
    #   Password[key * 3] = '\0'; line 62 in xcode? not working here.
    Encrypted_Password = ''.join(Encrypted_Password) #convert to a string


    return (Password_ID, Encrypted_Password, key, Username, PW_Location)

# End Encrypt  ============================================================
# =========================================================================
# =========================================================================
# =========================================================================
# Read file line  =========================================================
def Read_File_Line():

    vault_file = [2,'h','er']

    f = open('Vault.txt')

    vault_file = f.readline()

    f_contents = []
    for x in range(len(vault_file)):
        f_contents.extend(vault_file[x])

    # This is the full line, encrypted, as a list.

    #Turn list into a string
    fullLine_str = ''.join(f_contents)

    # Sending the line we just read to the decrypt function.
    # This is just to get the key value from the first 2 digits.
    return f_contents

# End Read from file  =====================================================
# =========================================================================
# =========================================================================
# =========================================================================
# Decrypt the password Function ===========================================
def Decrypt_the_NumberID(changer, key, x):

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

def Use_Key_to_Decrypt_Num_ID(key, Encrypted_Password):

    Encrypted_List = []
    Number_ID = []
    # Turn string into a list.
    for x in range(len(Encrypted_Password)):
        Encrypted_List.extend(Encrypted_Password[x])

    # Run the length of the password but stop at the space
    # changer = changer + (9 * x + key // 5)  # multiply ascii value by the key/5
    for x in range(len(Encrypted_Password)):
        changer = Encrypted_List[x+2]
        changer = Decrypt_the_NumberID(changer, key, x)
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
# =========================================================================
# Decrypt the Password Function ===========================================

def Decrypt_The_Password(changer, key):

    changer = ord(changer)  # change to ascii value
    changer = changer - (5 + key // 5)  # Add to value based on password length
    changer = chr(changer)  # Change new value back to a char

    return changer

# Decrypt password ========================================================
# =========================================================================
# =========================================================================
# =========================================================================
# Decrypt password ========================================================
def now_decrypt_Password(key, numberID, password):
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
        changer = Decrypt_The_Password(changer, len(username))
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
        changer = Decrypt_The_Password(changer, len(location))
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
        changer = Decrypt_The_Password(changer, key)
        user_password.extend(changer)

    user_password_STRING = ''.join(user_password)


    return (key, userID_STRING, user_password_STRING, username, location )


# End Decrypt password ====================================================
# =========================================================================
# =========================================================================
# =========================================================================
# Just decrpyted password, now have a space then Username
def decrypt_Username():
    print "fillerinewiwn"
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# Just decrpyted username, now have a space then Location

# =========================================================================
# =========================================================================
# =========================================================================
# Convert_2Digit Front_Key ================================================

def Decrypt_2Digit_Front_Key(changer):

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
# =========================================================================
# Convert_Password_Number =================================================
def Convert_Password_Number(lines):

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
        changer = lines[x]   # Switch first char to changer
        changer = Decrypt_2Digit_Front_Key(changer)
        lines[x] = changer   # set char back into Encrpted it is a number but not right yet


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
# =========================================================================
# =========================================================================
def filler_lines(filler_key):


    filler_password = []
    filler_ID = []
    filler_username = []
    filler_location = []
    # -------------------

    filler_ID.extend(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '!'+'@'+'#'+'%'+'^'+'&'+'*'+','+'.'+'/'+'?'+';'+':'+'['+']'+'{'+'}'+'-'+'_')for x in range(8))
    filler_ID = ''.join(filler_ID)

    # -------------------

    filler_password.extend(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '!'+'@'+'#'+'%'+'^'+'&'+'*'+','+'.'+'/'+'?'+';'+':'+'['+']'+'{'+'}'+'-'+'_') for i in range(random.randrange(10,128,2)))
    filler_password = ''.join(filler_password)

    # -------------------

    filler_username.extend(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '!'+'@'+'#'+'%'+'^'+'&'+'*'+','+'.'+'/'+'?'+';'+':'+'['+']'+'{'+'}'+'-'+'_') for i in range(10))
    filler_username = ''.join(filler_username)

    # -------------------

    filler_location.extend(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '!'+'@'+'#'+'%'+'^'+'&'+'*'+','+'.'+'/'+'?'+';'+':'+'['+']'+'{'+'}'+'-'+'_') for i in range(10))
    filler_location = ''.join(filler_location)




    Write_to_File(filler_ID, filler_password, filler_key, filler_username, filler_location)

# =========================================================================
# =========================================================================
# =========================================================================
def de_100():


    Full_Encrypted_List = []

    with open("Vault.txt") as fp:
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


    return Full_Encrypted_List

# End Full_Encrypted_List =================================================
# =========================================================================
# =========================================================================
# Final Encrypt
def encrypt_in_Main():
    # Write to file, uses the returned Encryption string.
    glo_UID_Str, glo_U_P_Str, glo_2Dkey_Int, glo_Username_Str, glo_location_Str = encryption()
    Write_to_File(glo_UID_Str, glo_U_P_Str, glo_2Dkey_Int, glo_Username_Str, glo_location_Str)

    spare_key = 00
    for x in range(99):
        filler_lines(spare_key)
        while (spare_key < 100):
            spare_key = spare_key + 1 * 3
            spare_key = spare_key * 3
        if (spare_key > 100):
            spare_key = spare_key - 99

# End Encrypt in Main Func=================================================
# =========================================================================
# =========================================================================
# Decrypt in main Func ====================================================

def decrypt_in_Main():
    password_List = de_100()

    for x in range(len(password_List)):
        f_contents = []

        transfer = password_List[x]
        for i in range(len(password_List[x])):
            f_contents.extend(transfer[i])

        key, encrypted_send = Convert_Password_Number(f_contents)
        key, Number_ID, Encrypted_List = Use_Key_to_Decrypt_Num_ID(key, encrypted_send)
        glo_2Dkey_Int, glo_UID_Str, glo_U_P_Str, glo_Username_Str, glo_location_Str = now_decrypt_Password(key, Number_ID,
                                                                                          Encrypted_List)

        final_list.append(glo_UID_Str)
        final_list.append(glo_location_Str)
        final_list.append(glo_Username_Str)
        final_list.append(glo_U_P_Str)

    print "--------------------------------------"
    for x in range(len(final_list)):
        print x+1,  '[ User ID# ]\t' + final_list[4*x]
        print x+1,  '[ Location ]\t' + final_list[4*x+1]
        print x+1,  '[ Username ]\t' + final_list[4*x+2]
        print x+1,  '[ Password ]\t' + final_list[4*x+3]
        print "--------------------------------------"

        if (x == (len(final_list)/4 - 1)):
            break

# =========================================================================
# =========================================================================
# below is just for display as we work out the program
if __name__ == '__main__':

    final_list = []

    userChoice = 0
    while (userChoice != 3):
        userChoice = int(Menu())

        if (userChoice == 1):
            encrypt_in_Main()

        elif (userChoice == 2):
            decrypt_in_Main()



