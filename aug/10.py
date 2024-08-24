
cel = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0]

fahrenhiet = list(map(lambda temp: (temp * 9.0 / 5.0) + 32.0, cel))
print(fahrenhiet)