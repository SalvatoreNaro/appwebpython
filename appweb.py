import customtkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import csv
import threading
import pyperclip
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from PIL import Image, ImageSequence

window = customtkinter.CTk()
window.config(bg="black")
window.title("App")
window.geometry("800x600")
window.resizable(False, False)
threading.Thread(target=window).start()
main_frame = customtkinter.CTkFrame(window, fg_color="black")
main_frame.pack(fill="both", expand=True)

canvas = Canvas(main_frame, bg="black", highlightthickness=0)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = customtkinter.CTkScrollbar(main_frame, orientation="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)
scrollable_frame = customtkinter.CTkFrame(canvas, fg_color="black")
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", on_frame_configure)

def on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", on_mousewheel)
def download():
    save = filedialog.asksaveasfilename(defaultextension=".csv",
                                        title="Save file csv",
                                        filetypes=[("Csv","*.csv")])
    with open (save,"w",newline="") as file:
        linguaggi = {
            "Python": "matplotlib",
            "Python": "tkinter",
            "Python": "customtkinter",
            "Python": "keras",
            "Python": "os",
            "Python": "tensorflow",
            "Python": "pytorch",
            "Python": "numpy",
            "Python": "scipy",
            "Python": "cmath",
            "Python": "sys",
            "Python": "pandas",
            "Python": "flask",
            "Python": "turtle",
            "Python": "pygame",
            "Python": "manim",
            "Python": "requests",
            "Python": "beautifulsoup4",
            "Python": "selenium",
            "Python":"PyQt5",
            "Python": "Threading",
            "Python":"Re",
            "Javascipt":"Three",
            "Javascript":"React",
            "Javascript":"Gsap",
            "Javascript":"Vue"
        }
        file_name = csv.writer(file)
        file_name.writerow(["linguaggi","librerie"])
        for key,value in linguaggi.items():
            value_str = str(value)
            file_name.writerow([key,str(value_str)])
    
frame1 = customtkinter.CTkFrame(scrollable_frame, width=300, height=200, fg_color="black", corner_radius=10)
frame1.grid(row=0, column=0, padx=50, pady=50)

label = customtkinter.CTkLabel(frame1, text="Chat -", text_color="white", font=("Arial", 32))
label.grid(row=0, column=0, padx=5, pady=15)

label2 = customtkinter.CTkLabel(frame1, text="B", text_color="blue", font=("Arial", 32))
label2.grid(row=0, column=1, padx=5, pady=15)

button = customtkinter.CTkButton(frame1, text="Home", text_color="White", fg_color="black", command=lambda: messagebox.showinfo("Home", "Sei già nella home"))
button.grid(row=0, column=3, padx=20, pady=5)

about_btn = customtkinter.CTkButton(frame1, text="About", text_color="White", fg_color="black", command=lambda: open_about_window())
about_btn.grid(row=0, column=4, padx=5, pady=5)

contact_btn = customtkinter.CTkButton(frame1, text="download", text_color="White", fg_color="black",command=download)
contact_btn.grid(row=0, column=5, padx=5, pady=5)

testo_originale = "Benvenuto su Chat-B"
text_label = customtkinter.CTkLabel(scrollable_frame, text="", text_color="white", font=("Arial", 32))
text_label.grid(row=1, column=0, padx=5, pady=10)

incremento = True
testo = 0
def animate_text():
    global incremento, testo
    if incremento:
        testo += 1
        if testo > len(testo_originale):
            incremento = False
    else:
        testo -= 1
        if testo == 0:
            incremento = True
    text_label.configure(text=testo_originale[:testo])
    window.after(100, animate_text)

animate_text()

gif_path1 = "C:\\Users\\salva\\Downloads\\sakrim.gif"
try:
    gif1 = Image.open(gif_path1)
    frames1 = []
    for frame in ImageSequence.Iterator(gif1):
        frames1.append(customtkinter.CTkImage(light_image=frame.copy(), size=(400, 400)))

    gif_label1 = customtkinter.CTkLabel(scrollable_frame, text="")
    gif_label1.grid(row=2, column=0, padx=10, pady=20)

    def animate_gif1(frame_num=0):
        frame_num = (frame_num + 1) % len(frames1)
        gif_label1.configure(image=frames1[frame_num])
        window.after(10, animate_gif1, frame_num)

    animate_gif1()
except:
    print("caricamento gif")

frase_label = customtkinter.CTkLabel(scrollable_frame, text="Chat-B è stato fondato da Salvatore Naro" ,text_color="white", font=("Arial", 20))
frase_label.grid(row=3, column=0, padx=5, pady=10)
frase_label2 = customtkinter.CTkLabel(scrollable_frame, text="Software-engineer di Ai e designer" ,text_color="white", font=("Arial", 12))
frase_label2.grid(row=4, column=0, padx=5, pady=10)
button = customtkinter.CTkButton(scrollable_frame,text="View Chat-B",text_color="white",fg_color="Black",bg_color="Black")
button.grid(row=5,column=0,padx=20,pady=10,sticky="se")
frase_label3 = customtkinter.CTkLabel(scrollable_frame, text="Rocket-B" ,text_color="white", font=("Arial", 32))
frase_label3.grid(row=6, column=0, padx=10, pady=10)
frase_label4 = customtkinter.CTkLabel(scrollable_frame, text="Esplora l'universo con Rocket-B" ,text_color="white", font=("Arial", 15))
frase_label4.grid(row=7, column=0, padx=5, pady=10)
button2 = customtkinter.CTkButton(scrollable_frame,text="View Rocket-B",text_color="white",fg_color="Black",bg_color="Black")
button2.grid(row=8,column=0,padx=20,pady=10,sticky="se")
gif_path2 = "C:\\Users\\salva\\Downloads\\sam.gif"
try:
    gif2 = Image.open(gif_path2)
    frames2 = []
    for frame in ImageSequence.Iterator(gif2):
        frames2.append(customtkinter.CTkImage(light_image=frame.copy(), size=(400, 400)))

    gif_label2 = customtkinter.CTkLabel(scrollable_frame, text="")
    gif_label2.grid(row=9, column=0, padx=5, pady=20)

    def animate_gif2(frame_num=0):
        frame_num = (frame_num + 1) % len(frames2)
        gif_label2.configure(image=frames2[frame_num])
        window.after(10, animate_gif2, frame_num)

    animate_gif2()
except:
    print("Caricamento gif")
label5 = customtkinter.CTkLabel(scrollable_frame,text="Salvatore Naro",text_color="white",font=("Arial",32))
label5.grid(row=10,column=0,padx=5,pady=10)

label6 = customtkinter.CTkLabel(scrollable_frame,text="Salvatore Naro è un software engineer specializzato in intelligenza artificiale e designer,",font=("Arial",14),text_color="White")
label6.grid(row=10,column=0,padx=5,pady=10)

label7 = customtkinter.CTkLabel(scrollable_frame,text="con competenze elevate in",text_color="white",font=("Arial",14))
label7.grid(row=11,column=0,sticky="S",padx=5,pady=10)
frame5 = customtkinter.CTkFrame(scrollable_frame,width=250,height=250,fg_color="Black")
frame5.grid(row=12,column=0,padx=5,pady=10,sticky="S")
label8 = customtkinter.CTkLabel(frame5,text="Python, Pandas, TensorFlow, PyTorch, Keras, NumPy, Matplotlib, SQLite3, Flask",font=("Arial",14),text_color="White")
label8.grid(row=12,column=0,sticky="WE",padx=5,pady=10)
label9 = customtkinter.CTkLabel(frame5,text="customtkinter, tkinter, PyQt5, React, Three.js, GSAP, Vue e Unreal Engine.",font=("Arial",16),text_color="White")
label9.grid(row=13,column=0,sticky="WE",padx=5,pady=10)
gif_path3 = "C:\\Users\\salva\\Downloads\\earth.gif"
try:
    gif3 = Image.open(gif_path3)
    frames3 = []
    for frame in ImageSequence.Iterator(gif3):  
        frames3.append(customtkinter.CTkImage(light_image=frame.copy(), size=(400, 400)))

    gif_label3 = customtkinter.CTkLabel(scrollable_frame, text="")
    gif_label3.grid(row=14, column=0, padx=5, pady=20)

    def animate_gif3(frame_nums=0):
        frame_nums = (frame_nums + 1) % len(frames3)
        gif_label3.configure(image=frames3[frame_nums])
        window.after(15, animate_gif3, frame_nums)

    animate_gif3()
except Exception as e:
    print(f"Errore durante il caricamento del GIF : {e}")
except:
    print("Caricamento gif")
label10 = customtkinter.CTkLabel(scrollable_frame,text="App created",text_color="white",font=("Arial",32))
label10.grid(row=17,column=0,sticky="s",padx=5,pady=10)
label11 = customtkinter.CTkLabel(scrollable_frame,text="by",text_color="white",font=("Arial",20))
label11.grid(row=18,column=0,sticky="s",padx=5,pady=5)
label12= customtkinter.CTkLabel(scrollable_frame,text="Salvatore Naro",text_color="white",font=("Arial",32))
label12.grid(row=19,column=0,sticky="s",padx=5,pady=10)
gif_path4 = "c:\\Users\\salva\Downloads\\Line Cube GIF.gif"  
try:
    gif4 = Image.open(gif_path4)
    frames4 = []
    for frame in ImageSequence.Iterator(gif4):  
        frames4.append(customtkinter.CTkImage(light_image=frame.copy(), size=(400, 400)))

    gif_label4 = customtkinter.CTkLabel(scrollable_frame, text="",bg_color="black",fg_color="Black")
    gif_label4.grid(row=20, column=0, padx=5, pady=20)

    def animate_gif4(frame_nums=0):
        frame_nums = (frame_nums + 1) % len(frames4)
        gif_label4.configure(image=frames4[frame_nums])
        window.after(25, animate_gif4, frame_nums)

    animate_gif4()
except Exception as e:
    print(f"Errore durante il caricamento del quarto GIF: {e}")
label13 = customtkinter.CTkLabel(scrollable_frame,text="Salvatore Naro",text_color="white",font=("Arial",22))
label13.grid(row=22,column=0,sticky="s",padx=5,pady=10)
parola = "Say Hello !"
label14 = customtkinter.CTkLabel(scrollable_frame,text=parola,text_color="white",font=("Arial",22))
label14.grid(row=23,column=0,sticky="se",padx=5,pady=10)

conto =  True
indice = len(parola)
def animate_text3():
    global indice,conto
    if conto:
        indice+=1
        if indice > len(parola):
            conto=False
    else:
        indice-=1
        if indice == 0:
            conto=True
    label14.configure(text=parola[:indice])
    window.after(100,animate_text3)
animate_text3()
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def verifica():
    nome = input_utente.get()
    cognome = input_cognome.get()
    messaggio_testo = messaggio.get("1.0", "end").strip()

    if nome == "" or cognome == "" or messaggio_testo == "":
        messagebox.showinfo(title="Errore 404", message="Compilare tutti i campi")
        return

    
    sender_email = "yourgmail@gmail.com"#your gmail  
    sender_password = "Your password"#ypur passowrd 
    recipient_email = "narosalvo8@gmail.com"  

    subject = f"Messaggio da {nome} {cognome}"
    body = f"Nome: {nome}\nCognome: {cognome}\n\nMessaggio:\n{messaggio_testo}"

  
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()

        messagebox.showinfo(title="Successo!", message="Messaggio inviato con successo!")
        input_cognome.delete(0, customtkinter.END)
        input_utente.delete(0, customtkinter.END)
        messaggio.delete("1.0", "end")
    except Exception as e:
        messagebox.showerror(title="Errore", message=f"Errore durante l'invio: {e}")

label15 = customtkinter.CTkLabel(scrollable_frame,text="Are you looking for a developer?",text_color="white",font=("Arial",22))
label15.grid(row=24,column=0,sticky="s",padx=5,pady=10)
frame6 = customtkinter.CTkFrame(scrollable_frame,width=250,height=250,fg_color="Black")
frame6.grid(row=25,column=0,padx=5,pady=10,sticky="s")
input_utente = customtkinter.CTkEntry(frame6,placeholder_text="Nome",text_color="white",fg_color="Black",bg_color="Black")
input_utente.grid(row=25,column = 0,padx=5,pady=10)
input_cognome = customtkinter.CTkEntry(frame6,placeholder_text="Cognome",text_color="white",bg_color="black",fg_color="black")
input_cognome.grid(row=25,column=1,padx=5,pady=10)
lavori = {
    "Data-Scientist", 
    "Designer", 
    "Data-Analisi", 
    "Software-Engineer", 
    "Ricercatore senior Ai", 
    "Machine Learning Engineer", 
    "Full Stack Developer", 
    "DevOps Engineer", 
    "Cybersecurity Specialist", 
    "Cloud Architect",
    "AI Research Scientist",
    "Big Data Engineer",
    "Blockchain Developer",
    "Business Intelligence Analyst",
    "Computer Vision Engineer",
    "Database Administrator",
    "Embedded Systems Engineer",
    "Game Developer",
    "Hardware Engineer",
    "IT Consultant",
    "IT Support Specialist",
    "Mobile App Developer",
    "Network Administrator",
    "Product Manager",
    "Project Manager",
    "Quality Assurance Engineer",
    "Robotics Engineer",
    "SEO Specialist",
    "Site Reliability Engineer",
    "Software Architect",
    "System Administrator",
    "Technical Writer",
    "UI/UX Designer",
    "Virtual Reality Developer",
    "Web Developer",
    "3D Animator",
    "Algorithm Engineer",
    "Application Developer",
    "Augmented Reality Developer",
    "Automation Engineer",
    "Bioinformatics Specialist",
    "Cloud Engineer",
    "Computer Graphics Programmer",
    "Cryptographer",
    "Data Architect",
    "Data Engineer",
    "Data Visualization Specialist",
    "Deep Learning Engineer",
    "DevSecOps Engineer",
    "Digital Marketing Specialist",
    "E-commerce Specialist",
    "Edge Computing Engineer",
    "Ethical Hacker",
    "Firmware Developer",
    "Front-End Developer",
    "Game Designer",
    "GIS Specialist",
    "HCI Researcher",
    "IoT Developer",
    "IT Auditor",
    "IT Manager",
    "Knowledge Engineer",
    "Machine Vision Engineer",
    "Middleware Developer",
    "Natural Language Processing Engineer",
    "Penetration Tester",
    "Performance Engineer",
    "Platform Engineer",
    "Predictive Analytics Specialist",
    "Quantum Computing Researcher",
    "Robotics Programmer",
    "Security Analyst",
    "Security Engineer",
    "Simulation Engineer",
    "Software Development Manager",
    "Software Tester",
    "Speech Recognition Engineer",
    "Systems Analyst",
    "Technical Support Engineer",
    "Telecommunications Engineer",
    "Video Game Tester",
    "Web Designer",
    "Wireless Network Engineer",
    "AI Ethics Specialist",
    "API Developer",
    "Application Security Engineer",
    "AR/VR Content Creator",
    "Automation Tester",
    "Bioinformatics Programmer",
    "Business Analyst",
    "Cloud Security Engineer",
    "Computer Forensics Analyst",
    "Content Strategist",
    "Control Systems Engineer",
    "Cybersecurity Analyst",
    "Data Governance Specialist",
    "Data Quality Analyst",
    "Digital Forensics Investigator",
    "Digital Twin Developer",
    "E-Learning Developer",
    "Energy Systems Engineer",
    "Enterprise Architect",
    "ERP Consultant",
    "Firmware Engineer",
    "Full Stack Engineer",
    "Game Programmer",
    "Geospatial Analyst",
    "Health Informatics Specialist",
    "Human-Centered AI Designer",
    "Industrial Automation Engineer",
    "Information Security Analyst",
    "Infrastructure Engineer",
    "Integration Specialist",
    "Interactive Media Developer",
    "IT Operations Manager",
    "Knowledge Management Specialist",
    "Logistics Software Developer",
    "Machine Learning Researcher",
    "Mainframe Developer",
    "Medical Imaging Specialist",
    "Microservices Developer",
    "Mobile Game Developer",
    "Network Engineer",
    "NoSQL Database Administrator",
    "Open Source Contributor",
    "Operations Research Analyst",
    "Performance Tester",
    "Platform Architect",
    "Power BI Developer",
    "Process Automation Engineer",
    "Product Designer",
    "Quantum Software Developer",
    "Real-Time Systems Developer",
    "Renewable Energy Software Engineer",
    "Research Scientist",
    "Risk Analyst",
    "Robotics Technician",
    "Satellite Systems Engineer",
    "Search Engine Developer",
    "Security Consultant",
    "Semantic Web Developer",
    "Sensor Data Analyst",
    "Service Desk Analyst",
    "Sitecore Developer",
    "Smart Grid Engineer",
    "Software Configuration Manager",
    "Software Deployment Engineer",
    "Software Localization Specialist",
    "Software Release Manager",
    "Space Systems Engineer",
    "Speech Synthesis Engineer",
    "Streaming Media Engineer",
    "Supply Chain Software Developer",
    "Sustainability Data Analyst",
    "Systems Integration Engineer",
    "Technical Account Manager",
    "Telemedicine Developer",
    "Test Automation Engineer",
    "UI Animator",
    "Unreal Engine Developer",
    "User Researcher",
    "Video Compression Engineer",
    "Virtualization Engineer",
    "Voice User Interface Designer",
    "Web Accessibility Specialist",
    "Web Analytics Developer",
    "Web Optimization Specialist",
    "Wireless Systems Engineer",
    "Workflow Automation Specialist",
    "Xamarin Developer",
    "Zero Trust Architect",
    "3D Printing Specialist",
    "AI Trainer",
    "Algorithm Designer",
    "Application Integration Specialist",
    "AR/VR Hardware Engineer",
    "Audio Engineer",
    "Autonomous Vehicle Engineer",
    "Bioinformatics Data Scientist",
    "Blockchain Architect",
    "Business Process Analyst",
    "Chatbot Developer",
    "Cloud Migration Specialist",
    "Computer Network Architect",
    "Content Management System Developer",
    "Control Engineer",
    "Cybersecurity Manager",
    "Data Center Engineer",
    "Data Loss Prevention Specialist",
    "Data Scientist Manager",
    "Digital Transformation Consultant",
    "Distributed Systems Engineer",
    "Drone Software Developer",
    "Edge AI Developer",
    "Embedded AI Engineer",
    "Energy Data Analyst",
    "Enterprise Data Architect",
    "ERP Developer",
    "Ethical AI Specialist",
    "Game AI Programmer",
    "Geospatial Data Scientist",
    "Healthcare IT Specialist",
    "High-Performance Computing Engineer",
    "Human Factors Specialist",
    "Industrial IoT Developer",
    "Information Architect",
    "Infrastructure Architect",
    "Interactive Designer",
    "IT Risk Manager",
    "Knowledge Discovery Engineer",
    "Localization Engineer",
    "Machine Learning Operations Engineer",
    "Mainframe Systems Programmer",
    "Medical Software Developer",
    "Microcontroller Programmer",
    "Mobile Security Specialist",
    "Network Security Engineer",
    "Open Source Advocate",
    "Operations Manager",
    "Performance Optimization Specialist",
    "Platform Developer",
    "Predictive Maintenance Engineer",
    "Quantum Algorithm Developer",
    "Real-Time Data Analyst",
    "Renewable Energy Data Scientist",
    "Research Engineer",
    "Risk Management Consultant",
    "Robotics Software Engineer",
    "Satellite Communications Engineer",
    "Search Engine Optimization Engineer",
    "Security Operations Center Analyst",
    "Semantic Data Modeler",
    "Sensor Fusion Engineer",
    "Service Reliability Engineer",
    "Simulation Software Developer",
    "Smart City Developer",
    "Software Build Engineer",
    "Software Deployment Specialist",
    "Software Internationalization Engineer",
    "Software Packaging Engineer",
    "Spacecraft Software Engineer",
    "Speech Processing Engineer",
    "Streaming Data Engineer",
    "Supply Chain Data Scientist",
    "Sustainability Software Developer",
    "Systems Programmer",
    "Technical Evangelist",
    "Telecommunications Specialist",
    "Test Engineer",
    "UI Developer",
    "Unreal Engine Programmer",
    "User Experience Researcher",
    "Video Game Designer",
    "Virtual Reality Programmer",
    "Voice Recognition Engineer",
    "Web Application Developer",
    "Web Content Manager",
    "Web Performance Engineer",
    "Wireless Network Specialist",
    "Workflow Developer",
    "XaaS Developer",
    "Zero Trust Security Specialist"
}
x = customtkinter.StringVar(value="altro")
scelta_utente = customtkinter.CTkOptionMenu(frame6,variable=x,values=[str(i)for i in lavori],fg_color="black",bg_color="black",text_color="white")
scelta_utente.grid(row=26,column=0,padx=2,pady=10,sticky="we")



label16 = customtkinter.CTkLabel(frame6,text="Scrivi il tuo messaggio qua sotto",text_color="white",font=("Arial",16))
label16.grid(row=27,column=1,padx=5,pady=10,sticky="we")

messaggio = customtkinter.CTkTextbox(frame6,state="normal",width = 150,height=150,text_color="white",fg_color="black",bg_color="black")
messaggio.grid(row=28,padx=5,pady=10,columnspan=2,sticky="we")
button_invio = customtkinter.CTkButton(frame6,text="Invia",text_color="White",fg_color="black",bg_color="Black",command=verifica)
button_invio.grid(row=30,column=0,padx=5,pady=10,sticky="s")
fine = customtkinter.CTkFrame(scrollable_frame,width=250,height=250,bg_color="black",fg_color="Black")
fine.grid(row=31,column = 0,padx=50,pady=50,)
riservatezza  = customtkinter.CTkLabel(master=fine,text="©Salvatore Naro. All rights reserved. Privacy Policy",text_color="White",fg_color="Black",bg_color="Black")
riservatezza.grid(row=32,column=1,padx=20,pady=5,sticky="we")
def open_about_window():
    about_window = customtkinter.CTkToplevel(window)
    about_window.title("About")
    about_window.geometry("600x400")
    about_window.config(bg="Black")
    about_window.resizable(False, False)
    fonte = "Salvatore Naro"
    label33 = customtkinter.CTkLabel(about_window,text=fonte,font = ("Arial",32),text_color="White",fg_color="Black",bg_color="Black")
    label33.pack(pady=10)
    label43 = customtkinter.CTkLabel(about_window,text="Salvatore Naro è riconosciuto per i suoi progetti tra cui Chat-B e Rocket-B",font=("Arial",16),text_color="White",bg_color="Black",fg_color="Black")
    label43.pack(pady=5)
    label53=customtkinter.CTkLabel(about_window,text="Trovami su questi social",bg_color="Black",fg_color="Black",text_color="white",font=("Arial",16))
    label53.pack(pady=5)

    frame_app = customtkinter.CTkFrame(about_window, fg_color="Black", bg_color="Black")
    frame_app.pack(pady=10)
   
    def linkedin():
        testo = "Salvatore Naro"
        pyperclip.copy(testo)
        messagebox.showinfo(title="Profilo Linkedin",message="il nome dell'account  è stato copiato negli appunti")
    def github():
        testo = "Salvatore Naro"
        pyperclip.copy(testo)
        messagebox.showinfo(title="Profilo GitHub",message="il nome dell'account  è stato copiato negli appunti")
    def x():
        testo = "Salvatore Naro"
        pyperclip.copy(testo)
        messagebox.showinfo(title="Profilo X",message="il nome dell'account  è stato copiato negli appunti")

    blue_frame = customtkinter.CTkFrame(frame_app, width=20, height=20, fg_color="Blue", corner_radius=10)
    blue_frame.grid(row=0, column=0, padx=5, pady=5)
    blue_button = customtkinter.CTkButton(frame_app, text="In", text_color="White", fg_color="Black", command=linkedin)
    blue_button.grid(row=0, column=1, padx=5, pady=5)

    pink_frame = customtkinter.CTkFrame(frame_app, width=20, height=20, fg_color="Pink", corner_radius=10)
    pink_frame.grid(row=0, column=2, padx=5, pady=5)
    pink_button = customtkinter.CTkButton(frame_app, text="GitHub", text_color="White", fg_color="Black", command=github)
    pink_button.grid(row=0, column=3, padx=5, pady=5)

    red_frame = customtkinter.CTkFrame(frame_app, width=20, height=20, fg_color="Red", corner_radius=10)
    red_frame.grid(row=0, column=4, padx=5, pady=5)
    red_button = customtkinter.CTkButton(frame_app, text="X", text_color="White", fg_color="Black", command=x)
    red_button.grid(row=0, column=5, padx=5, pady=5)
    labelringraziemento = customtkinter.CTkLabel(frame_app,text="Thanks!",text_color="White",fg_color="black",bg_color="Black",font=("Arial",32))
    labelringraziemento.grid(row=1,column=3,padx=10,pady=10)
    labelsayhello = customtkinter.CTkLabel(frame_app,text="Say hello",text_color="White",fg_color="Black",bg_color="Black",font=("Arial",16))
    labelsayhello.grid(row=2,pady=10,padx=20,column=4)
    labelgmail = customtkinter.CTkLabel(frame_app,text="narosalvo8@gmail.com",text_color="White",fg_color="Black",bg_color="Black",font=("Arial",12))
    labelgmail.grid(row=3,pady=10,padx=20,column=3)

    
    


window.mainloop()
