import csv
import json

class Group:
    def __init__(self, name, featuresAggregate, myFeatures):
        '''The Constructor will receive three arrguments:
        name(of the group), 
        featuresAggregate(Dict that holds {feature: aggragate,....},
        myFeatures(Dict that holds {feature: value,...}
        -> and generate a Group object'''
        self.name = name
        self.featuresAggregate = featuresAggregate
        self.myFeatures = myFeatures

    def __str__(self):
        '''Represents the grout by string in this format - ford - {Color(mode): Red, Kilometers(max): 55000}'''
        retString = ""
        retString += f"{self.name} - "
        for n, i in enumerate(self.featuresAggregate):
            retString += f"{i}({self.featuresAggregate[i]}): {self.myFeatures[i]}"
            if n != len(self.featuresAggregate) - 1:
                retString += ", "
        return retString 
    
    def __getitem__(self,key):
        ''' Will receive a key(either numerical(positive or negative) or textual(the group name), and returns the value at this index) '''
        for i, feature in enumerate(self.myFeatures):
            if key < 0:
                if key < len(self.myFeatures) * -1:
                    raise StopIteration
                key = key + len(self.myFeatures)
            if feature == key or i == key:
                if type(key) == int:
                    return self.myFeatures[feature]
                elif type(key) == str:
                    return self.myFeatures[i]
                else:
                    return None
    
    def __iter__(self):
        ''' Initialize the variable n to be -1(for the __next__ function to iterate) '''
        self.n = -1
        return self

    def __next__(self):
        ''' '''
        if self.n < len(self.myFeatures):
            self.n += 1
            feature = list(self.myFeatures.keys())
            tmpList = []
            tmpList.append(feature[self.n])
            tmpList.append(self.myFeatures[feature[self.n]])
            tmpTuple = tuple(tmpList)
            return tmpTuple
        else:
            raise StopIteration

# ---------------------------------------------------------------------------------------------- #

class Summary:
    def __init__(self, csvFile, jsonFile):
        """init with csvFile as the first parameter and jsonFile as the second"""
        if csvFile == '' or jsonFile == '':
            self.csvFile = ''
            self.jsonFile = ''
            return

        self.csvFile = csvFile
        self.jsonFile = jsonFile
        self.groupsNamesAsSet = set()
        self.groups = []

        with open(jsonFile) as json_file:
            data = json.load(json_file)

        groupBy = data['groupby']
        self.GroupBy = groupBy
        features = data['features']
        featuresList = []
        aggregateList = []
        featuresAndTypes = {}

        # Creating a feature-aggrefate dict named - festureDict && feature-type dict named - featuresAndTypes
        for feature in features:
            for i in feature:
                if feature[i]['type'] != 'textual':
                    featuresAndTypes[i] = feature[i]['type']
                    featuresList.append(i)
                    aggregateList.append(feature[i]['aggregate'])
        self.featuresDict = dict(zip(featuresList, aggregateList))


        # Creating list of dicts from the CSV named - csvDataInList
        with open(csvFile) as csv_file:
            reader = csv.DictReader(csv_file)
            csvDataInList = []
            for i in reader:
                csvDataInList.append(i)

        for row in csvDataInList:
            for key, value in row.items():
                if value == "":
                    if featuresAndTypes[key] == 'numerical':
                        row[key] = 0
                    if featuresAndTypes[key] == 'categorical':
                        row[key] = 'NA'
                

        # Creating set of the group names - groupNamesAsSet
        for i in csvDataInList:
            self.groupsNamesAsSet.add(i[groupBy])

        
        lengthOfFeatures = len(self.featuresDict)

        for name in self.groupsNamesAsSet:
            groupValues = {}
            for feature in self.featuresDict:
                logic = Logics(csvDataInList, feature, name, groupBy)
                if self.featuresDict[feature] == 'max':
                    returnVal = logic.maxFromList()
                    groupValues[feature] = returnVal

                if self.featuresDict[feature] == 'mode':
                    returnVal = logic.mode()
                    groupValues[feature] = returnVal
                
                if self.featuresDict[feature] == 'unique':
                    returnVal = logic.unique()
                    groupValues[feature] = returnVal

                if self.featuresDict[feature] == 'count':
                    returnVal = logic.counter()
                    groupValues[feature] = returnVal

                if self.featuresDict[feature] == 'union':
                    returnVal = logic.union()
                    groupValues[feature] = returnVal

                if self.featuresDict[feature] == 'min':
                    returnVal = logic.minFromList()
                    groupValues[feature] = returnVal
                
                if self.featuresDict[feature] == 'median':
                    returnVal = logic.median()
                    groupValues[feature] = returnVal

                if self.featuresDict[feature] == 'sum':
                    returnVal = logic.sumOfList()
                    groupValues[feature] = returnVal
                
                if self.featuresDict[feature] == 'mean':
                    returnVal = logic.mean()
                    groupValues[feature] = returnVal

                if len(groupValues) == lengthOfFeatures:
                    self.groups.append(Group(name, self.featuresDict, groupValues))

    def getGroups(self):
        for group in self.groups:
            print(group)

    def getSpec(self):
        return self.featuresDict

    def saveSummary(self, filename, inputDelimiter= ","):   
        """creats a csv file according to the Summry members using specific delimiter"""
        header = {self.GroupBy:'(groupby)'}
        for i in self.featuresDict:
            header[i] =  f"({self.featuresDict[i]})"

        print(f"HEADER: {header}") ############## delete! #################

        if type(inputDelimiter) == int:
            inputDelimiter = ',' 
        if inputDelimiter.isalnum() or inputDelimiter == '\"' or inputDelimiter == "\'":
            inputDelimiter = ','  

        fieldnames = []
        for i in header:
            fieldnames.append(f"{i} {header[i]}")
            
        with open(filename ,"w") as file:
            writer = csv.writer(file, fieldnames, delimiter = inputDelimiter)
            writer.writerow(fieldnames)
            for gro in self.groups:
                listOfFeaturesMF = []
                listOfFeaturesMF.append(gro.name)
                for i, featu in enumerate(gro.myFeatures):
                    listOfFeaturesMF.append(gro.myFeatures[featu])
                    if i == len(gro.myFeatures) - 1:
                        writer.writerow(listOfFeaturesMF)


    def __str__(self):
        retString = ""
        for i in self.groups:
            retString += f"{i.__str__()}\n"
        return retString

    def __getitem__(self,key):
        for i in self.groups:
            if i.name == key:
                return i

    def __iter__(self):
        self.n = -1
        return self

    def __next__(self):
        #print( len(self.groups))
        if self.n < len(self.groups):
            self.n += 1
            return self.groups[self.n]
        else:
            raise StopIteration

# ---------------------------------------------------------------------------------------------- #

class Logics:
    """ start with {Kilometers: max, Color: mode, Model: unique}  """
    def __init__(self, csvList, featureName, groupName, groupBy):
        self.csvList = csvList
        self.featureName = featureName
        self.groupName = groupName
        self.groupBy = groupBy
        # [{},{}], {'Color': 'mode', 'Kilometers': 'max', 'Model': 'unique'}, Ford, Brand

    def maxFromList(self):
        """ docstring """
        maxList = []
        for row in self.csvList:
            if row[self.groupBy] == self.groupName:
                maxList.append(int(row[self.featureName]))
                
        return max(maxList)

    def mode(self): 
        modeList = []
        for row in self.csvList:
            if row[self.groupBy] == self.groupName:
                modeList.append(row[self.featureName])
        counter = 0
        num = modeList[0]   
        modeList.sort()

        for i in modeList: 
            curr_frequency = modeList.count(i) 
            tieList = []
            if curr_frequency == counter:
                tieList.append(i)
                tieList.append(num)
            if curr_frequency > counter: 
                counter = curr_frequency 
                num = i
            if len(tieList) > 0:
                tieList.sort()
                return tieList[0] 
        return num

    def unique(self):
        """
        docstring
        """
        uniqueSet = set()
        for row in self.csvList:
            if row[self.groupBy] == self.groupName:
                uniqueSet.add(row[self.featureName])

        return len(uniqueSet) 

    def counter(self):
        """
        docstring
        """
        counter = 0
        for row in self.csvList:
            if row[self.groupBy] == self.groupName:
                counter += 1

        return counter

    def union(self):
        """
        docstring
        """
        uniqueSet = set()
        for row in self.csvList:
            if row[self.groupBy] == self.groupName:
                uniqueSet.add(row[self.featureName])

        string = ""
        for i, item in enumerate(uniqueSet):
            string += str(item)
            if i != len(uniqueSet)-1:
                string += ";"

        return string
        
    def minFromList(self):
        """
        docstring
        """
        minList = []
        for row in self.csvList:
            if row[self.groupBy] == self.groupName:
                minList.append(int(row[self.featureName]))
                
        return min(minList)    

    def median(self):
        """
        docstring
        """
        medianList = []
        for row in self.csvList:
            if row[self.groupBy] == self.groupName:
                medianList.append(int(row[self.featureName])) 
        
        medianList.sort()
        n = len(medianList)
        
        if n % 2 == 0:
            median1 = medianList[n//2] 
            median2 = medianList[n//2 - 1] 
            median = (median1 + median2)/2
        else: 
            median = medianList[n//2] 
        return median


    def sumOfList(self):
        """
        docstring
        """
        mySum = 0
        for row in self.csvList:
            if row[self.groupBy] == self.groupName:
                mySum += int(row[self.featureName])
     
        return mySum

    def mean(self):
        """
        docstring
        """
        counter = 0
        mySum = 0
        for row in self.csvList:
            if row[self.groupBy] == self.groupName:
                mySum += int(row[self.featureName])
                counter += 1

        return float(mySum / counter)

# ---------------------------------------------------------------------------------------------- #

if __name__ == '__main__':
    s1 = Summary('Animal.csv', 'AnimalFeatures.json')
    # print("specs: ", s1.getSpec())
    # s1.getGroups()
    #print(s1['Ford']['Color']) #- test getitem of class Group
    #print(s1['Ford'])
    i = iter(iter(s1))
    print(type(i))
    ii = iter(s1['Dog'])
    groupTest = s1['Dog']
    print(groupTest[-3])
    print(next(ii))
    print(next(ii))
    print(next(ii))

    s1.saveSummary("data.csv", 1)
    print(s1)

        