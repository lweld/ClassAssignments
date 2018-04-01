#This program takes requests from Tim Hortons customers using Linked Lists.

import urllib.request

'''
This function reads each Tim Hortons order.
'''
def readHtml(counter):
    response = urllib.request.urlopen("http://research.cs.queensu.ca/home/cords2/timOrders.txt")
    i = -1
    # reads the request after the request recently processed
    while i < counter:
        html = response.readline()
        i += 1
    data = html.decode('utf-8').split()
    return data

'''
This function takes the order returned from readHtml and converts
it to a list that's easily used throughout the program.
'''
def htmlParser (data):
    # order id is always stored at index position 1
    orderID = int(data[1])
    # price of the order is always stored at last position
    price = float(data[-1])
    # deleting everything in the list other than the food ordered
    del data[0]
    del data[0]
    del data[-1]
    newList = []
    # The list contains only the food order. Loop through each element, remove '%',
    # join the elements together and store it as a single string in a new variable.
    for i in data:
        if "%" in i:
            cleanStr = i.replace("%","")
            newList.append(cleanStr)
        else:
            newList.append(i)
    food = " ".join(newList)
    finalList = [orderID, food, price]
    return finalList

'''
This function adds a new order to the end of the list.
'''
def addToEnd(myList, order):
    ptr = myList
    # creates the first node in the list if the list is empty
    if ptr == None:
        node = {}
        node['id'] = order[0]
        node['food'] = order[1]
        node['price'] = order[2]
        node['next'] = myList
        print("Adding order", order[0], "to the queue")
        return node
    else:
        while ptr['next'] != None:
            ptr = ptr['next']
        newNode = {}
        newNode['id'] = order[0]
        newNode['food'] = order[1]
        newNode['price'] = order[2]
        newNode['next'] = None
        # the new node is now the last node in the list
        ptr['next'] = newNode
        print("Adding order", order[0], "to the queue")
        return myList

'''
This function modifies an order.
'''
def updateOrder(myList, order):
    ptr = myList
    if ptr == None:
        print("Cannot modify order.")
        return myList
    # checks if the id of each node is equal to the id of the order to be modified
    while ptr['id'] != order[0]:
        ptr = ptr['next']
        if ptr == None:
            print("Cannot modify order")
            return myList
    ptr['food'] = order[1]
    # the order is now fully modified
    ptr['price'] = order[2]
    return myList

'''
This function cancels an order.
'''
def cancelOrder(myList, data):
    ptr = myList
    orderID = int(data[1])
    # Catches the case where the linked list is a single node with an id equal to desired
    # order id to cancel. If this wasn't in place the while loop would return an error.
    if ptr['id'] == orderID:
        ptr = ptr['next']
        return ptr
    # Catches if the linked list has no nodes or one node that isn't equal to desired
    # order id to cancel
    elif ptr == None or ptr['next'] == None:
        print("Unable to cancel this job -- it has already been processed.")
        return myList
    while ptr['next']['id'] != orderID:
        ptr = ptr['next']
    # skips over the node we want to cancel
    ptr['next'] = ptr['next']['next']
    return myList

'''
This function completes the next order in the queue.
'''
def deleteHead(myList):
    ptr = myList
    if ptr == None:
        return ptr
    print("Completed order", ptr['id'])
    # as long as the list isn't empty, always set the current head to the next node
    ptr = ptr['next']
    return ptr

'''
This function adds up the number of orders in the queue and their total value.
'''
def queue(myList):
    ptr = myList
    counter = 0
    totalOrderValue = float(0.0)
    while ptr != None:
        # total number of orders
        counter += 1
        # total value of orders
        totalOrderValue += ptr['price']
        ptr = ptr['next']
    print("There are", counter, "orders in the queue with a total value of $", totalOrderValue)

'''
This function executes the program.
'''
def main():
    myList = None
    counter = 0
    data = readHtml(counter)
    # continues reading new orders as long as there are orders to read
    while data != []:
        if data[0] == 'submit':
            parsedOrder = htmlParser(data)
            myList = addToEnd(myList, parsedOrder)
        elif data[0]=='modify':
            parsedOrder = htmlParser(data)
            myList = updateOrder(myList, parsedOrder)
        elif data[0]=='cancel':
            myList = cancelOrder(myList, data)
        elif data[0]=='complete':
            myList = deleteHead(myList)
        elif data[0]=='queue':
            queue(myList)
        # counts the number of orders that have been read to allow the readline()
        # method to read the appropriate order
        counter += 1
        data = readHtml(counter)
main()
