from flask import Flask, render_template, request, flash
from forms import SubmitImageForm
from utils import save_picture, get_pictures

app = Flask(__name__)
app.secret_key = 'h+\xd24\xeb\xf0\xe3\xe9\x9c\xecce'

@app.route("/",  methods=["GET"])
def home():
    return render_template('index.html')

@app.route("/submit",  methods=["GET", "POST"])
def submit():
    form = SubmitImageForm()
    if request.method == 'POST':
        print("POST")
        if form.validate_on_submit():
            file = request.files['picture'].read()
            saved_picture = save_picture(file_name=str(request.files['picture'].filename), folder_name="test_user", form_picture=file)
            if saved_picture:
                flash('Picture saved', 'success')
            else:
                flash('Picture could not be saved', 'danger')
        else:
            flash('Please submit picture', 'danger') 
    else:
        flash('Please submit an image', 'info')
    return render_template('submit_image.html', form=form)

@app.route("/view/<int:page_num>",  methods=["GET"])
def view(page_num):
    if page_num == None:
        page_num = 1
    images = get_pictures(folder_name="test_user", page_num=page_num)
    return render_template('view_images.html', images=images)

if __name__ == "__main__":
    app.run(debug=True)
