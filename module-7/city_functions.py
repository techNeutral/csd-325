#Brett Fuller
#11/30/2024
#CSD 325  – Assignment 7.2

def formatCityCountry(city, country, language='', population=''):
    formattedString = city + ", " + country
    suffix = ''
    if(population):
        suffix = " - population " + population
    if(language):
        suffix = suffix + ", " + language 
    formattedString = formattedString + suffix
    return formattedString
print(formatCityCountry("London", "England"))
print(formatCityCountry("Paris", "France", "2103000"))
print(formatCityCountry("Omaha", "USA", "English", "500000"))

