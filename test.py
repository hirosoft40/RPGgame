while True:
    try:
        item = int(input("What would you like to {res}}?: "))

    except ValueError:
        print ("Invalid input. Please choose numbers from above list.") 
    except:
        if item not in items:
            print ("Please choose items from above list.")
    else:
        break