import os

c=0
for i in os.listdir(r"C:\Users\Arflok\Desktop\Datasets\rc_plane"):
    a = i.split(".")
    if a[1] == "txt":
        print("t")
    else:
        old_path = "C:/Users/Arflok/Desktop/Datasets/rc_plane/"+str(c)+"."+a[1]
        new_path = "C:/Users/Arflok/Desktop/Datasets/rc_p/"+str(c)+".jpg"
        os.rename(old_path,new_path)
        c+=1
    print(a[1])
print(c)
#