# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import Python_DHT as dht

# Möglich sind .DHT11, DHT22, oder AM2302.
sensor = dht.DHT11

# Hier wird der Pin festgelegt an dem Sensor mit dem Breadboard verbunden wird. (Nach .BCM)
pin = 4

# Wenn keine Daten gelesen werden können versucht das Programm das bis 15mal nochmal mit 2sekunden abstand
humidity, temperature = dht.read_retry(sensor, pin)
# humidity = Luftfeuchtigkeit
# temperature = Temperatur


# Wenn Messwerte vorhanden sind, werden diese Ausgegeben.
if humidity is not None and temperature is not None:
	print('Temperatur={0:0.1f}*C  Luftfeuchtigkeit={1:0.1f}%'.format(temperature, humidity))
else:
	print('Daten konnten nicht gelesen werden!')
