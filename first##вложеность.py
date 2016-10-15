while True:
    reply = input("text:")
    if reply == "stop":
        break
    elif not reply.isdigit():
        print("Fuck you!" * 8)
    else:
        num = int(reply)
        if num < 20:
            print("low")
        else:
            print(num ** 2)
print("Bye")
