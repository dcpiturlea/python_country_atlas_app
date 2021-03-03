from countryinfo import CountryInfo


def get_capital_by_country(country):
    country = CountryInfo(country)
    return country.capital()


def get_area_by_country(country):
    country = CountryInfo(country)
    return country.area()


def get_continent_by_country(country):
    country = CountryInfo(country)
    return country.region()


def get_wiki_page_by_country(country):
    country = CountryInfo(country)
    return country.wiki()


def get_timezone_by_country(country):
    country = CountryInfo(country)
    return country.timezones()


def get_provinces_by_country(country):
    country = CountryInfo(country)
    return country.provinces()


def get_currencies_by_country(country):
    country = CountryInfo(country)
    return country.currencies()


def get_population_by_country(country):
    country = CountryInfo(country)
    return country.population()


def get_all_countries_by_country():
    country = CountryInfo()
    return country.all().keys()


def get_all_info_for_country(country):
    result = CountryInfo(country)
    return result.info()


def get_country_code_from_country(country):
    result = CountryInfo(country)
    return result.iso(2).lower()

# Example
# country_name = 'Taiwan'
