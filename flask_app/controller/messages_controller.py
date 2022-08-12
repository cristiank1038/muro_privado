from flask import render_template, redirect, session, request, flash     #importaciones de módulos de flask
from flask_app import app

from flask_app.models.messages import Message

@app.route('/send_messages', methods=['post'])
def send_messages():
    if 'usuario_id' not in session:
        return redirect('/')

    Message.save(request.form)
    return redirect('/wall')

@app.route('/eliminar/mensaje/<int:id>')
def eliminar_mensaje(id):
    formulario = { "id" : id }
    Message.destroy(formulario)
    return redirect('/wall')