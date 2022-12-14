from flask import Blueprint, current_app, make_response, request

mod = Blueprint('flask_z5', __name__)


# print(app_socketio)


@mod.route('/pause', methods=['GET', 'POST'])
def pause():
    generator = current_app.config['generator']
    if request.method == 'POST':
        code = 500
        if generator.status == 'running':
            generator.paused = True
            code = 201
        return make_response(generator.status, code)
    return generator.status


@mod.route('/start', methods=['GET', 'POST'])
def start():
    generator = current_app.config['generator']
    if request.method == 'POST':
        code = 500
        if generator.status == 'paused':
            generator.paused = False
            code = 201
        return make_response(generator.status, code)
    return generator.status


@mod.route('/update', methods=['GET', 'POST'])
def update():
    generator = current_app.config['generator']
    if request.method == 'POST':
        try:
            if 'protocol' in request.form:
                generator.protocol = request.form['protocol']
            if 'interval' in request.form:
                generator.interval = float(request.form['interval'])
            if 'data_source' in request.form:
                generator.data_source = request.form['data_source']
            if 'url' in request.form:
                generator.url = request.form['url']
            return make_response(generator.status, 201)
        except KeyError:
            return make_response('key error', 500)
    return generator.status


@mod.route('/status', methods=['GET', 'POST'])
def status():
    generator = current_app.config['generator']
    generator_status = {
        'name': generator.app_name,
        'address': generator.address,
        'protocol': generator.protocol,
        'interval': generator.interval,
        'data_source': generator.data_source,
        'url': generator.url,
        'status': generator.status,
    }
    return generator_status
