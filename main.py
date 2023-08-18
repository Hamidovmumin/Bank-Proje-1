from tkinter import*
from PIL import ImageTk,Image
from time import gmtime,strftime
from tkinter import messagebox
import time
import math

def Elave_et(master):
    file3 = open(str(m) + '.txt', 'r')
    data3= file3.read().splitlines()
    n = data3[1]
    n1 = int(n[21::])
    msg_box3=messagebox.askquestion('Diqqət!','Balansınıza '+str(en2.get()) +'$ əlavə etmək isteyirsiz?',icon='warning')
    if (msg_box3=='yes'):
        elave_et= int(n1) + int(en2.get())
    else:
        elave_et = n1
    file3.close()

    file4 = open(str(m) + '.txt', 'w')
    file4.write('Adiniz:' + str(ad) + "\n")
    file4.write('Banka qoyulan mebleg:' + str(elave_et) + "\n")
    file4.write('Pin kod:' + str(pin_kod) + '\n')
    file4.write('Hesab nomreniz:' + str(hesab_nomre2) + "\n")
    file4.close()
    p2=int(0)
    if(elave_et!=n1):
        file3 = open(str(m) + "-rec.txt", 'a+')
        file3.write(
            str(strftime("[%Y-%m-%d] [%H:%M:%S]  ", gmtime())) + "     " + str(p2) + "             " + str(en2.get()) + "              " + str(elave_et) + "\n")
        file3.close()

    master.destroy()

    Daxil_olan_sehife()

def geri_qayit_4(master):
    msg_box4 = messagebox.askquestion('Diqqət!','Səhifədən çıxmaq isteyirsiz?', icon='warning')
    if (msg_box4== 'yes'):
        master.destroy()
        Daxil_olan_sehife()

def Pul_elave_et(master):
    master.destroy()
    pencere6= Tk()
    pencere6.geometry('700x400')
    img9 = Image.open('Pul-2.png')
    img9_9 = img9.resize((700,350))
    img9= ImageTk.PhotoImage(img9_9)
    label20 = Label(pencere6,image=img9)
    label20.image = img9
    label20.place(x=0, y=50)

    frame5= Frame(pencere6, width=700, height=50, bg='red', bd=5)
    frame5.place(x=0, y=0)
    label21=Label(frame5,text='Banka xoş gəlmisiz ' +'\U0001F642',font=("Arial","20","bold"),bg='red',fg='yellow')
    label21.place(x=200, y=3)

    label22=Label(pencere6,text="Banka qoymaq istədiyiniz\nməbləği daxil edin!",font=("Arial","22","bold"),bg="white", fg="red")
    label22.place(x=310, y=70)

    global en2
    en2 = StringVar()
    en2 = Entry(pencere6,font=("Arial","15","bold"),bg="cyan", width=24, textvariable=en2,justify="center")
    en2.place(x=356, y=165)

    btn7=Button(pencere6,text='Pulu əlavə et',bg="yellow",fg="red",font=("Arial","13","bold"),width=12,command=lambda:Elave_et(pencere6))
    btn7.place(x=340,y=230)

    btn8=Button(pencere6,text='Ana menü',bg="yellow",fg="red",font=("Arial","13","bold"),width=12,command=lambda:geri_qayit_4(pencere6))
    btn8.place(x=510,y=230)

    label23 = Label(pencere6, text='© Синхронизация, 2023', font=("Arial", "13", "bold"), bg='white')
    label23.place(x=480, y=350)

def Pul_cix_2(master):
    file=open(str(m)+'.txt', 'r')
    data2=file.read().splitlines()
    k=data2[1]
    k1=int(k[21::])
    if(int(k1)<int(en1.get())):
        messagebox.showinfo('Xəta','Balansınızda kifayət qədər məbləğ yoxdur!')
        pul_cix = k1
    else:
        msg_box1=messagebox.askquestion('Diqqət!', 'Balansınızdan '+str(en1.get())+'$ çıxarmaq isteyirsiz?',icon='warning')
        if(msg_box1=='yes'):
            pul_cix=int(k1)-int(en1.get())
        else:
            pul_cix=k1
    file.close()

    file2=open(str(m)+'.txt', 'w')
    file2.write('Adiniz:' + str(ad) + "\n")
    file2.write('Banka qoyulan mebleg:' + str(pul_cix) + "\n")
    file2.write('Pin kod:' + str(pin_kod) + '\n')
    file2.write('Hesab nomreniz:' + str(hesab_nomre2) + "\n")
    file2.close()
    p1=int(0)
    if(pul_cix!=k1):
        file3 = open(str(m) + "-rec.txt", 'a+')
        file3.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ", gmtime())) + "     " +str(en1.get())+ "              " + str(p1) + "              " + str(pul_cix) + "\n")
        file3.close()

    master.destroy()

    Daxil_olan_sehife()

def geri_qayit_3(master):
    msg_box2 = messagebox.askquestion('Diqqət!','Səhifədən çıxmaq isteyirsiz?',icon='warning')
    if(msg_box2=='yes'):
        master.destroy()
        Daxil_olan_sehife()

def Pul_cix_1(master):
    master.destroy()
    pencere5=Tk()
    pencere5.geometry('700x400')
    img8 = Image.open('Pul-1.png')
    img8_8 = img8.resize((700, 400))
    img8 = ImageTk.PhotoImage(img8_8)
    label16 = Label(pencere5, image=img8)
    label16.image = img8
    label16.place(x=0, y=0)

    frame4=Frame(pencere5,width=700,height=50,bg='red',bd=5)
    frame4.place(x=0,y=0)
    label17=Label(frame4,text='Banka xoş gəlmisiz '+'\U0001F642',font=("Arial", "20", "bold"),bg='red',fg='yellow')
    label17.place(x=200,y=3)

    label18= Label(pencere5, text="Götürmək istədiyiniz\nməbləği daxil edin!", font=("Arial", "22", "bold"), bg="white", fg="red")
    label18.place(x=5, y=80)

    global en1
    en1=StringVar()
    en1=Entry(pencere5,font=("Arial", "15", "bold"),bg="cyan",width=24,textvariable=en1,justify="center")
    en1.place(x=5,y=180)

    btn5=Button(pencere5,text='Pulu çıxar',bg="yellow",fg="red",font=("Arial","13","bold"),width=12,command=lambda:Pul_cix_2(pencere5))
    btn5.place(x=5,y=250)

    btn6=Button(pencere5,text='Ana menü',bg="yellow",fg="red",font=("Arial","13","bold"),width=12,command=lambda:geri_qayit_3(pencere5))
    btn6.place(x=145, y=250)

    label19=Label(pencere5,text='© Синхронизация, 2023',font=("Arial","13","bold"),bg='white')
    label19.place(x=5,y=350)

def Daxil_olan_sehife():
    pencere4 = Tk()
    pencere4.geometry('700x500')
    pencere4.configure(background='white')

    img6=Image.open('person-1.png')
    img6_6=img6.resize((100,100))
    img6=ImageTk.PhotoImage(img6_6)
    label12=Label(pencere4,image=img6)
    label12.image=img6
    label12.grid(row=0,column=0)

    frame_esas=Frame(pencere4,width=600,height=102,background='red',bd=3,highlightcolor='blue')
    frame_esas.place(x=100,y=0)

    frame1=Frame(frame_esas,width=600,height=51,bg='yellow')
    frame1.place(x=0,y=0)
    label13=Label(frame1,text='BANKING SYSTEM',font=("Arial", "20", "bold"),bg='yellow')
    label13.place(x=165,y=9)
    global m
    m=int(b[15::])
    label13_1 = Label(frame1, text='Hesab nömrəniz: '+ str(m) ,font=("Arial", "8", "bold"),fg='red',bg='yellow')
    label13_1.place(x=425, y=16)

    frame2 = Frame(frame_esas, width=300,height=51, bg='blue')
    frame2.place(x=0,y=51)
    label14 = Label(frame2, text='Salam:'+a[7::]+'\U0001F642', font=("Arial", "20", "bold"), bg='blue')
    label14.place(x=10, y=5)

    frame3 = Frame(frame_esas, width=300,height=51, bg='green')
    frame3.place(x=300,y=51)
    file3 = open(str(hesab_nomre2) + '.txt', 'r')
    data3 = file3.read().splitlines()
    s=data3[1]
    label14 = Label(frame3, text='Balansınız:' + s[21::] + '\U0001F4B5', font=("Arial", "20", "bold"), bg='green')
    label14.place(x=5, y=8)

    img7 = Image.open('kapital-1.jpg')
    img7_7 = img7.resize((700, 100))
    img7 = ImageTk.PhotoImage(img7_7)
    label15 = Label(pencere4, image=img7)
    label15.image = img7
    label15.place(x=0,y=102)

    buton9=Button(pencere4,text='Pulu götür',bg="yellow",fg="red",font=("Arial","13","bold"),width=12,command=lambda:Pul_cix_1(pencere4))
    buton9.place(x=100,y=240)

    buton9_9=Button(pencere4,text='Pul əlavə et',bg="yellow",fg="red",font=("Arial","13","bold"),width=12,command=lambda:Pul_elave_et(pencere4))
    buton9_9.place(x=460, y=240)


    pencere4.mainloop()
#================================================== Daxil ol ==========================================================#
def check_log_in(master):
    f1_1 = open(str(entry2.get()) + '.txt', 'r')
    data = f1_1.read().splitlines()
    global a
    global b
    global c
    global d
    a = data[0]
    b = data[3]
    c = data[2]
    d = data[1]

    global ad
    global pin_kod
    global hesab_nomre2
    ad=entry1.get()
    pin_kod=entry3.get()
    hesab_nomre2=entry2.get()

    if (a[7::] == str(entry1.get()) and b[15::] == str(entry2.get()) and c[8::] == str(entry3.get())):
        messagebox.showinfo("Uğurlu əməliyyat",'Sistəmə uğurla daxil olduz!')
        master.destroy()
        Daxil_olan_sehife()
    else:
        messagebox.showinfo('Xəta', 'Daxil olunan məlumatlar sehvdir!')

def geri_qayit_1(master):
    master.destroy()
    Main_menu()

def Login(master):
    master.destroy()
    pencere2=Tk()
    pencere2.geometry("790x500")
    pencere2.title("BANKING SYSTEM")

    img3 =Image.open("Bank2.png")
    img3_3=img3.resize((830,500))
    img3=ImageTk.PhotoImage(img3_3)
    label2 = Label(pencere2, image=img3)
    label2.image=img3
    label2.place(x=0,y=0)

    img4= Image.open("lodin.png")
    img4_4 = img4.resize((130, 130))
    img4= ImageTk.PhotoImage(img4_4)
    label3 = Label(pencere2, image=img4)
    label3.image = img4
    label3.place(x=580, y=50)

    global entry1
    global entry2
    global entry3

    entry1=StringVar()
    entry2=StringVar()
    entry3=StringVar()

    label4=Label(pencere2,text="Adınızı daxil edin!",font=("Arial", "15", "bold"),bg="white",fg="red")
    label4.place(x=510,y=190)
    entry1=Entry(pencere2,font=("Arial", "15", "bold"),textvariable=entry1,bg="cyan",width=24)
    entry1.place(x=510,y=215)

    label5 = Label(pencere2, text="Hesab nömrənizi daxil edin!", font=("Arial", "15", "bold"), bg="white",fg="red")
    label5.place(x=510, y=250)
    entry2 = Entry(pencere2, font=("Arial", "15", "bold"),textvariable=entry2,bg="cyan",width=24)
    entry2.place(x=510, y=275)

    label6 = Label(pencere2, text="Pin kod daxil edin!", font=("Arial", "15", "bold"), bg="white", fg="red")
    label6.place(x=510, y=310)
    entry3 = Entry(pencere2, font=("Arial", "15", "bold"),show='*',textvariable=entry1,bg="cyan", width=24)
    entry3.place(x=510, y=335)

    def Pin_kodu_goster_2():
        if (entry3.cget("show") == ''):
            entry3.config(show='*')
        else:
            entry3.config(show='')

    button_n = Checkbutton(pencere2, font=("Arial", 13, "bold"), bg="yellow", fg="red", height=0,command=Pin_kodu_goster_2)
    button_n.place(x=747, y=334)

    button4=Button(pencere2,text="Daxil ol",bg="yellow",fg="red",font=("Arial", "13", "bold"),width=12,command=lambda:check_log_in(pencere2))
    button4.place(x=510,y=400)
    button5 = Button(pencere2,text="Geri qayıt",bg="yellow",fg="red",font=("Arial","13","bold"),width=12,command=lambda:geri_qayit_1(pencere2))
    button5.place(x=650, y=400)

#======================================================================================================================#

#================================================ Qeydiyyatdan kec ====================================================#
def melumat_yazmaq(master):
    if(e1.get()=='' and e2.get()=='' and e3.get()==''):
        messagebox.showinfo('Xəta','Zəhmət olmasa boş xanaları doldurun')
    if(e1.get()=='' and e2.get()!='' and e3.get()!=''):
        messagebox.showinfo('Xəta', 'Zəhmət olmasa adınızı daxil edin')
    if (e1.get() != '' and e2.get() == '' and e3.get() != ''):
        messagebox.showinfo('Xəta', 'Zəhmət olmasa banka qoyulacaq məbləği daxil edin')
    if (e1.get() != '' and e2.get() != '' and e3.get() == ''):
        messagebox.showinfo('Xəta', 'Zəhmət olmasa pin kodu daxil edin')
    if (e1.get() != '' and e2.get() != '' and e3.get() != ''):
        f1 = open("Hesab_data.txt", "r")
        hesab_nomre = int(f1.readline())
        hesab_nomre += 1
        f1.close()

        f1 = open("Hesab_data.txt", "w")
        f1.write(str(hesab_nomre))
        f1.close()

        f2 = open(str(hesab_nomre) + ".txt", "w")
        f2.write('Adiniz:' + str(e1.get()) + "\n")
        f2.write('Banka qoyulan mebleg:' + str(e2.get()) + "\n")
        f2.write('Pin kod:' + str(e3.get()) + '\n')
        f2.write('Hesab nomreniz:' + str(hesab_nomre) + "\n")
        f2.close()

        f3 = open(str(hesab_nomre) + "-rec.txt", 'w')
        f3.write("Date                             Credit      Debit     Balance\n")
        f3.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ", gmtime())) + "      " + str(e2.get()) + "           " + str(
            e2.get()) + "\n")
        f3.close()

        messagebox.showinfo("Ugurlu emeliyyat", "Hesab nömrəniz:" + str(hesab_nomre))
        master.destroy()
        return


def geri_qayit_2(master):
    master.destroy()
    Main_menu()

def qeydiyyat(master):
    master.destroy()
    pencere3=Tk()
    pencere3.geometry("790x500")
    pencere3.title("BANKING SYSTEM")

    img5=Image.open("Register.png")
    img5_5=img5.resize((790,500))
    img5=ImageTk.PhotoImage(img5_5)
    label8=Label(pencere3,image=img5)
    label8.image=img5
    label8.pack()

    global e1
    global e2
    global e3

    e1 = StringVar()
    e2 = StringVar()
    e3 = StringVar()

    label9=Label(pencere3,text="Adınızı daxil edin!",font=("Arial", "15", "bold"),bg="white",fg="red")
    label9.place(x=500,y=150)
    entry1_1= Entry(pencere3, font=("Arial", "15", "bold"), bg="cyan", width=24,textvariable=e1)
    entry1_1.place(x=500, y=175)

    label10 = Label(pencere3, text="Banka qoyulacaq məbləğ?", font=("Arial", "15", "bold"), bg="white", fg="red")
    label10.place(x=500, y=210)
    entry2_2= Entry(pencere3, font=("Arial", "15", "bold"), bg="cyan", width=24,textvariable=e2)
    entry2_2.place(x=500, y=240)

    label11 = Label(pencere3, text="Pin kod daxil edin!", font=("Arial", "15", "bold"), bg="white", fg="red")
    label11.place(x=500, y=270)
    entry3_3 = Entry(pencere3, font=("Arial", "15", "bold"),show='*',bg="cyan", width=24,textvariable=e3)
    entry3_3.place(x=500, y=300)

    def Pin_kodu_goster_1():
        if(entry3_3.cget("show")==''):
            entry3_3.config(show='*')
        else:
            entry3_3.config(show='')

    button6=Checkbutton(pencere3,font=("Arial", 13, "bold"),bg="yellow",fg="red",height=0,command=Pin_kodu_goster_1)
    button6.place(x=738,y=299)

    button7=Button(pencere3,text="Qeydiyyatdan keç",bg="yellow",fg="red",font=("Arial", "13", "bold"),width=14,command=lambda:melumat_yazmaq(pencere3))
    button7.place(x=500,y=350)
    button8 = Button(pencere3, text="Geri qayıt", bg="yellow", fg="red", font=("Arial", "13", "bold"), width=10,
                     command=lambda: geri_qayit_2(pencere3))
    button8.place(x=660, y=350)
    return
#======================================================================================================================#
def Main_menu():
    pencere1=Tk()
    pencere1.geometry("790x500")
    pencere1.title("BANKING SYSTEM")

#     #====== Şəkil qoymaq =======#
    img1=ImageTk.PhotoImage(Image.open("Bank1.png"))
    label1=Label(pencere1,image=img1)
    label1.pack()
    #=====================================================================#

    #====== Saatı düzəltmək ======#
    # Width = 100
    # Height = 100
    # frame = Canvas(label1, width=100, height=100, bg="#0edbc7")
    # frame.place(x=150,y=40)

    # def Daire():
    #     frame.delete("all")
    #     vaxt = time.localtime()
    #     saat = vaxt.tm_hour % 12
    #     deqiqe = vaxt.tm_min
    #     saniye = vaxt.tm_sec
    #     frame.create_oval(2, 2, Width, Height, outline="black", width=1)
    #
    #     for i in range(1,13,1):
    #         reqemler = i * math.pi / 6 - math.pi / 2
    #         x = Width / 2 + 0.7 * Width / 2 * math.cos(reqemler)
    #         y = Height / 2 + 0.7 * Width / 2 * math.sin(reqemler)
    #         frame.create_text(x, y, text=str(i), fill="blue", font=("Helvetica", 8))
    #
    #     for i in range(60):
    #         reqemler = i * math.pi / 30 - math.pi / 2
    #         x1 = Width / 2 + 0.8 * Width / 2 * math.cos(reqemler)
    #         y1 = Height / 2 + 0.8 * Height / 2 * math.sin(reqemler)
    #         x2 = Width / 2 + 0.9 * Width / 2 * math.cos(reqemler)
    #         y2 = Height / 2 + 0.9 * Height / 2 * math.sin(reqemler)
    #         if (i % 5 == 0):
    #             frame.create_line(x1, y1, x2, y2, fill="red", width=2)
    #         else:
    #             frame.create_line(x1, y1, x2, y2, fill="black", width=1)
    #
    #     saat_xett = (saat + deqiqe / 60) * math.pi / 6 - math.pi / 2
    #     saat_x = Width / 2 + 0.5 * Width / 2 * math.cos(saat_xett)
    #     saat_y = Height / 2 + 0.5 * Height / 2 * math.sin(saat_xett)
    #     frame.create_line(Width / 2, Height / 2, saat_x, saat_y, fill="black", width=1)
    #
    #     deqiqe_xett = (deqiqe + saniye / 60) * math.pi / 30 - math.pi / 2
    #     deqiqe_x = Width / 2 + 0.7 * Width / 2 * math.cos(deqiqe_xett)
    #     deqiqe_y = Height / 2 + 0.7 * Height / 2 * math.sin(deqiqe_xett)
    #     frame.create_line(Width / 2, Height / 2, deqiqe_x, deqiqe_y, fill="yellow", width=3)
    #
    #     saniye_xett = saniye * math.pi / 30 - math.pi / 2
    #     saniye_x = Width / 2 + 0.6 * Width / 2 * math.cos(saniye_xett)
    #     saniye_y = Height / 2 + 0.6 * Width / 2 * math.sin(saniye_xett)
    #     frame.create_line(Width / 2, Height / 2, saniye_x, saniye_y, fill="red", width=1)
    #
    #     frame.after(10, Daire)
    # Daire()
    #======================================================================================#

    #====== Buttonlar ======#
    button1=Button(label1,text="Sistəmə daxil ol",bg="yellow",fg="red",font=("Arial", "13", "bold"),command=lambda:Login(pencere1))
    button1.place(x=438,y=110)

    button2=Button(label1,text="Hesab yarat",bg="yellow",fg="red",font=("Arial", "13", "bold"),command=lambda:qeydiyyat(pencere1))
    button2.place(x=595,y=110)

    img2 = Image.open("exit1.png")
    img2_2=img2.resize((100,40))
    img2=ImageTk.PhotoImage(img2_2)
    button3=Button(label1,width=100,height=35,image=img2,command=pencere1.destroy)
    button3.place(x=645,y=1)

    pencere1.mainloop()

Main_menu()

