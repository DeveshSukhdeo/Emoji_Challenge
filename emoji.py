#Variables 

#Syeda - Bottom Left Quadrant
        canvas.draw_circle((width/2, height/2), width/2 - 50, 10, "#c0c0bf","#c0c0bf")
        canvas.draw_line((150,150),(200,150), 4, "Black") #left eyebrow 
        canvas.draw_line((400, 150),(450,150), 4, "Black") #right eyebrow
        canvas.draw_circle((200,250), 50, 2, "Black") #left eye
        canvas.draw_circle((400,250), 50, 2, "Black") #right eye
        canvas.draw_line((150,230), (250,230), 4, "Black") #left eyelid
        canvas.draw_line((350,230), (450,230), 4, "Black") #right eyelid
        canvas.draw_line((250,350), (350,350), 4, "Black") #mouth
#Micah - Bottom Right Quadrant
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
        canvas.draw_circle((width/4, height/4), width/4 - 25, 10, "Yellow", "Yellow")  
        canvas.draw_circle((width/4 - 55, height/4 - 50), 30, 1, "black", "white")   
        canvas.draw_circle((width/4 + 55, height/4 - 50), 30, 1, "black", "white")   
        canvas.draw_circle((width/4 - 55, height/4 - 50), 10, 1, "black", "black")  
        canvas.draw_circle((width/4 + 55, height/4 - 50), 10, 1, "black", "black")  
        canvas.draw_polygon([(width/4 - 100, height/4 + 30), (width/4 - 50, height/4 + 80), (width/4 + 50, height/4 + 80), (width/4 + 100, height/4 + 30)], 1, "black", "white")   

#Towaf - Top Right Quadrant
