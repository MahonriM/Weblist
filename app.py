from flask import Flask,render_template,redirect,request
app=Flask(__name__)
lista=[]
@app.route('/',methods=['POST','GET'])
def Index():
    if request.method=='POST':
        try:
            n=request.form['txtelem']
            lista.append(n)
            return  render_template("index.html",lista=lista)
        except:
            return 'Ha ocurrdo un error'
    else:
        return render_template('index.html')
if __name__=="__main__":
    app.run(debug=True)
