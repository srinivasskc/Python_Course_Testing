

# Way 2 - Using Case : Unknown

tv = input("Enter Your TV Name: ")

match tv:
    case "LG":
        print("Your TV Name is LG")
    case "Sony":
        print("Your TV Name is Sony")
    case "Videocon":
        print("Your TV Name is Videocon")
    case "Onida":
        print("Your TV Name is Onida")
    case Unknown:
        print(f"Your TV name {Unknown} is not found in the match case list")



# Way 2 - Using Case : Wildcard
phone = input("Enter your Phone Name: ")

match phone:
    case "Samsung":
        print("Your Phone Name is Samsung")
    case "Redmi":
        print("Your Phone Name is Redmi")
    case "Vivo":
        print("Your Phone Name is Vivo")
    case "Nokia":
        print("Your Phone Name is Nokia")
    case _:
        print("The entered phone is not found in the list")
