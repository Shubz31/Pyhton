def display_menu():
    print("\n 1. Display the Dictionary")
    print(" 2. Print a specific Element")
    print(" 3. OverWritten Dictionary")
    print(" 4. Print Keys")
    print(" 5. Print Values")
    print(" 6. Print Items")
    print(" 7. Pop(delete) Element")
    print(" 8. Pop Item")
    print(" 9. Clear Dictionary")
    print(" 10. Exit \n")
    
def main():
    dictName = {1: 'Java', 2: 'Web Development', 3: 'Pyhton'}
    while(True):
        display_menu()
        choice = int(input("Enter your Choice: "))
        
        if choice == 1:
            print(dictName)
            
        elif choice == 2:
            element = int(input("Enter element you want to display: "))
            print(dictName[element])
            
        elif choice == 3:
            dictName = {'First' : 'Shubham', 'Second' : 'Sushant', 'Third' : 'Aditya'}
            print(dictName)
            
        elif choice == 4:
            print(dictName.keys())
                
        elif choice == 5:
            print(dictName.values())
            
        elif choice == 6:
            print(dictName.items())
        
        elif choice == 7:
            popedvalue = dictName.pop('Third')
            print('Value:', popedvalue)
            print('Dictionary:', dictName)
            
        elif choice == 8:
            poped_item = dictName.popitem()
            print("Key, Values: ", poped_item)
            print("Dictionary: ", dictName)
            
        elif choice == 9:
            dictName.clear()
            print(dictName)
        
        elif choice == 10:
            exit()
            break
            
        else:
            print("Enter valid input")
        
if __name__ == "__main__":
    main()       