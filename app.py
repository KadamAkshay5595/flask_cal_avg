from flask import Flask,render_template,redirect,url_for,request

app = Flask(__name__)

@app.route('/')
def hello():
    return "This is Calculator App"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:val>')
def success(val):
    return '<h1> Congrats..!!! You are pass and Marks are </h1>'+str(val)
    
@app.route('/fail/<int:val>')
def fail(val):
    return "<h1> Sorry..!!! You are Fail and Marks are </h1>"+str(val)

@app.route('/calculate',methods=['GET','POST'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])
    
        average_marks = (maths+science+history)/3
      
        if average_marks > 40:
            result = 'success'
        else:
            result = 'fail'
            
        # return redirect(url_for(result,val=average_marks))
        return render_template('result.html',results=average_marks)
    
if __name__ == "__main__":
    app.run(debug=True)
    
