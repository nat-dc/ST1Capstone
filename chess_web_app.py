from flask import Flask, Blueprint, render_template, redirect, url_for, request
from werkzeug.middleware.proxy_fix import ProxyFix
import sys
from argparse import ArgumentParser
from chess_model import *

appweb = Blueprint('hello', __name__)

@appweb.route('/')
def home():
    return render_template("index.html")

@appweb.route('/send', methods=['POST'])
def send(predict=predict):
    if request.method == 'POST':
        rated = request.form['rated']
        time_increment = request.form['time_increment']
        white_rating = request.form['white_rating']
        black_rating = request.form['black_rating']
        openingmoves = request.form['openingmoves']
        openingshortname = request.form['openingshortname']
        openingresponse = request.form['openingresponse']
        openingvariation = request.form['openingvariation']

        if rated == 'True':
            rated = 1
        else:
            rated = 0

        time_increment = int(time_increment)
        white_rating = int(white_rating)
        black_rating = int(black_rating)
        opening_moves = int(openingmoves)
        opening_shortname = int(openingshortname)
        opening_response = int(openingresponse)
        opening_variation = int(openingvariation)

        # Accuracy of Model
        best_model.fit(x_train, y_train)  # <-- this line
        acc = best_model.score(x_train, y_train)

        chess_info = [rated, time_increment, white_rating, black_rating, opening_moves, opening_shortname,
                      opening_response, opening_variation]

        chess_prediction = best_model.predict([chess_info])
        disp_string = ("This prediction has an accuracy of:", str(model_accuracy))

        result = chess_prediction

        if (chess_prediction == [0]):
            predict = (disp_string, '\n', "Black Wins")
        elif (chess_prediction == [1]):
            predict = (disp_string, '\n', "Draw")
        else:
            predict = (disp_string, '\n', "White Wins")

        return render_template('index.html', predict=predict)

    else:
        return render_template('index.html', predict=predict)

@appweb.route('/about')
def about():
    return render_template("about.html")



if __name__ == '__main__':

    # arg parser for the standard anaconda-project options
    parser = ArgumentParser(prog="home",
                            description="Simple Flask Application")
    parser.add_argument('--anaconda-project-host', action='append', default=[],
                        help='Hostname to allow in requests')
    parser.add_argument('--anaconda-project-port', action='store', default=8086, type=int,
                        help='Port to listen on')
    parser.add_argument('--anaconda-project-iframe-hosts',
                        action='append',
                        help='Space-separated hosts which can embed us in an iframe per our Content-Security-Policy')
    parser.add_argument('--anaconda-project-no-browser', action='store_true',
                        default=False,
                        help='Disable opening in a browser')
    parser.add_argument('--anaconda-project-use-xheaders',
                        action='store_true',
                        default=False,
                        help='Trust X-headers from reverse proxy')
    parser.add_argument('--anaconda-project-url-prefix', action='store', default='',
                        help='Prefix in front of urls')
    parser.add_argument('--anaconda-project-address',
                        action='store',
                        #default='0.0.0.0',
                        help='IP address the application should listen on.')

    args = parser.parse_args()

    app = Flask(__name__)
    app.register_blueprint(appweb, url_prefix = args.anaconda_project_url_prefix)

    app.config['PREFERRED_URL_SCHEME'] = 'https'

    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(host=args.anaconda_project_address, port=args.anaconda_project_port)

