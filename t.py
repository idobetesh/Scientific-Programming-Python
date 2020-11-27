def mode(List): 
    counter = 0
    num = List[0] 
      
    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency > counter): 
            counter = curr_frequency 
            num = i 
    return num 
  
dic = {"d":2, "e": 6}
print(list(dic.values()))




lst = [112,333,444]  
print(lst[-4])
List = ['red', 'red', 'blue', 'green', 'green', 'green'] 
print(mode(List))
print(mode(lst))
