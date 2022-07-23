def try_me():
    choice = input('Enter 1 if you\'re a regression person \n Enter 2 if you\'re a classification person')
    if choice == '1':
        return "Ride that slope!"
    elif choice == '2':
        return "You like judging people?"
    else:
        return "WRONG DATA"
