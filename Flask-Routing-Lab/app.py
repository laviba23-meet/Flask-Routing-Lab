from flask import Flask, redirect, request, render_template, url_for


app = Flask( 
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)
@app.route('/')
def homepage():
    return render_template("home.html")



@app.route('/GrandPiano')
def grand():
    return render_template("grand.html")






if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
