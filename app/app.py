from flask import Flask, render_template,redirect,request
import form as form




app=Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():

    return redirect('/Español')

@app.route('/<language>',methods=['GET', 'POST'])
def automata(language):
    Comment_form = form.CommentForm(request.form)
    if (request.method=='POST'):
        if(str(Comment_form.Word.data)!="None"):
            return redirect('/automata/'+language+'/'+str(Comment_form.Word.data)+'/'+str(Comment_form.Time.data))

    idioms=['Español','Ingles']
    data={}
    if(language=="Español"):
        data={
            'Pagetitle':'Automata',
            'Maintitle':'expresión para el automata',
            'Button':'Evaluar',
            'Time':'Tiempo(milisegundos)',
            'Texarea':'Ingrese la palabra a evaluar',
            'Idioms':idioms,

        }
    elif(language=="Ingles"):
        data={
            'Pagetitle':'Automaton',
            'Maintitle':'expression for the Automaton',
            'Button':'Evaluate',
            'Time':'Time(miliseconds)',
            'Texarea':'Enter the word to evaluate',
            'Idioms':idioms,
            'Back':'Back'
        }

    return render_template('automata.html',data=data,form=Comment_form)

@app.route('/automata/<language>/<wordEvaluated>/<Time>')
def EvaluateWord(wordEvaluated,language,Time):
    stop=False
    wordAccepted=False
    numberOfState=0
    Steps=[]
    for index in range(0,len(wordEvaluated)):
        if(numberOfState==0):
            if(wordEvaluated[index]=='b'):
                Steps.append("Q0")
                Steps.append("Q1")
                numberOfState=1
            elif(wordEvaluated[index]=='c'):
                Steps.append("Q0")
                Steps.append("Q3")
                numberOfState=3
            elif(wordEvaluated[index]=='d'):
                stop=True
                wordAccepted=True
                Steps.append("Q0")
                Steps.append("Q4")
                numberOfState=4
            elif(wordEvaluated[index]=='|'):
                Steps.append("Q0")
                wordAccepted=True
            else:
                wordAccepted=False
                break
        elif(numberOfState==1):
            if(wordEvaluated[index]=='a'):
                Steps.append("Q2")
                numberOfState=2
                wordAccepted=True
            else:
                wordAccepted=False
                break
        elif(numberOfState==2):
            if(wordEvaluated[index]=='b'):
                wordAccepted=False
                Steps.append("Q1")
                numberOfState=1
            elif(wordEvaluated[index]=='c'):
                wordAccepted=False
                Steps.append("Q3")
                numberOfState=3
            elif(wordEvaluated[index]=='d'):
                stop=True
                Steps.append("Q4")
                numberOfState=4
            else:
                wordAccepted=False
                break
        elif(numberOfState==3):
            if(wordEvaluated[index]=='d'):
                wordAccepted=True
                Steps.append("Q4")
                numberOfState=4
            elif(wordEvaluated[index]=='c'):
                Steps.append("Q3")
                numberOfState=3
            else:
                wordAccepted=False
                break
        elif(numberOfState==4):
            if(wordEvaluated[index]=='d'):
                Steps.append("Q4")
                numberOfState=4
            elif(wordEvaluated[index]=='c'):
                if(stop==True):
                    wordAccepted=False
                    break
                else:
                    Steps.append("Q3")
                    wordAccepted=False
                    numberOfState=3
            else:
                wordAccepted=False
                break
    if(language=="Español"):
        data={
            'Resultado':wordAccepted,
            'Steps':Steps,
            'Time':Time,
            'Back':'Volver'
        }
    
    elif(language=="Ingles"):
        data={
            'Resultado':wordAccepted,
            'Steps':Steps,
            'Time':Time,
            'Back':'Back'
        }
    
    return render_template('resultado.html',data=data)
 


if __name__=='__main__':
    app.run(debug=False)


