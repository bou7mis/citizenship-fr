import os
import subprocess
import shutil
from PIL import Image
from pypdf import PdfReader, PdfWriter

BASE_DIR = "/Users/ahmed/Personal/citizenship-fr"
PDF_PATH = os.path.join(BASE_DIR, "LIVRET DU CITOYEN 2026.pdf")
IMG_DIR = os.path.join(BASE_DIR, "assets/images")
FC_IMG_DIR = os.path.join(BASE_DIR, "assets/images/flashcards")
DIST_FC_IMG_DIR = os.path.join(BASE_DIR, "dist/assets/images/flashcards")
SCRATCH_DIR = "/Users/ahmed/.gemini/antigravity-ide/brain/b139ad40-4e2c-470f-af7a-134ece919672/scratch"

os.makedirs(FC_IMG_DIR, exist_ok=True)
os.makedirs(DIST_FC_IMG_DIR, exist_ok=True)

reader = PdfReader(PDF_PATH)

def render_page_hires(pnum, target_h=1684):
    pdf_tmp = os.path.join(SCRATCH_DIR, f"page_{pnum}_tmp.pdf")
    png_tmp = os.path.join(SCRATCH_DIR, f"page_{pnum}_hires.png")
    if not os.path.exists(png_tmp):
        writer = PdfWriter()
        writer.add_page(reader.pages[pnum - 1])
        with open(pdf_tmp, "wb") as f:
            writer.write(f)
        subprocess.run(["sips", "-s", "format", "png", "-Z", str(target_h), pdf_tmp, "--out", png_tmp],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if os.path.exists(pdf_tmp):
            os.remove(pdf_tmp)
    return Image.open(png_tmp)

print("Starting precise high-res cropping from LIVRET DU CITOYEN 2026.pdf...")

# ================= PAGE 18 =================
# Total size: (1191, 1684)
p18 = render_page_hires(18)

# 1. Full Diagram: Responsables de l'État & Institutions
im_p18_full = p18.crop((70, 40, 1120, 1620))
im_p18_full.save(os.path.join(FC_IMG_DIR, "fc_responsables_etat.png"), optimize=True)
im_p18_full.save(os.path.join(FC_IMG_DIR, "fc_institutions.png"), optimize=True)
im_p18_full.save(os.path.join(FC_IMG_DIR, "fc_sieges_pouvoirs.png"), optimize=True)

# 2. Palais de l'Élysée (Président de la République box)
# PRÉSIDENT at y=616. Box starts ~580 to ~960, x=810 to 1130
im_elysee = p18.crop((810, 580, 1135, 965))
im_elysee.save(os.path.join(FC_IMG_DIR, "fc_palais_elysee.png"), optimize=True)

# 3. Assemblée Nationale (Palais Bourbon)
# ASSEMBLÉE at y=877. Box from ~850 to 1130, x=420 to 760
im_ass = p18.crop((420, 850, 760, 1135))
im_ass.save(os.path.join(FC_IMG_DIR, "fc_presidente_assemblee.png"), optimize=True)

# 4. Sénat (Palais du Luxembourg)
# SÉNAT at y=1161. Box from ~1140 to 1425, x=420 to 760
im_senat = p18.crop((420, 1140, 760, 1425))
im_senat.save(os.path.join(FC_IMG_DIR, "fc_president_senat.png"), optimize=True)


# ================= PAGE 17 =================
# Démocratie & Droit de vote (Section B: Le droit de vote, l'isoloir, l'urne)
p17 = render_page_hires(17)
im_democratie = p17.crop((60, 430, 1130, 1340))
im_democratie.save(os.path.join(FC_IMG_DIR, "fc_democratie.png"), optimize=True)


# ================= PAGE 38 =================
# Timeline Histoire de France
p38 = render_page_hires(38)
im_histoire = p38.crop((20, 380, 1170, 1590))
im_histoire.save(os.path.join(FC_IMG_DIR, "fc_histoire_france_timeline.png"), optimize=True)


# ================= PAGE 47 =================
# Présidents de la Ve République (full timeline)
p47 = render_page_hires(47)
im_presidents = p47.crop((20, 60, 1170, 1550))
im_presidents.save(os.path.join(FC_IMG_DIR, "fc_presidents_ve_republique.png"), optimize=True)


# ================= PAGE 46 =================
# Grandes réformes républicaines (Loi Veil, Abolition peine de mort, Mariage pour tous)
p46 = render_page_hires(46)
im_lois = p46.crop((200, 440, 1150, 1520))
im_lois.save(os.path.join(FC_IMG_DIR, "fc_lois_marquantes.png"), optimize=True)


# ================= PAGE 39 =================
# Rois, Reines, Philosophes des Lumières
p39 = render_page_hires(39)

# Lumières (Voltaire gravure + texte)
im_lumieres = p39.crop((310, 1220, 1150, 1620))
im_lumieres.save(os.path.join(FC_IMG_DIR, "fc_philosophes_lumieres.png"), optimize=True)

# Rois (Henri IV + Louis XIV)
im_rois = p39.crop((200, 600, 1150, 1215))
im_rois.save(os.path.join(FC_IMG_DIR, "fc_rois_francais.png"), optimize=True)

# Reines / Femmes célèbres (Jeanne d'Arc gravure 1858)
im_reines = p39.crop((200, 190, 1150, 580))
im_reines.save(os.path.join(FC_IMG_DIR, "fc_reines_france.png"), optimize=True)


# ================= PAGE 51 =================
# Montagnes & Fleuves
p51 = render_page_hires(51)

# Montagnes (Mont-Blanc photo + Alpes, Pyrénées, Massif central)
im_montagnes = p51.crop((60, 250, 1130, 675))
im_montagnes.save(os.path.join(FC_IMG_DIR, "fc_montagnes_france.png"), optimize=True)

# Fleuves (La Garonne traversant Toulouse + Loire, Seine, Rhône, Rhin)
im_fleuves = p51.crop((60, 680, 1130, 1205))
im_fleuves.save(os.path.join(FC_IMG_DIR, "fc_fleuves_france.png"), optimize=True)


# ================= PAGE 23 =================
# Siège de l'UE à Bruxelles
p23 = render_page_hires(23)
im_bruxelles = p23.crop((60, 750, 1130, 1260))
im_bruxelles.save(os.path.join(FC_IMG_DIR, "fc_siege_ue_bruxelles.png"), optimize=True)


# ================= PAGE 42 =================
# Victor Hugo (Les Misérables, Notre-Dame de Paris)
p42 = render_page_hires(42)
im_hugo = p42.crop((200, 850, 1150, 1070))
im_hugo.save(os.path.join(FC_IMG_DIR, "fc_litteraires_francais.png"), optimize=True)
im_hugo.save(os.path.join(FC_IMG_DIR, "fc_alexandre_dumas.png"), optimize=True)


# ================= DIRECT ASSETS LINKING =================
existing_mappings = {
    "carte_europe.png": "fc_frontieres_france.png",
    "p7_Im98.png": "fc_devise_republique.png",
    "p11_Image1386.png": "fc_laicite.png",
    "p35_Image5659.png": "fc_droits_devoirs.png",
    "marianne.png": "fc_marianne.png",
    "p21_Image2893.png": "fc_regions_france.png",
    "drapeau_francais.png": "fc_drapeau_francais.png",
    "p54_Image10504.png": "fc_monuments_parisiens.png",
    "p60_Image11657.png": "fc_plats_typiques.png",
    "p22_Image2978.png": "fc_symboles_europe.png",
    "p44_Image7806.png": "fc_debarquement_normandie.png",
}

for src_name, dst_name in existing_mappings.items():
    src_path = os.path.join(IMG_DIR, src_name)
    dst_path = os.path.join(FC_IMG_DIR, dst_name)
    im = Image.open(src_path)
    im.save(dst_path, optimize=True)

# Symboles de la France composite (Drapeau + Marianne)
im_drapeau = Image.open(os.path.join(IMG_DIR, "drapeau_francais.png"))
im_marianne = Image.open(os.path.join(IMG_DIR, "marianne.png"))
target_h = 350
w_dr = int(im_drapeau.width * (target_h / im_drapeau.height))
w_mar = int(im_marianne.width * (target_h / im_marianne.height))
dr_resized = im_drapeau.resize((w_dr, target_h), Image.Resampling.LANCZOS)
mar_resized = im_marianne.resize((w_mar, target_h), Image.Resampling.LANCZOS)
comp = Image.new("RGB", (w_dr + w_mar + 20, target_h), (255, 255, 255))
comp.paste(dr_resized, (0, 0))
comp.paste(mar_resized, (w_dr + 20, 0))
comp.save(os.path.join(FC_IMG_DIR, "fc_symboles_france.png"), optimize=True)

# Sync all to dist
for f in os.listdir(FC_IMG_DIR):
    shutil.copy2(os.path.join(FC_IMG_DIR, f), os.path.join(DIST_FC_IMG_DIR, f))

print("All flashcard images cropped and synchronized successfully!")
