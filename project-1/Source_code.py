import os
import pickle
import sys
def show():
    with open('billing.pickle','rb') as svitem:
        try:
            dict = pickle.load(svitem)
            while not dict == 0:
                print(dict)
                dict = pickle.load(svitem)
        except EOFError:
            pass
def bill():
    svitem = open('billing.pickle','rb')
    price = 0
    thatprice = 0
    code = 'nothing'
    sum = 0
    quantity = 0
    choice ='y'
    svditem = open('bill.txt','w')
    while choice == 'y':
        print('enter item code','rb')
        code = input()
        try:
            dict = pickle.load(svitem)
            while not dict == 0:
                if dict['code'] == code:
                    price = dict['price']
                    print('Enter quantity :',end = '')
                    quantity = input()
                    thatprice = int(price) * int(quantity)
                    sum += thatprice
                    svditem.write(' Code = ' + dict['code'] + ', Name =' + dict['name'] + ', Price = ' + price + ', Quantity : ' + str(quantity) + "\n")
                    break
                dict = pickle.load(svitem)
        except EOFError:
            print('no such item in our shop')
            pass
        print('want to enter more items ()y/n: ')
        choice = input()
    svditem.write('total = ' + str(sum)   )
    svditem.close()
    svitem.close()
    svditem = open('bill.txt','r')
    print(svditem.read())
    svditem.close()

def Addi():
    price = 0
    itemsleft = 0
    name = 'nothing'
    itemcode = 'nothing'
    ch = 'y'
    svitem = open('billing.pickle', 'ab')
    while ch == 'y':
        print('Enter item code :', end='')
        itemcode = input()
        print('Enter item name :', end='')
        name = input()
        print('Enter item prjce :', end='')
        price = input()
        dict = {'code': itemcode, 'name': name, 'price': price}
        pickle.dump(dict, svitem)
        print('Do you want to enter more items(y/n)')
        ch = input()
    svitem.close()

ch = 'y'
choice = 0
while ch == 'y':
    print("""                            WELCOME TO OUR BILLING SYSTEM
                                          1)Add items to list
                                          2)Display info of all items 
                                          3)Create bill
                                          4)Exit
                                    Enter your choice : """,end='')
    choice = input()
    if choice == '1':
        Addi()
    elif choice == '2':
        show()
    elif choice == '3':
        bill()
    elif choice == '4':
        sys.exit()
    else :
        print('wrong choice')
    print('do you want to continue :',end='')
    ch = input()
print("Thank you for using our program.")

