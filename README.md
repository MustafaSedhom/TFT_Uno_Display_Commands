# 🎨 TFT Uno Display Commands

### 🚀 A Serial-Based Graphics Command Library for Arduino TFT Displays

A lightweight command interface for controlling TFT display graphics through serial communication. Send simple text commands from a PC or another microcontroller to draw shapes, render text, and create graphical interfaces on an Arduino-powered TFT display.

<p align="center">
  <strong>🖥️ Text Rendering</strong> &nbsp; • &nbsp;
  <strong>📐 Geometric Shapes</strong> &nbsp; • &nbsp;
  <strong>🎨 RGB565 Colors</strong> &nbsp; • &nbsp;
  <strong>🔌 Serial Communication</strong>
</p>

---

## 📚 Table of Contents

* [✨ Features](#-features)
* [📡 Command Format](#-command-format)
* [🧩 Supported Commands](#-supported-commands)
* [📝 Command Reference](#-command-reference)
* [💻 Usage Examples](#-usage-examples)
* [🎨 Color Format](#-color-format)
* [⚙️ Notes](#️-notes)

---

## ✨ Features

* 📝 **Text Rendering** — Display custom text using U8g2 fonts.
* ▫️ **Rectangle Drawing** — Draw rectangular outlines or filled rectangles.
* 📍 **Pixel Drawing** — Set individual pixels.
* 📏 **Line Drawing** — Connect two points with a line.
* ⭕ **Circle Drawing** — Draw circle outlines or filled circles.
* 🥚 **Ellipse Drawing** — Draw elliptical shapes.
* 🔵 **Circle Helper** — Draw selected portions of a circle.
* 🔺 **Triangle Drawing** — Draw triangular outlines or filled triangles.
* 🌈 **RGB565 Colors** — Specify colors using hexadecimal values.
* 🔗 **Serial Commands** — Control display graphics using readable text instructions.

---

## 📡 Command Format

Commands use a comma-separated format and end with a semicolon (`;`).

```text
Command, parameter1, parameter2, ..., parameterN;
```

### Example

```text
Text, 15, 30, Mustafa Sedhom, 0xffff, 0x0000, 1, u8g2_font_VCR_OSD_tr;
```

### How It Works

1. 📤 Send a command through the serial interface.
2. 🔍 The Arduino parses the command and its parameters.
3. 🎨 The display executes the corresponding drawing operation.

> **Note:** The command parser must support the specified command name, parameter order, and data types.

---

## 🧩 Supported Commands

| Command        | Description                        | Category    |
| :------------- | :--------------------------------- | :---------- |
| `Text`         | Renders text using a selected font | 📝 Text     |
| `Rect`         | Draws a rectangle                  | 📐 Shape    |
| `Pixel`        | Draws a single pixel               | 📍 Graphics |
| `Line`         | Draws a line between two points    | 📏 Graphics |
| `Circle`       | Draws a circle                     | ⭕ Shape     |
| `Ellipse`      | Draws an ellipse                   | 🥚 Shape    |
| `CircleHelper` | Draws selected circle sections     | 🔵 Graphics |
| `Triangle`     | Draws a triangle                   | 🔺 Shape    |

---

## 📝 Command Reference

### 1. 📝 Text

Render text at a specified position with foreground and background colors.

**Syntax**

```text
Text, x, y, text, foreground, background, font_mode, font;
```

**Example**

```text
Text, 15, 30, Mustafa Sedhom, 0xffff, 0x0000, 1, u8g2_font_VCR_OSD_tr;
```

| Parameter    | Description              |
| :----------- | :----------------------- |
| `x`          | Horizontal text position |
| `y`          | Vertical text position   |
| `text`       | Text to display          |
| `foreground` | Text color               |
| `background` | Background color         |
| `font_mode`  | Font rendering mode      |
| `font`       | U8g2 font identifier     |

---

### 2. ▫️ Rect

Draw a rectangle with a configurable corner radius, color, fill mode, and rotation parameter.

**Syntax**

```text
Rect, x, y, width, height, radius, color, fill, rotation;
```

**Example**

```text
Rect, 10, 10, 100, 100, 5, 0xffff, 1, 0;
```

| Parameter  | Description        |
| :--------- | :----------------- |
| `x`, `y`   | Rectangle position |
| `width`    | Rectangle width    |
| `height`   | Rectangle height   |
| `radius`   | Corner radius      |
| `color`    | Rectangle color    |
| `fill`     | Fill mode          |
| `rotation` | Rotation parameter |

**Important:** Confirm the meanings and accepted values of `fill` and `rotation` against your implementation.

---

### 3. 📍 Pixel

Draw an individual pixel at the specified coordinates.

**Syntax**

```text
Pixel, x, y, color;
```

**Example**

```text
Pixel, 10, 20, 0xffff;
```

| Parameter | Description       |
| :-------- | :---------------- |
| `x`, `y`  | Pixel coordinates |
| `color`   | Pixel color       |

---

### 4. 📏 Line

Draw a straight line between two points.

**Syntax**

```text
Line, x0, y0, x1, y1, color;
```

**Example**

```text
Line, 10, 10, 100, 100, 0xf800;
```

| Parameter  | Description    |
| :--------- | :------------- |
| `x0`, `y0` | Starting point |
| `x1`, `y1` | Ending point   |
| `color`    | Line color     |

---

### 5. ⭕ Circle

Draw a circle outline or a filled circle.

**Syntax**

```text
Circle, x, y, radius, color, fill;
```

**Example**

```text
Circle, 100, 100, 30, 0x07e0, 1;
```

| Parameter | Description   |
| :-------- | :------------ |
| `x`, `y`  | Circle center |
| `radius`  | Circle radius |
| `color`   | Circle color  |
| `fill`    | Fill mode     |

---

### 6. 🥚 Ellipse

Draw an ellipse with independently specified horizontal and vertical radii.

**Syntax**

```text
Ellipse, x, y, radius_x, radius_y, color, fill;
```

**Example**

```text
Ellipse, 100, 100, 50, 25, 0x001f, 0;
```

| Parameter  | Description       |
| :--------- | :---------------- |
| `x`, `y`   | Ellipse center    |
| `radius_x` | Horizontal radius |
| `radius_y` | Vertical radius   |
| `color`    | Ellipse color     |
| `fill`     | Fill mode         |

---

### 7. 🔵 CircleHelper

Draw selected sections of a circle, useful for arcs, rounded corners, and custom graphical elements.

**Syntax**

```text
CircleHelper, x, y, radius, corner_mask, delta, color, fill;
```

**Example**

```text
CircleHelper, 100, 100, 30, 3, 20, 0xffff, 1;
```

| Parameter     | Description                    |
| :------------ | :----------------------------- |
| `x`, `y`      | Circle center                  |
| `radius`      | Circle radius                  |
| `corner_mask` | Section selection mask         |
| `delta`       | Additional geometric parameter |
| `color`       | Drawing color                  |
| `fill`        | Fill mode                      |

> The precise behavior of `corner_mask`, `delta`, and `fill` depends on how your command parser implements this operation.

---

### 8. 🔺 Triangle

Draw a triangle using three vertices.

**Syntax**

```text
Triangle, x0, y0, x1, y1, x2, y2, color, fill;
```

**Example**

```text
Triangle, 10, 10, 100, 10, 50, 80, 0xf800, 1;
```

| Parameter  | Description    |
| :--------- | :------------- |
| `x0`, `y0` | First vertex   |
| `x1`, `y1` | Second vertex  |
| `x2`, `y2` | Third vertex   |
| `color`    | Triangle color |
| `fill`     | Fill mode      |

---

## 💻 Usage Examples

### Draw a Simple Interface

The following sequence demonstrates how multiple commands can be combined to create a simple screen layout.

```text
// Draw a white rectangle.
Rect, 10, 10, 300, 200, 5, 0xffff, 0, 0;

// Display a title.
Text, 20, 30, SEDHOM DISPLAY, 0xffff, 0x0000, 1, u8g2_font_VCR_OSD_tr;

// Draw a green circle.
Circle, 60, 100, 25, 0x07e0, 1;

// Draw a red line.
Line, 100, 100, 250, 150, 0xf800;

// Draw a blue ellipse.
Ellipse, 200, 100, 40, 20, 0x001f, 0;
```

**Important:** These examples assume your parser accepts each command in this format and that the selected font and display dimensions are supported.

### Send Commands from a Serial Terminal

Configure your serial terminal to match the baud rate used by your Arduino firmware.

For example, if your firmware uses `115200` baud, configure the terminal accordingly and send a command such as:

```text
Circle, 100, 100, 30, 0x07e0, 1;
```

Make sure your serial sender transmits the terminating semicolon.

---

## 🎨 Color Format

Colors are specified using hexadecimal RGB565 values.

| Color    | Hexadecimal |  RGB565  |
| :------- | :---------: | :------: |
| ⚫ Black  |   `0x0000`  | `0x0000` |
| ⚪ White  |   `0xFFFF`  | `0xFFFF` |
| 🔴 Red   |   `0xF800`  | `0xF800` |
| 🟢 Green |   `0x07E0`  | `0x07E0` |
| 🔵 Blue  |   `0x001F`  | `0x001F` |

### RGB565 Overview

RGB565 represents colors using 16 bits:

* 🔴 Red: 5 bits
* 🟢 Green: 6 bits
* 🔵 Blue: 5 bits

This format is widely used in embedded TFT display applications because it provides a compact representation of color.

---

## ⚙️ Notes

* Coordinates depend on the display resolution and orientation.
* Colors use RGB565 hexadecimal values.
* Font names must match the fonts available in your firmware.
* The command parser must correctly handle the chosen parameter format.
* Commands are terminated with a semicolon (`;`).
* Ensure that text containing commas is handled correctly by your parser.

---

## 👨‍💻 Author

**Mustafa Sedhom**

Embedded Software & Hardware Developer

**Project:** TFT Uno Display Commands

🔗 **GitHub Repository:** [TFT_Uno_Display_Commands](https://github.com/MustafaSedhom/TFT_Uno_Display_Commands)

---

<p align="center">
  <strong>Built with ❤️ for Embedded Systems & TFT Graphics</strong>
  <br>
  <em>Developed by SEDHOM</em>
</p>
