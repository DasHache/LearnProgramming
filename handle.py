class Handle:                                                                                                                                                
     def __init__(self, world):                                                
         self.canvas = world.canvas
         self.canvas.bind("<Button-1>", self.handle_mouse)                     
         self.canvas.bind("<Key>", self.handle_key)                            
         self.canvas.focus_set()

     def handle_key(self, event):                                              
         print "You pressed a key!"                                            
         if event.char == u'1':                                                
             print " ... key is '1'"                                           
         elif event.char == u'a':                                              
             print " ... key is 'a'"                                           
         else:                                                                 
             print " ... key is unknown"                                       
                                                                               
     def handle_mouse(self, event):                                            
         print "You clicked a mouse button."         
