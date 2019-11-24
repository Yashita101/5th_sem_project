import spidev
class TemperatureSensor:
    def __init__(self, temp_channel = 0):
        self.temp_channel  = temp_channel
        
    def ReadChannel(self):
        self.adc = spi.xfer2([1,(8+self.temp_channel)<<4,0])
        self.data = ((self.adc[1]&3) << 8) + self.adc[2]
        return self.data

     
    def ConvertVolts(self,data,places):
      self.volts = (self.data * 3.3) / float(1023)
      self.volts = round(self.volts,self.places)  
      return self.volts
      

    def ConvertTemp(self,data,places):
      self.temp = ((self.data * 330)/float(1023))-50
      self.temp = round(self.temp,self.places)
      return self.temp

