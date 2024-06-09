from flask import render_template, url_for, flash, redirect, request
from ProyectoIng.app import app
from ProyectoIng.forms import AudioForm
import json
from datetime import datetime

DATA_FILE = 'data.json'

def load_audios():
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def save_audios(audios):
    with open(DATA_FILE, 'w') as file:
        json.dump(audios, file, indent=4)

@app.route('/')
@app.route('/index')
def index():
    audios = load_audios()
    return render_template('index.html', audios=audios)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = AudioForm()
    if form.validate_on_submit():
        audios = load_audios()
        new_audio = {
            'id': len(audios) + 1,
            'name': form.name.data,
            'client_name': form.client_name.data,
            'campaign_name': form.campaign_name.data,
            'upload_date': datetime.utcnow().isoformat(),
            'status': 'Pendiente',
            'transcription': ''
        }
        audios.append(new_audio)
        save_audios(audios)
        flash('Audio uploaded successfully!')
        return redirect(url_for('index'))
    return render_template('upload.html', form=form)
