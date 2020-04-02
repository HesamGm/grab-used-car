import sqlite3
def createTable(cursor):
    cursor.execute("""CREATE TABLE used_car(
                    id integer, company text, model text, 
                    mileage integer, price integer, buildYear integer
                    )""")

def save(car):
    connection = sqlite3.connect('carDetails.db')
    cursor = connection.cursor()
    try:
        createTable(cursor)
    except:
        pass
    # TODO id is not unique
    rs = cursor.execute("SELECT id FROM used_car WHERE company = :company and model = :model and mileage = :mileage and price = :price and buildYear = :buildYear"
                    , {'company' : car.companyName, 'model': car.model, 'mileage' : car.mileage, 'price': car.price, 'buildYear' : car.buildYear})
    result = rs.fetchall()
    if(len(result) < 1):
        cursor.execute("""INSERT INTO used_car VALUES(:id, :company, :model, :mileage, :price, :buildYear)"""
                    , {'id' : car.id, 'company' : car.companyName, 'model': car.model, 'mileage' : car.mileage, 'price': car.price, 'buildYear' : car.buildYear})
        connection.commit()
        connection.close()
        return True
    else:
        connection.close()
        return False

def select():
    connection = sqlite3.connect('carDetails.db')
    cursor = connection.cursor()
    rs = cursor.execute("select * from brands")
    result = rs.fetchall()
    connection.close()
    return result

def getAllBrands():
    connection = sqlite3.connect('carDetails.db')
    cursor = connection.cursor()
    rs = cursor.execute('SELECT c.Company FROM used_car c GROUP BY c.company')
    result = rs.fetchall()
    connection.close()
    return result

def getModelByBrand(company):
    connection = sqlite3.connect('carDetails.db')
    cursor = connection.cursor()
    rs = cursor.execute("SELECT c.model FROM used_car c WHERE c.company = :company", {'company' : company})
    result = rs.fetchall()
    connection.close()
    return result

def getByModel(company, model):
    connection = sqlite3.connect('carDetails.db')
    cursor = connection.cursor()
    rs = cursor.execute("SELECT c.mileage, c.price, c.buildYear FROM used_car c WHERE c.company = :company and c.model = :model", {'company': company,'model' : model})
    result = rs.fetchall()
    connection.close()
    return result

def clean():
    connection = sqlite3.connect('carDetails.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM used_car")
    connection.commit()
    connection.close()