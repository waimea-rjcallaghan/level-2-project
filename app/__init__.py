#===========================================================
# PROJECT NAME HERE
# By YOUR NAME HERE
#===========================================================

from flask import Flask, request, session, render_template, flash, redirect, send_file, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from os import getenv
from io import BytesIO
import html
from app.helpers import *


# Create the app
app = Flask(__name__)


#===========================================================
# App Routes Handlers
#===========================================================

#-----------------------------------------------------------
# Home page - Show all notes
#-----------------------------------------------------------
@app.get("/")
def show_notes():
    with connect_db() as db:
        sql = """
            SELECT id, title, body, pinned, created
            FROM note
            ORDER BY pinned DESC, created DESC
        """
        params = ()
        notes = db.execute(sql, params).fetchall()

        flash("Test message")
        flash("Test SUCCESS message", "success")
        flash("Test INFO message", "info")
        flash("Test WARNING message", "warning")
        flash("Test ERROR message", "error")

        return render_template("pages/note_list.jinja", notes=notes)



#-----------------------------------------------------------
# Home page - Show all notes
#-----------------------------------------------------------

@app.post("/data/new")
def process_data_form():
    repno. = request.form.get("repno.", "unknown").strip()
    name = request.form.get("name", "unknown").strip()
    date = request.form.get("date", "unknown").strip()
    repweight = request.form.get("repweight", "unknown").strip()

    # connect to the db
    with connect_db() as db:
        sql = """
            INSERT INTO data (repno., name, repweight, date)
            VALUES (?, ?, ?, ?)
        """
        params = (repno., name, repweight, date)

        #run the query
        db.execute(sql, params)

        flash(f"data {name} added succesfully")

        return redirect("/data")        



#-----------------------------------------------------------
# Home page - Show all notes
#-----------------------------------------------------------

@app.get("/data/new")
def show_data_form():
    return render_template("_pages/data_form.jinja")

#===========================================================
# Configure the app
#===========================================================
load_dotenv()
app.config.from_prefixed_env()
init_logging(app)
init_text_filters(app)
init_date_filters(app)
init_error_handlers(app)
init_database()
register_commands(app)

