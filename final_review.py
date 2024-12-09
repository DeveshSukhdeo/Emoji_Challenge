# Devesh, Towaf, Micah, Syeda
# Period 1-2
# 12/9/24

import simplegui

# Global Variables
width = int(input("Pick a frame width between 200 to 600: "))
height = int(input("Pick a frame height between 200 to 600: "))
face1 = False
face2 = False
face3 = False
face4 = False
show_all = False

# Event Handlers
def all_false():
    global face1, face2, face3, face4, show_all
    face1 = face2 = face3 = face4 = show_all = False

def toggle_face1():
    global face1, face2, face3, face4, show_all
    all_false()
    face1 = True

def toggle_face2():
    global face1, face2, face3, face4, show_all
    all_false()
    face2 = True

def toggle_face3():
    global face1, face2, face3, face4, show_all
    all_false()
    face3 = True

def toggle_face4():
    global face1, face2, face3, face4, show_all
    all_false()
    face4 = True

def toggle_all():
    global show_all
    all_false()
    show_all = True

def clear_all():
    all_false()

def draw_face(canvas, x, y, size, face_type):
    if face_type == 1:  # Devesh
        canvas.draw_circle((x, y), size, 10, "Yellow", "Yellow")  
        canvas.draw_circle((x - size/3, y - size/3), size/5, 1, "black", "white")   
        canvas.draw_circle((x + size/3, y - size/3), size/5, 1, "black", "white")   
        canvas.draw_circle((x - size/3, y - size/3), size/10, 1, "black", "black")  
        canvas.draw_circle((x + size/3, y - size/3), size/10, 1, "black", "black")  
        canvas.draw_polygon([(x - size/1.5, y + size/5), (x - size/3, y + size/2), (x + size/3, y + size/2), (x + size/1.5, y + size/5)], 1, "black", "white")
        canvas.draw_text("Devesh", (x - size/2, y + size*1.2), size/5, "white")
    elif face_type == 2:  # Towaf
        canvas.draw_circle((x, y), size, 10, "Skyblue", "Skyblue")
        canvas.draw_circle((x - size/3, y - size/3), size/4, 5, "Black")
        canvas.draw_circle((x + size/3, y - size/3), size/4, 5, "Black")
        canvas.draw_line((x - size/2, y + size/2), (x + size/2, y + size/2), 5, "Red")
        canvas.draw_text("Towaf", (x - size/3, y + size*1.2), size/5, "white")
    elif face_type == 3:  # Syeda
        canvas.draw_circle((x, y), size, 10, "#c0c0bf","#c0c0bf")
        canvas.draw_line((x-size/2, y-size/2), (x-size/3, y-size/2), 4, "Black")
        canvas.draw_line((x+size/3, y-size/2), (x+size/2, y-size/2), 4, "Black")
        canvas.draw_circle((x-size/3, y), size/4, 2, "Black")
        canvas.draw_circle((x+size/3, y), size/4, 2, "Black")
        canvas.draw_line((x-size/2, y-size/6), (x-size/6, y-size/6), 4, "Black")
        canvas.draw_line((x+size/6, y-size/6), (x+size/2, y-size/6), 4, "Black")
        canvas.draw_line((x-size/4, y+size/3), (x+size/4, y+size/3), 4, "Black")
        canvas.draw_text("Syeda", (x - size/3, y + size*1.2), size/5, "white")
    elif face_type == 4:  # Micah
        canvas.draw_circle((x, y), size, 10, "#ffde34", "#ffde34")
        canvas.draw_circle((x - size/4, y - size/4), size/8, 5, "Black")
        canvas.draw_line((x + size/8, y - size/4), (x + size/2.5, y - size/4), 5, "Black")
        canvas.draw_circle((x - size/4, y - size/4), size/16, 5, "Black", "Black")
        canvas.draw_circle((x, y + size/3), size/12, 1, "Red", "Red")
        canvas.draw_polygon([(x - size/2.5, y + size/8), (x, y + size/2.5), (x + size/2.5, y + size/8)], 10, "Black")
        canvas.draw_polygon([(x - size/2.5, y), (x + size/2.5, y), (x + size/2.5, y + size/8), (x - size/2.5, y + size/8)], 1, "#ffde34", "#ffde34")
        canvas.draw_circle((x - size/2.5, y + size/8), size/12, 1, "#FFB6C1", "#FFB6C1")
        canvas.draw_circle((x + size/2.5, y + size/8), size/12, 1, "#FFB6C1", "#FFB6C1")
        canvas.draw_text("Micah", (x - size/3, y + size*1.2), size/5, "white")

def draw(canvas):
    quad_size = min(width, height) / 2.5
    if show_all:
        draw_face(canvas, width/4, height/4, quad_size/2, 1)
        draw_face(canvas, 3*width/4, height/4, quad_size/2, 2)
        draw_face(canvas, width/4, 3*height/4, quad_size/2, 3)
        draw_face(canvas, 3*width/4, 3*height/4, quad_size/2, 4)
    else:
        if face1:
            draw_face(canvas, width/4, height/4, quad_size/2, 1)
        elif face2:
            draw_face(canvas, 3*width/4, height/4, quad_size/2, 2)
        elif face3:
            draw_face(canvas, width/4, 3*height/4, quad_size/2, 3)
        elif face4:
            draw_face(canvas, 3*width/4, 3*height/4, quad_size/2, 4)

frame = simplegui.create_frame("Emoji Selector", width, height)
frame.set_draw_handler(draw)
frame.add_button("Devesh", toggle_face1, 100)
frame.add_button("Towaf", toggle_face2, 100)
frame.add_button("Syeda", toggle_face3, 100)
frame.add_button("Micah", toggle_face4, 100)
frame.add_button("Show All", toggle_all, 100)
frame.add_button("Clear All", clear_all, 100)

frame.start()
