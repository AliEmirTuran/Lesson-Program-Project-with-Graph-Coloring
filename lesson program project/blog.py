#Projemizin flask arayüzünü tasarlamadan önce Udemy platformu üzerinden Mustafa Murat Coşkun Öğretmenin python kursunun flask famework kısmını deatylı inceledik.
from ast import Pass, Return, keyword
from calendar import c
from os import error
from symbol import flow_stmt
from turtle import title
from unittest import result
from django.shortcuts import render
from flask import Flask,render_template,flash,redirect,url_for,request
from flask_mysqldb import MySQL,cursors
from sympy import content, false, true
from wtforms import Form,StringField,TextAreaField,PasswordField,SelectField,IntegerField
from passlib.hash import sha256_crypt
import mysql.connector
import pymysql.cursors
import hashlib
from functools import wraps
from collections import defaultdict
import networkx as nx
import matplotlib as plt

app=Flask(__name__)
app.secret_key="ders_programi_projesi"

#Veritabanı bağlantı bilgileri
db = pymysql.connect(host='localhost',
                             user='root',
                             password='111234Aet!',
                             db='ders_programi_projesi',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


#Öğretmen Ekleme Formu
class teacherForm(Form):
     choices = [('1', 'Türkçe'), ('2', 'Matematik'), ('3', 'Hayat Bilgisi'),('4', 'Görsel Sanatlar'),('5', 'Müzik'),('6', 'Beden Eğitimi')]
     teacherName=StringField('İsim')
     teacherSurname=StringField('Soyisim')
     teacherBranch=SelectField('Branşı',choices=choices)

#Kısıt Ekleme Formu
class kısıtForm(Form):
     teacher_id=IntegerField('Teacher id')
     choices1=[('1','Pazartesi'),('2','Salı'),('3','Çarşamba'),('4','Perşembe'),('5','Cuma')]
     day_constraint=SelectField('İzin Günü',choices=choices1)
     choices2=[('1','09:00-09:40'),('2','09:50-10:30'),('3','10:40-11:20'),('4','12:20-13:00'),('5','13:10-13:50'),('6','14:00-14:40')]
     time_around=SelectField('İzin Saati',choices=choices2)
     
#Ders Programı Oluşturma Çizge Renklendirme algoritması


derssaati = ['1.Ders 9.00-9.40', '2.Ders 10.00-10.40', '3.Ders 11.00-11.40', '4.Ders 13.00-13.40', '5.Ders 14.00-14.40', '6.Ders 15.00-15.40']
günler = ['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma']

# Gün adlarına uygun anahtarlar kullanarak graph sözlüğü oluşturma
graph = {
    'Pazartesi': ['1', '2', '3', '4', '5', '6', '7', '13', '19'],
    'Salı': ['8', '9', '10', '11', '12', '1', '14', '20'],
    'Çarşamba': ['15', '16', '17', '18', '1', '7', '13', '19'],
    'Perşembe': ['22', '23', '24', '2', '8', '14', '20'],
    'Cuma': ['3', '9', '15', '21', '4', '10', '16', '22'],
}

# Gün adlarına uygun düğümler sözlüğü
dügümler = {
    "1": {"class": "1-A", "lesson": "Türkçe"},
    "2": {"class": "1-A", "lesson": "Matematik"},
    "3": {"class": "1-A", "lesson": "Hayat Bilgisi"},
    "4": {"class": "1-A", "lesson": "Resim"},
    "5": {"class": "1-A", "lesson": "Müzik"},
    "6": {"class": "1-A", "lesson": "Beden"},
    "7": {"class": "2-A", "lesson": "Türkçe"},
    "8": {"class": "2-A", "lesson": "Matematik"},
    "9": {"class": "2-A", "lesson": "Hayat Bilgisi"},
    "10": {"class": "2-A", "lesson": "Resim"},
    "11": {"class": "2-A", "lesson": "Müzik"},
    "12": {"class": "2-A", "lesson": "Beden"},
    "13": {"class": "3-A", "lesson": "Türkçe"},
    "14": {"class": "3-A", "lesson": "Matematik"},
    "15": {"class": "3-A", "lesson": "Hayat Bilgisi"},
    "16": {"class": "3-A", "lesson": "Resim"},
    "17": {"class": "3-A", "lesson": "Müzik"},
    "18": {"class": "3-A", "lesson": "Beden"},
    "19": {"class": "4-A", "lesson": "Türkçe"},
    "20": {"class": "4-A", "lesson": "Matematik"},
    "21": {"class": "4-A", "lesson": "Hayat Bilgisi"},
    "22": {"class": "4-A", "lesson": "Resim"},
    "23": {"class": "4-A", "lesson": "Müzik"},
    "24": {"class": "4-A", "lesson": "Beden"},
}

# Derslere farklı renkler atama
renkler = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']

# Renk ve ders saatlerini eşleştiren sözlük
renk_ders_saatleri = {renk: derssaati[i % len(derssaati)] for i, renk in enumerate(renkler)}

# Düğümlere farklı renkler atama
renk_atama = {ders: renkler[i % len(renkler)] for i, ders in enumerate(dügümler)}

# Düğümleri renklere göre uygun ders saatine atama
derssaat = {ders: renk_ders_saatleri[renk_atama[ders]] for ders in dügümler}

# Renklendirme fonksiyonu
#Kodun bu kısmını yazarken çeşitli yapay zeka araçlarından ve raporda bulunan çeşitli makalelerden yardım aldık.
def colour_vertices(graph):
    colour_result = {}  # Ders saatlerini tutacak
    for gun, ders_listesi in graph.items():
        for ders_saat in derssaati:
            ders = dügümler[ders_listesi[int(ders_saat[0])]]["lesson"]  
            renk = renk_atama.get(ders, 'white')  # Dersi renk_atama'dan al, eğer yoksa beyaz kullan 
            if gun not in colour_result:
                colour_result[gun] = []
            colour_result[gun].append((ders, renk, ders_saat))
    return colour_result






    
# Ana Sayfa
@app.route("/")
def index():
    return render_template("index.html")
#Dersler
@app.route("/lessons")
def lessons():
    imlec=db.cursor()
    sorgu="SELECT * FROM lessons "
    result=imlec.execute(sorgu)
    if result>0:
        lessons=imlec.fetchall()
        
        return render_template("lessons.html",lessons=lessons)
    else:
        flash("Veritabanında böyle bir bilgi bulunmamaktadır...","danger")
        return render_template("lessons.html")

#Öğretmenler
@app.route("/teachers")
def teachers():
    imlec=db.cursor()
    sorgu="Select teacher.teacher_name,teacher.teacher_surname,lessons.lesson_name from teacher inner join lessons on teacher.teacher_branch= lessons.lesson_id" # Buraya bir inner hoin ile ders isimlerini döndürmeyi dene!!!!!!!! veya 2. bi sorgu yazıp oradan veriyi çekmeyi dene!!!!!!!!
    result=imlec.execute(sorgu)
    if result>0:
        teachers=imlec.fetchall()
        
        return render_template("teachers.html",teachers=teachers)
    else:
        flash("Veritabanında böyle bir bilgi bulunmamaktadır...","danger")
        return render_template("teachers.html")
    
#Öğretmen Ekleme
@app.route("/teacher-add",methods=['GET','POST']) 
def teacheradd():
    form=teacherForm(request.form)
    if request.method =="POST":
       teachername=form.teacherName.data
       teachersurname=form.teacherSurname.data
       teacherbranch=form.teacherBranch.data
       
       imlec=db.cursor()
       sorgu="Insert into teacher(teacher_name,teacher_surname,teacher_branch) VALUES (%s,%s,%s)"
       imlec.execute(sorgu,(teachername,teachersurname, teacherbranch))
       db.commit()
       flash("Öğretmen Başarı ile Kaydedildi...","success")
       return redirect(url_for("teachers"))
    else:
       return render_template("teacheradd.html",form=form)

#Kısıtlar
@app.route("/kisit")
def kisitlar():
    imlec=db.cursor()
    sorgu = "SELECT * FROM (kısıtlar AS k INNER JOIN teacher AS t ON k.teacher_id = t.teacher_id) INNER JOIN lessons AS l ON t.teacher_branch = l.lesson_id INNER JOIN days as d ON k.day_constraint =d.day_id INNER JOIN lesson_time as lt ON k.time_constraint =lt.lesson_time_id"

    result=imlec.execute(sorgu)
    if result>0:
        kisit=imlec.fetchall()
        return render_template("kısıtlar.html",kisit=kisit)
    else:
        flash("Veritabanında herhangi bir kısıt bulunmamaktadır...","danger")
        return render_template("index.html")
    
#Kısıt Ekleme
@app.route("/kisit-add",methods=['GET','POST']) 
def kisitadd():
    form=kısıtForm(request.form)
    if request.method =="POST":
       teacher_id=form.teacher_id.data
       constraint_day=form.day_constraint.data
       around_time=form.time_around.data
       
       
       imlec=db.cursor()
       sorgu="Insert into kısıtlar(teacher_id,day_constraint,time_constraint) VALUES (%s,%s,%s)"
       imlec.execute(sorgu,(teacher_id,constraint_day, around_time))
       db.commit()
       flash("Kısıt Başarı ile Kaydedildi...","success")
       return redirect(url_for("kisitlar"))
    else:
       return render_template("kısıtadd.html",form=form)
   
#Ders Programı Sayfası
@app.route("/program")
def program():
    colour_result = colour_vertices(graph)
    return render_template('lessonprogram.html', renk_atama=renk_atama, günler=günler, derssaati=derssaati, colour_result=colour_result,graph=graph,dügümler=dügümler)




if __name__ =="__main__":
    app.run(debug=True)
