from flask import Flask, render_template_string, render_template
from wtforms import Form
from wtforms.fields import *
from wtforms.fields.html5 import *
from  wtforms import validators
from flask import request, flash

app = Flask(__name__)
app.config['DEBUG'] = True


class NlgForm(Form):
    syntactic = DecimalRangeField('Syntactic complexity',   [validators.NumberRange(min=-10, max=10)],  default=0)
    semantics = TextAreaField(u'Semantic representation', [validators.optional()])

@app.route("/", methods=['GET',])
def home():
    form = NlgForm(csrf_enabled=False)
    return render_template("index.html", form=form)

@app.route("/", methods=['POST',])
def do_home():
    form = NlgForm(request.form)
    if form.validate():
        return str(form.data)
    else:
        return "invalid"

if __name__ == "__main__":
    app.run()
