# app.py

from flask import Flask, render_template, redirect, url_for, session, request
from models import db, Sushi, Main, Dop, Main22, Main222

app = Flask(__name__)

# --- КОНФІГУРАЦІЯ FLASK ---
app.config['SECRET_KEY'] = 'your_super_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


# --- МАРШРУТИ (ROUTES) ---

@app.route('/')
def home():
    """
    Головна сторінка додатку.
    """
    return render_template('index.html')

@app.route('/step1',methods=["GET","POST"])
def step1():
    if request.method=="POST":
        sushi_id=request.form.get("sushi")
        session["sushi_id"]=int(sushi_id)
        if sushi_id=="3":
            return redirect(url_for("step2"))
        if sushi_id=="2":
            return redirect(url_for("step22"))
        if sushi_id=="1":
            return redirect(url_for("step222"))
    session.clear()
    sushis=Sushi.query.all()
    return render_template('step1.html',sushis=sushis)


@app.route('/step2',methods=["GET","POST"])
def step2():
    if "sushi_id"not in session:
        return redirect(url_for("step1"))

    if request.method=="POST":
        main_id=request.form.get("main")
        session["main_id"]=int(main_id)
        return redirect(url_for("step3"))
    selected_main_id=session.get("main_id")
    mains=Main.query.all()
    return render_template('step2.html',mains=mains, selected_main_id=selected_main_id)

@app.route('/step22',methods=["GET","POST"])
def step22():
    if "sushi_id"not in session:
        return redirect(url_for("step1"))

    if request.method=="POST":
        main_id=request.form.get("main")
        session["main_id"]=int(main_id)
        return redirect(url_for("step3"))
    selected_main_id=session.get("main_id")
    mains=Main22.query.all()
    return render_template('step22.html',mains=mains, selected_main_id=selected_main_id)

@app.route('/step222',methods=["GET","POST"])
def step222():
    if "sushi_id"not in session:
        return redirect(url_for("step1"))

    if request.method=="POST":
        main_id=request.form.get("main")
        session["main_id"]=int(main_id)
        return redirect(url_for("step3"))
    selected_main_id=session.get("main_id")
    mains=Main222.query.all()
    return render_template('step222.html',mains=mains, selected_main_id=selected_main_id)

@app.route('/step3',methods=["GET","POST"])
def step3():
    if 'main_id' not in session:
        return redirect(url_for('step2'))
    if request.method == "POST":

     if 'main_id' not in session:
        return redirect(url_for('step2'))
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        comment = request.form.get("comment")

        session['name'] = name
        session['phone'] = phone
        session['comment'] = comment

        dop_ids = [int(value) for value in request.form.getlist('dop')]





        session['dop_ids'] = dop_ids



        return  redirect(url_for('sum'))
    #GET коли входимо на сторінку
    dops = Dop.query.all()#oтримуємо всі данні
    return render_template('step3.html', dops=dops)

@app.route('/sum',methods=['GET',"POST"])
def sum():
    total_price = 0
    name = session.get('name', "Не вказано")
    phone = session.get('phone', "Не вказано")
    comment = session.get('comment', "Не вказано")
    sushi_id = session.get('sushi_id')
    main_id = session.get('main_id')
    sushi = Sushi.query.get(sushi_id)
    if sushi_id == 3:
        main = Main.query.get(main_id)
    elif sushi_id == 2:
        main = Main22.query.get(main_id)
    elif sushi_id == 1:
        main = Main222.query.get(main_id)
    else:
        main = None

    dop_ids = session.get('dop_ids')
    dops = Dop.query.filter(Dop.id.in_(dop_ids)).all()

    total_price= main.price
    for dop in dops:
        total_price+=dop.price
    return render_template('sum.html', total_price=total_price,
                           name=name, comment=comment,
                           phone=phone, sushi=sushi,
                           main=main, dops=dops,

                           )
@app.route('/final',methods=['GET',"POST"])
def final():
    session.clear()
    return redirect(url_for("s"))

@app.route('/s',methods=['GET',"POST"])
def s():
    return render_template('thank_you.html')

# --- ЗАПУСК ДОДАТКА ---
if __name__ == '__main__':
    # create_db()
    app.run(debug=True)
