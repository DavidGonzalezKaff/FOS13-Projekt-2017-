from initialise import *
import functools


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text,pos_x,pos_y,size = 50, fix_right = 0, fix_left = 0, fixed_point = display_width/2 ):
    
    largeText = pig.font.Font(schrift,size)
    TextSurf, TextRect = text_objects(text, largeText)
    if fix_right == 1: 
            
            length = len(text)*size*0.8
            pos_x = fixed_point - length/2
    TextRect.center = ((pos_x),(pos_y))
    gameDisplay.blit(TextSurf, TextRect)  


    

class event_queue():

    events =  pig.event.get() 
    
    @classmethod       
    def events_update(cls):
        cls.events = pig.event.get()
        
class label(event_queue):
    
    keys = { pig.K_1 : 1, pig.K_2 : 2, pig.K_3 : 3 , pig.K_4 : 4 , pig.K_5 :5 , pig.K_6 : 6, pig.K_7 : 7
            , pig.K_8 : 8 ,pig.K_9 : 9, pig.K_0 : 0}
    
    values = []
    
    def __init__(self, x,y, size = 50):
        
        self.x = x
        self.y = y
        self.size = size
      
        
    def fill_values(self):
        
        for event in event_queue.events:
            
            if event.type == pig.KEYDOWN:
                
                for taste in self.keys:
                    
                    if event.key == taste:
                        
                        self.values.append(self.keys[taste])
                        
                if event.key == pig.K_BACKSPACE:
                    try:
                        del self.values[-1]
                    except:
                        #index out of bounds
                        pass
                    
    @property               
    def number(self):
        num = 0
        for i,lit in enumerate(self.values):
            num += lit*10**(len(self.values) -i-1)
        return num     
                                   
    def display(self):
        num = ''.join(str(i) for i in self.values)        
        message_display(num, self.x, self.y, self.size)
        
    @classmethod    
    def delete(cls):
        cls.values[:] = []
       
  
def button(x,y,w,h, text, func = lambda : None, size = 30):
    #wenn innerhalb button
    mouse = pig.mouse.get_pos()
    
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pig.draw.rect(gameDisplay, black,(x,y,w,h))
        
        #wenn gedrückt
        
        for event in event_queue.events:
            if event.type == pig.MOUSEBUTTONDOWN:
                
                func()
   
    else:
        #zeig den button
        pig.draw.rect(gameDisplay, red,(x,y,w,h))
        message_display(text,x+(w/2),y+(h/2),size)        


    
                      

def maindeco(func):
 
    
    def structure(*args):
        while 1:
            
            event_queue.events_update()
            for event in event_queue.events:        
    
                if event.type == pig.QUIT:
                    
                    pig.quit()
                    quit()
            
            gameDisplay.fill(white)
            func(*args)

            pig.display.update()      
            
            clock.tick(30)
    return structure
