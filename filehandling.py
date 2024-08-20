try :
    f = open(r"C:\Users\Pccoe\Downloads\sohan.txt","r") 
    cont = f.read()
    num = cont.split()
    print("content of file :",cont) 
    print("number of words : ",len(num))
    
except:
    print("file not found")
