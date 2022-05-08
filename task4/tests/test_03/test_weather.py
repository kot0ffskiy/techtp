from weather_03.weather_wrapper import WeatherWrapper, FORECAST_URL
from pytest import raises
from os import environ


# Token inizializartion
token = environ.get("API_TOKEN")

def test_weather():
    city = 'Argentina'
    param = WeatherWrapper(token)
    func = param.get_tomorrow_diff(city)
    tom_temp = param.get_tomorrow_temperature(city) 
    tod_temp = param.get_temperature(city)
    delta = tom_temp - tod_temp

    if delta > 3:
        response = 'much warmer'
    elif delta > 0.5:
        response = 'warmer'
    elif delta < -3:
        response = 'much colder'
    elif delta < -0.5:
        response = 'colder'
    else:
        response = 'the same'
    expect = f'The weather in {city} tomorrow will be {response} than today'
    assert func == expect

    city_2 = 'New York'
    temp_diff = param.find_diff_two_cities(city, city_2)
    func1 = param.get_diff_string(city, city_2)
    func2 = param.get_diff_string(city_2, city)
    if temp_diff < 0:
        _status = 'colder'
        temperature_diff = -temp_diff
        status = 'warmer'
    else:
        _status = 'warmer'
        temperature_diff = temp_diff
        status = 'colder'

    temperature_diff = int(temperature_diff)    
    expect_1 = f'Weather in {city} is {_status} than in {city_2} by {temperature_diff} degrees'
    expect_2 = f'Weather in {city_2} is {status} than in {city} by {temperature_diff} degrees'
    assert expect_1 == func1
    assert expect_2 == func2

    #raise error
    #bad_city = 'Borsch'
    with raises(AttributeError) as func:
        param.get_response_city("Bad_city", FORECAST_URL)
    rfunc = func.value.args[0]
    expect = 'Incorrect city'
    assert rfunc == expect
