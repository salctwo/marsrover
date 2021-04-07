from flask import Response, request, redirect
from render import render_grid
from service import action

car = (0,0,'N')


class Controller:
    def __init__(self, flask_app):
        
        @flask_app.route('/', methods = ['GET'])
        def index():
            return Response(render_grid(car), mimetype = 'text/plain')
        
        @flask_app.route('/', methods = ['POST'])
        def post():
            global car
            commands = request.json['command'].upper()
            for c in commands:
                print(c)
                print(car)
                car = action(car,c)
                print(car)
            return Response(render_grid(car), mimetype = 'text/plain')


