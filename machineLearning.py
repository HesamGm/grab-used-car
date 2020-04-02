import repository
from sklearn import tree
def guessPrice(company, model, mileage, buildYear):
    newData = [[mileage, buildYear]]
    result = repository.getByModel(company, model)
    if(len(result) < 10):
        print("collected data number is less than 10, try updating with more pages to get more reasonable result")
    x = []
    y = []
    for currentData in result:
        x.append([currentData[0],currentData[2]])
        y.append(currentData[1])
    clf = tree.DecisionTreeClassifier()
    machineGuess = clf.fit(x, y)
    answer = machineGuess.predict(newData)
    return answer[0]