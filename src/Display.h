#pragma once

#include "Imports.h"

MCUFRIEND_kbv Display;
U8G2_FOR_ADAFRUIT_GFX u8g2;

void Init_Display()
{
    uint16_t displayID = Display.readID();

    Display.begin(displayID);
    Display.setRotation(1);
    Display.fillScreen(0x0000);
    u8g2.begin(Display);
}


// Text, 15, 30, Mustafa Sedhom, 0xffff, 0x0000, 1, u8g2_font_VCR_OSD_tr;
// Rect, 10, 10, 100, 100, 5, 0xffff, 1, 0;
// Pixel, 10, 20, 0xffff;
// Line, 10, 10, 100, 100, 0xf800;
// Circle, 100, 100, 30, 0x07e0, 1;
// Ellipse, 100, 100, 50, 25, 0x001f, 0;
// CircleHelper, 100, 100, 30, 3, 20, 0xffff, 1;
// Triangle, 10, 10, 100, 10, 50, 80, 0xf800, 1;