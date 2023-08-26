import customtkinter as ctk
from base import *
import random
from CTkMessagebox import CTkMessagebox

root = ctk.CTk()
root.geometry("450x550")
root.title("tdh")


tabs1 = ctk.CTkTabview(root, width=400, height=300)
tabs2 = ctk.CTkTabview(root, width=400, height=490)
tabs2.pack()
tabs3 = ctk.CTkTabview(root, width=400, height=500)


trivia_tab = tabs1.add("Trivia")
daily_tab = tabs2.add("Daily")
historical_tab = tabs3.add("Historical")


def mode_switch():
    if dark_light.get() == "dark":
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")


dark_light = ctk.CTkSwitch(historical_tab, text="", onvalue="dark", offvalue="light", command=mode_switch)
dark_light.place(x=340, y=4)

dark_light_label = ctk.CTkLabel(historical_tab, fg_color="transparent", text="Dark Mode:", font=("Bahnschrift", 12))
dark_light_label.place(x=275, y=1)

frame1 = ctk.CTkFrame(root, width=400, height=100)

frame2 = ctk.CTkFrame(trivia_tab, width=375, height=60)
frame2.pack(pady=20)

def select_tab1():
    tabs2.forget()
    tabs3.forget()
    tabs1.pack()
    frame1.place(x=25, y=370)
    tabs1.set("Trivia")


def select_tab2():
    frame1.place_forget()
    tabs1.forget()
    tabs3.forget()
    tabs2.pack()
    tabs2.set("Daily")


def select_tab3():
    frame1.place_forget()
    tabs1.forget()
    tabs2.forget()
    tabs3.pack()
    tabs3.set("Historical")


FONT = ("Bahnschrift", 20)
trivia_button = ctk.CTkButton(root, text="Trivia", width=130, font=FONT, command=select_tab1, corner_radius=0)
trivia_button.place(x=30, y=500)

daily_button = ctk.CTkButton(root, text="Daily", width=130, font=FONT, command=select_tab2, corner_radius=0)
daily_button.place(x=161, y=500)

historical_button = ctk.CTkButton(root, text="Historical", width=130, font=FONT, command=select_tab3, corner_radius=0)
historical_button.place(x=292, y=500)


trivia_categories = ["General Knowledge", "Books", "Film", "Music", "Sports", "History", "Geography", "Mythology",
                     "Video Games", "Animals", "Nature", "Politics"]

trivia_categories_dict = {"General Knowledge": 9, "Books": 10, "Film": 11, "Music": 12, "Mythology": 20, "Sports": 21,
                          "Geography": 22, "History": 23, "Video Games": 15, "Animals": 27, "Nature": 17, "Politics": 24}


trivia_categories_combobox = ctk.CTkComboBox(frame1, state="readonly", values=trivia_categories, width=130, corner_radius=15)
trivia_categories_combobox.place(x=5, y=10)
trivia_categories_combobox.set("Categories")

difficulty_list = ["Easy", "Medium", "Hard"]
difficulty_combobox = ctk.CTkComboBox(frame1, state="readonly", values=difficulty_list, width=130, corner_radius=15)
difficulty_combobox.place(x=5, y=40)
difficulty_combobox.set("Difficulty")

questions_type = ["Multiple", "Boolean"]
questions_type_combobox = ctk.CTkComboBox(frame1, state="readonly", values=questions_type, width=130, corner_radius=15)
questions_type_combobox.place(x=5, y=70)
questions_type_combobox.set("Question Type")


def compose_question():
    try:
        a = trivia_categories_combobox.get()
        if a in trivia_categories_dict.keys():
            c = trivia_categories_dict[a]
        else:
            c = 9

        trivia1 = Trivia(c, difficulty_combobox.get().lower(), questions_type_combobox.get().lower())
        abc = trivia1.trivia_func()
        question = abc['question']
        correct_answer = abc['correct_answer']
        incorrect_answers = abc['incorrect_answers']
        incorrect_answers.append(correct_answer)
        answers_list = incorrect_answers
        random.shuffle(answers_list)

        question_label = ctk.CTkTextbox(frame2, width=350, fg_color="transparent")
        question_label.insert("0.0", question)
        question_label.place(x=10, y=10)
        question_label.configure(state="disabled")

        answers_menu_var = ctk.StringVar(value="Options")
        answers_menu = ctk.CTkOptionMenu(trivia_tab, values=answers_list, variable=answers_menu_var, font=FONT2)
        answers_menu.place(x=130, y=100)
    except:
        CTkMessagebox(title="Info", message="""\nThe combination you have chosen may not contain a question.
                                                \nTry a different combination.""", font=FONT2)

    def check_answer():
        if answers_menu.get() == correct_answer:
            CTkMessagebox(title="Info", message="Correct!", font=FONT)
        else:
            CTkMessagebox(title="Info", message=f"Incorrect Answer\n Correct Answer : {correct_answer}", font=FONT)

    question_button2 = ctk.CTkButton(trivia_tab, text="Check!", width=80, command=check_answer, font=FONT2)
    question_button2.place(x=150, y=180)


FONT2 = ("Bahnschrift", 15)

question_button = ctk.CTkButton(frame1, text="Compose!", width=80, command=compose_question, font=FONT2)
question_button.place(x=180, y=40)


useless_fact_frame = ctk.CTkFrame(daily_tab, width=400, height=70)
useless_fact_frame.place(y=30)

useless_fact_title = ctk.CTkLabel(daily_tab, text="Useless Fact:", font=FONT2)
useless_fact_title.place(x=10, y=5)

fact_frame = ctk.CTkFrame(daily_tab, width=400, height=70)
fact_frame.place(y=130)

fact_title = ctk.CTkLabel(daily_tab, text="Random Fact:", font=FONT2)
fact_title.place(x=10, y=105)

joke_frame = ctk.CTkFrame(daily_tab, width=400, height=70)
joke_frame.place(y=230)

joke_title = ctk.CTkLabel(daily_tab, text="Joke:", font=FONT2)
joke_title.place(x=10, y=205)

joke_box_var = ctk.StringVar(value="Joke Categories")
joke_box = ctk.CTkOptionMenu(daily_tab, values=["Programming", "Miscellaneous", "Dark", "Pun", "Spooky"],
                             variable=joke_box_var, font=("Bahnschrift", 14))
joke_box.place(x=245, y=410)

quote_frame = ctk.CTkFrame(daily_tab, width=400, height=70)
quote_frame.place(y=330)

quote_title = ctk.CTkLabel(daily_tab, text="Quote", font=FONT2)
quote_title.place(x=10, y=305)
quotes_categories = ["Attitude", "Business", "Change", "Education", "Experience", "Graduation", "Happiness",
                     "Imagination", "Intelligence", "Knowledge", "Leadership", "Success"]

quote_box_var = ctk.StringVar(value="Quote Categories")
quote_box = ctk.CTkOptionMenu(daily_tab, values=quotes_categories, variable=quote_box_var, font=("Bahnschrift", 14))
quote_box.place(x=5, y=410)


def get_daily():
    try:
        useless_fact_var = useless_fact()
        fact_var = facts()
        joke_var = joke_box.get()
        joke_cat_var = Joker(f"{joke_var}")
        joke_output = joke_cat_var.joker_func()
        quote_var = quote_box.get()
        quote, quote_author = quotes(f"{quote_var}")

        useless_fact_label = ctk.CTkTextbox(useless_fact_frame, fg_color="transparent", width=350, height=60)
        useless_fact_label.insert("0.0", useless_fact_var)
        useless_fact_label.place(x=20, y=5)
        useless_fact_label.configure(state="disabled")

        fact_label = ctk.CTkTextbox(fact_frame, fg_color="transparent", width=350, height=60)
        fact_label.insert("0.0", fact_var)
        fact_label.place(x=20, y=5)
        fact_label.configure(state="disabled")

        if type(joke_output) != list:
            joke_label = ctk.CTkTextbox(joke_frame, fg_color="transparent", width=350, height=60)
            joke_label.insert("0.0", joke_output)
            joke_label.place(x=20, y=5)
            joke_label.configure(state="disabled")

        elif type(joke_output) == list:
            joke_label = ctk.CTkTextbox(joke_frame, fg_color="transparent", width=350, height=60)
            joke_label.insert("0.0", joke_output[0] + "\n")
            joke_label.insert("2.0", joke_output[1])
            joke_label.place(x=20, y=5)
            joke_label.configure(state="disabled")

        quote_label = ctk.CTkTextbox(quote_frame, fg_color="transparent", width=350, height=70)
        quote_label.insert("0.0", quote + "\n -" + quote_author)
        quote_label.place(x=20, y=5)
        quote_label.configure(state="disabled")
    except:
        CTkMessagebox(title="Error", message="""Try again! \n\n •You might not have chosen the joke and quotes categories.
                                                                • It could be a API error.""")


qq = ctk.CTkButton(daily_tab, text="Get!", command=get_daily, width=80, font=FONT2)
qq.place(x=160, y=410)


historical_tab_frame1 = ctk.CTkFrame(historical_tab, width=380, height=250, corner_radius=20)
historical_tab_frame1.place(x=5, y=30)


def checkbox_event():
    checkbox2.deselect()


check_var = ctk.StringVar(value="off")
checkbox = ctk.CTkCheckBox(historical_tab, text="Event", command=checkbox_event, font=FONT2,
                                           variable=check_var, onvalue="on", offvalue="off")
checkbox.place(x=110, y=300)
checkbox.deselect()


def checkbox_event2():
    checkbox.deselect()


check_var2 = ctk.StringVar(value="off")
checkbox2 = ctk.CTkCheckBox(historical_tab, text="Figure", command=checkbox_event2, font=FONT2,
                                         variable=check_var2, onvalue="on", offvalue="off")
checkbox2.place(x=220, y=300)
checkbox2.deselect()

historical_tab_frame2 = ctk.CTkFrame(historical_tab, width=280, height=100, corner_radius=20)
historical_tab_frame2.place(x=70, y=330)

historical_entry = ctk.CTkEntry(historical_tab_frame2)
historical_entry.place(x=30, y=60)

historical_entry_label = ctk.CTkLabel(historical_tab_frame2, text="Enter the word you want to search for."
                                                                  "\n(Ex: Atatürk, Roman Empire etc.)", font=FONT2)
historical_entry_label.place(x=20, y=10)


def get_historical():
    if check_var.get() == "on":
        historical_entry_input = historical_entry.get()
        test = Historical(f"{historical_entry_input}")
        test1 = test.historical_event()

        historical_textbox = ctk.CTkTextbox(historical_tab_frame1, fg_color="transparent", width=350, height=250)
        historical_textbox.insert("0.0", random.choice(test1)["event"])
        historical_textbox.insert("25.0", random.choice(test1)["year"])

        historical_textbox.place(x=20, y=5)

    elif check_var2.get() == "on":
        historical_entry_input = historical_entry.get()
        test = Historical(f"{historical_entry_input}")
        test1 = test.historical_figure()

        historical_textbox = ctk.CTkTextbox(historical_tab_frame1, fg_color="transparent", width=350, height=250)
        historical_textbox.insert("0.0", test1[0]["name"]+"\n")
        historical_textbox.insert("2.0", test1[0]["title"]+"\n")
        for key, value in test1[0]["info"].items():
            metin = f"{key}: {value}\n"
            historical_textbox.insert("end", metin)

        historical_textbox.place(x=20, y=5)
        historical_textbox.configure(state="disabled")

    else:
        CTkMessagebox(title="Info", message="You have to select event or figure.")


get_event_button = ctk.CTkButton(historical_tab_frame2, text="Get!", width=80, command=get_historical, font=FONT2)
get_event_button.place(x=180, y=60)


root.mainloop()
