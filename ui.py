import tkinter
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
SCORE_FONT = ("Arial", 12, "normal")
QUESTION_FONT = ("Arial", 20, "italic")

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # build ui window
        self.window = tkinter.Tk()
        self.window.title("Quizler")
        self.window.config(padx=18, pady=18,
                bg=THEME_COLOR
        )
        # score label
        self.score_label = tkinter.Label(text = "Score: 0",
                                font = SCORE_FONT,
                                bg=THEME_COLOR,
                                fg = "white"        
        )
        self.score_label.grid(row = 0, column = 1)
        # question canvas
        self.canvas = tkinter.Canvas(width=306,
                                        height=252,
                                        bg="white",
                                        highlightthickness=0
        )
        self.question_text = self.canvas.create_text(153, 126, 
                                            text="question", 
                                            fill="black", 
                                            font=(QUESTION_FONT),
                                            width=288
        
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=36)
        # false button
        false_img = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(image=false_img,
                                        highlightthickness=0,
                                        command=self.false_button_clicked
        )
        self.false_button.grid(row=2, column=0)
        # true button
        true_img = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(image=true_img,
                                            highlightthickness=0,
                                            command=self.true_button_clicked
        )
        self.true_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, 
                                    text=q_text
            )
        else:
            self.canvas.itemconfig(self.question_text,
                                    text="You've Completed This Quiz"
            )
            # disable buttons
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_button_clicked(self):
        is_right = self.quiz.check_answer("True")
        self.screen_feedback(is_right)

    def false_button_clicked(self):
        is_right = self.quiz.check_answer("False")
        self.screen_feedback(is_right)

    def screen_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else: 
            self.canvas.config(bg="red")
        # after one second go to the next question
        self.window.after(ms=1000, 
                            func=self.get_next_question
        )

