init python:
    import random
    nonunicode = "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž"
    h_cg_available = persistent.h_scene
    def glitchtext(length):
        output = ""
        for x in range(length):
            output += random.choice(nonunicode)
        return output
    if h_cg_available == 1:
        avail = "Disponible"
    else:
        avail = "No Disp."
    if persistent.kt_kill == False:
        gtext = glitchtext(6)
    elif persistent.kt_kill == True:
        gtext = "Kotonoha"
    elif persistent.kt_kill == True and persistent.ending[2] == True:
        gtext = "Kotonoha"
    if persistent.ending[2] == False:
        avail_b = "No Disp."
    else:
        avail_b = "Disponible"
    def MaxScale(img, minwidth=config.screen_width, minheight=config.screen_height):
        currwidth, currheight = renpy.image_size(img)
        xscale = float(minwidth) / currwidth
        yscale = float(minheight) / currheight

        if xscale > yscale:
            maxscale = xscale
        else:
            maxscale = yscale

        return im.FactorScale(img, maxscale, maxscale)

    def MinScale(img, maxwidth=config.screen_width, maxheight=config.screen_height):
        currwidth, currheight = renpy.image_size(img)
        xscale = float(maxwidth) / currwidth
        yscale = float(maxheight) / currheight

        if xscale < yscale:
            minscale = xscale
        else:
            minscale = yscale

        return im.FactorScale(img, minscale, minscale)

    maxnumx = 2
    maxnumy = 2
    maxthumbx = config.screen_width / (maxnumx + 1)
    maxthumby = config.screen_height / (maxnumy + 1)
    maxperpage = maxnumx * maxnumy
    gallery_page = 0
    closeup_page = 0

    class GalleryItem:
        def __init__(self, name, images, thumb, locked="locked"):
            self.name = name
            self.images = images
            self.thumb = thumb
            self.locked = locked
            self.refresh_lock()

        def num_images(self):
            return len(self.images)

        def refresh_lock(self):
            self.num_unlocked = 0
            lockme = False
            for img in self.images:
                if not renpy.seen_image(img):
                    lockme = True
                else:
                    self.num_unlocked += 1
            self.is_locked = lockme


    gallery_items = []
    gallery_items.append(GalleryItem("Sayu-nara", ["y_d1", "y_d2"], "tb2"))
    gallery_items.append(GalleryItem("Regreso de\nMonika", ["mroom", "m_cg2", "m_cg3", "m_cg4", "m_cg5", "m_cg6"], "tb1"))
    gallery_items.append(GalleryItem("Ya Está...", ["mc_kt_cg"], "tb4"))
    gallery_items.append(GalleryItem("Charla con Nat", ["n_cg1_1", "n_cg1_2", "n_cg1_3", "n_cg1_4"], "tb3"))
    gallery_items.append(GalleryItem("El lamento de\nNatsuki", ["m_n_cg_1", "m_n_cg_2", "m_n_cg_3_a", "m_n_cg_3_b"], "tb5"))
    gallery_items.append(GalleryItem("Exceso de Confianza", ["mi_desk1a", "mi_desk1b"], "tb11"))
    gallery_items.append(GalleryItem("Una Linda Cena", ["m_d2", "m_d2a", "m_d2b"], "tb7"))
    gallery_items.append(GalleryItem("A la Playa", ["beach1a", "beach1b"], "tb15"))
    gallery_items.append(GalleryItem("Nuestro Momento", ["mc_m_ice1a", "mc_m_ice1b", "mc_m_ice1c", "mc_m_ice1d", "mc_m_ice1e"], "tb8"))
    gallery_items.append(GalleryItem("Culminación del Amor\n(" + avail + ")", ["mc_m_sx", "mc_m_sxb"], "tb14"))
    gallery_items.append(GalleryItem("Oh no...", ["mi_gun", "mi_gunb"], "tb16"))
    gallery_items.append(GalleryItem("Mio, ¿estás bien?", ["mi_kn1a", "mi_kn1b"], "tb9"))
    gallery_items.append(GalleryItem("Su Último Adiós", ["kt_kill_letter"], "tb17"))
    gallery_items.append(GalleryItem("Después del Tiroteo", ["sayo_sad"], "tb13"))
    gallery_items.append(GalleryItem("Adiós, " + gtext, ["kt_kill_cg"], "tb10"))
    gallery_items.append(GalleryItem("Nuevo Inicio", ["m_mc_ks"], "tb19"))
    gallery_items.append(GalleryItem("Al fin juntas...\nDe nuevo", ["sec_ed"], "tb12"))
    gallery_items.append(GalleryItem("Belleza Sinfónica\n(" + avail_b + ")", ["m_kt_duet"], "tb18"))
    gallery_items.append(GalleryItem("Sólo Kotonoha", ["j_kt_1a", "j_kt_1b", "j_kt_1c", "j_kt_1ca", "j_kt_2","j_kt_3", "j_kt_3a"], "tb6"))
