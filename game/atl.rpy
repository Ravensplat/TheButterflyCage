transform lside:
    xalign 0.06

transform half: 
    zoom 0.5
transform double:
    zoom 2

transform woo:
    easeout .175 xalign 0.06

transform quart: 
    zoom 0.25
transform down:
    ypos -100

define in_eye = ImageDissolve("eye", 2.0)
define out_eye = ImageDissolve("eye", 0.3, reverse=True)


#char left/right transforms. default is too far along.
transform char_left:
    xalign 0.15
    yalign 1.0

transform char_right:
    xalign 0.85
    yalign 1.0

image tb_n:
    "textbox_normal"
    zoom 0.35
    center
    yalign 0.1
image tb_nar:
    "textbox_narrator"
    zoom 0.35
    center
    yalign 0.1

image bed_day:
    "bedroom_day"
    zoom 0.5

image bg_bar:
    "bar"
    zoom 0.5