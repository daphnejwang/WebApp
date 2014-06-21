from flask import Flask, render_template, request
import hackbright_app 

app = Flask(__name__)

@app.route("/")
def get_github():
    return render_template("get_github.html")

@app.route("/student")
def get_student():
    hackbright_app.connect_to_db()
    student_github = request.args.get("github")
    row = hackbright_app.get_student_by_github(student_github)
    row2 = hackbright_app.show_grade(student_github)
    print "row2 _____!!!___!!__!!__%r" % row2
    html = render_template("student_info.html", first_name=row[0], last_name=row[1], github=row[2], grade=row2[:])
    return html


@app.route("/classlist")
def full_class_list():
    hackbright_app.connect_to_db()
    project = request.args.get("project_title")
    row = hackbright_app.query_all_grades(project)
    html = render_template("grades.html", project_title=project, grades = row)
    return html

@app.route("/newstudent")
def new_student_page():
    # return render_template("new_student.html")
    return render_template("new_student.html")

@app.route("/confirmation")
def create_new_student():
    hackbright_app.connect_to_db()
    firstname = request.args.get("first_name")
    lastname = request.args.get("last_name")
    github = request.args.get("github")
    hackbright_app.make_new_student(firstname, lastname, github)
    # html = render_template("confirmation.html", yourface=firstname, last_name = lastname, github = github)
    # return html
    return "YAY! Student added!"

if __name__ == "__main__":
    app.run(debug=True)