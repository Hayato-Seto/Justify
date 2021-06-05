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

        light_speed_km_s = 30
        lorentz_factor = (1-(v1/v3)**2)**0.5
        speed_km_s = round(light_speed_km_s*lorentz_factor, 3)
        distance_km = round(light_speed_km_s*lorentz_factor*v3*60, 3)
        # light_year=lorentz_factor*v3/60/24/365 <- use after

        flash(
            "距離{}万kmの場所から<br>\
            秒速{}万kmで目的地に向かえば<br>\
            遅刻は相対論的に正当化されます".format(distance_km, speed_km_s)
        )

    return render_template('calculation.html')
