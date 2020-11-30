from csv_summary import Summary

if __name__ == '__main__':

    # ----------------------------------------Cars--------------------------------------- #
    carsSummary = Summary('Data-Samples/carsData.csv', 'Data-Samples/carFeatures.json')
    print("specs: ", carsSummary.getSpec())
    print(f"carsSummary['Nissan']['Color'].__getitem__:{carsSummary['Nissan']['Color']}") 

    groups = carsSummary.getGroups()
    for group in groups:
        print(group)
        
    i = iter(iter(carsSummary))
    print(type(i))

    groupTest = carsSummary['Ford']
    print(f"by index: {groupTest[-2]}")
    
    ii = iter(carsSummary['Ford'])
    print(next(ii))
    print(next(ii))

    carsSummary.saveSummary('output_summary.csv')
    print(carsSummary)


    # --------------------------------------Animals-------------------------------------- #

    # ii = iter(carsSummary['110'])
    # groupTest = carsSummary['120']


    # --------------------------------------Movies--------------------------------------- #