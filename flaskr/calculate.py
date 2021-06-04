from flask import (
    Blueprint, render_template, flash, request
)

bp = Blueprint('calculate', __name__, url_prefix='/calculate')


@bp.route('/form', methods=('GET', 'POST'))
def form():
    if request.method == 'POST':
        v1 = int(request.form['value1'])
        v2 = int(request.form['value2'])
        v3 = v1+v2

        flash(v3)

    return render_template('calculation.html')
