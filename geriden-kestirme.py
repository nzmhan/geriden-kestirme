# NAZIM HAN TARAFINDAN PROGRAMLANMISTIR

import math
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

def get_download_url(file_id):
    return f'https://drive.google.com/uc?export=download&id={file_id}'

def extract_file_id(drive_url):
    file_id = drive_url.split('/d/')[1].split('/')[0]
    return file_id

def download_image_from_drive(drive_url):
    file_id = extract_file_id(drive_url)
    dwn_url = get_download_url(file_id)
    response = requests.get(dwn_url)
    return Image.open(BytesIO(response.content))



def hesapla():
    try:
        # Değerleri al
        a = float(entry_alfa.get())
        b = float(entry_beta.get())
        XA = float(entry_XA.get())
        YA = float(entry_YA.get())
        XB = float(entry_XB.get())
        YB = float(entry_YB.get())
        XC = float(entry_XC.get())
        YC = float(entry_YC.get())

        # SAC hesaplama
        SAC = math.sqrt((XC - XA)**2 + (YC - YA)**2)

        # Açıları radian cinsine dönüştür
        a_rad = a * (math.pi / 200)
        b_rad = b * (math.pi / 200)
        c_rad = (200 - a - b) * (math.pi / 200)

        # tAC ve tCA hesaplama
        tAC = (2 * math.atan((YC - YA) / ((XC - XA) - SAC))) * (200 / math.pi) + 200
        tCA = (2 * math.atan((YA - YC) / ((XA - XC) - SAC))) * (200 / math.pi) + 200

        # SAQ ve SCQ hesaplama
        SAQ = SAC * math.sin(a_rad) / math.sin(c_rad)
        SCQ = SAC * math.sin(b_rad) / math.sin(c_rad)

        # tAQ ve tCQ hesaplama
        tAQ = tAC - b
        tCQ = tCA + a

        # Açıları radian cinsine dönüştür
        tAQ_rad = tAQ * (math.pi / 200)
        tCQ_rad = tCQ * (math.pi / 200)

        # Q noktasının koordinatlarını bulma
        XQ1 = XA + SAQ * math.cos(tAQ_rad)
        XQ2 = XC + SCQ * math.cos(tCQ_rad)
        YQ1 = YA + SAQ * math.sin(tAQ_rad)
        YQ2 = YC + SCQ * math.sin(tCQ_rad)
        XQ = (XQ1 + XQ2) / 2
        YQ = (YQ1 + YQ2) / 2

        # SQB ve SQC hesaplama
        SQB = math.sqrt((XB - XQ)**2 + (YB - YQ)**2)
        SQC = math.sqrt((XC - XQ)**2 + (YC - YQ)**2)

        # tQB ve tQC hesaplama
        tQB = (2 * math.atan((YB - YQ) / ((XB - XQ) - SQB))) * (200 / math.pi) + 200
        tQC = (2 * math.atan((YC - YQ) / ((XC - XQ) - SQC))) * (200 / math.pi) + 200

        # d1 ve d2 hesaplama
        d1 = tQB - tAQ
        d2 = tCQ - tQC

        # d hesaplama
        d = d1 + d2

        # SAP ve SCP hesaplama
        SAP = SAC * math.sin(d1 * (math.pi / 200)) / math.sin(d * (math.pi / 200))
        SCP = SAC * math.sin(d2 * (math.pi / 200)) / math.sin(d * (math.pi / 200))

        # tAP ve tCP hesaplama
        tAP = tAC - d1
        tCP = tCA + d2

        # P noktasının koordinatlarını bulma
        XP1 = XA + SAP * math.cos(tAP * (math.pi / 200))
        XP2 = XC + SCP * math.cos(tCP * (math.pi / 200))
        YP1 = YA + SAP * math.sin(tAP * (math.pi / 200))
        YP2 = YC + SCP * math.sin(tCP * (math.pi / 200))
        XP = (XP1 + XP2) / 2
        YP = (YP1 + YP2) / 2

        # Sonuçları göster
        result_label.config(text="P Noktasının Koordinatları: ({:.3f} m, {:.3f} m)".format(XP, YP))

    except Exception as e:
        result_label.config(text="Hata: " + str(e))

def show_intermediate_steps():
    try:
        result_label.config(text="")  # Önce temizle

        # Değerleri al
        a = float(entry_alfa.get())
        b = float(entry_beta.get())
        XA = float(entry_XA.get())
        YA = float(entry_YA.get())
        XB = float(entry_XB.get())
        YB = float(entry_YB.get())
        XC = float(entry_XC.get())
        YC = float(entry_YC.get())

        # SAC hesaplama
        SAC = math.sqrt((XC - XA)**2 + (YC - YA)**2)
        result_text = "# SAC hesaplama: SAC = {:.3f} m\n".format(SAC)
        
        # tAC ve tCA hesaplama
        tAC = (2 * math.atan((YC - YA) / ((XC - XA) - SAC))) * (200 / math.pi) + 200
        tCA = (2 * math.atan((YA - YC) / ((XA - XC) - SAC))) * (200 / math.pi) + 200
        result_text += "# tAC hesaplama: tAC = {:.3f}\n".format(tAC)
        result_text += "# tCA hesaplama: tCA = {:.3f}\n".format(tCA)

        # Açıları radian cinsine dönüştür
        a_rad = a * (math.pi / 200)
        b_rad = b * (math.pi / 200)
        c_rad = (200 - a - b) * (math.pi / 200)
        result_text += "# Açıları radian cinsine dönüştür: a_rad = {:.3f}, b_rad = {:.3f}, c_rad = {:.3f}\n".format(a_rad, b_rad, c_rad)

        # SAQ ve SCQ hesaplama
        SAQ = SAC * math.sin(a_rad) / math.sin(c_rad)
        SCQ = SAC * math.sin(b_rad) / math.sin(c_rad)
        result_text += "# SAQ hesaplama: SAQ = {:.3f} m\n".format(SAQ)
        result_text += "# SCQ hesaplama: SCQ = {:.3f} m\n".format(SCQ)

        # tAQ ve tCQ hesaplama
        tAQ = tAC - b
        tCQ = tCA + a
        result_text += "# tAQ hesaplama: tAQ = {:.3f}\n".format(tAQ)
        result_text += "# tCQ hesaplama: tCQ = {:.3f}\n".format(tCQ)

        # Açıları radian cinsine dönüştür
        tAQ_rad = tAQ * (math.pi / 200)
        tCQ_rad = tCQ * (math.pi / 200)
        result_text += "# Açıları radian cinsine dönüştür: tAQ_rad = {:.3f}, tCQ_rad = {:.3f}\n".format(tAQ_rad, tCQ_rad)

        # Q noktasının koordinatlarını bulma
        XQ1 = XA + SAQ * math.cos(tAQ_rad)
        XQ2 = XC + SCQ * math.cos(tCQ_rad)
        YQ1 = YA + SAQ * math.sin(tAQ_rad)
        YQ2 = YC + SCQ * math.sin(tCQ_rad)
        XQ = (XQ1 + XQ2) / 2
        YQ = (YQ1 + YQ2) / 2
        result_text += "# Koordinatlar: XQ = {:.3f} m, YQ = {:.3f} m\n".format(XQ, YQ)

        # SQB ve SQC hesaplama
        SQB = math.sqrt((XB - XQ)**2 + (YB - YQ)**2)
        SQC = math.sqrt((XC - XQ)**2 + (YC - YQ)**2)
        result_text += "# SQB hesaplama: SQB = {:.3f} m\n".format(SQB)
        result_text += "# SQC hesaplama: SQC = {:.3f} m\n".format(SQC)

        # tQB ve tQC hesaplama
        tQB = (2 * math.atan((YB - YQ) / ((XB - XQ) - SQB))) * (200 / math.pi) + 200
        tQC = (2 * math.atan((YC - YQ) / ((XC - XQ) - SQC))) * (200 / math.pi) + 200
        result_text += "# tQB hesaplama: tQB = {:.3f}\n".format(tQB)
        result_text += "# tQC hesaplama: tQC = {:.3f}\n".format(tQC)

        # d1 ve d2 hesaplama
        d1 = tQB - tAQ
        d2 = tCQ - tQC
        result_text += "# d1 hesaplama: d1 = {:.3f}\n".format(d1)
        result_text += "# d2 hesaplama: d2 = {:.3f}\n".format(d2)

        # d hesaplama
        d = d1 + d2
        result_text += "# d hesaplama: d = {:.3f}\n".format(d)

        # SAP ve SCP hesaplama
        SAP = SAC * math.sin(d1 * (math.pi / 200)) / math.sin(d * (math.pi / 200))
        SCP = SAC * math.sin(d2 * (math.pi / 200)) / math.sin(d * (math.pi / 200))
        result_text += "# SAP hesaplama: SAP = {:.3f} m\n".format(SAP)
        result_text += "# SCP hesaplama: SCP = {:.3f} m\n".format(SCP)

        # tAP ve tCP hesaplama
        tAP = tAC - d1
        tCP = tCA + d2
        result_text += "# tAP hesaplama: tAP = {:.3f}\n".format(tAP)
        result_text += "# tCP hesaplama: tCP = {:.3f}\n".format(tCP)

        # P noktasının koordinatlarını bulma
        XP1 = XA + SAP * math.cos(tAP * (math.pi / 200))
        XP2 = XC + SCP * math.cos(tCP * (math.pi / 200))
        YP1 = YA + SAP * math.sin(tAP * (math.pi / 200))
        YP2 = YC + SCP * math.sin(tCP * (math.pi / 200))
        XP = (XP1 + XP2) / 2
        YP = (YP1 + YP2) / 2
        result_text += "# P Noktasının Koordinatları: ({:.3f} m, {:.3f} m)".format(XP, YP)

        result_label.config(text=result_text)

    except Exception as e:
        result_label.config(text="Hata: " + str(e))



# Ana pencere oluşturma
root = tk.Tk()
root.title("Geriden Kestirme Uygulaması")

# A Noktası için girdi alanı
frame_a = tk.LabelFrame(root, text="A Noktası")
frame_a.grid(row=0, column=0, padx=10, pady=10)

tk.Label(frame_a, text="XA değeri:").grid(row=0, column=0)
entry_XA = tk.Entry(frame_a)
entry_XA.grid(row=0, column=1)

tk.Label(frame_a, text="YA değeri:").grid(row=1, column=0)
entry_YA = tk.Entry(frame_a)
entry_YA.grid(row=1, column=1)

# B Noktası için girdi alanı
frame_b = tk.LabelFrame(root, text="B Noktası")
frame_b.grid(row=0, column=1, padx=10, pady=10)

tk.Label(frame_b, text="XB değeri:").grid(row=0, column=0)
entry_XB = tk.Entry(frame_b)
entry_XB.grid(row=0, column=1)

tk.Label(frame_b, text="YB değeri:").grid(row=1, column=0)
entry_YB = tk.Entry(frame_b)
entry_YB.grid(row=1, column=1)

# A noktası başlığı altında C noktası başlığı tablosu
table_frame_a = tk.LabelFrame(root, text="C Noktası")
table_frame_a.grid(row=2, column=0, padx=10, pady=10)

tk.Label(table_frame_a, text="XC değeri:").grid(row=0, column=0)
entry_XC = tk.Entry(table_frame_a)
entry_XC.grid(row=0, column=1)

tk.Label(table_frame_a, text="YC değeri:").grid(row=1, column=0)
entry_YC = tk.Entry(table_frame_a)
entry_YC.grid(row=1, column=1)

# B noktası başlığı altında açı değerleri tablosu
table_frame_b = tk.LabelFrame(root, text="Açı Değerleri")
table_frame_b.grid(row=2, column=1, padx=10, pady=10)

tk.Label(table_frame_b, text="Alfa değeri:").grid(row=0, column=0)
entry_alfa = tk.Entry(table_frame_b)
entry_alfa.grid(row=0, column=1)

tk.Label(table_frame_b, text="Beta değeri:").grid(row=1, column=0)
entry_beta = tk.Entry(table_frame_b)
entry_beta.grid(row=1, column=1)

# Hesapla düğmesi
calculate_button = tk.Button(root, text="Hesapla", command=hesapla, bg="lightblue")
calculate_button.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

# Ara adımları göster düğmesi
show_steps_button = tk.Button(root, text="Ara Adımları Göster", command=show_intermediate_steps, bg="lightblue")
show_steps_button.grid(row=3, column=1, padx=20, pady=20, sticky="ew")

# Google Drive'dan fotoğrafı indir ve göster
drive_url = 'https://drive.google.com/file/d/1WEv2_b-L3UYUpAL2BI1TobYc24WUkSYa/view?usp=sharing'
image = download_image_from_drive(drive_url)
photo = ImageTk.PhotoImage(image)

# Fotoğrafı bir etiket içinde göster
image_label = tk.Label(root, image=photo)
image_label.grid(row=0, column=3, rowspan=4, padx=10, pady=10)

# Sonuç etiketi
result_label = tk.Label(root, text="", justify="left", padx=10, pady=10, bg="#F5F5DC", font=("Helvetica", 12))
result_label.grid(row=4, column=0, columnspan=4, sticky="ew")

# Ana döngüyü başlat
root.mainloop()

