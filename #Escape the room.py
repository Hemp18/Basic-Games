 #Escape the room
import time

passcode = "1581"
door_locked = True
player_has_passcode = False

#Dictionary for rooms.
rooms = {
    "level 1": {
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
        }},

    "level 2": {
        "lincoln's office": {
            "note from henry's wife": "2 more weeks!",
            "reminder": "Just reminding you of our little arrangement.",
            "voicenote from ted": "Hey, Lincoln, may need, uh... we may need more time in Bay 1, the patient isn't taking well to treatment. We still don't know what they have."
        },
        "george's office": {
            "voicemessage": "George, meet with me urgently. Meet me tomorrow, my office, 1PM.",
            "open terminal": "(Blank screen)",
            "personal reminder": "Remember to visit the marshall about a recent break-in."
        },
        "storage area": {
            "open box": "Empty.",
            "log book": "Henry: 4 prescription antidepressants.\n Lincoln: 2 prescription painkillers.",
            "open locker": "Remember to pick up a roses."
        }
    },
    "level 3": {
        "coffee area": {
            "book": "(Nothing of relevance)",
            "receipt": "1x Black Coffee \n £2.87"
        },
        "floor manager's office": {
            "open terminal": "Reminder for Tim: Keycard is in locker.",
            "file": "Remind workers to flush after themselves. Running low on tea bags and coffee, request a refill from Goods Office.",
            "locker": "Keycard."
        },
        "snack bar": {
            "empty tables": "A few paper bags are scattered around, nothing relevant here...",
            "notes pinned to wall": "Some advertisements for station services, seem pleasant.",
            "half open bag": "There's a half eaten sandwich inside, looks like ham and cheese."
        }
    },
    "level 4": {
            "toy shop": {
                "wooden toy aisle": "A few wooden ships, trains and blocks fill the aisle, but none seem to be what you're looking for.",
                "plastic toy aisle": "Building blocks and mischellaneous toys line the shelves. That blue square may do the job.",
                "construction toy aisle": "A few small spades, toy blowtorches and hammers are scattered around the shelves"
            },
            "tool shop": {
                "screws 'n' nails aisle": "Neat rows of nails and screws line the shelves, but nothing of use seems to be in sight.",
                "general tools aisle": "Hammers, screwdrivers, maintanence tools and more are dotted around, yet there seems to be nothing useful here.",
                "specialised tool aisle (permit required)": "Blowtorches, grade 3 door locks and other specialised tools are lined up behind protective, locked casings, but there seems to be nothing useable here."
            },
            "general shop": {
                "snack aisle": "The snack aisle seems nearly empty, as half eaten and the stray empty packet lay discarded on the floor.",
                "fruit 'n' veg aisle": "This aisle smells, the fruit and veg seems to have gone off.",
                "liquid meal aisle": "The aisle seems almost completely empty, as only a few, mouldy packets remain."
            }
    },
    "level 5": {
            "bay 1a": {
                "notes on desk": "Patient 3 doesn't seem to be suffering from any side effects after coming into contact with a foreign organism. Further monitoring recommended.",
                "empty bed": "The bed is neatly laid, but leaves little in the way of info.",
                "patient chart": "Name: Frederick Schumacher. \n Age: 27 years old.\n Sex: Male. \n Final status: Fine, further monitoring recommended."
            },
            "bay 1b": {
                "open terminal": "Urgent Request to Dr Lincoln, \n We need more supplies desperately in the medical bays, as patients are suffering and will soon be unable to receive treatment. \n Please meet me soon, \n Amanda Roberts, Lead Bay Nurse.",
                "medication notes": "2x Aspirin, \n 3x Promethazine, \n 4x Melatonin, \n 1x Sertraline, \n 0x Lorazepam. \n We are in desperate need of supplies.",
                "messy bed": "The bed seems to have been left in a messy state, maybe they were in a rush?"
            },
            "bay 1c": {
                "open case file": "Patient requires painkillers, but we're running low and have to spread our resources thin. \n We need more painkillers. If this request is ignored, I will go higher. \n Sam Harley, Vice Lead Nurse.",
                "empty bed": "Neatly kept bed.",
                "locker": "Meeting overheads on the 9th."
            },
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