class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class graph:
    def __init__(self):
        self.head = None
        self.lst = []
        self.weight = {"A": 5, "B": 6, "C": 4, "D": 3, "E": 3, "F": 1, "G" : 0}
        self.directions = {"A": [1,4], "B": [2, 3], "C": [5], "D": [2,4], "E": [3], "F": [1]}
        self.leaf=[]

    def main(self):
        print("                Welcome to the graph program!")
        print("Here you can create a graph and perform various operations on it.")
        
        ver = int(input("Enter the number of vertices in the graph: "))
        print("Example of input: 1-2,5,10. (where 1 is the vertex and 2,5,10 are its linked vertices)")
        print("If the vertex has no linked vertices, you can just enter the vertex number followed by a hyphen (e.g., 3-.)")
        while ver > 0:
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
                
                if data[z] == '-' and z == 0:
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
                        self.head = node(tempData)
                        self.lst.append(self.head)
                        tempData = ""
                        continue
                    elif y == ',':
                        temp = self.head
                        while temp.next != None:
                            temp = temp.next
                        temp.next = node(tempData)
                        tempData = ""
                        continue
                    elif y == ".":
                        if tempData != "":
                            temp = self.head
                            while temp.next != None:
                                temp = temp.next
                            temp.next = node(tempData)
                        continue
                    tempData += y

        print("You can now perform operations on the graph.")
        print("0: Exit")
        print("1: Display the graph")
        print("2: A Star Search")
        userInput = int(input("Enter the operation you want to perform: "))
        while userInput != 0:
            if userInput == 1:
                self.display()
                userInput = int(input("Enter the operation you want to perform: "))
            elif userInput == 2:
                value=0
                self.AStar(self.lst[0], self.lst[-1], 0)
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
    
    def AStar(self,start,goal,pathValue):
        tempNode = start
        goal=goal
        finalPath=pathValue
        if tempNode.data == goal.data:
            print(tempNode.data,end=" ")
            print(finalPath)
            print()
            return
        else:
            templst=[]
            index=0
            finalSum=0
            tempNode = tempNode.next
            while tempNode != None:
                finalPath=pathValue
                templst.append(tempNode)
                finalPath+=self.directions[str(start.data)][index]
                templst.append(finalPath)
                finalSum=finalPath+self.weight[str(tempNode.data)]
                templst.append(finalSum)
                index+=1
                tempNode = tempNode.next
                self.leaf.append(templst)
                templst=[]
            
            removeIndx=0
            keep=self.leaf[0]
            for i in range(len(self.leaf)):
                if self.leaf[i][2] > keep[2] or self.leaf[i][2] == keep[2]:
                    continue
                else:
                    keep=self.leaf[i]
                    removeIndx=i
            self.leaf.pop(removeIndx)
            for y in range(len(self.lst)):
                if self.lst[y].data == keep[0].data:
                    break
            
            self.AStar(self.lst[y],goal,keep[1])
             
            

                
                

g=graph()
g.main()