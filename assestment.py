
"""
Assignment 2
Write a program to check student attendance. A student will not be allowed to sit an exam if his/her attendance is less than 75%. Example:

Input:

Class_held = 20

Student = [“Asnawi”, “Haaland”, “Hazard”, “Maudy Ayunan”,  “Marselino”, “Dembele”]

Class_attended = [18, 19, 10, 20, 17, 13]

Output:

Kehadiran asnawi lebih dari 75%, dapat mengikuti ujian cunin

Kehadiran hazard kurang dari 75%, tidak dapat mengikuti ujian cunin

Kehadiran dembele kurang dari 75%, tidak dapat mengikuti ujian cunin
"""

def pengecekan_kelulusan(absensi, siswa, kehadiran):
    cek = (kehadiran / absensi)*100
    if cek >= 75:
        return print(f"Kehadiran {siswa} lebih dari 75%, dapat mengikuti ujian chunin")
    else:
        return print(f"Kehadiran {siswa} kurang dari 75% tidak dapat mengikuti ujian chunin")
    
class_held = 20
student = ["Asnawi", "Haaland", "Hazard", "Maudy Ayunan", "Marcelino", "Dembele"]
class_attended = [18, 19, 10, 20, 17, 13]

for i in range (len(student)):
    siswa = student[i]
    kehadiran = class_attended[i]
    hasil = pengecekan_kelulusan(class_held, siswa, kehadiran)
    print(hasil)

            

                






