# S1-import Flask

from flask import Flask ,render_template,request,redirect,url_for

# S2-Create a Flask Object and pass __name__
app =  Flask(__name__)
app.static_folder= "static"
notes=[]

######################################
# S3-Create a route and bind it to a fun
@app.route("/",methods=["GET","POST"])
def index():
    if request.method =="POST":
        note =request.form.get("note")
        
        if note:
            notes.append(note)
            return redirect(url_for("index"))
        
    indexed_notes=list(enumerate(notes))
    return render_template("home.html",notes=indexed_notes)

@app.route("/edit",methods=["GET","POST"])
def edit_note():
    if request.method =="POST":
        note_index= int(request.form.get("note_index"))
        new_note=request.form.get("new_note")
        notes[note_index]=new_note
        return redirect(url_for('index'))
    
    
@app.route("/delete",methods=["GET","POST"])
def delet_note():
    if request.method=="POST":
        note_index=int(request.form.get("note_index"))
        del notes[note_index]
        return redirect(url_for("index"))
    
#######################################

# S4-Run the Application
if __name__ == "__main__":
    app.run(debug=True)