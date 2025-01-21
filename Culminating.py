# Import necessary libraries for the application
from tkinter import *  # For creating the GUI
from tkinter.font import Font  # For working with custom fonts
from PIL import Image, ImageTk  # For handling and displaying images in Tkinter
from quiz_data import quiz_data1  # Import quiz data from an external file
import random  # For shuffling questions and options in the quiz

# Initialize the main application window
window = Tk() 
window.title("Food Security")  # Set the window title
window.geometry("800x700")  # Define the window size
window.resizable(False, False)  # Prevent the user from resizing the window

# Define functions to display text below the images on the intro page
def intro_image_text1():
    
    #Updates the text below the first image on the intro page 
    #with a description of food insecurity.
    
    image1_label.config(text='Food insecurity is when people can\'t access \nthe food they need to live their fullest lives.')

def intro_image_text2():

    #Updates the text below the second image on the intro page 
    #with a description of countries affected by food insecurity.

    image2_label.config(text="""Some of the countries most affected by \nfood insecurity include: 

Somalia: A protracted hunger crisis is driven 
by conflict, drought, and economic challenges. 

Yemen: Families in Yemen face a humanitarian \ncrisis due to war.

South Sudan: A weak economy, conflict, and \nwidespread flooding 
are likely to worsen the \nhunger crisis. 
""")

# Configure a custom font for the title
title_font = Font(
    family="Helvetica",  # Font family
    size=60,  # Font size
    weight="normal"  # Weight (normal or bold)
)

# Create frames for different sections/pages of the application
start_screen = Frame(window, bg="#8FBC8F")  # Home/start screen
intro_page = Frame(window, bg="#8FBC8F")  # Introduction page
solutions_page = Frame(window, bg="#8FBC8F")  # Solutions page
problems_page = Frame(window, bg="#8FBC8F")  # Problems page
test_page = Frame(window, bg="#8FBC8F")  # Quiz page

# Place all frames in the same position and size to overlap
for frame in (start_screen, intro_page, solutions_page, problems_page, test_page):
    frame.place(relwidth=1, relheight=1)  # Make the frame cover the full window

# Define a dictionary for button styling
button_config = {
    "bg": "#87CEFA",  # Background color of the button
    "fg": "navy",  # Foreground (text) color of the button
    "activebackground": "#87CEFA",  # Button color when pressed
    "activeforeground": "navy",  # Text color when button is pressed
    "font": ("Arial", 14),  # Font style and size for button text
    "width": 25,  # Width of the button
    "height": 2,  # Height of the button
}

# Start Screen
# Title label for the start screen
title = Label(
    start_screen, 
    text="Food Security",  # Title text
    bg="#8FBC8F",  # Background color
    fg="navy",  # Text color
    font=(title_font)  # Use the custom font
)
title.pack(pady=40)  # Add vertical padding

# Button to navigate to the intro page
intro_button = Button(
    start_screen,
    text="What is Food Security?",  # Button label
    **button_config,  # Apply button styles
    command=lambda: intro_page.tkraise()  # Switch to the intro page when clicked
)
intro_button.pack(pady=10)  # Add vertical padding

# Button to navigate to the problems page
problems_button = Button(
    start_screen,
    text="Problems of Food Insecurity",  # Button label
    **button_config,
    command=lambda: problems_page.tkraise()  # Switch to the problems page when clicked
)
problems_button.pack(pady=10)

# Button to navigate to the solutions page
solutions_button = Button(
    start_screen,
    text="Solutions to Food Insecurity",  # Button label
    **button_config,
    command=lambda: solutions_page.tkraise()  # Switch to the solutions page when clicked
)
solutions_button.pack(pady=10)

# Button to navigate to the quiz page
test_button = Button(
    start_screen,
    text="QUIZ!",  # Button label
    **button_config,
    command=lambda: test_page.tkraise()  # Switch to the quiz page when clicked
)
test_button.pack(pady=10)

# Intro Page
# Title for the intro page
intro_title = Label(
    intro_page, 
    text="What is Food Security?",  # Title text
    bg="#8FBC8F",  # Background color
    fg="navy",  # Text color
    font=("Ubuntu", 40)  # Font settings
)
intro_title.pack(pady=50)  # Add vertical padding

# Container to hold the buttons and labels side by side
button_frame = Frame(intro_page, bg="#8FBC8F")
button_frame.pack(pady=20)

# Create containers for images and labels
container1 = Frame(button_frame, bg="#8FBC8F")  # First image and label container
container1.pack(side=LEFT, padx=10)  # Pack to the left with padding

container2 = Frame(button_frame, bg="#8FBC8F")  # Second image and label container
container2.pack(side=LEFT, padx=10)

# Load the first image
image1 = Image.open('food insecurity.jpg')  # Open the image file
image1 = image1.resize((375, 250), Image.Resampling.LANCZOS)  # Resize the image
image1 = ImageTk.PhotoImage(image1)  # Convert image for Tkinter

# Button displaying the first image, triggers a text update
image_button1 = Button(container1, command=intro_image_text1, image=image1)
image_button1.pack()

# Label for the text below the first image
image1_label = Label(
    container1, 
    text='',  # Initially empty
    bg="#8FBC8F", 
    fg="navy", 
    font=("Helvetica", 14),  # Font settings
    width=40,  # Fixed width
    height=4,  # Fixed height
    anchor="nw",  # Align text to top-left
    justify="left"  # Align text to left
)
image1_label.pack(pady=50)

# Load the second image
image2 = Image.open('food map.jpg')  # Open the image file
image2 = image2.resize((375, 250), Image.Resampling.LANCZOS)  # Resize the image
image2 = ImageTk.PhotoImage(image2)  # Convert image for Tkinter

# Button displaying the second image, triggers a text update
image_button2 = Button(container2, command=intro_image_text2, image=image2)
image_button2.pack()

# Label for the text below the second image
image2_label = Label(
    container2, 
    text='',  # Initially empty
    bg="#8FBC8F", 
    fg="navy", 
    font=("Helvetica", 14), 
    width=40,  # Fixed width
    height=8,  # Fixed height
    anchor="nw",  # Align text to top-left
    justify="left"  # Align text to left
)
image2_label.pack(pady=20)

# Back button for the intro page
back_button1 = Button(
    intro_page,
    text="Back to Home",  # Button label
    **button_config,
    command=lambda: start_screen.tkraise()  # Switch back to the start screen
)
back_button1.pack(side=BOTTOM, pady=20)

# Problems Page
# Title for the problems page
problems_title = Label(
    problems_page,
    text="Problems of Food Insecurity",  # Title text
    bg="#8FBC8F",  # Background color
    fg="navy",  # Text color
    font=("Ubuntu", 40)  # Font settings
)
problems_title.pack(pady=40)

# Back button for the problems page
back_button2 = Button(
    problems_page,
    text="Back to Home",  # Button label
    **button_config,
    command=lambda: start_screen.tkraise()  # Switch back to the start screen
)
back_button2.pack(side=BOTTOM, pady=20)

# Load the image for the problems page
image3 = Image.open('problems food.png')  # Open the image file
image3 = image3.resize((600, 300), Image.Resampling.LANCZOS)  # Resize the image
image3 = ImageTk.PhotoImage(image3)  # Convert image for Tkinter

# Frame to display the image on the problems page
image_frame3 = Frame(problems_page, bg="#8FBC8F")
image_frame3.pack(pady=40)

# Label to display the image on the problems page
image_label3 = Label(image_frame3, image=image3, bg="#8FBC8F")
image_label3.pack()

# Solutions Page
solutions_title = Label(solutions_page, text="Solutions to Food Insecurity", bg="#8FBC8F", fg="navy", font=("Ubuntu", 40)) # Title Text
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

class Quiz:
    def __init__(self, master):
        self.master = master
        self.score = 0
        self.current_question = 0
        self.selected_option = IntVar()

        # Shuffle the questions
        self.quiz_data = quiz_data1[:]  # Make a copy of the quiz data
        random.shuffle(self.quiz_data)

        # Create quiz widgets
        self.question_label = Label(
            master, 
            wraplength=600,
            bg="#8FBC8F",
            fg="navy",
            font=("Arial", 16)
        )
        self.question_label.pack(pady=20)

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
        
        self.radio_buttons = []
        self.option_texts = []
        # Label to encourage user to keep going in the quiz
        self.feedback_label = Label(
            master,
            bg="#8FBC8F",
            fg="navy",
            font=("Arial", 12)
        )
        self.feedback_label.pack(pady=10)
        # Button to go to the next question
        self.next_button = Button(
            master,
            text="Next Question",
            **button_config,
            command=self.check_answer
        )
        self.next_button.pack(pady=10)
        
        self.show_question()
    
    def show_question(self):
        if self.current_question < len(self.quiz_data):
            # Clear existing radio buttons for the previous question
            for rb in self.radio_buttons:
                rb.destroy()
            self.radio_buttons.clear()
            self.option_texts.clear()

            question = self.quiz_data[self.current_question]
            self.question_label.config(text=question["question"])

            # Shuffle the options for the current question
            options = question["options"][:]
            correct_index = question["correct"]
            option_mapping = list(enumerate(options))
            random.shuffle(option_mapping)

            # Update options and correct index after shuffling
            shuffled_options = [opt[1] for opt in option_mapping]
            new_correct_index = [opt[0] for opt in option_mapping].index(correct_index)

            question["options"] = shuffled_options
            question["correct"] = new_correct_index

            # Create radio buttons for the shuffled options
            for i, option in enumerate(shuffled_options):
                option_text = StringVar()
                self.option_texts.append(option_text)
                rb = Radiobutton(
                    self.option_frame,
                    bg="#8FBC8F",
                    fg="navy",
                    font=("Arial", 12),
                    variable=self.selected_option,
                    value=i,
                    textvariable=option_text
                )
                rb.pack(pady=5, anchor='w')
                self.radio_buttons.append(rb)
                option_text.set(option)

            self.selected_option.set(-1)  # Reset selection
            self.feedback_label.config(text="")
        else: # Encouraging the user based on their score
            self.question_label.config(text=f"Quiz completed! Your score: {self.score}/{len(self.quiz_data)}")
            if self.score >= 7:
                self.finish_label.config(text="Great job!")
            else:
                self.finish_label.config(text="Keep practicing!")
            self.option_frame.pack_forget()
            self.next_button.pack_forget()

    def check_answer(self):
        if self.selected_option.get() == -1:  # Check if no option was selected
            self.feedback_label.config(text="Please select an answer!", fg="red")
            return

        question = self.quiz_data[self.current_question]
        if self.selected_option.get() == question["correct"]:  # Check if the selected answer is correct
            self.score += 1
            if not self.score < len(self.quiz_data) // 2:  # Nested `if` using `not`: Score is at least halfway
                self.feedback_label.config(
                    text=f"Correct! You're doing great! Current score: {self.score}", fg="green"
                )
            else:
                self.feedback_label.config(
                    text=f"Correct! Keep going! Current score: {self.score}", fg="green"
                )
        else:  # Outer `if` condition: Incorrect answer
            if not self.score == 0:  # Nested `if` using `not`: Score is not zero
                self.feedback_label.config(
                    text=f"Incorrect! Don't lose hope! Score: {self.score}", fg="red"
                )
            else:
                self.feedback_label.config(
                    text="Incorrect! Let's try harder on the next one!", fg="red"
                )

        self.current_question += 1
        self.master.after(1000, self.show_question)


# Modify the test page section
test_title = Label(test_page, text="Food Security Quiz", bg="#8FBC8F", fg="navy", font=("Ubuntu", 40))
test_title.pack(pady=20)

#Start the quiz once on the page
quiz = Quiz(test_page)

#Button to go back to the home page
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