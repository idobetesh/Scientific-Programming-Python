from csv_summary_update import Summary

if __name__ == '__main__':
    s1 = Summary('Data-Samples/moviesData.csv', 'Data-Samples/movieFeatures.json')
    # print("specs: ", s1.getSpec())
    # s1.getGroups()
    #print(s1['Ford']['Color']) #- test getitem of class Group
    groups = s1.getGroups()
    for group in groups:
        print(group)
    #print(s1['Ford'])
    i = iter(iter(s1))
    print(type(i))
    ii = iter(s1['Canada'])
    groupTest = s1['Brazil']
    print(groupTest[-1])
    print(next(ii))
    print(next(ii)) 

    s1.saveSummary("output_summary.csv", ';')
    print(s1)

        