from flask import Flask, render_template, request
from helpers import corresponding_link_getter, count_points, most_answered, find_villain, user

app: Flask = Flask(__name__)
users: list[user] = []
user_number: int = 0


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        global users
        global user_number

        fname: str = request.form['fname']
        lname: str = request.form['lname']
        pop_song: str = request.form['favorite pop song']
        rap_song: str = request.form['favorite rap song']
        throwback_song: str = request.form['favorite throwback song']
        disney_song: str = request.form['favorite disney song']
        musical_song: str = request.form['favorite musical song']
        christmas_song: str = request.form['favorite christmas song']
        classical_song: str = request.form['favorite classical song']
        international_song: str = request.form['favorite international song']
        answer_choices: list[str] = [pop_song, rap_song, throwback_song, disney_song, musical_song, christmas_song, classical_song, international_song]

        if fname == '' or lname == '':
            return render_template("quiz.html")

        total_points: dict[str, int] = count_points(answer_choices)
        most_chosen_answer: str = most_answered(total_points)
        villain: str = find_villain(most_chosen_answer)
        image_link: str = corresponding_link_getter(villain)
        new_user: user = user(user_number, fname, lname, villain)
        users.append(new_user)

        user_number += 1

        return render_template("result.html", villain=villain, image_link=image_link)
    return render_template("quiz.html")


@app.route('/all-results')
def all_results():
    return render_template('all-results.html', users=users)


@app.route('/user<usernumber>')
def display_user(usernumber: str):
    return render_template('user.html', user=users[int(usernumber)])


if __name__ == '__main__':
    app.run(debug=True)