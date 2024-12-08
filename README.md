# Emoji_Challenge

w = x # Highest val <br/>
h = y # Highest Val <br/>

leftQuadrant >= 0 <br/>
leftQuadrant <= (w/2) <br/>

rightQuadrant >= (W/2) <br/>
rightQuadrant <= W <br/>

up >= 0 <br/>
up <= h/2 <br/>
down > h/2 <br/>
down < h <br/>

For example, in (x - size/3, y - size/3), size/5:
The element is positioned 1/3 of the main element's size to the left and up from the center.
The element's size is 1/5 of the main element's size.

In-code example: The following code shows how you use variables to keep an image stagnant with a change in dimensions. Also shows how a change in size affects output.

'''
    
    import simplegui
    
    #Global Variables
    width = 400
    height = 400
    face_size = 100
    face_x = width // 2
    face_y = height // 2
    
    def draw_face(canvas, x, y, size):
        # Main face circle
        canvas.draw_circle((x, y), size, 2, "Yellow", "Yellow")
        
        # Left eye
        canvas.draw_circle((x - size/3, y - size/3), size/10, 2, "Black", "Black")
        
        # Right eye
        canvas.draw_circle((x + size/3, y - size/3), size/10, 2, "Black", "Black")
        
        # Mouth
        canvas.draw_line((x - size/2, y + size/4), (x + size/2, y + size/4), 2, "Black")
    
    def draw(canvas):
        draw_face(canvas, face_x, face_y, face_size)
    
    def increase_size():
        global face_size
        face_size += 10
        if face_size > min(width, height) // 2:
            face_size = min(width, height) // 2
    
    def decrease_size():
        global face_size
        face_size -= 10
        if face_size < 20:
            face_size = 20
    
    frame = simplegui.create_frame("Face Drawing", width, height)
    frame.set_draw_handler(draw)
    frame.add_button("Increase Size", increase_size, 100)
    frame.add_button("Decrease Size", decrease_size, 100)
    
    #Start the frame animation
    frame.start()
'''
