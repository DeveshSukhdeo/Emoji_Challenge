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

def draw_face(canvas, x, y, size, face_type):
    if face_type == 1:  # person 1
        canvas.draw_circle((x, y), size, 2, "Yellow", "Yellow")
        canvas.draw_circle((x - size/3, y - size/3), size/6, 2, "Black")
        canvas.draw_circle((x + size/3, y - size/3), size/6, 2, "Black")
        canvas.draw_text("Happy", (x - size/3, y + size*0.8), size/5, "Black")
    elif face_type == 2:  # person 2
        canvas.draw_circle((x, y), size, 2, "Blue", "Blue")
        canvas.draw_circle((x - size/3, y - size/3), size/6, 2, "Black")
        canvas.draw_circle((x + size/3, y - size/3), size/6, 2, "Black")
        canvas.draw_text("Sad", (x - size/4, y + size*0.8), size/5, "Black")
    elif face_type == 3:  # person 3
        canvas.draw_circle((x, y), size, 2, "Red", "Red")
        canvas.draw_line((x - size/2, y - size/3), (x - size/4, y - size/2), 2, "Black")
        canvas.draw_line((x + size/2, y - size/3), (x + size/4, y - size/2), 2, "Black")
        canvas.draw_circle((x - size/3, y - size/4), size/6, 2, "Black")
        canvas.draw_circle((x + size/3, y - size/4), size/6, 2, "Black")
        canvas.draw_polygon([(x - size/2, y + size/3), (x, y + size/6), (x + size/2, y + size/3)], 2, "Black")
        canvas.draw_text("Angry", (x - size/3, y + size*0.8), size/5, "Black")
    elif face_type == 4:  # person 4
        canvas.draw_circle((x, y), size, 2, "Green", "Green")
        canvas.draw_circle((x - size/3, y - size/3), size/5, 2, "Black")
        canvas.draw_circle((x + size/3, y - size/3), size/5, 2, "Black")
        canvas.draw_circle((x, y + size/4), size/3, 2, "Black")
        canvas.draw_text("Surprised", (x - size/2, y + size*0.8), size/5, "Black")

def draw(canvas):
    quad_size = min(width, height) / 2.5
    if show_all:
        draw_face(canvas, width/4, height/4, quad_size/2, 1)
        draw_face(canvas, 3*width/4, height/4, quad_size/2, 2)
        draw_face(canvas, width/4, 3*height/4, quad_size/2, 3)
        draw_face(canvas, 3*width/4, 3*height/4, quad_size/2, 4)
    else:
        if face1:
            draw_face(canvas, width/2, height/2, quad_size, 1)
        elif face2:
            draw_face(canvas, width/2, height/2, quad_size, 2)
        elif face3:
            draw_face(canvas, width/2, height/2, quad_size, 3)
        elif face4:
            draw_face(canvas, width/2, height/2, quad_size, 4)

frame = simplegui.create_frame("Emoji Selector", width, height)
frame.set_draw_handler(draw)
frame.add_button("Happy", toggle_face1, 100)
frame.add_button("Sad", toggle_face2, 100)
frame.add_button("Angry", toggle_face3, 100)
frame.add_button("Surprised", toggle_face4, 100)
frame.add_button("Show All", toggle_all, 100)

frame.start()
