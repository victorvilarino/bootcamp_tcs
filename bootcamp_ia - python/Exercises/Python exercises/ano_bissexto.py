# 1. Se o ano for divisível por 4 → pode ser bissexto
# 2. Se também for divisível por 100 → deixa de ser bissexto
# 3. Mas se for divisível por 400 → volta a ser bissexto

def leap_year (year):
    if year % 400 == 0:
        return True
    
    elif year % 100 == 0:
        return False
    
    elif year % 4 == 0:
        return True

    else:
        return False

year = int(input())
print(leap_year(year))