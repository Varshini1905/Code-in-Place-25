# 🎨 Personal Art Generator

A fun and interactive Python-based GUI application that lets users generate unique digital art based on their preferences! Built using the `tkinter` library, this project is a creative exercise in combining GUI design, user input handling, and simple 2D graphics.

## 🧠 Project Overview

The **Personal Art Generator** allows users to create randomized or grid-patterned artworks using geometric shapes like circles, squares, and triangles. Users can customize:

- **Shape Type** (Circle, Square, Triangle)
- **Primary Color** for the shapes
- **Background Color** for the canvas
- **Pattern Style** (Random or Grid)

Each time the user clicks the **Generate Art** button, the program renders a fresh and unique design based on the selected inputs.

---

## 🚀 Features

- 🎨 Interactive GUI for customizing art
- 📐 Multiple shape options: Circle, Square, Triangle
- 🌈 Color selection for both shapes and background
- 🔀 Two drawing patterns: Random and Grid
- 🖼 Canvas rendering using `tkinter.Canvas`
- 🧪 Input validation with defaults for robustness

---

## 🛠 Technologies Used

- **Python 3.x**
- **tkinter** – Python's standard GUI library
- **random** – For random positioning and sizing of shapes

---

## 💡 How It Works

1. The GUI allows the user to select shape, primary color, background color, and pattern.
2. Once the user clicks **Generate Art**, the canvas is cleared and repainted based on the selected parameters.
3. The shapes are drawn using:
   - `canvas.create_oval()` for circles
   - `canvas.create_rectangle()` for squares
   - `canvas.create_polygon()` for triangles
4. Two patterns are supported:
   - **Grid Pattern:** Shapes are evenly spaced in a grid format.
   - **Random Pattern:** Shapes are placed randomly on the canvas.

---

## 🖥 Usage

1. **Run the script** using Python:
   ```bash
   python personalised_art_generator.py

2. **🎛 Choose Your Preferences** from the Dropdown Menus:

- **Shape**: Circle, Square, Triangle  
- **Primary Color**: Red, Blue, Green, Yellow, Purple, Orange  
- **Background Color**: Red, Blue, Green, Yellow, Purple, Orange  
- **Pattern**: Grid, Random  

Click **"Generate Art"** to create your artwork!  

![cip_optimized](https://github.com/user-attachments/assets/14851516-6996-47f0-b8da-657a2e6d5bbc)

🎉 **Enjoy experimenting with different combinations to make unique digital designs!**

