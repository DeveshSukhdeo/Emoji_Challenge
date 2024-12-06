import simplegui
import math
                
# Global Variables
width = 600
height = 600
face1 = False
face2 = False
face3 = False
face4 = False
face5 = False
                
# Event Handlers
def all_false():
        global face1
        global face2
        global face3
        global face4
        global face5
        face1 = False
        face2 = False
        face3 = False
        face4 = False
        face5 = False
                    
def toggle_face1():
        all_false()
                global face1
                face1 = not face1
                    
def toggle_face2():
        all_false()
                global face2
                face2 = not face2
                      
def toggle_face3():
        all_false()
                global face3
                face3 = not face3
                    
def toggle_face4():
        all_false()
                global face4
                face4 = not face4
        
def toggle_face5():
        all_false()
                global face5
                face5 = not face5
        
#Syeda - Bottom Left Quadrant
        def draw_handler(canvas):
                if face1:
                canvas.draw_circle((width/2, height/2), width/2 - 50, 10, "#c0c0bf","#c0c0bf")
                canvas.draw_line((150,150),(200,150), 4, "Black") #left eyebrow 
                canvas.draw_line((400, 150),(450,150), 4, "Black") #right eyebrow
                canvas.draw_circle((200,250), 50, 2, "Black") #left eye
                canvas.draw_circle((400,250), 50, 2, "Black") #right eye
                canvas.draw_line((150,230), (250,230), 4, "Black") #left eyelid
                canvas.draw_line((350,230), (450,230), 4, "Black") #right eyelid
                canvas.draw_line((250,350), (350,350), 4, "Black") #mouth
#Micah - Bottom Right Quadrant
                if face2: 
                canvas.draw_circle((width/2, height/2), width/2 - 50, 10, "#ffde34", "#ffde34")
                canvas.draw_circle((width/2 - 60, height/2 - 60), 30, 5, "Black")
                canvas.draw_line((width/2 + 30, height/2 - 60), (width/2 + 90, height/2 - 60), 5, "Black")
                canvas.draw_circle((width/2 - 60, height/2 - 60), 15, 5, "Black", "Black")
                canvas.draw_circle((width/2, height/2 + 80), 20, 1, "Red", "Red")
                canvas.draw_polygon([(width/2 - 100, height/2 + 30), (width/2, height/2 + 100), (width/2 + 100, height/2 + 30)], 10, "Black")
                canvas.draw_polygon([(width/2 - 100, height/2), (width/2 + 100, height/2), (width/2 + 100, height/2 + 30), (width/2 - 100, height/2 + 30)], 1, "#ffde34", "#ffde34")
                canvas.draw_circle((width/2 - 100, height/2 + 30), 20, 1, "#FFB6C1", "#FFB6C1")
                canvas.draw_circle((width/2 + 100, height/2 + 30), 20, 1, "#FFB6C1", "#FFB6C1")
#Devesh - Top Left Quadrant
                if face3:
                canvas.draw_circle((width/4, height/4), width/4 - 25, 10, "Yellow", "Yellow")  
                canvas.draw_circle((width/4 - 55, height/4 - 50), 30, 1, "black", "white")   
                canvas.draw_circle((width/4 + 55, height/4 - 50), 30, 1, "black", "white")   
                canvas.draw_circle((width/4 - 55, height/4 - 50), 10, 1, "black", "black")  
                canvas.draw_circle((width/4 + 55, height/4 - 50), 10, 1, "black", "black")  
                canvas.draw_polygon([(width/4 - 100, height/4 + 30), (width/4 - 50, height/4 + 80), (width/4 + 50, height/4 + 80), (width/4 + 100, height/4 + 30)], 1, "black", "white")   
        
#Towaf - Top Right Quadrant
                if face4:
                canvas.draw_circle((width/4, height/4), width/4 - 50, 10, "Yellow", "Yellow")
                canvas.draw_circle((200, 150), 50, 10, "Black")
                canvas.draw_circle((400, 150), 50, 10, "Black")
                canvas.draw_polygon([(200, 350), (400, 350), (400, 250), (200,250)], 5, "Red")
        
#All 
                if face5:
                        canvas.draw_point((0,0), 2, "white") #temporary, u can delete when somethings here 
        
frame = simplegui.create_frame("Pictures", width, height) 
        
frame.set_draw_handler(draw)
frame.add_button("Happy", toggle_face1, 100)
frame.add_button("Sad", toggle_face2, 100)
frame.add_button("Angry", toggle_face3, 100)
frame.add_button("Surprised", toggle_face4, 100)
frame.add_button("Emoticon", toggle_face5, 100)
        
# Remember to start the frame
frame.start()
