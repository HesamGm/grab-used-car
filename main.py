import fetchData, repository, re, machineLearning

while(True):
    # TODO id is not uniqe & data fetch by car model
    statementParts = re.findall(r"\w+", input("type your command or 'help' to get guide\n>>> "))
    if(statementParts[0] == 'help'):
        print("""List of commands:
    
    help                                             get information
    exit                                             to terminate the program
    update pageNumber                                to update the data until the given number of pages[for certain car model]
    brands                                           to see all brands that exist
    models                                           to show the models by company name(brands)
    grab                                             to grab the whole data from a certain car model
    determine                                        an estimation of price by mileage and buildYear
    clean                                            it will clean all data that was collected, useful to clear old data and update again
                """)
    elif(statementParts[0] == "update"):
        pageNumber = int(statementParts[1])
        cars = fetchData.getData(pageNumber, 'all-brands', 'all-models')
        counter = 0
        for car in cars:
            registeration = repository.save(car)
            if(registeration == True):
                counter = counter + 1
        if(counter > 0):
            print("successfully updated...")
            print(f"{counter} added")
        else:
            print("nothing to do, already updated")
    elif(statementParts[0] == "brands"):
        brands = repository.getAllBrands()
        for brand in brands:
            print(f"\t{brand[0]}")
    elif(statementParts[0] == "models"):
        company = input("type the company name: ")
        for model in repository.getModelByBrand(company):
            print(f"\t{model[0]}")
    elif(statementParts[0] == "grab"):
        company = input("type company name: ")
        model = input("type model name: ")
        cars = repository.getByModel(company, model)
        for car in cars:
            print(f"\t{car}")
    elif(statementParts[0] == "determine"):
        company = input("type company name: ")
        model = input("type model name: ")
        mileage = input("type your mileage: ")
        buildYear = input("type your buidYear: ")
        price = machineLearning.guessPrice(company, model, mileage, buildYear)
        print(f"it costs {price}")
    elif(statementParts[0] == "clean"):
        repository.clean()
        print("all the data is removed, use update to collect again")
    elif(statementParts[0] == "exit"):
        break
    else:
        print("invalid command, type 'help' for information")