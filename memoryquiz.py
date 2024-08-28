import tkinter as tk
from tkinter import messagebox
import random

class MemoryQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Quiz Game")

        self.score = 0
        self.questions = [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
            {"question": "What is 6 multiplied by 8?", "answer": "48"},
        ]

        self.current_question = None

        self.create_widgets()

    def show_question(self):
        self.current_question = random.choice(self.questions)
        self.question_label.config(text=self.current_question["question"])
        self.answer_entry.delete(0, tk.END)

    def check_answer(self):
        user_answer = self.answer_entry.get()
        correct_answer = self.current_question["answer"]
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", f"Sorry, the correct answer is {correct_answer}")
        self.score_label.config(text=f"Score: {self.score}")
        self.show_question()

    def create_widgets(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.root.quit)

        self.question_label = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.question_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        self.answer_label = tk.Label(self.root, text="Your Answer:", font=("Helvetica", 12))
        self.answer_label.grid(row=1, column=0, padx=20, pady=10, sticky="e")

        self.answer_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.answer_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        self.check_button = tk.Button(self.root, text="Check Answer", font=("Helvetica", 12), command=self.check_answer)
        self.check_button.grid(row=2, column=0, columnspan=2, pady=20)

        self.score_label = tk.Label(self.root, text="Score: 0", font=("Helvetica", 14, "bold"))
        self.score_label.grid(row=3, column=0, columnspan=2, pady=10)

        self.show_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = MemoryQuizApp(root)
    root.mainloop()
