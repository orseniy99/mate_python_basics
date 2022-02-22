def parity_checker() -> None:
    # write your code here
    number = input("What number do you want to check?")
    if int(number) % 2 == 0:
        print("Even")
    else:
        print("Odd")
