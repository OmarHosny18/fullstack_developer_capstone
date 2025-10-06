from .models import CarMake, CarModel

def initiate():
    # Populate CarMake data
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology", "country": "Japan", "founded_year": 1933},
        {"name": "Mercedes", "description": "Luxury cars. German engineering excellence", "country": "Germany", "founded_year": 1926},
        {"name": "Audi", "description": "Performance-oriented cars. German technology", "country": "Germany", "founded_year": 1909},
        {"name": "Kia", "description": "Reliable and affordable Korean vehicles", "country": "South Korea", "founded_year": 1944},
        {"name": "Toyota", "description": "Innovative and efficient cars. Japanese reliability", "country": "Japan", "founded_year": 1937},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(
                name=data['name'],
                description=data['description'],
                country=data['country'],
                founded_year=data['founded_year']
            )
        )

    # Populate CarModel data
    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "color": "Black", "car_make": car_make_instances[0]},
        {"name": "Qashqai", "type": "SUV", "year": 2023, "color": "Blue", "car_make": car_make_instances[0]},
        {"name": "XTRAIL", "type": "SUV", "year": 2023, "color": "Silver", "car_make": car_make_instances[0]},

        {"name": "A-Class", "type": "HATCHBACK", "year": 2023, "color": "White", "car_make": car_make_instances[1]},
        {"name": "C-Class", "type": "SEDAN", "year": 2023, "color": "Black", "car_make": car_make_instances[1]},
        {"name": "E-Class", "type": "SEDAN", "year": 2023, "color": "Grey", "car_make": car_make_instances[1]},

        {"name": "A4", "type": "SEDAN", "year": 2023, "color": "Silver", "car_make": car_make_instances[2]},
        {"name": "A5", "type": "COUPE", "year": 2023, "color": "Red", "car_make": car_make_instances[2]},
        {"name": "A6", "type": "SEDAN", "year": 2023, "color": "Blue", "car_make": car_make_instances[2]},

        {"name": "Sorrento", "type": "SUV", "year": 2023, "color": "White", "car_make": car_make_instances[3]},
        {"name": "Carnival", "type": "WAGON", "year": 2023, "color": "Grey", "car_make": car_make_instances[3]},
        {"name": "Cerato", "type": "SEDAN", "year": 2023, "color": "Silver", "car_make": car_make_instances[3]},

        {"name": "Corolla", "type": "SEDAN", "year": 2023, "color": "White", "car_make": car_make_instances[4]},
        {"name": "Camry", "type": "SEDAN", "year": 2023, "color": "Black", "car_make": car_make_instances[4]},
        {"name": "Kluger", "type": "SUV", "year": 2023, "color": "Blue", "car_make": car_make_instances[4]},
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            type=data['type'],
            year=data['year'],
            color=data['color']
        )
