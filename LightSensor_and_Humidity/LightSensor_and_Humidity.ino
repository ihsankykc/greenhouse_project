#include "DHT11.h"

int sensorPinLDR = A2;  // Analog pin connected to the sensor
float sensorValue;  // Analog reading (0-1023)
float voltage;  // Voltage at the sensor
float irradiance;  // Light level in W/m²
float V_ref = 5.0;  // Reference voltage for the ADC
int sensorPinDHT11 = A2;  // Analog pin connected to the sensor

int counter = 0; // Initialize a counter
unsigned long previousMillis = 0; // Stores last time the counter was updated
const long interval = 5000; // Interval to send counter value (1 second)

void setup() {
  Serial.begin(9600);
}

void loop() {
  
  float humidity = DHT11.getHumidity();
  float temperature = DHT11.getTemperature();

    // Read the LDR sensor value (0-1023)
    sensorValue = analogRead(sensorPinLDR);

    // Convert analog reading to voltage
    voltage = (sensorValue / 1023.0) * V_ref;

    //assume 1V = 100 W/m² 
    // convert voltage to irradiance
    irradiance = voltage * 200.0;  

    // Output the light level in W/m²
    // Temprature and humidity
    
    Serial.println(irradiance);
    Serial.println(humidity);
    Serial.println(temperature);

    

    delay(5000);
    
  

}
