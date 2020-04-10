#Cars
def make_car(manufacturer, model, **car_info):
    car_profile = {}
    car_profile['manufacturer'] = manufacturer
    car_profile['model'] = model
    for k, v in car_info.items():
        car_profile[k] = v
    return car_profile

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)