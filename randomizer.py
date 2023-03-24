import random
import botsecrets

PROB_INITIAL = botsecrets.PROB_INITIAL
PROB_STEP = botsecrets.PROB_STEP

class Randomizer:
    def __init__(self):
        self.__probability_initial = PROB_INITIAL
        self.__probability = self.__probability_initial
        self.__step = PROB_STEP

    def generate(self): 
        rand = random.random()
        result = rand <= self.__probability
        self.__update_randomizer_state(result=result)
        return result
    
    def __update_randomizer_state(self, result):
        if result:
            self.__probability = self.__probability_initial
        else:
            self.__probability += self.__step
    
__randomizer = Randomizer()

def is_need_to_send_message():
    return __randomizer.generate()
