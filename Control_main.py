import control as co
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont
HEIGHT = 500
WIDTH = 600



class control_system:
    def get_TF(self, entry1, entry2):
        input1 = [int(n) for n in entry1.split()]
        input2 = [int(n) for n in entry2.split()]
        transfer_function = co.tf(input1, input2)
        return transfer_function

    def print_TF(self, window, entry1, entry2, fontsize="9", relx=0, rely=0, relwidth=1, min=False, relheight=1):
        transfer_function = self.get_TF(entry1,entry2)
        if min:
            transfer_function = co.minreal(transfer_function)
        label2 = tk.Label(window, text=str(transfer_function), bg="#EBE7E7", font="comicsans "+fontsize)
        label2.place(relx=relx, rely=rely, relwidth=relwidth)

    def plot_type(self, type, TF):
        if type == "step":
            t1, y1 = co.step_response(TF)
        if type == "impulse":
            t1, y1 = co.impulse_response(TF)
        return [t1, y1]

    def plot(self, type, entry1, entry2):
        transfer_function = self.get_TF(entry1, entry2)
        if type == "bode":
            co.bode_plot(transfer_function)
        elif type == "nyquist":
            co.nyquist(transfer_function)
        elif type == "rootlocus":
            co.root_locus(transfer_function)
        else:
            [t1, y1] = self.plot_type(type, transfer_function)
            plt.plot(t1, y1)
            plt.xlabel('Time(s)')
            plt.ylabel('Amplitude')
            plt.grid()
        plt.show()


    def print_TF_props(self, window, key, text):
        frame1 = tk.Frame(window, bg="#EBE7E7")
        frame1.place(relx=0, rely=0, relwidth=1, relheight=1)
        label4 = tk.Label(frame1, text=text, font="comicsans 10", bg="#EBE7E7", justify="left")
        label4.grid(row=1, column=0)
        label2 = tk.Label(frame1, text=key, font="comicsans 10", bg="#EBE7E7", justify="left")
        label2.grid(row=1, column=1)


    def TF_properties(self, window, key, entry1, entry2):
        transfer_function = self.get_TF(entry1, entry2)
        if key == "dcgain":
            dc_gain = co.dcgain(transfer_function)
            self.print_TF_props(window, dc_gain, "DC Gain:")
        elif key == "poles":
            poles = co.pole(transfer_function)
            self.print_TF_props(window, poles, "Poles:")
        elif key == "zeros":
            zeros = co.zero(transfer_function)
            self.print_TF_props(window, str(zeros), "Zeros:")



def gen_TF():
    WIN = tk.Tk()
    canvas = tk.Canvas(WIN, height=HEIGHT, width=WIDTH)
    canvas.pack()

    label1 = tk.Label(WIN, text="View Transfer Function", font="comicsans 18")
    label1.place(relx=0.1, rely=0.03, relwidth=0.8)
    label = tk.Label(WIN, text="Type the space-separated coeficients of the transfer function and click View", font="comicsans 8")
    label.place(relx=0.1, rely=0.15, relwidth=0.8)
    label2 = tk.Label(WIN, text="Enter numerator coefficients:", font="comicsans 10")
    label2.place(relx=0.05, rely=0.25, relwidth=0.4)
    label3 = tk.Label(WIN, text="Enter denominator coefficients:", font="comicsans 10")
    label3.place(relx=0.55, rely=0.25, relwidth=0.4)
    label4 = tk.Label(WIN, text="Transfer Function:", font="comicsans 10")
    label4.place(relx=0.3, rely=0.45, relwidth=0.4)

    entry1 = tk.Entry(WIN, font=25)
    entry1.place(relx=0.05, rely=0.3, relwidth=0.4)
    entry2 = tk.Entry(WIN, font=25)
    entry2.place(relx=0.55, rely=0.3, relwidth=0.4)
    view_TF = tk.Button(WIN, text="View Transfer Function", bg="#6666FF",
                        command=lambda: control.print_TF(WIN, entry1.get(), entry2.get(), "15", 0, 0.5, 1))
    view_TF.place(relx=0.35, rely=0.8, relwidth=0.3)

    WIN.mainloop()


def plots_func():
    WIN = tk.Toplevel()
    canvas = tk.Canvas(WIN, height=HEIGHT, width=WIDTH)
    canvas.pack()

    frame = tk.Frame(WIN, bg="#FFFFFF")
    frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    BG = Image.open("C:\\Users\\Admin\\Desktop\\Deck\\graphBG.png").resize((WIDTH, HEIGHT))
    draw = ImageDraw.Draw(BG)
    font1 = ImageFont.truetype("GARABD", 28)
    font2 = ImageFont.truetype("ANTQUAB", 13)
    draw.text((170, 230), "Make different plots!", "white", font=font1)

    BG1 = ImageTk.PhotoImage(image=BG)
    BG_label = tk.Label(frame, image=BG1)
    BG_label.place(relx=0, rely=0, relwidth=1, relheight=0.16)

    graph = Image.open("C:\\Users\\Admin\\Desktop\\Deck\\graph.png").resize((90,90))
    grp_img = ImageTk.PhotoImage(image=graph)
    grp_img_label = tk.Label(frame, image=grp_img)
    grp_img_label.place(relx=0.72, rely=0.2)

    label2 = tk.Label(WIN, text="Enter numerator coefficients (space separated):", font="comicsans 10", bg="#FFFFFF")
    label2.place(relx=0.05, rely=0.20, relwidth=0.45)
    label3 = tk.Label(WIN, text="Enter denominator coefficients (space separated):", font="comicsans 10", bg="#FFFFFF")
    label3.place(relx=0.05, rely=0.35, relwidth=0.47)

    frame1 = tk.Frame(frame, bg="#EBE7E7")
    frame1.place(relx=0.05, rely=0.57, relwidth=0.5, relheight=0.2)
    label4 = tk.Label(frame, text="Transfer Function:", font="comicsans 10", bg="#FFFFFF")
    label4.place(relx=0.05, rely=0.50, relwidth=0.4)

    entry1 = tk.Entry(frame, font=30, bg="#EBE7E7")
    entry1.place(relx=0.05, rely=0.25, relwidth=0.4)
    entry2 = tk.Entry(frame, font=30, bg="#EBE7E7")
    entry2.place(relx=0.05, rely=0.40, relwidth=0.4)


    view_TF = tk.Button(frame, text="View Transfer Function", fg="#FFFFFF",bg="#004C99",
                        command=lambda: control.print_TF(frame1, entry1.get(), entry2.get()))
    view_TF.place(relx=0.1, rely=0.85, relwidth=0.3)
    step_response = tk.Button(frame, text="Step Response", fg="#FFFFFF",bg="#004C99",
                        command=lambda: control.plot("step", entry1.get(), entry2.get()))
    step_response.place(relx=0.65, rely=0.45, relwidth=0.3)
    impulse_response = tk.Button(frame, text="Impulse Response",fg="#FFFFFF",bg="#004C99",
                        command=lambda: control.plot("impulse", entry1.get(), entry2.get()))
    impulse_response.place(relx=0.65, rely=0.55, relwidth=0.3)
    bode_plot = tk.Button(frame, text="Bode plot", fg="#FFFFFF",bg="#004C99",
                        command=lambda: control.plot("bode", entry1.get(), entry2.get()))
    bode_plot.place(relx=0.65, rely=0.65, relwidth=0.3)
    nyquist_plot = tk.Button(frame, text="Nyquist plot",fg="#FFFFFF",bg="#004C99",
                        command=lambda: control.plot("nyquist", entry1.get(), entry2.get()))
    nyquist_plot.place(relx=0.65, rely=0.75, relwidth=0.3)
    root_locus = tk.Button(frame, text="Root Locus",fg="#FFFFFF",bg="#004C99",
                        command=lambda: control.plot("rootlocus", entry1.get(), entry2.get()))
    root_locus.place(relx=0.65, rely=0.85, relwidth=0.3)

    WIN.mainloop()


def tf_properties():
    WIN = tk.Toplevel()
    canvas = tk.Canvas(WIN, height=HEIGHT, width=WIDTH)
    canvas.pack()

    frame = tk.Frame(WIN, bg="#FFFFFF")
    frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    BG = Image.open("C:\\Users\\Admin\\Desktop\\Deck\\graphBG.png").resize((WIDTH, HEIGHT))
    draw = ImageDraw.Draw(BG)
    font1 = ImageFont.truetype("GARABD", 23)
    font2 = ImageFont.truetype("ANTQUAB", 13)
    draw.text((75, 240), "Find different properties of transfer function", "white", font=font1)

    BG1 = ImageTk.PhotoImage(image=BG)
    BG_label = tk.Label(frame, image=BG1)
    BG_label.place(relx=0, rely=0, relwidth=1, relheight=0.16)


    label2 = tk.Label(frame, text="Enter numerator coefficients (space separated):", bg="#FFFFFF", font="comicsans 10")
    label2.place(relx=0.05, rely=0.20, relwidth=0.45)
    label3 = tk.Label(frame, text="Enter denominator coefficients (space separated):", bg="#FFFFFF", font="comicsans 10")
    label3.place(relx=0.05, rely=0.35, relwidth=0.47)
    label4 = tk.Label(frame, text="Transfer Function:", bg="#FFFFFF", font="comicsans 10")
    label4.place(relx=0.05, rely=0.50, relwidth=0.4)

    entry1 = tk.Entry(frame, font=30, bg="#EBE7E7")
    entry1.place(relx=0.05, rely=0.25, relwidth=0.4)
    entry2 = tk.Entry(frame, font=30, bg="#EBE7E7")
    entry2.place(relx=0.05, rely=0.40, relwidth=0.4)
    frame1 = tk.Frame(frame, bg="#EBE7E7")
    frame1.place(relx=0.05, rely=0.82, relwidth=0.9, relheight=0.12)
    frame2 = tk.Frame(frame, bg="#EBE7E7")
    frame2.place(relx=0.05, rely=0.57, relwidth=0.5, relheight=0.2)

    view_TF = tk.Button(frame, text="View Transfer Function",  bg="#004C99", fg="#FFFFFF",
                        command=lambda: control.print_TF(frame2, entry1.get(), entry2.get()))
    view_TF.place(relx=0.65, rely=0.25, relwidth=0.3)
    min_TF = tk.Button(frame, text="Min. transfer function", bg="#004C99", fg="#FFFFFF",
                              command=lambda: control.print_TF(frame2, entry1.get(), entry2.get(), min=True))
    min_TF.place(relx=0.65, rely=0.35, relwidth=0.3)
    DC_gain = tk.Button(frame, text="DC Gain", bg="#004C99", fg="#FFFFFF",
                                 command=lambda: control.TF_properties(frame1, "dcgain", entry1.get(), entry2.get()))
    DC_gain.place(relx=0.65, rely=0.45, relwidth=0.3)
    Poles = tk.Button(frame, text="Poles", bg="#004C99", fg="#FFFFFF",
                                 command=lambda: control.TF_properties(frame1, "poles", entry1.get(), entry2.get()))
    Poles.place(relx=0.65, rely=0.55, relwidth=0.3)
    Zeros = tk.Button(frame, text="Zeros", bg="#004C99", fg="#FFFFFF",
                      command=lambda: control.TF_properties(frame1, "zeros", entry1.get(), entry2.get()))
    Zeros.place(relx=0.65, rely=0.65, relwidth=0.3)


    WIN.mainloop()



def main_window():
    WIN = tk.Tk()
    canvas = tk.Canvas(WIN, height=HEIGHT, width=WIDTH)
    WIN.title("CS Toolbox")
    canvas.pack()

    frame = tk.Frame(WIN, bg="#FFFFFF")
    frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    img = Image.open("C:\\Users\\Admin\\Desktop\\Deck\\function.png").resize((100,100))
    BG = Image.open("C:\\Users\\Admin\\Desktop\\Deck\\control-bg3.png").resize((WIDTH, HEIGHT))
    draw = ImageDraw.Draw(BG)
    font1 = ImageFont.truetype("GARABD", 27)
    font2 = ImageFont.truetype("ANTQUAB", 15)
    draw.text((78, 240), "Welcome to Control Systems Toolbox!", "white", font=font1)



    BG1 = ImageTk.PhotoImage(image=BG)
    BG_label = tk.Label(frame, image=BG1)
    BG_label.place(relx=0, rely=0, relwidth=1, relheight=0.2)

    
    label1 = tk.Label(frame, text="Visualise and analyse control systems easily\n1. View a transfer function by giving the numerator and denominator coefficients\n"
                                "2. Make various plots and get time and frequency responses\n"
                                "3. Get transfer function properties like DC gain, poles and zeros", font="comicsans 12", bg="#FFFFFF")
    label1.place(relx=0, rely=0.58, relwidth=1)


    image = ImageTk.PhotoImage(Image.open("C:\\Users\\Admin\\Desktop\\Deck\\feedback.png").resize((150,120)))
    image_label = tk.Label(frame, image=image, bg="#FFFFFF")
    image_label.place(relx=0.29, rely=0.29, relwidth=0.4)


    View_button = tk.Button(frame, text="View TF", bg="#004C99", fg="#FFFFFF", command=lambda: gen_TF())
    View_button.place(relx=0.15, rely=0.82, relwidth=0.2)

    Plots_button = tk.Button(frame, text="Generate plots", bg="#004C99", fg="#FFFFFF", command=lambda: plots_func())
    Plots_button.place(relx=0.40, rely=0.82, relwidth=0.2)

    TF_Properties = tk.Button(frame, text="TF Properties", bg="#004C99", fg="#FFFFFF", command=lambda: tf_properties())
    TF_Properties.place(relx=0.65, rely=0.82, relwidth=0.2)

    WIN.mainloop()




if __name__ == "__main__":
    control = control_system()
    main_window()
