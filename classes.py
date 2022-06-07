class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        
        self.__C = Television.MIN_CHANNEL
        self.__V = Television.MIN_VOLUME
        self.__S = False
        pass

    def power(self):
        
        if self.__S == False:
            self.__S = True
        elif self.__S == True:
            self.__S = False
        pass

    def channel_up(self):
        
        if self.__S == True:
            if self.__C == Television.MAX_CHANNEL:
                self.__C = Television.MIN_CHANNEL
            else:
                self.__C += 1
        pass

    def channel_down(self):
        
        if self.__S == True:
            if self.__C == Television.MIN_CHANNEL:
                self.__C = Television.MAX_CHANNEL
            else:
                self.__C -= 1
        pass

    def volume_up(self):
        
        if self.__S == True:
            if self.__V != Television.MAX_VOLUME:
                self.__V += 1
        pass

    def volume_down(self):
        
        if self.__S == True:
            if self.__V != Television.MIN_VOLUME:
                self.__V -= 1
        pass

    def __str__(self):
        
        return(f"TV status: Is on = {self.__S}, Channel = {self.__C}, Volume = {self.__V}")
        pass
