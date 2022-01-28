# importa los módulos time y playsound
import time
from playsound import playsound 
  
# define la función countdown timer 
def countdown_timer(seconds):
    
    while seconds > 0:       

        mins = int(seconds / 60)
        secs = int(seconds % 60)

        timer = f'{mins}:{secs}'

        print(timer)
        
        seconds -= 1
      
    print('¡Se acabó el tiempo!')

    playsound('mixkit-sound.wav')
  
  
# tiempo del input en segunods
seconds = input("Ingresa el tiempo en segundos: ")
  
# llamar a la función
countdown_timer(int(seconds))
