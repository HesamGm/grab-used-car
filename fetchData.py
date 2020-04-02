import requests, repository, re
from bs4 import BeautifulSoup
class Car:
    number = 0
    def __init__(self, companyName, model, mileage, price, buildYear):
        Car.number = Car.number + 1
        self.id = Car.number
        self.companyName = companyName
        self.model = model
        self.mileage = mileage
        self.price = price
        self.buildYear = buildYear

def getData(pageNumber, brand, model):
    url = f'https://bama.ir/car/{brand}/{model}/all-trims?page='
    data = []
    for i in range(1, pageNumber + 1):
        page = requests.get(url + str(i))
        # *********************            TODO a better progressing show
        print(f"page number {i} is progressing\n {pageNumber-i} more pages are remained ...")
        soup = BeautifulSoup(page.text, 'html.parser')
        cars = soup.find_all('div', {'class' : 'listdata'})
        for car in cars:
            cartitleTag = car.find('a', {'class' : 'cartitle-mobile'})
            cartitles = cartitleTag.select('h2')[0].contents[0].split('،')
            companyName = cartitles[0].strip()
            model = cartitles[1].strip()
            mileage = car.find('p', {'class' : 'price'}).contents[0]
            mileage = mileage.replace(',','')
            mileage = re.findall(r'\d+', mileage)
            tmpPrice = car.find('span', {'itemprop' : 'price'})
            buildYear = car.find('span', {'itemprop' : 'releaseDate'}).contents[0]
            buildYear = re.findall(r'\d+', buildYear)
            if(len(mileage) >= 1 and len(buildYear) >= 1 and tmpPrice != None and tmpPrice != 0):
                mileage = mileage[0]
                buildYear = buildYear[0]
                price = tmpPrice['content']
                car = Car(companyName, model, mileage, price, buildYear)
                data.append(car)
    return data