import csv

def cleanfile(inf):
    inputfile = inf + ".csv"
    with open (inputfile, "rb") as f:
        reader=csv.reader(f,delimiter=',')
        titles=[]
        prices=[]
        mileages=[]
        for row in reader:
            titles.append(row[0])
            prices.append(row[1])
            mileages.append(row[5])
    
    rows=[]
    for i in range(len(titles)):
        temp_list=titles[i].strip().split(" ")

        if temp_list[0] == 'Certified':
    #       temp_list[0] =1
            Certified=1
        else:
    #       temp_list[0]=0
            Certified=0
        year=temp_list[1]
        brand=temp_list[2]
        model=temp_list[3:-1]
        model_str=str(model)
        model_str=model_str.replace("[","").replace("]","").replace("]","").replace("'","").replace(",","")
        if not model_str:
            continue
        price=prices[i]
        mileage=mileages[i]
        rows.append([Certified,year,brand,model_str,price,mileage])
    ouf = "clean_" + inf + ".csv"
    with open(ouf, "a") as out_f:
        writer = csv.writer(out_f)
        writer.writerows(rows)
    return ouf

def cleanspace(inputfile):
    with open(inputfile, 'rb') as inp:
        valid_rows = [row for row in csv.reader(inp) if any(field.strip() for field in row)]
    
    with open(inputfile, 'wb') as out:
        csv.writer(out).writerows(valid_rows)
        
if __name__ == "__main__":
    clean_list = ["njauto_Acura", "njauto_Audi", "njauto_BMW", "njauto_Chevrolet","njauto_Dodge", "njauto_Benz", \
                  "njauto_Ford", "njauto_Honda", "njauto_Lexus", "njauto_Jeep", "njauto_Mazda", "njauto_Nissan", "njauto_Toyota"]
    for i in clean_list:
        temp = cleanfile(i)
        cleanspace(temp)

