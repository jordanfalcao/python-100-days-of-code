from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):  # quiz_brain is type: QuizBrain object
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question here.",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, pady=50, columnspan=2)

        self.true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.true_pressed, bd=0)
        self.true_button.grid(row=2, column=1)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.false_pressed, bd=0)
        self.false_button.grid(row=2, column=0)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 16))
        self.score_label.grid(row=0, column=1)

        self.get_next_question()  # method created

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()  # inherited method from QuizBrain
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.buttons_state(ACTIVE)  # active the button if still has questions
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the questions.")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("true"))  # SAME
        self.buttons_state(DISABLED)  # fix the button bug

    def false_pressed(self):
        is_right = self.quiz.check_answer("false")  # SAME
        self.give_feedback(is_right)
        self.buttons_state(DISABLED)  # fix the button bug

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    # fix the bug when rapid click the buttons
    def buttons_state(self, state: str):
        self.true_button.config(state=state)
        self.false_button.config(state=state)