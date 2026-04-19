import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

mydb = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()    

def printstmt():
    results = mycursor.fetchall()
    
    header = f"{'ID':<10}{'Airline':<15}{'Booking ID':<15}{'First Name':<15}{'Last Name':<15}{'Phone':<15}{'Age':<8}{'From':<10}{'To':<10}{'Date':<12}{'Time':<10}{'Verification':<10}"
    separator = "-" * len(header)

    print(header)
    print(separator)

    if not results:
        print("No ticket found for the given detail")
        return

    for row in results:
        print(f"{str(row[0]):<10}{str(row[1]):<15}{str(row[2]):<15}{str(row[3]):<15}{str(row[4]):<15}{str(row[5]):<8}{str(row[6]):<10}{str(row[7]):<10}{str(row[8]):<15}{str(row[9]):<12}{str(row[10]):<10}{str(row[11]):<10}")

    if len(results) > 1:
        which = input("\nMore than one record found. Which ID do you want to verify: ")
        print(header)
        print(separator)
        for row in results:
            print(f"{str(row[0]):<10}{str(row[1]):<15}{str(row[2]):<15}{str(row[3]):<15}{str(row[4]):<15}{str(row[5]):<8}{str(row[6]):<10}{str(row[7]):<10}{str(row[8]):<15}{str(row[9]):<12}{str(row[10]):<10}{str(row[11]):<10}")
    else:
        which = results[0][0]
        print(f"\nProcessing ID: {which}")

    verify = input("Is the ticket Verified or not? (Yes/No): ").capitalize()
    
    if verify == "Yes":
        ver_status = "VERIFIED"
        query2 = "UPDATE ticket SET Verification = %s WHERE ID = %s;"
        mycursor.execute(query2, (ver_status, which))
        mydb.commit()
        print(f"Ticket {which} has been updated to VERIFIED.")
    else:
        print("Action cancelled. Ticket status not changed.")


def getDetailType():
    detail = input("Enter the type of detail you can provide to get the ticket(Name/Phone/ID): ").capitalize()
    print()
    match detail:
        case "Name":
            fname = input("Enter the first name: ")
            lname = input("Enter the last name: ")
            query = "SELECT * FROM ticket WHERE `First Name` = %s AND `Last Name` = %s"
            mycursor.execute(query, (fname, lname))
            print()
            printstmt()

        case "Phone":
            phone = (input("Enter phone number: "))
            query = "SELECT * FROM ticket WHERE `Phone No` = %s"
            mycursor.execute(query, (phone,))
            print()
            printstmt()

        case "ID":
            bid = input("Enter the Booking ID: ")
            query = "SELECT * FROM ticket WHERE BOOKINGID = %s"
            mycursor.execute(query, (bid,))
            print()
            printstmt()


getDetailType()
