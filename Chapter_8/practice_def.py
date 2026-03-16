def watches(type, model, year):
    print(f"\nProduct: {type}")
    print(f"Type: {model}")
    print(f"Price: ${year}")


watches('Rolex', 'DeepSea James Cameron', 2012)


watches(type='Omega',
        model='Seamaster Spectre', year=2015)


watches(type='Rolex', model='Submariner',
        year=2008)


def watches(type='Rolex', model='DayDate'):
    print(f"\n{type} {model}.")

watches()    