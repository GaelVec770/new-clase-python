class ConversionTemperatura:
    # Atributos: Encapsulación
    __temperaturaCelsius = 0.0
    __temperaturaFahrenheit = 0.0
    __temperaturaKelvin = 0.0

    # Métodos: Cada uno resuelve un caso de uso
    def convertirTemperaturas(self, temperaturaCelsius):
        # Precondición: Se recibe una temperatura en grados Celsius
        # La temperatura debe ser un valor numérico
        self.__temperaturaCelsius = temperaturaCelsius
        self.__temperaturaFahrenheit = (self.__temperaturaCelsius * 9/5) + 32
        self.__temperaturaKelvin = self.__temperaturaCelsius + 273.15

        # Postcondición: Temperaturas convertidas a Fahrenheit y Kelvin
        return self.__temperaturaFahrenheit, self.__temperaturaKelvin

    def verificarCongelacionEBullicion(self):
        # Verificar si la temperatura corresponde al punto de congelación o ebullición en alguna escala
        if self.__temperaturaCelsius == 0:
            estado = "Congelación del agua (Celsius)"
        elif self.__temperaturaCelsius == 100:
            estado = "Ebullición del agua (Celsius)"
        elif self.__temperaturaFahrenheit == 32:
            estado = "Congelación del agua (Fahrenheit)"
        elif self.__temperaturaFahrenheit == 212:
            estado = "Ebullición del agua (Fahrenheit)"
        elif self.__temperaturaKelvin == 273.15:
            estado = "Congelación del agua (Kelvin)"
        elif self.__temperaturaKelvin == 373.15:
            estado = "Ebullición del agua (Kelvin)"
        else:
            estado = "No corresponde al punto de congelación o ebullición en ninguna escala"

        # Postcondición: Devuelve el estado de la temperatura en relación a la congelación o ebullición
        return estado
