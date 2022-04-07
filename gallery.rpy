style gallery_label_text:
    font "gui/font/RifficFree-Bold.ttf"
    size gui.title_text_size
    color "#6debab"
    outlines [(6, "#7dc4df", 0, 0), (3, "#7dc4df", 2, 2)]
    yalign 0.5
image gallery_str:
  Text("Galería", style="gallery_label_text")
  xalign 0.5 yalign 0.5
image gallery_navigation:
  "mod_assets/game_menu_b.png"
  truecenter

screen gallery:

    tag menu
    if persistent.timeday == "normal":
        add "menu_bg"
        add "gallery_navigation"
    elif persistent.timeday == "afternoon":
        add "menu_bg_an"
        add "game_menu_b_an"
    else:
        add "menu_bg_n"
        add "game_menu_b_n"
    add "gallery_str"
    #add "menu_nav"
    #add "m_sticker_menu_b"

    $ start = gallery_page * maxperpage
    $ end = min(start + maxperpage - 1, len(gallery_items) - 1)
    
    # los cuadros del menu de la galeria
    grid maxnumx maxnumy:
        xfill True
        yfill True

        for i in range(start, end + 1):
            $ gallery_items[i].refresh_lock()
            if gallery_items[i].is_locked:
                add gallery_items[i].locked:
                    xalign 0.5
                    yalign 0.5
            else:
                imagebutton idle gallery_items[i].thumb:
                    action Show("gallery_closeup", dissolve, gallery_items[i].images)
                    xalign 0.5
                    yalign 0.5
        for i in range(end - start + 1,  maxperpage):
           null

    grid maxnumx maxnumy:
        xfill True
        yfill True

        for i in range(start, end + 1):
            hbox:
                spacing maxthumbx - 70
                xalign 0.5
                yalign 0.1
                $ total = gallery_items[i].num_images()
                $ partial = gallery_items[i].num_unlocked
                text gallery_items[i].name
                text "[partial]/[total]"
        for i in range(end - start + 1, maxperpage):
            null


    if gallery_page > 0:
        textbutton "Anterior":
            action SetVariable("gallery_page", gallery_page - 1)
            xalign 0.5
            yalign 0.23
            style "return_button"
    if (gallery_page + 1) * maxperpage < len(gallery_items):
        textbutton "Siguiente":
            action SetVariable("gallery_page", gallery_page + 1)
            xalign 0.5
            yalign 0.8
            style "return_button"
    # boton de return
    textbutton "Regresar":
        action [Return()] xalign 0.5 yalign 0.98
        style "return_button"
screen gallery_closeup(images):
    add "dark" at truecenter
    add "dark" at truecenter
    add "dark" at truecenter
    add "dark" at truecenter
    add images[closeup_page] at truecenter

    if closeup_page >= 0:
        textbutton "Volver a\nálbumes":
            action [
                SetVariable("closeup_page", 0), 
                Hide("gallery_closeup", dissolve)
            ]
            xalign 0.7
            yalign 0.98
            style "return_button"
    if closeup_page > 0:
        textbutton "Anterior":
            action SetVariable("closeup_page", closeup_page - 1)
            xalign 0.1
            yalign 0.98
            #background "menu_bg"
            style "return_button"
    if closeup_page < len(images) - 1:
        textbutton "Siguiente":
            action SetVariable("closeup_page", closeup_page + 1)
            xalign 0.9
            yalign 0.98
            #background "menu_bg"
            style "return_button"
    textbutton "Regresar":
        action [
            SetVariable("closeup_page", 0), 
            Hide("gallery_closeup", dissolve),
            ShowMenu('galleries_window')
        ]
        xalign 0.5
        yalign 0.98
        style "return_button"