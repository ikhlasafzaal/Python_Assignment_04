def add_three_copies(list,data):
     
     # yeh loop bar bar chalega
    for i in range(3):
        list.append(data) # har bar message ko list main add krega

def main():
    message = input("Enter the message to copy") # user say message poche ga

    list = [] # yeh empty list hai

    print("Before list",list)
    add_three_copies(list,message)
    print("After list",list)

if __name__ == '__main__':
     main()
