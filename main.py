from csv_summary import Summary

if __name__ == '__main__':

    # ----------------------------------------Cars--------------------------------------- #
    carsSummary = Summary('Data-Samples/carsData.csv',
                          'Data-Samples/carFeatures.json')
    print("specs: ", carsSummary.getSpec())
    print(
        f"carsSummary['Nissan']['Color'].__getitem__:{carsSummary['Nissan']['Color']}")

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
    # animalSummary = Summary('Data-Samples/animalData.csv', 'Data-Samples/animalFeatures.json')
    # print("specs: ", animalSummary.getSpec())
    # print(f"animalSummary['Turtle']['country'].__getitem__:{animalSummary['Turtle']['country']}")

    # groups = animalSummary.getGroups()
    # for group in groups:
    #     print(group)

    # i = iter(iter(animalSummary))
    # print(type(i))

    # groupTest = animalSummary['Alligator']
    # print(f"by index: {groupTest[0]}")

    # ii = iter(animalSummary['Alligator'])
    # print(next(ii))
    # print(next(ii))

    # animalSummary.saveSummary('output_summary.csv')
    # print(animalSummary)

    # --------------------------------------Movies--------------------------------------- #
    # movieSummary = Summary('Data-Samples/moviesData.csv', 'Data-Samples/movieFeatures.json')
    # print("specs: ", movieSummary.getSpec())
    # print(f"movieSummary[120]['country'].__getitem__:{movieSummary['120']['Country']}")

    # groups = movieSummary.getGroups()
    # for group in groups:
    #     print(group)

    # i = iter(iter(movieSummary))
    # print(type(i))

    # groupTest = movieSummary['80']
    # print(f"by index: {groupTest[0]}")

    # ii = iter(movieSummary['110'])
    # print(next(ii))
    # print(next(ii))

    # movieSummary.saveSummary('output_summary.csv')
    # print(movieSummary)