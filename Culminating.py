from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk

# Initialize the window
window = Tk()
window.title("Food Security")
window.geometry("800x700")
window.resizable(False, False)

# Functions
def intro_image_text1():
    image1_label.config(text='Food insecurity is when people can\'t access \nthe food they need to live their fullest lives.')

def intro_image_text2():
    image2_label.config(text="""Some of the countries most affected by \nfood insecurity include: 

Somalia: A protracted hunger crisis is driven 
by conflict, drought, and economic challenges. 

Yemen: Families in Yemen face a humanitarian \ncrisis due to war.

South Sudan: A weak economy, conflict, and \nwidespread flooding 
are likely to worsen the \nhunger crisis. 
""")

# Variables, Images, and Tkinter Widgets
title_font = Font(
    family="Helvetica",
    size=60,
    weight="normal"
)

# Create Frames for Pages
start_screen = Frame(window, bg="#8FBC8F")
intro_page = Frame(window, bg="#8FBC8F")
solutions_page = Frame(window, bg="#8FBC8F")
problems_page = Frame(window, bg="#8FBC8F")
test_page = Frame(window, bg="#8FBC8F")

# Place all frames in the same location
for frame in (start_screen, intro_page, solutions_page, problems_page, test_page):
    frame.place(relwidth=1, relheight=1)

# Button Style Configuration
button_config = {
    "bg": "#87CEFA",
    "fg": "navy",
    "activebackground": "#87CEFA",
    "activeforeground": "navy",
    "font": ("Arial", 14),
    "width": 25,
    "height": 2,
}

# Start Screen
title = Label(start_screen, text="Food Security", bg="#8FBC8F", fg="navy", font=(title_font))
title.pack(pady=40)

intro_button = Button(
    start_screen,
    text="What is Food Security?",
    **button_config,
    command=lambda: intro_page.tkraise()
)
intro_button.pack(pady=10)

problems_button = Button(
    start_screen,
    text="Problems of Food Insecurity",
    **button_config,
    command=lambda: problems_page.tkraise()
)
problems_button.pack(pady=10)

solutions_button = Button(
    start_screen,
    text="Solutions to Food Insecurity",
    **button_config,
    command=lambda: solutions_page.tkraise()
)
solutions_button.pack(pady=10)

test_button = Button(
    start_screen,
    text="QUIZ!",
    **button_config,
    command=lambda: test_page.tkraise()
)
test_button.pack(pady=10)

# Intro Page
intro_title = Label(intro_page, text="What is Food Security?", bg="#8FBC8F", fg="navy", font=("Ubuntu", 40))
intro_title.pack(pady=50)

# Create a frame to hold the buttons and labels side by side
button_frame = Frame(intro_page, bg="#8FBC8F")
button_frame.pack(pady=20)

# Create container frames for each image+label pair
container1 = Frame(button_frame, bg="#8FBC8F")
container1.pack(side=LEFT, padx=10)

container2 = Frame(button_frame, bg="#8FBC8F")
container2.pack(side=LEFT, padx=10)

# Load and display an image
image1 = Image.open('food insecurity.jpg')
image1 = image1.resize((375, 250), Image.Resampling.LANCZOS)
image1 = ImageTk.PhotoImage(image1)

# First image and its label
image_button1 = Button(container1, command=intro_image_text1, image=image1)
image_button1.pack()
image1_label = Label(container1, text='', bg="#8FBC8F", fg="navy", font=("Helvetica", 14), width=40, height=4, anchor="nw", justify="left")
image1_label.pack(pady=50)

# Load and display an image
image2 = Image.open('food map.jpg')
image2 = image2.resize((375, 250), Image.Resampling.LANCZOS)
image2 = ImageTk.PhotoImage(image2)

# Second image and its label
image_button2 = Button(container2, command=intro_image_text2, image=image2)
image_button2.pack()
image2_label = Label(container2, text='', bg="#8FBC8F", fg="navy", font=("Helvetica", 14), width=40, height=8, anchor="nw", justify="left")
image2_label.pack(pady=20)

# Add "Back to Home" button at the bottom of the page
back_button1 = Button(
    intro_page,
    text="Back to Home",
    **button_config,
    command=lambda: start_screen.tkraise()
)
back_button1.pack(side=BOTTOM, pady=20)

# Problems Page
problems_title = Label(problems_page, text="Problems of Food Insecurity", bg="#8FBC8F", fg="navy", font=("Ubuntu", 40))
problems_title.pack(pady=40)

back_button2 = Button(
    problems_page,
    text="Back to Home",
    **button_config,
    command=lambda: start_screen.tkraise()
)
back_button2.pack(side=BOTTOM, pady=20)

# Display image3 in the problems_page
image3 = Image.open('problems food.png')
image3 = image3.resize((600, 300), Image.Resampling.LANCZOS)
image3 = ImageTk.PhotoImage(image3)

image_frame3 = Frame(problems_page, bg="#8FBC8F")
image_frame3.pack(pady=40)

image_label3 = Label(image_frame3, image=image3, bg="#8FBC8F")
image_label3.pack()


# Solutions Page
solutions_title = Label(solutions_page, text="Solutions to Food Insecurity", bg="#8FBC8F", fg="navy", font=("Ubuntu", 40))
solutions_title.pack(pady=40)

back_button3 = Button(
    solutions_page,
    text="Back to Home",
    **button_config,
    command=lambda: start_screen.tkraise()
)
back_button3.pack(side=BOTTOM, pady=20)

# Display image3 in the problems_page
image4 = Image.open('solutions food.png')
image4 = image4.resize((600, 300), Image.Resampling.LANCZOS)
image4 = ImageTk.PhotoImage(image=image4)

image_frame4 = Frame(solutions_page, bg="#8FBC8F")
image_frame4.pack(pady=40)

image_label4 = Label(image_frame4, image=image4, bg="#8FBC8F")
image_label4.pack()

# Test Page
test_title = Label(test_page, text="QUIZ!!", bg="#8FBC8F", fg="navy", font=("Ubuntu", 40))
test_title.pack(pady=40)


quiz_data = [
    {
        "question": "What is food security?",
        "options": [
            "Having enough food for one day",
            "Having physical and economic access to sufficient, safe, nutritious food",
            "Having a secure place to store food",
            "Having enough money to buy food"
        ],
        "correct": 1
    },
    {
        "question": "Which of these is a major cause of food insecurity?",
        "options": [
            "Poverty",
            "Abundance of food",
            "Too many grocery stores",
            "High literacy rates"
        ],
        "correct": 0
    },
    {
        "question": "Which factor does NOT contribute to food insecurity?",
        "options": [ 
            "Conflict and war",
            "Climate change",
            "Stable government policies",
            "Economic instability"
        ],
        "correct": 2
    },
    {
        "question": "Which region is most affected by food insecurity?",
        "options": [ 
            "Sub-Saharan Africa",
            "Western Europe",
            "North America",
            "East Asia"
        ],
        "correct": 0
    },
    {
        "question": "What percentage of the world's population suffers from hunger?",
        "options": [ 
            "8%",
            "10%",
            "20%",
            "30%"
        ],
        "correct": 1
    },
    {
        "question": "Which organization focuses on eradicating hunger globally?",
        "options": [ 
            "World Food Programme (WFP)",
            "World Health Organization (WHO)",
            "International Monetary Fund (IMF)",
            "United Nations Educational, Scientific and Cultural Organization (UNESCO)"
        ],
        "correct": 0
    },
    {
        "question": "What is one solution to food insecurity?",
        "options": [
            "Help others with their math homework",
            "Give people in poorer countries a plane ticket to the US",
            "Don't give people in need any money",
            "Proper funding for countries in need towards their quality of agriculture and technology."
        ],
        "correct": 3
    },

    {
        "question": "Developed countries",
        "options": [
            "have low levels of food security and less waste",
            "have less food than they need and low levels of waste",
            "have more food than they need and high levels of waste",
            "have high levels of food security and low levels of waste"
        ],
        "correct": 2
    },

    {
        "question": "There is enough food produced in the world to feed everyone.",
        "options": [
            "True",
            "False"
        ],
        "correct": 0
    },

    {
        "question": "If your a country has high food security, can people still be undernourished",
        "options": [
            "Yes",
            "No"
        ],
        "correct": 0
    }
]
class Quiz:
    def __init__(self, master):
        self.master = master
        self.score = 0
        self.current_question = 0
        self.selected_option = IntVar()
        
        # Create quiz widgets
        self.question_label = Label(
            master, 
            wraplength=600,
            bg="#8FBC8F",
            fg="navy",
            font=("Arial", 16)
        )
        self.question_label.pack(pady=20)

        # Create quiz widgets
        self.finish_label = Label(
            master, 
            wraplength=600,
            bg="#8FBC8F",
            fg="navy",
            font=("Arial", 16)
        )
        self.finish_label.pack(pady=20)
        
        self.option_frame = Frame(master, bg="#8FBC8F")
        self.option_frame.pack(pady=10)
        
        # Initialize radio buttons and option texts list
        self.radio_buttons = []
        self.option_texts = []  # Store StringVar for each option

        self.feedback_label = Label(
            master,
            bg="#8FBC8F",
            fg="navy",
            font=("Arial", 12)
        )
        self.feedback_label.pack(pady=10)
        
        self.next_button = Button(
            master,
            text="Next Question",
            **button_config,
            command=self.check_answer
        )
        self.next_button.pack(pady=10)
        
        self.show_question()
    
    def show_question(self):
        if self.current_question < len(quiz_data):
            # Clear existing radio buttons for the previous question
            for rb in self.radio_buttons:
                rb.destroy()
            self.radio_buttons.clear()
            self.option_texts.clear()

            question = quiz_data[self.current_question]
            self.question_label.config(text=question["question"])

            # Create radio buttons for the new question
            i = 0
            while i < len(question["options"]):
                option_text = StringVar()  # Create StringVar for each option
                self.option_texts.append(option_text)  # Store the StringVar
                rb = Radiobutton(
                    self.option_frame,
                    bg="#8FBC8F",
                    fg="navy",
                    font=("Arial", 12),
                    variable=self.selected_option,
                    value=i,  # Set the value as the index of the option
                    textvariable=option_text  # Use textvariable instead of text
                )
                rb.pack(pady=5, anchor='w')
                self.radio_buttons.append(rb)
                i += 1  # Increment the index

            # Update each option's text using StringVar
            for i, option in enumerate(question["options"]):
                self.option_texts[i].set(option)

            self.selected_option.set(-1)  # Reset selection
            self.feedback_label.config(text="")
        else:
            # Quiz completed
            self.question_label.config(text=f"Quiz completed! Your score: {self.score}/{len(quiz_data)}")
            if self.score >= 7 and self.score <= 9:
                self.finish_label.config(text=f"So close to a perfect score! Better luck next time!")
            elif self.score == 10:
                self.finish_label.config(text=f"Perfect score! You got all the questions right!")
            elif self.score < 6:
                self.finish_label.config(text=f"You got less than half of the questions right. You can do better!")
            self.option_frame.pack_forget()
            self.next_button.pack_forget()
            self.feedback_label.config(text="")
    
    def check_answer(self):
        if self.selected_option.get() == -1:
            self.feedback_label.config(text="Please select an answer!", fg="red")
            return
            
        question = quiz_data[self.current_question]
        if self.selected_option.get() == question["correct"]:
            self.score += 1
            self.feedback_label.config(text="Correct!", fg="green")
        else:
            self.feedback_label.config(text="Incorrect!", fg="red")
        
        self.current_question += 1
        self.master.after(1000, self.show_question)


# Modify the test page section
test_title = Label(test_page, text="Food Security Quiz", bg="#8FBC8F", fg="navy", font=("Ubuntu", 40))
test_title.pack(pady=20)

quiz = Quiz(test_page)

back_button4 = Button(
    test_page,
    text="Back to Home",
    **button_config,
    command=lambda: start_screen.tkraise()
)
back_button4.pack(side=BOTTOM, pady=20)

# Show the Start Screen Initially
start_screen.tkraise()

window.mainloop()