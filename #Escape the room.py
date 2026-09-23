 #Escape the room
import time

passcode = "1581"
door_locked = True
player_has_passcode = False

#Dictionary for rooms.
rooms = {

    "room 1": {
            "computer with a document open": "Tuesday 1st, nothing happened.",
            "open file": "New idea for synthetics pending...",
            "sticky note": "Remember to bring keycard!"
        },
    "room 2": {
        "whiteboard": "We need 5 new ideas to make the synthetics look less unsettling.",
        "note on desk": "New engineers are coming in soon...",
        "document": "Tim, could please start organising a new crew? The company are desperate to send another ship out soon."
    },
    "room 3": {
        "stray notes": "Reminder: Send an engineer into the ventilation system to fix the AC.",
        "opened letter": "Reminder: Henry, I'm still waiting on my invoice. Don't mess me around, have it to me by the 8th.",
        "note pinned to wall": "Sort out invoices before January 1st."
    }
}

#-------------------------------------------------------------------------------------
#Game start

print("===========Welcome!==========")
time.sleep(3)
print("You must search the room for four whole numbers hidden amongst notes documents.")
time.sleep(2)

#-------------------------------------------------------------------------------------
#Player begins searching

print("Where would you like to look first?")

time.sleep(2)
print("Room 1:" \
"\n computer with a document open," \
"\n open file," \
"\n sticky note.")

time.sleep(1)
print("Room 2:" \
"\n whiteboard," \
"\n note on desk," \
"\n document.")

time.sleep(1)
print("Room 3:" \
"\n stray notes," \
"\n opened letter," \
"\n note pinned to wall.")

#-------------------------------------------------------------------------------------

search = True
while search == True:
    room = input("What room would you like to search? ").lower()

    if room in rooms:

        item = input("What item would you like to read? ").lower()

        if item in rooms[room]:
            print(rooms[room][item])
        else:
            print("That item isn't in this room.")

        choice = input("Would you like to search again, enter the passcode or exit? ").lower()

        if choice == "no" or choice == "exit":
            search = False
        elif choice == "yes":
            print("You continue searching...")
        elif choice == "passcode":
            attempt = input("Enter passcode: ")

            if attempt == passcode:
                print("Correct, unlocking door...")
                search = False
                player_has_passcode = True

            else:
                print("Passcode incorrect, try again.")

    else:
        print("That room doesn't exist.")

if player_has_passcode == True:
    print("You escaped!")