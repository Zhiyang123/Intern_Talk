import pandas as pd

def get_values(ccy_key):
    s = ""
    pkmndata = pd.read_csv(r"C:\Users\Zhi Yang\OneDrive\Documents\NTU y1s2 mods\Hackathon\internship_test.csv")

    for i in range(5):
        s += str(pkmndata[ccy_key][i])
        s += '\n'
        
    return s

def get_salary(salary):
    p = ""
    pkmndata = pd.read_csv(r"C:\Users\Zhi Yang\OneDrive\Documents\NTU y1s2 mods\Hackathon\internship_test.csv")

    cnt_above = 0
    cnt_below = 0
    i = 0
    temp = -1
    length = len(pkmndata)

    if salary > pkmndata['monthlySalary'][0] + 1000:
        return p
    
    for i in range(len(pkmndata)):
        if salary >= int(pkmndata['monthlySalary'][i]):
            temp = i
            break
        
    if temp == -1:
        return p
        
    if temp < 4:
        temp = 4
    elif temp > length - 6:
        temp = length - 6
        
    for i in range(temp+5, temp-5, -1):
        ls = '\U0001F3E2: {} \n\U0001F4CD: {} \n\U0001F4C6: {} \n\U0001F343: {} \n\U0001F4B0: ${} / month\n'.format(pkmndata['company'][i], pkmndata['city'][i], pkmndata['year'][i], pkmndata['season'][i], pkmndata['monthlySalary'][i])
        p += ls
        p += '\n'
        
    return p

def hiring_season(year, season):
    p = ""
    pkmndata = pd.read_csv(r"C:\Users\Zhi Yang\OneDrive\Documents\NTU y1s2 mods\Hackathon\internship_test.csv")

    cnt = 0

    for i in range(len(pkmndata)):
        if cnt == 5:
            break;
        elif int(pkmndata['year'][i]) == year and pkmndata['season'][i] == season:
            ls = '\U0001F3E2: {} \n\U0001F4CD: {} \n\U0001F4C6: {} \n\U0001F343: {} \n\U0001F4B0: ${} / month\n'.format(pkmndata['company'][i], pkmndata['city'][i], pkmndata['year'][i], pkmndata['season'][i], pkmndata['monthlySalary'][i])
            p += ls
            p += '\n'
            cnt += 1
    return p

def find_cities(city):
    p = ""
    pkmndata = pd.read_csv(r"C:\Users\Zhi Yang\OneDrive\Documents\NTU y1s2 mods\Hackathon\internship_test.csv")

    cnt = 0

    for i in range(len(pkmndata)):
        if cnt == 5:
            break;
        elif pkmndata['city'][i] == city:
            ls = '\U0001F3E2: {} \n\U0001F4CD: {} \n\U0001F4C6: {} \n\U0001F343: {} \n\U0001F4B0: ${} / month\n'.format(pkmndata['company'][i], pkmndata['city'][i], pkmndata['year'][i], pkmndata['season'][i], pkmndata['monthlySalary'][i])
            p += ls
            p += '\n'
            cnt += 1
    return p

def get_company(company):
    p = ""
    pkmndata = pd.read_csv(r"C:\Users\Zhi Yang\OneDrive\Documents\NTU y1s2 mods\Hackathon\internship_test.csv")
    for i in range(len(pkmndata)):
        if pkmndata['company'][i] == company:
            ls = '\U0001F3E2: {} \n\U0001F4CD: {} \n\U0001F4C6: {} \n\U0001F343: {} \n\U0001F4B0: ${} / month\n\nDetails:\n{}\n\nApply Link: {}\n'.format(pkmndata['company'][i], pkmndata['city'][i], pkmndata['year'][i], pkmndata['season'][i], pkmndata['monthlySalary'][i], pkmndata['benefits'][i], pkmndata['applyLink'][i])
            p += ls
            p += '\n'
            return p
    return p
    
    
        
            
    
        
    


