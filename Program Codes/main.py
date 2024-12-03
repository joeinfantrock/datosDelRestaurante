from flask import Flask, render_template, request,redirect


import mysql.connector as sqlcon
from _overlapped import NULL

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template("homee.html")

@app.route('/Search', methods = ["POST"])
def Search():
    user = request.form["user"]
    password = request.form["pass"]
    customname = database(user,password)
    if customname != "User Doesn't Exist...Please Register":
        return render_template("movchoose.html",cust = customname[0]) 
    else:
        return render_template("Wrongcow.html")
 
@app.route('/Reg', methods = ["POST"])
def Reg():
    return render_template("Regisss.html")

@app.route('/RegData', methods = ["POST"])
def RegData():
    user = request.form["user"]
    customname = request.form["customname"]
    password = request.form["pass"]
    conpassword = request.form["confirmpass"]
    if(password!=conpassword):
        warn = "Password entered in both the fields don't match!"
        return render_template("Registro.html",wa = warn)
    warn = intoBase(user,customname,password)
    return render_template("Triunfo.html",suc = warn)
def intoBase(iduser,idcustomname,idpassword):
    mycon = sqlcon.connect(host = "localhost", user = "root", passwd = "Unicorn@123", database = "cow")
    cursor = mycon.cursor()
    User = iduser
    Pass = idpassword
    idCust = idcustomname
    myscom2 = "INSERT INTO credentials (Username,Password,Customername) VALUES(%s, %s, %s)" 
    values = (User,Pass,idCust)
    cursor.execute(myscom2,values)
    mycon.commit()
    return "Credentials Acquired"
def database(duser,dpassword):
    mycon = sqlcon.connect(host = "localhost", user = "root", passwd = "Unicorn@123", database = "cow")
    cursor = mycon.cursor()
    User = duser
    Pass = dpassword
    myscom1 = "select Customername from credentials where Username = (%s) AND Password = (%s)"
    values = (User,Pass)
    cursor.execute(myscom1,values)
    custname = cursor.fetchone()
    if custname == None:
        custname = "User Doesn't Exist...Please Register"
    return custname
 
@app.route("/order", methods = ["POST"])
def order():
    global moviewanted
    global quantity
    moviewanted = request.form["hidden"]
    '''if request.form["hidden3"] == "bulkbro":
    quantity = request.form["Quantitytext2"]
    else:'''
    quantity = request.form["hidden2"]
    if quantity == '1':
        return render_template("selectSeat.html", fo = moviewanted,quan = quantity) 
    elif quantity == '2':
        return render_template("selectSeat2.html", fo = moviewanted,quan = quantity) 
    elif quantity == '3':
        return render_template("selectSeat3.html", fo = moviewanted,quan = quantity) 
    elif quantity == '4':
        return render_template("selectSeat4.html", fo = moviewanted,quan = quantity) 
    else:
        return render_template("selectSeat5.html", fo = moviewanted,quan = quantity) 
 
@app.route("/confo", methods = ["POST"])
def confirm():
    if quantity == '1':
        seat_name = request.form["rowal"]
        seat_no = request.form["rownum"]
        return render_template("Finalpage.html", sn = seat_name,sno = seat_no,mow = moviewanted, qu = quantity) 
        '''if request.form["hidden3"] == "bulkbro":
        quantity = request.form["Quantitytext2"]
        else:'''
 
    elif quantity == '2':
        seat_name = request.form["rowal"]
        seat_no = request.form["rownum"]
        seat_name2 = request.form["rowal2"]
        seat_no2 = request.form["rownum2"]
        return render_template("Finalpage2.html", sn = seat_name,sno = seat_no,sn2 = seat_name2,sno2 = seat_no2, mow = moviewanted, qu = quantity) 
 
    elif quantity == '3':
        seat_name = request.form["rowal"]
        seat_no = request.form["rownum"]
        seat_name2 = request.form["rowal2"]
        seat_no2 = request.form["rownum2"]
        seat_name3 = request.form["rowal3"]
        seat_no3 = request.form["rownum3"]
        return render_template("Finalpage3.html", sn = seat_name,sno = seat_no,sn2 = seat_name2,sno2 = seat_no2, sn3 = seat_name3,sno3 = seat_no3, mow = moviewanted, qu = quantity) 
 
    elif quantity == '4':
        seat_name = request.form["rowal"]
        seat_no = request.form["rownum"]
        seat_name2 = request.form["rowal2"]
        seat_no2 = request.form["rownum2"]
        seat_name3 = request.form["rowal3"]
        seat_no3 = request.form["rownum3"]
        seat_name4 = request.form["rowal4"]
        seat_no4 = request.form["rownum4"]
        return render_template("Finalpage4.html", sn = seat_name,sno = seat_no,sn2 = seat_name2,sno2 = seat_no2, sn3 = seat_name3,sno3 = seat_no3, sn4 = seat_name4,sno4 = seat_no4, mow = moviewanted, qu         = quantity) 
 
    else:
        seat_name = request.form["rowal"]
        seat_no = request.form["rownum"]
        seat_name2 = request.form["rowal2"]
        seat_no2 = request.form["rownum2"]
        seat_name3 = request.form["rowal3"]
        seat_no3 = request.form["rownum3"]
        seat_name4 = request.form["rowal4"]
        seat_no4 = request.form["rownum4"]
        seat_name5 = request.form["rowal5"]
        seat_no5 = request.form["rownum5"]
        return render_template("Finalpage5.html", sn = seat_name,sno = seat_no,sn2 = seat_name2,sno2 = seat_no2, sn3 = seat_name3,sno3 = seat_no3, sn4 = seat_name4,sno4 = seat_no4, sn5 = seat_name5,sno5                 = seat_no5, mow = moviewanted, qu = quantity) 
 
 
 
 
if __name__ == "__main__":
    app.run(debug=True)

