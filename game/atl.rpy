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

#lil image rezises
image l_n: 
    "lil_neutral"
    zoom 0.65
image l_ag_s:
    "lil_angry_speaking"
    zoom 0.65
image l_ag:
    "lil_angry"
    zoom 0.65
image l_an_sp:
    "lil_annoyed_speaking"
    zoom 0.65
image l_an:
    "lil_annoyed"
    zoom 0.65
image l_ap_sp:
    "lil_apologetic_speaking"
    zoom 0.65
image l_ap: 
    "lil_apologetic"
    zoom 0.65
image l_h_b:
    "lil_happy_blush"
    zoom 0.65
image l_h_sp_b:
    "lil_happy_speaking_blush"
    zoom 0.65
image l_h_sp: 
    "lil_happy_speaking"
    zoom 0.65
image l_h:
    "lil_happy"
    zoom 0.65
image l_n_s_b:
    "lil_happy_speaking_blush"
    zoom 0.65
image l_n_s_sp:
    "lil_neutral_smile_speaking"
    zoom 0.65
image l_n_s: 
    "lil_neutral_smile"
    zoom 0.65
image l_n_sp:
    "lil_neutral_speaking"
    zoom 0.65
image l_n: 
    "lil_neutral"
    zoom 0.65
image l_sa_sp: 
    "lil_sad_speaking"
    zoom 0.65
image l_sa:
    "lil_sad"
    zoom 0.65
image l_su_sp:
    "lil_suprised_speaking"
    zoom 0.65
image l_su:
    "lil_suprised"
    zoom 0.65
image l_sy:
    "lil_sympathetic"
    zoom 0.65



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