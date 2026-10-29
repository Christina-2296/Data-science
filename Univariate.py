class Univariate:
    def quanQual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            #print(columnName)
            if(dataset[columnName].dtype=="O"):
               #print("qual")
               qual.append(columnName)
            else:
               #print("quan")
               quan.append(columnName)
        return quan,qual
        
    def Univariate(dataset,quan):
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","Q4:100%","IQR","1.5rule","Lesser","Greater","min","max"],columns=quan)
        for columnName in quan:
            descriptive[columnName]["Mean"]=dataset[columnName].mean()
            descriptive[columnName]["Median"]=dataset[columnName].median()
            descriptive[columnName]["Mode"]=dataset[columnName].mode()[0]
            #"We use describe() to automatically calculate and display important statistical information about a dataset in a single table."
            descriptive[columnName]["Q1:25%"]=dataset.describe()[columnName]["25%"]
            descriptive[columnName]["Q2:50%"]=dataset.describe()[columnName]["50%"]
            descriptive[columnName]["Q3:75%"]=dataset.describe()[columnName]["75%"]
            descriptive[columnName]["Q4:100%"]=dataset.describe()[columnName]["max"]
            descriptive[columnName]["IQR"]=descriptive[columnName]["Q3:75%"]- descriptive[columnName]["Q1:25%"]
            descriptive[columnName]["1.5rule"]=1.5*descriptive[columnName]["IQR"]
            descriptive[columnName]["Lesser"]=descriptive[columnName]["Q1:25%"]-descriptive[columnName]["1.5rule"]
            descriptive[columnName]["Greater"]=descriptive[columnName]["Q3:75%"]+descriptive[columnName]["1.5rule"]
            descriptive[columnName]["min"]=dataset[columnName].min()
            descriptive[columnName]["max"]=dataset[columnName].max()  
            return descriptive

    def freqTable(columnName,dataset):
       freqTable=pd.DataFrame(columns=["Unique_Values","Frequency","Relative_Frequency","Cumsum"]) 
       freqTable["Unique_Values"]=dataset[columnName].value_counts().index
       freqTable["Frequency"]=dataset[columnName].value_counts().index
       freqTable["Relative_Frequency"]=freqTable["Frequency"]/103
       freqTable["Cumsum"]=freqTable["Relative_Frequency"].cumsum()    
       return freqTable   
        
    def check():
        Lesser=[]
        Greater=[]
        for columnName in quan:
            if(descriptive[columnName]["min"]<descriptive[columnName]["Lesser"]):
                Lesser.append(columnName);
            if(descriptive[columnName]["max"]>descriptive[columnName]["Greater"]):
                Greater.append(columnName);
        return Lesser,Greater 

 def replace():
    for columnName in Lesser:
        dataset[columnName][dataset[columnName]<descriptive[columnName]["Lesser"]]=descriptive[columnName]["Lesser"]
    for columnName in Greater:
        dataset[columnName][dataset[columnName]>descriptive[columnName]["Greater"]]=descriptive[columnName]["Greater"]
    return Lesser,Greater

        