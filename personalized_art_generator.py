import tkinter as tk
import random

# Predefined color options
COLORS = ["red", "blue", "green", "yellow", "purple", "orange"]
SHAPES = ["circle", "square", "triangle"]
PATTERNS = ["grid", "random"]

def get_user_inputs():
    """Get user preferences for the artwork via GUI entries."""
    shape = shape_var.get().lower()
    primary_color = primary_color_var.get().lower()
    bg_color = bg_color_var.get().lower()
    pattern = pattern_var.get().lower()
    
    # Validate inputs
    if shape not in SHAPES:
        shape = "circle"  # Default
    if primary_color not in COLORS:
        primary_color = "blue"
    if bg_color not in COLORS:
        bg_color = "white"
    if pattern not in PATTERNS:
        pattern = "random"
        
    return shape, primary_color, bg_color, pattern

def draw_circle(canvas, x, y, size, color):
    """Draw a circle on the canvas at (x, y) with given size and color."""
    canvas.create_oval(x - size, y - size, x + size, y + size, fill=color, outline="")

def draw_square(canvas, x, y, size, color):
    """Draw a square on the canvas at (x, y) with given size and color."""
    canvas.create_rectangle(x - size, y - size, x + size, y + size, fill=color, outline="")

def draw_triangle(canvas, x, y, size, color):
    """Draw a triangle on the canvas at (x, y) with given size and color."""
    points = [x, y - size, x - size, y + size, x + size, y + size]
    canvas.create_polygon(points, fill=color, outline="")

def draw_grid_pattern(canvas, shape, color, canvas_width, canvas_height):
    """Draw shapes in a grid pattern."""
    step = 80  # Distance between shapes
    min_size = 20
    max_size = 40
    
    for x in range(50, canvas_width - 50, step):
        for y in range(50, canvas_height - 50, step):
            size = random.randint(min_size, max_size)
            if shape == "circle":
                draw_circle(canvas, x, y, size, color)
            elif shape == "square":
                draw_square(canvas, x, y, size, color)
            elif shape == "triangle":
                draw_triangle(canvas, x, y, size, color)

def draw_random_pattern(canvas, shape, color, canvas_width, canvas_height):
    """Draw shapes in a random pattern."""
    num_shapes = 30  # Number of shapes to draw
    min_size = 10
    max_size = 50
    
    for _ in range(num_shapes):
        x = random.randint(50, canvas_width - 50)
        y = random.randint(50, canvas_height - 50)
        size = random.randint(min_size, max_size)
        if shape == "circle":
            draw_circle(canvas, x, y, size, color)
        elif shape == "square":
            draw_square(canvas, x, y, size, color)
        elif shape == "triangle":
            draw_triangle(canvas, x, y, size, color)

def generate_art():
    """Generate artwork based on user inputs."""
    # Clear previous artwork
    canvas.delete("all")
    
    # Get user inputs
    shape, primary_color, bg_color, pattern = get_user_inputs()
    
    # Set canvas background
    canvas.configure(bg=bg_color)
    
    # Draw patterns
    if pattern == "grid":
        draw_grid_pattern(canvas, shape, primary_color, canvas_width, canvas_height)
    else:
        draw_random_pattern(canvas, shape, primary_color, canvas_width, canvas_height)
    
    # Display confirmation
    status_label.config(text="Artwork generated! Try different inputs to create more.")

# Set up the GUI
root = tk.Tk()
root.title("Personalized Digital Art Generator")
canvas_width = 600
canvas_height = 400

# Variables for dropdown menus
shape_var = tk.StringVar(value="Circle")
primary_color_var = tk.StringVar(value="Blue")
bg_color_var = tk.StringVar(value="White")
pattern_var = tk.StringVar(value="Random")

# GUI elements
tk.Label(root, text="Welcome to the Art Generator!").pack(pady=10)

tk.Label(root, text="Choose shape:").pack()
shape_menu = tk.OptionMenu(root, shape_var, *SHAPES)
shape_menu.pack()

tk.Label(root, text="Choose primary color:").pack()
primary_color_menu = tk.OptionMenu(root, primary_color_var, *COLORS)
primary_color_menu.pack()

tk.Label(root, text="Choose background color:").pack()
bg_color_menu = tk.OptionMenu(root, bg_color_var, *COLORS)
bg_color_menu.pack()

tk.Label(root, text="Choose pattern:").pack()
pattern_menu = tk.OptionMenu(root, pattern_var, *PATTERNS)
pattern_menu.pack()

# Generate button
tk.Button(root, text="Generate Art", command=generate_art).pack(pady=10)

# Status label
status_label = tk.Label(root, text="")
status_label.pack()

# Canvas for drawing
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack(pady=10)

# Start the GUI loop
root.mainloop()