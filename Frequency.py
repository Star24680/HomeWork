TestDictionary={'Rohma':26,'Hadia':27,'Sakina':29,'Gul':28,'fizza':29}
print("OriginalDictionary: "+str(TestDictionary))
K=29
Res=0
for key in TestDictionary:
    if TestDictionary[key]==K:
       Res=Res+1
print("Frequency of Highest Marks is: "+str(Res))

#Miss the hw said the same thing we did in class so i did the samething just with different marks of tests