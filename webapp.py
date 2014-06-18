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
    html = render_template("student_info.html", first_name=row[0], last_name=row[1], github=row[2], grade=row2[:])
    return html


@app.route("/classlist")
def full_class_list():
    hackbright_app.connect_to_db()
    project = request.args.get("project_title")
    row = hackbright_app.query_all_grades(project)
    html = render_template("grades.html", project_title=project, grades = row)
    return html

if __name__ == "__main__":
    app.run(debug=True)