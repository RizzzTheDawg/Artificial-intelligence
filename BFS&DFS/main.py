class node:
    def __init__(self, data):
        self.data = data
        self.next = None



class graph:
    def __init__(self):
        self.head = None
        self.lst = []
        self.colour = {}

    def main(self):
        print("                Welcome to the graph program!")
        print("Here you can create a graph and perform various operations on it.")
        
        ver = int(input("Enter the number of vertices in the graph: "))
        print("Example of input: 1-2,5,10. (where 1 is the vertex and 2,5,10 are its linked vertices)")
        print("If the vertex has no linked vertices, you can just enter the vertex number followed by a hyphen (e.g., 3-.)")
        while ver > 0:
            allowed = "12345678980-,."
            status = False
            tempData = ""
            data = input("Enter the data for vertex including its linked vertices: ")
            length = len(data)
            count1 = 0
            count2 = 0
            for z in range (length):
                if data[z] == '-':
                    count1 += 1
                elif data[z] == '.':
                    count2 += 1
                if data[z] not in allowed:
                    print("Invalid input. Please enter the data again.")
                    status = True
                    break
                elif data[z] == '-' and z == 0:
                    print("Invalid input. Please enter the data again.")
                    status = True
                    break
                elif data[z] ==  ',' and data[z+1]  == ',':
                    print("Invalid input. Please enter the data again.2")
                    status = True
                    break
                elif data[z] ==  '.' and z != length-1:
                    print("Invalid input. Please enter the data again.")
                    status = True
                    break
            if (count1 > 1 or count2 > 1 or count1 ==0  or count2 == 0) and status == False:
                print("Invalid input. Please enter the data again.1")
                status = True

            if status:
                continue
            else:
                ver -= 1
                tempData = ""
                self.head = None
                for y in data:
                    if y == '-' and self.head == None:
                        self.colour[int(tempData)] = "white"
                        self.head = node(int(tempData))
                        self.lst.append(self.head)
                        tempData = ""
                        continue
                    elif y == ',':
                        temp = self.head
                        while temp.next != None:
                            temp = temp.next
                        temp.next = node(int(tempData))
                        tempData = ""
                        continue
                    elif y == ".":
                        if tempData != "":
                            temp = self.head
                            while temp.next != None:
                                temp = temp.next
                            temp.next = node(int(tempData))
                        continue
                    tempData += y

        print("You can now perform operations on the graph.")
        print("0: Exit")
        print("1: Display the graph")
        print("2: BFS")
        print("3: DFS")
        userInput = int(input("Enter the operation you want to perform: "))
        while userInput != 0:
            if userInput == 1:
                self.display()
                userInput = int(input("Enter the operation you want to perform: "))
            elif userInput == 2:
                for v in self.colour:
                    self.colour[v] = "white"
                self.BFS()
                userInput = int(input("Enter the operation you want to perform: "))
            elif userInput == 3:
                for v in self.colour:
                    self.colour[v] = "white"
                for head in self.lst:
                    self.DFS(head)
                print()
                userInput = int(input("Enter the operation you want to perform: "))
        print("Thank you for using the graph program!")

    
    def display(self):
        for i in self.lst:
            temp=i
            while temp != None:
                if temp.next !=None:
                    print(temp.data, end=" -> ")
                else:
                    print(temp.data)
                temp = temp.next

    def BFS(self):
        queue = []
        for node in self.lst:
            tempNode = node
            if self.colour[tempNode.data] == "grey" or self.colour[tempNode.data] == "black":
                continue
            if self.colour[tempNode.data] == "white":
                self.colour[tempNode.data] = "grey"
                queue.append(tempNode)
                while tempNode.next != None:
                    tempNode = tempNode.next
                    if self.colour[tempNode.data] == "white":
                        self.colour[tempNode.data] = "grey"
                        queue.append(tempNode)
                final=queue.pop(0)
                final.colour="black"
                print(final.data, end=" ")
                while len(queue) > 0:
                    final=queue.pop(0)
                    final.colour="black"
                    print(final.data, end=" ")
                    tempNode = final
                    while tempNode.next != None:
                        tempNode = tempNode.next
                        if self.colour[tempNode.data] == "white":
                            self.colour[tempNode.data] = "grey"
                            queue.append(tempNode)
        print()
    
    def DFS(self, start):
        if self.colour[start.data] == "white":
            self.colour[start.data] = "grey"
            print(start.data, end=" ")
            tempnode = start.next
            while tempnode != None:
                if self.colour[tempnode.data] == "white":
                    self.DFS(tempnode)
                tempnode = tempnode.next
            self.colour[start.data] = "black"

    



g = graph()
g.main()