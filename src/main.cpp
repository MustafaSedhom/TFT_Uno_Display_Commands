#include "Display.h"


// ============================================================
// Function Declarations
// ============================================================

void code_analysis(String code);

void Text_Code(String code);
void Rectangle_code(String code);
void Pixel_Code(String code);
void Line_Code(String code);
void Circle_Code(String code);
void Ellipse_Code(String code);
void CircleHelper_Code(String code);
void Triangle_Code(String code);

// Shared parser
bool Parse_Arguments(String code,const char *command,String args[],int expected);

// ============================================================
// Setup
// ============================================================

void setup()
{
    Serial.begin(115200);
    Init_Display();
}

// ============================================================
// Main Loop
// ============================================================

void loop()
{
    static String receivedString = "";
    while (Serial.available() > 0)
    {
        char c = Serial.read();
        if (c == ';')
        {
            code_analysis(receivedString);
            receivedString = "";
        }
        else
        {
            if (receivedString.length() < 150)
            {
                receivedString += c;
            }
            else
            {
                receivedString = "";
                Serial.println("Error: Command too long!");
            }
        }
    }
}

// ============================================================
// Command Analysis
// ============================================================

void code_analysis(String code)
{
    code.trim();

    if (code.startsWith("Text"))
    {
        Text_Code(code);
    }
    else if (code.startsWith("Rect"))
    {
        Rectangle_code(code);
    }
    else if (code.startsWith("Pixel"))
    {
        Pixel_Code(code);
    }
    else if (code.startsWith("Line"))
    {
        Line_Code(code);
    }
    else if (code.startsWith("CircleHelper"))
    {
        CircleHelper_Code(code);
    }
    else if (code.startsWith("Circle"))
    {
        Circle_Code(code);
    }
    else if (code.startsWith("Ellipse"))
    {
        Ellipse_Code(code);
    }
    else if (code.startsWith("Triangle"))
    {
        Triangle_Code(code);
    }
    else if (code.length() > 0)
    {
        Serial.println("Error: Unknown command!");
    }
}

// ============================================================
// Shared Argument Parser
// ============================================================

bool Parse_Arguments(String code,const char *command,String args[],int expected)
{
    code.trim();

    // Validate command name
    if (!code.startsWith(command))
    {
        return false;
    }

    // Remove command name
    code.remove(0, strlen(command));
    code.trim();

    // Remove leading comma
    if (code.startsWith(","))
    {
        code.remove(0, 1);
    }

    // Remove trailing semicolon if present
    if (code.endsWith(";"))
    {
        code.remove(code.length() - 1);
    }

    code.trim();

    int argIndex = 0;

    while (code.length() > 0 && argIndex < expected)
    {
        int commaIndex = code.indexOf(',');

        if (commaIndex == -1)
        {
            args[argIndex] = code;
            code = "";
        }
        else
        {
            args[argIndex] = code.substring(0, commaIndex);
            code.remove(0, commaIndex + 1);
        }

        args[argIndex].trim();
        argIndex++;
    }

    return argIndex == expected;
}


void U8G2_Render(uint16_t foreground_color,uint16_t background_color,bool font_mode, const uint8_t* font)
{
    u8g2.setFont(font);
    u8g2.setFontMode(font_mode);
    u8g2.setForegroundColor(foreground_color);
    u8g2.setBackgroundColor(background_color);
}



// ============================================================
// Text Command
// Format:
// Text, x, y, txt, foreground_color, background_color, font_mode, font;
//
// Example:
// Text, 15, 30, Mustafa Sedhom, 0xffff, 0x0000, 1, u8g2_font_VCR_OSD_tr;
// ============================================================

void Text_Code(String code)
{
    String args[7];

    if (!Parse_Arguments(code, "Text", args, 7))
    {
        return;
    }

    int x = args[0].toInt();
    int y = args[1].toInt();

    String text = args[2];
    String foregroundString = args[3];
    String backgroundString = args[4];

    bool font_mode = args[5].toInt() != 0;

    String fontName = args[6];

    uint16_t foreground_color = (uint16_t)strtoul(
        foregroundString.c_str(), NULL, 0
    );

    uint16_t background_color = (uint16_t)strtoul(
        backgroundString.c_str(), NULL, 0
    );
    U8G2_Render(foreground_color,background_color,font_mode,u8g2_font_VCR_OSD_tr);
    u8g2.drawStr(x,y,text.c_str());
}

// ============================================================
// Rectangle Command
// Format: Rect, x, y, h, w, r, color, fill, rotate;
// ============================================================

void Rectangle_code(String code)
{
    String args[8];

    if (!Parse_Arguments(code, "Rect", args, 8))
    {
        return;
    }

    int x = args[0].toInt();
    int y = args[1].toInt();
    int h = args[2].toInt();
    int w = args[3].toInt();
    int r = args[4].toInt();

    uint16_t color = (uint16_t)strtoul(
        args[5].c_str(), NULL, 0
    );

    bool fill = args[6].toInt() != 0;
    int rotate = args[7].toInt();

    if (w <= 0 || h <= 0)
    {
        Serial.println("Error: Invalid rectangle dimensions!");
        return;
    }

    rotate = ((rotate % 360) + 360) % 360;

    // Standard or rounded rectangle
    if (rotate == 0)
    {
        if (r > 0)
        {
            if (fill)
                Display.fillRoundRect(x, y, w, h, r, color);
            else
                Display.drawRoundRect(x, y, w, h, r, color);
        }
        else
        {
            if (fill)
                Display.fillRect(x, y, w, h, color);
            else
                Display.drawRect(x, y, w, h, color);
        }

        return;
    }
    if(rotate != 0)
    {
        if (fill)
        {
          Display.fillRotatedRect(x, y, w, h, rotate, color);
        }
        else
        {
          Display.drawRotatedRect(x, y, w, h, rotate, color);
        }
    }
}

// ============================================================
// Pixel Command
// Format: Pixel, x, y, color;
// ============================================================

void Pixel_Code(String code)
{
    String args[3];

    if (!Parse_Arguments(code, "Pixel", args, 3))
    {
        return;
    }

    int x = args[0].toInt();
    int y = args[1].toInt();

    uint16_t color = (uint16_t)strtoul(
        args[2].c_str(), NULL, 0
    );

    Display.drawPixel(x, y, color);
}

// ============================================================
// Line Command
// Format: Line, x1, y1, x2, y2, color;
// ============================================================

void Line_Code(String code)
{
    String args[5];

    if (!Parse_Arguments(code, "Line", args, 5))
    {
        return;
    }

    int x1 = args[0].toInt();
    int y1 = args[1].toInt();
    int x2 = args[2].toInt();
    int y2 = args[3].toInt();

    uint16_t color = (uint16_t)strtoul(
        args[4].c_str(), NULL, 0
    );

    Display.drawLine(x1, y1, x2, y2, color);
}

// ============================================================
// Circle Command
// Format: Circle, x, y, r, color, fill;
// ============================================================

void Circle_Code(String code)
{
    String args[5];

    if (!Parse_Arguments(code, "Circle", args, 5))
    {
        return;
    }

    int x = args[0].toInt();
    int y = args[1].toInt();
    int r = args[2].toInt();

    uint16_t color = (uint16_t)strtoul(
        args[3].c_str(), NULL, 0
    );

    bool fill = args[4].toInt() != 0;

    if (r < 0)
    {
        Serial.println("Error: Invalid circle radius!");
        return;
    }

    if (fill)
        Display.fillCircle(x, y, r, color);
    else
        Display.drawCircle(x, y, r, color);
}

// ============================================================
// Ellipse Command
// Format: Ellipse, x, y, rx, ry, color, fill;
// ============================================================

void Ellipse_Code(String code)
{
    String args[6];

    if (!Parse_Arguments(code, "Ellipse", args, 6))
    {
        return;
    }

    int x = args[0].toInt();
    int y = args[1].toInt();
    int rx = args[2].toInt();
    int ry = args[3].toInt();

    uint16_t color = (uint16_t)strtoul(
        args[4].c_str(), NULL, 0
    );

    bool fill = args[5].toInt() != 0;

    if (rx < 0 || ry < 0)
    {
        Serial.println("Error: Invalid ellipse radii!");
        return;
    }
    if (fill)
    {
      Display.fillEllipse(x,y,rx,ry,color);
    }
    else
    {
      Display.drawEllipse(x,y,rx,ry,color);
    }
    
    
}

// ============================================================
// CircleHelper Command
// Format: CircleHelper, x, y, r, corners, delta, color, fill;
// Example: CircleHelper, 100, 100, 30, 3, 20, 0xffff, 1;
// ============================================================

void CircleHelper_Code(String code)
{
    String args[7];

    if (!Parse_Arguments(code, "CircleHelper", args, 7))
    {
        return;
    }

    int x = args[0].toInt();
    int y = args[1].toInt();
    int r = args[2].toInt();

    uint8_t corners = (uint8_t)args[3].toInt();
    int delta = args[4].toInt();

    uint16_t color = (uint16_t)strtoul(
        args[5].c_str(), NULL, 0
    );

    bool fill = args[6].toInt() != 0;

    if (r < 0 || delta < 0)
    {
        Serial.println("Error: Invalid radius or delta!");
        return;
    }

    if (fill)
    {
        Display.fillCircleHelper(
            x, y, r, corners, delta, color
        );
    }
    else
    {
        Display.drawCircleHelper(
            x, y, r, corners, color
        );
    }
}

// ============================================================
// Triangle Command
// Format: Triangle, x1, y1, x2, y2, x3, y3, color, fill;
// ============================================================

void Triangle_Code(String code)
{
    String args[8];

    if (!Parse_Arguments(code, "Triangle", args, 8))
    {
        return;
    }

    int x1 = args[0].toInt();
    int y1 = args[1].toInt();
    int x2 = args[2].toInt();
    int y2 = args[3].toInt();
    int x3 = args[4].toInt();
    int y3 = args[5].toInt();

    uint16_t color = (uint16_t)strtoul(
        args[6].c_str(), NULL, 0
    );

    bool fill = args[7].toInt() != 0;

    if (fill)
    {
        Display.fillTriangle(
            x1, y1, x2, y2, x3, y3, color
        );
    }
    else
    {
        Display.drawTriangle(
            x1, y1, x2, y2, x3, y3, color
        );
    }
}






