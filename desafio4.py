from machine import Pin, time_pulse_us
import time

PINO_TRIG = 25
PINO_ECHO = 27
PINO_LED_INTRUSO = 26

trig = Pin(PINO_TRIG, Pin.OUT)
echo = Pin(PINO_ECHO, Pin.IN)
led_intruder = Pin(PINO_LED_INTRUSO, Pin.OUT)

contador_caixas = 0  
CAIXAS_POR_LOTE = 10

def obter_distancia():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    duracao = time_pulse_us(echo, 1, 30000)
    distancia = (duracao / 2) * 0.0343
    return distancia

while True:
    dist = obter_distancia()
    print("Distância:", dist, "cm")

    if dist <= 10:
        print("Caixa detectada!")
        led_intruder.value(1)

        
        contador_caixas += 1
        print("Contador:", contador_caixas)

        if contador_caixas >= CAIXAS_POR_LOTE:
            print(">> LOte concluido 10 caixas no total, comecando proximo lote...")
            contador_caixas = 0
            
            for i in range(3):
                led_intruder.value(1)
                time.sleep(0.3)
                led_intruder.value(0)
                time.sleep(0.3)

        time.sleep(2)  

    else:
        print("Sem caixa.")
        led_intruder.value(0)

    time.sleep(0.5)
