import csv
import json

class Group:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        # ford -> {Color(mode): Red, Kilometers(max): 55000}
        return f"{self.name} "

#----------------------------------------------------------------------------------------------#

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
        features = data['features']
        featuresList = []
        aggregateList = []


        # Creating a feature-aggrefate dict named - festureDict
        for feature in features:
            for i in feature:
                if feature[i]['type'] != 'textual':
                    featuresList.append(i)
                    aggregateList.append(feature[i]['aggregate'])
        self.featuresDict = dict(zip(featuresList, aggregateList))
        

        # Creating list of dicts from the CSV named - csvDataInList
        with open(csvFile) as csv_file:
            reader = csv.DictReader(csv_file)
            csvDataInList = []
            for i in reader:
                csvDataInList.append(i)

        # Creating set of the group names - groupNamesAsSet
        for i in csvDataInList:
            print(i)
            self.groupsNamesAsSet.add(i[groupBy])
        print(self.groupsNamesAsSet)

       
        # listOfGroupLists = [[]] * len(self.groupsNamesAsSet)

        # for i, name in enumerate(self.groupsNamesAsSet):
        #     for data in csvDataInList:
        #     listOfGroupLists[i].append(name)

        # print(listOfGroupLists)
        t = []
        for elm in csvDataInList:
            t.append(elm.get('Color'))

        print(t)
        
                    

    def getGroups(self):
        for group in self.groups:
            print(group)

    def getSpec(self):
        return self.featuresDict

    def saveSummary(self, filename, delimiter):
        """creats a csv file according to the Summry members using specific delimiter"""
        if delimiter == type(int) or delimiter == "":
            pass
        pass

    def __str__(self):
        return f"hi {self.csvFile}, {self.jsonFile}"


#----------------------------------------------------------------------------------------------#






#----------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    s1 = Summary('data samples.csv', 'specs.json')
    print("specs: ", s1.getSpec())
    s1.getGroups()