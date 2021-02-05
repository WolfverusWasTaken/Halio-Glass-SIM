from tkinter import *
from PIL import Image, ImageEnhance, ImageTk

root = Tk()
var = IntVar()
var1 = IntVar()
toggletemp = IntVar()
toggleHUD = IntVar()
im = Image.open("TestImage.jpg")
appim = Image.open("Capture.PNG")

InTemp = StringVar()
OutTemp = StringVar()
RTemp = StringVar()
tr = 28

TempUIx = 1050
TempUIy = 100

ImUIx = 360
ImUIy = 100

EModUIx = 10
EModUIy = 350

ScaleUIx = 10
ScaleUIy = 100

def updateval(event):
    manualval = var1.get()
    val = toggleHUD.get()

    if manualval:
        tintlevel = tint.get()
        # Checkbutton.config(bg = "green")

        tout = int(tr + (light.get() / 100) * 14)
        tin = int(tout - ((tint.get() / 100) * 14))

        #if light.get() < tint.get():
            #tin = int(tout - ((tint.get() - light.get() / 100) * 0.01))

        if tin < 28:
            tin = 28

        OutTempScale.set(tout)
        InTempScale.set(tin)

        if val:
            Connector.config(bg="orange red")
            Connector2.config(bg="lime green")
            Connector3.config(bg="lime green")
            Connector4.config(bg="lime green")

            activeline1.config(bg="lime green")
            activeline2.config(bg="orange red")
            activeline3.config(bg="lime green")
            activeline4.config(bg="lime green")

        else:
            Connector.config(bg="grey")
            Connector2.config(bg="grey")
            Connector3.config(bg="grey")
            Connector4.config(bg="grey")


    else:
        tintlevel = light.get()
        tint.set(tintlevel)
        # Checkbutton["fg"] = "red"

        tout = int(tr + (light.get() / 100) * 14)
        tin = int(tout - ((tint.get() / 100) * 12))

        OutTempScale.set(tout)
        InTempScale.set(tin)

        if val:
            Connector.config(bg="lime green")
            Connector2.config(bg="lime green")
            Connector3.config(bg="lime green")
            Connector4.config(bg="lime green")

            activeline1.config(bg="lime green")
            activeline2.config(bg="lime green")
            activeline3.config(bg="lime green")
            activeline4.config(bg="lime green")

        else:
            Connector.config(bg="grey")
            Connector2.config(bg="grey")
            Connector3.config(bg="grey")
            Connector4.config(bg="grey")

    tout = str(tout)
    tin = str(tin)

    InTemp.set("Temperature Inside: " + tin)
    OutTemp.set("Temperature Outside: " + tout)

    # print(tintlevel)
    tintrenderer(tintlevel)

# ====================================================================================
HUDbg2 = Label(root,
               height=20,
               width=46,
               bg="grey",
               relief=GROOVE,
               )

ScaleUI = Label(root,
                height=14,
                width=46,
                bg="grey",
                fg="white",
                relief=GROOVE,
                )

# ====================================================================================

EMod = Label(root,
             height=3,
             width=25,
             bg="WHITE",
             relief=FLAT,
             text="Energy Management Module",
             fg="BLACK",
             )

Connector4 = Label(root,
                   height=3,
                   width=1,
                   bg="WHITE",
                   relief=FLAT,
                   )

Gateway = Label(root,
                height=3,
                width=14,
                bg="WHITE",
                relief=FLAT,
                text="Halio Gateway",
                fg="BLACK",
                )

Connector2 = Label(root,
                   height=3,
                   width=1,
                   bg="WHITE",
                   relief=FLAT,
                   )


RSens = Label(root,
              height=3,
              width=14,
              bg="WHITE",
              relief=FLAT,
              text="Rooftop Sensor",
              fg="BLACK",
              )

Connector = Label(root,
                  height=3,
                  width=1,
                  bg="WHITE",
                  relief=FLAT,
                  )

Drivers = Label(root,
                height=3,
                width=14,
                bg="WHITE",
                relief=FLAT,
                text="Halio Drivers",
                fg="BLACK",
                )

Connector3 = Label(root,
                   height=3,
                   width=1,
                   bg="WHITE",
                   relief=FLAT,
                   )

activeline2 = Label(root,
                   height=1,
                   width=5,
                   bg="WHITE",
                   relief=SOLID,
                   )

activeline3 = Label(root,
                   height=1,
                   width=5,
                   bg="WHITE",
                   relief=SOLID,
                   )

activeline4 = Label(root,
                   height=1,
                   width=5,
                   bg="WHITE",
                   relief=SOLID,
                   )

activeline1 = Label(root,
                   height=11,
                   width=2,
                   bg="WHITE",
                   relief=SOLID,
                   )

# ====================================================================================

TempBg = Label(root,
               height=25,
               width=46,
               bg="grey",
               fg="white",
               relief=GROOVE,
               )

Regional = Label(root,
                 textvariable=RTemp,
                 height=1,
                 width=40,
                 bg="forest green",
                 fg="white",
                 relief=GROOVE
                 )

TempOut = Label(root,
                textvariable=OutTemp,
                height=1,
                width=40,
                bg="maroon",
                fg="white",
                relief=GROOVE
                )

TempIn = Label(root,
               textvariable=InTemp,
               height=1,
               width=40,
               bg="DeepSkyBlue3",
               fg="white",
               relief=GROOVE
               )
OutTempScale = Scale(root,
             orient=VERTICAL,
             length=200,
             from_=42, to=27,
             showvalue=1,
             label="Out\n(Celsius)",
             activebackground="firebrick",
             troughcolor="MAROON",
             bg="grey30",
             fg="white",
             highlightbackground="BLACK",
             sliderlength = 10,
             command=updateval,
             )

InTempScale = Scale(root,
              orient=VERTICAL,
              length=200,
              from_=42, to=27,
              showvalue=1,
              label="In\n(Celsius)",
              activebackground="firebrick",
              troughcolor="DEEPSKYBLUE3",
              bg="grey30",
              fg="white",
              highlightbackground="BLACK",
              sliderlength = 10,
              command=updateval,
              )

# ====================================================================================

def screeninit(x, y):
    root.title("Halio Smart Glass SIM")
    root.resizable(FALSE, FALSE)
    root.geometry("1400x750")
    # root.attributes("-fullscreen", 1)
    root.configure(bg='honeydew2')

    ImCanvas = Label(root,
                     height=25,
                     width=90,
                     bg="grey",
                     fg="white",
                     relief=GROOVE,
                     )
    ImCanvas.place(x=x, y=y)


screeninit(x=ImUIx, y=ImUIy)

test = ImageTk.PhotoImage(im)
panel = Label(root, image=test)
test2 = ImageTk.PhotoImage(appim)
panel2 = Label(root, image=test2)
# panel.image = test
panel.place(x=ImUIx + 42, y=ImUIy + 30)







def HideTempToggle(event=None):
    val = toggletemp.get()
    HUDval = toggleHUD.get()
    if val:
        TempBg.place(x=TempUIx, y=TempUIy)
        Regional.place(x=TempUIx + 20, y=TempUIy + 13)
        TempOut.place(x=TempUIx + 20, y=TempUIy + 53)
        TempIn.place(x=TempUIx + 20, y=TempUIy + 93)

        InTempScale.place(relx=0.1, rely=0.06, relwidth=10)
        OutTempScale.place(relx=0.1, rely=0.06, relwidth=10)

        InTempScale.pack(side=LEFT, padx=10, pady=0)
        OutTempScale.pack(side=LEFT, padx=0, pady=0)

        InTempScale.place(x=TempUIx + 20, y=TempUIy + 140)
        OutTempScale.place(x=TempUIx + 150, y=TempUIy + 140)

        if HUDval:
            toggleHUD.set(0)
            EMod.place_forget()
            Gateway.place_forget()
            RSens.place_forget()
            Drivers.place_forget()
            HUDbg2.place_forget()

            Connector.place_forget()
            Connector2.place_forget()
            Connector3.place_forget()
            Connector4.place_forget()

            activeline1.place_forget()
            activeline2.place_forget()
            activeline3.place_forget()
            activeline4.place_forget()

            panel2.place_forget()


    else:
        TempBg.place_forget()
        TempIn.place_forget()
        TempOut.place_forget()
        Regional.place_forget()

        InTempScale.place_forget()
        OutTempScale.place_forget()


def HideHUD(event=None):
    val = toggleHUD.get()
    tempval = toggletemp.get()
    if val:

        HUDbg2.place(x=EModUIx, y=EModUIy)

        RSens.place(x=EModUIx + 15, y=EModUIy + 35)
        Connector.place(x=EModUIx + 13, y=EModUIy + 35)

        Gateway.place(x=EModUIx + 15, y=EModUIy + 100)
        Connector2.place(x=EModUIx + 13, y=EModUIy + 100)

        Drivers.place(x=EModUIx + 15, y=EModUIy + 165)
        Connector3.place(x=EModUIx + 15, y=EModUIy + 165)

        EMod.place(x=EModUIx + 15, y=EModUIy + 230)
        Connector4.place(x=EModUIx + 15, y=EModUIy + 230)

        activeline1.place(x=EModUIx + 150, y=EModUIy + 50)

        activeline2.place(x=EModUIx + 125, y=EModUIy + 50)

        activeline3.place(x=EModUIx + 125, y=EModUIy + 115)

        activeline4.place(x=EModUIx + 125, y=EModUIy + 180)

        panel2.place(x=TempUIx, y=TempUIy)

        if tempval:
            toggletemp.set(0)
            TempBg.place_forget()
            TempIn.place_forget()
            TempOut.place_forget()
            Regional.place_forget()

            InTempScale.place_forget()
            OutTempScale.place_forget()


    else:
        EMod.place_forget()
        Gateway.place_forget()
        RSens.place_forget()
        Drivers.place_forget()
        HUDbg2.place_forget()

        Connector.place_forget()
        Connector2.place_forget()
        Connector3.place_forget()
        Connector4.place_forget()

        activeline1.place_forget()
        activeline2.place_forget()
        activeline3.place_forget()
        activeline4.place_forget()

        panel2.place_forget()


def tintrenderer(tintlevel):
    # factor = 1
    if tintlevel > 80:
        tintlevel = 80

    factor = 1 * (1 - (tintlevel / 100.0))
    img2 = ImageEnhance.Brightness(Image.open("TestImage.jpg")).enhance(factor)
    reimg = ImageTk.PhotoImage(img2)
    panel.config(image=reimg)
    panel.image = reimg


def controlpanel(x, y):
    SoftwareName = Label(root,
                         height=3,
                         width=199,
                         bg="orange red",
                         fg="BLACK",
                         relief=FLAT
                         ).place(x=x, y=y - 50)
    panelbg = Label(root,
                    height=2,
                    width=199,
                    bg="grey",
                    fg="white",
                    relief=RIDGE
                    ).place(x=x, y=y)

    Checkbutton(root, text="Manual Control",
                variable=var1,
                onvalue=1,
                offvalue=0,
                bg="red",
                selectcolor="forest green",
                overrelief=SUNKEN,
                bd=2,
                indicatoron=0,
                relief=RAISED,

                ).place(x=x + 10, y=y + 6)

    HideTempUI = Checkbutton(root, text="Toggle Temperature",
                             variable=toggletemp,
                             command=HideTempToggle,
                             onvalue=1,
                             offvalue=0,
                             bg="red",
                             selectcolor="forest green",
                             overrelief=SUNKEN,
                             bd=2,
                             indicatoron=0,
                             relief=RAISED,

                             ).place(x=x + 120, y=y + 6)

    HideTempUI = Checkbutton(root,
                             text="Toggle HUD",
                             variable=toggleHUD,
                             command=HideHUD,
                             onvalue=1,
                             offvalue=0,
                             bg="red",
                             selectcolor="forest green",
                             overrelief=SUNKEN,
                             bd=2,
                             indicatoron=0,
                             relief=RAISED,

                             ).place(x=x + 255, y=y + 6)

    SoftwareBase = Label(root,
                         height=2,
                         width=199,
                         bg="red3",
                         fg="BLACK",
                         relief=FLAT
                         ).place(x=x, y=y + 670)

    # HideTempUI.bind("<Button-1>", hideTempUI)


controlpanel(x=1, y=50)



tint = Scale(root,
             orient=HORIZONTAL,
             length=280,
             from_=0, to=100,
             showvalue=1,
             label="Tint Level(%)",
             activebackground="grey20",
             troughcolor="maroon4",
             bg="grey30",
             fg="white",
             highlightbackground="maroon4",
             command=updateval,
             )



light = Scale(root,
              orient=HORIZONTAL,
              length=280,
              from_=0, to=100,
              showvalue=1,
              label="Light Level(%)",
              activebackground="firebrick",
              troughcolor="gold",
              bg="grey30",
              fg="white",
              highlightbackground="light goldenrod",
              command=updateval,
              )

tint.place(relx=0.1, rely=0.06, relwidth=10)
light.place(relx=0.1, rely=0.06, relwidth=10)

tint.pack(side=LEFT, padx=10, pady=0)  # tint pos
light.pack(side=LEFT, padx=0, pady=0)  # light pos

tint.place(x=ScaleUIx + 20, y=ScaleUIy + 130)  # tint pos
light.place(x=ScaleUIx + 20, y=ScaleUIy + 30)  # light pos
ScaleUI.place(x=ScaleUIx, y=ScaleUIy)  # light pos

regtemp = str(tr)
RTemp.set("Regional Mean Temperature: " + regtemp)
OutTemp.set("Temperature Outside: --")
InTemp.set("Temperature Inside: --")




root.mainloop()
