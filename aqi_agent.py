# Simple Reflex Agent for AQI

def calculate_aqi(pm25, pm10, co, no2):
    
    if pm25 <= 50 and pm10 <= 50:
        return "Good"
    
    elif pm25 <= 100 and pm10 <= 100:
        return "Moderate"
    
    elif pm25 <= 150:
        return "Unhealthy for Sensitive Groups"
    
    elif pm25 <= 200:
        return "Unhealthy"
    
    elif pm25 <= 300:
        return "Very Unhealthy"
    
    else:
        return "Hazardous"


def read_sensor_data(filename):
    
    with open(filename, "r") as file:
        data = file.readline().split(",")

        pm25 = int(data[0])
        pm10 = int(data[1])
        co = int(data[2])
        no2 = int(data[3])

    return pm25, pm10, co, no2


pm25, pm10, co, no2 = read_sensor_data("sensor_data.txt")

aqi = calculate_aqi(pm25, pm10, co, no2)

print("AQI Level:", aqi)
