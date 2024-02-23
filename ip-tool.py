# IP Tool

def main():
    ip = input("IP address: ")
    mask = input("Mask: ")
    
    ip = ip.split(".")
    for i in range(len(ip)):
        ip[i] = format(int(ip[i]), "08b")
        
    print('\n')
    
    mask = mask.split(".")
    for i in range(len(mask)):
        mask[i] = format(int(mask[i]), "08b")
        
    print("IP address: ", end="")
    for i in ip:
        print(i, end=".")
        
    print("\n      Mask: ", end="")
    for i in mask:
        print(i, end=".")
    
    exit()    
    
if __name__ == "__main__":
    main()