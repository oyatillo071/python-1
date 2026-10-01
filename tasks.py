
userChoice=int(input("Enter your choice : "))

match userChoice:
    case 1:        
        myData={}
        def myFunction():
            myData["name"]=input("Enter your name: ")
            myData["age"]=int(input("Enter your age: "))
            myData["city"]=input("Enter your city: ")
            return myData
        myFunction()
        print(myData)
    case 2:
        raqamlar = [1, 2, 2, 3, 4, 4, 5, 1]
        uniq_number=  set(raqamlar)
        print(uniq_number)
    case 3:
        matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9] ]
        
        def copy_list(arg):
            result=[]
            for i in arg:
                col=[]
                for j in i:
                    col.append(j) 
                result.append(col)
            return result
        
        reverse_matrix=copy_list(matrix)
        
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                reverse_matrix[i][j]=matrix[j][i]
        for i in reverse_matrix:
            print(i, end="\n") 
            
            
        
        
