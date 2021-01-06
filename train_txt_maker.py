text_file = open(r"C:\Users\Arflok\Desktop\Datasets\data\train.txt", "w")

strings = ["/content/drive/MyDrive/Deep_learning_projeleri/yolov4_rcplane/dataset/",".jpg"]

for i in range(281):
    text_file.write(strings[0]+str(i)+strings[1]+"\n")
    
text_file.close()