import tkinter as tk
from chess_model import *


class chess_GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title = ('Chess Model Predictor')

        self.one_frame = tk.Frame()
        self.two_frame = tk.Frame()
        self.three_frame = tk.Frame()
        self.four_frame = tk.Frame()
        self.five_frame = tk.Frame()
        self.six_frame = tk.Frame()
        self.seven_frame = tk.Frame()
        self.eight_frame = tk.Frame()
        self.nine_frame = tk.Frame()
        self.ten_frame = tk.Frame()

        self.title_label = tk.Label(self.one_frame, text='CHESS GAME RESULT PREDICTOR', fg="Black", font=("Helvetica", 18))
        self.title_label.pack()

        # Create the widgets for two frame. (age input)
        self.rated_label = tk.Label(self.two_frame, text='Rated:')
        self.rated_entry = tk.Entry(self.two_frame, bg="white", fg="black", width=10)
        self.rated_label.pack(side='left')
        self.rated_entry.pack(side='left')

        self.increment_label = tk.Label(self.three_frame, text='Time Increment:')
        self.increment_entry = tk.Entry(self.three_frame, bg="white", fg="black", width=10)
        self.increment_label.pack(side='left')
        self.increment_entry.pack(side='left')

        self.whiterating_label = tk.Label(self.four_frame, text='White Rating:')
        self.whiterating_entry = tk.Entry(self.four_frame, bg="white", fg="black", width=10)
        self.whiterating_label.pack(side='left')
        self.whiterating_entry.pack(side='left')

        self.blackrating_label = tk.Label(self.five_frame, text='Black Rating:')
        self.blackrating_entry = tk.Entry(self.five_frame, bg="white", fg="black", width=10)
        self.blackrating_label.pack(side='left')
        self.blackrating_entry.pack(side='left')

        self.openingmoves_label = tk.Label(self.six_frame, text='Opening Moves Count:')
        self.openingmoves_entry = tk.Entry(self.six_frame, bg="white", fg="black", width=10)
        self.openingmoves_label.pack(side='left')
        self.openingmoves_entry.pack(side='left')

        self.openingshortname_label = tk.Label(self.seven_frame, text='Opening Shortname:')
        self.openingshortname_entry = tk.Entry(self.seven_frame, bg="white", fg="black", width=10)
        self.openingshortname_label.pack(side='left')
        self.openingshortname_entry.pack(side='left')

        self.openingresponse_label = tk.Label(self.eight_frame, text='Opening Response:')
        self.openingresponse_entry = tk.Entry(self.eight_frame, bg="white", fg="black", width=10)
        self.openingresponse_label.pack(side='left')
        self.openingresponse_entry.pack(side='left')

        self.openingvariation_label = tk.Label(self.nine_frame, text='Opening Variation:')
        self.openingvariation_entry = tk.Entry(self.nine_frame, bg="white", fg="black", width=10)
        self.openingvariation_label.pack(side='left')
        self.openingvariation_entry.pack(side='left')

        self.resultpredict_text = tk.Text(self.ten_frame, height=10, width=25, bg='light blue')
        self.resultpredict_text.pack(side='left')

        self.btn_predict = tk.Button(self.ten_frame, text='Predict Chess Result', command=self.predict_result)
        self.btn_quit = tk.Button(self.ten_frame, text='Quit', command=self.root.destroy)
        self.btn_predict.pack()
        self.btn_quit.pack()


        self.one_frame.pack()
        self.two_frame.pack()
        self.three_frame.pack()
        self.four_frame.pack()
        self.five_frame.pack()
        self.six_frame.pack()
        self.seven_frame.pack()
        self.eight_frame.pack()
        self.nine_frame.pack()
        self.ten_frame.pack()

        self.root.mainloop()

    def predict_result(self):
        result_string = ""
        self.resultpredict_text.delete(0.0, tk.END)

        if self.rated_entry.get() == 'True':
            rated = 1
        else:
            rated = 0

        time_increment = int(self.increment_entry.get())
        white_rating = int(self.whiterating_entry.get())
        black_rating = int(self.blackrating_entry.get())
        opening_moves = int(self.openingmoves_entry.get())
        opening_shortname = int(self.openingshortname_entry.get())
        opening_response = int(self.openingresponse_entry.get())
        opening_variation = int(self.openingvariation_entry.get())

        #opening shortname, response and variation are strings and rated is a bool so i tried to convert them to integers with the ordinal encoder
        chess_info = [rated, time_increment, white_rating, black_rating, opening_moves, opening_shortname,
                      opening_response, opening_variation]

        chess_prediction = best_model.predict([chess_info])
        disp_string = ("This prediction has an accuracy of:", str(model_accuracy))

        result = chess_prediction

        if (chess_prediction == [0]):
            result_string = (disp_string , '\n' , "Black Wins")
        elif (chess_prediction == [1]):
            result_string = (disp_string , '\n' , "Draw")
        else:
            result_string = (disp_string , '\n' , "White Wins")

        self.resultpredict_text.insert(1.0,result_string)





my_chess_GUI = chess_GUI()

