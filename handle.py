class Handle:                                                                                                                                                
     def __init__(self, world):                                                
          self.canvas = world.canvas
          self.canvas.bind("<Button-1>", self.handle_mouse)                     
          self.canvas.bind("<Key>", self.handle_key)                            
          self.canvas.focus_set()
          
     def handle_key(self, event):
          '''
          Press key 's' to shoot
          Press key ' ' to ....
          Press ... 
          '''

          print "You pressed a key!"
          if event.char == u'1':                                                
               print " You pressed '1'. Nothing will happen."
          elif event.char == u's':
               print " You pressed 's'. The tank will shoot."
          else:                                                                 
               print " No action for this key [" + event.char + "]"                                       
               
     def handle_mouse(self, event):                                            
          print "You clicked a mouse button."         
                    
