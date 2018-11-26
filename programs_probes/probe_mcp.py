#Librerias necesarias para leer datos de MCP
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import time as t

#Configuración de comunicación SPI
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

while True:
	val = [0]*2
	for i in range(2):
		val[i] = mcp.read_adc(i)
	print('|Val X|Val Y|')
	print('|{0:>4} |{1:>4} |'.format(*val))
	t.sleep(0.5)
