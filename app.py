#!/env/bin/python
# -*- coding: utf-8 -*-

import socket
from flask import Flask, request, Response, send_from_directory, render_template
from flask_socketio import SocketIO, emit, disconnect
from flask_cors import CORS
from libraries.browser import Browser

app = Flask(__name__, static_url_path='', static_folder='dist',)
CORS(app)
app.socketio = SocketIO(app, cors_allowed_origins="*")
app.browser = Browser()

## socketio
@app.socketio.on("message")
def handle_message(data):
    print("Received:", data)
    
@app.socketio.on("disconnect")
def handle_disconnect():
    disconnect()
    
@app.socketio.on("title")
def handle_title(data=None):
    title = app.browser.get_title()
    emit('title', title)
    
@app.socketio.on("open")
def handle_open(data):
    details = app.browser.open_address(data["address"])
    emit('details', details)
    
@app.socketio.on("play")
def handle_play(data=None):
    app.browser.play()
    
@app.socketio.on("pause")
def handle_pause(data=None):
    app.browser.pause()
    
@app.socketio.on("seek")
def handle_seek(data):
    app.browser.seek(data["time"])
    
@app.socketio.on("seekBackward")
def handle_seek_backward(data=None):
    app.browser.seek_backward()

@app.socketio.on("seekForward")
def handle_seek_forward(data=None):
    app.browser.seek_forward()

@app.socketio.on("fullscreen")
def handle_fullscreen(data=None):
    app.browser.fullscreen()

# routes
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_vue(path):
    return send_from_directory(app.static_folder, "index.html")

# @app.route("/connect")
# def handle_route_connect():
#     return send_from_directory(app.static_folder, "index.html")

@app.route("/connect")
def handle_route_connect():
    return render_template("qr.html", ip_addr=socket.gethostbyname(socket.gethostname()))

@app.route("/api/play", methods=["GET"])
def handle_play_event():
    app.socketio.emit("play")
    return Response(status=200)

@app.route("/api/pause", methods=["GET"])
def handle_pause_event():
    app.socketio.emit("pause")
    return Response(status=200)

@app.route("/api/timeupdate", methods=["GET"])
def handle_timeupdate_event():
    app.socketio.emit("timeupdate",{
        "currentTime":request.args["currentTime"],
        "duration": request.args["duration"],
        "paused": request.args["paused"],
        "title": request.args["title"],
    })
    return Response(status=200)