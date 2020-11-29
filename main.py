from csv_summary import Summary

if __name__ == '__main__':
    s1 = Summary('Data-Samples/carsData.csv', 'Data-Samples/carFeatures.json')
    # print("specs: ", s1.getSpec())
    # s1.getGroups()
    # print(s1['Ford']['Color']) #- test getitem of class Group
    groups = s1.getGroups()
    for group in groups:
        print(group)
    # print(s1['Ford'])
    i = iter(iter(s1))
    print(type(i))
    # ii = iter(s1['110'])
    # groupTest = s1['120']
    ii = iter(s1['Ford'])
    groupTest = s1['Ford']
    print(groupTest[-1])
    print(next(ii))
    print(next(ii))

    s1.saveSummary('output_summary.csv')
    print(s1)
