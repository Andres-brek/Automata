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
    wordEvaluated=wordEvaluated.lower()
    stop=False
    wordAccepted=False
    numberOfState=0
    Steps=["Q0"]
    for index in range(0,len(wordEvaluated)):
        if(numberOfState==-1):
            wordAccepted=False
            break
        elif(numberOfState==0):
            numberOfState,wordAccepted=State0(wordEvaluated[index])
            Steps.append(addStep(numberOfState))
            if(numberOfState==4):
                stop=True
        elif(numberOfState==1):
            numberOfState,wordAccepted=State1(wordEvaluated[index])
            Steps.append(addStep(numberOfState))
        elif(numberOfState==2):
            numberOfState,wordAccepted=State2(wordEvaluated[index])
            Steps.append(addStep(numberOfState))
            if(numberOfState==4):
                stop=True
        elif(numberOfState==3):
            numberOfState,wordAccepted=State3(wordEvaluated[index])
            Steps.append(addStep(numberOfState))
        elif(numberOfState==4):
            numberOfState,wordAccepted=State4(wordEvaluated[index])
            Steps.append(addStep(numberOfState))
            if(stop==True and numberOfState!=4):
                wordAccepted=False
                break
    if(language=="Español"):
        data={
            'Resultado':wordAccepted,
            'Steps':Steps,
            'Time':Time,
            'Back':'Volver',
            'WordAccepted':'Palabra aceptada',
            'WordNoAccepted':'Palabra rechazada'
        }
    
    elif(language=="Ingles"):
        data={
            'Resultado':wordAccepted,
            'Steps':Steps,
            'Time':Time,
            'Back':'Back',
            'WordAccepted':'Word accepted',
            'WordNoAccepted':'Word rejected'
        }
    
    return render_template('resultado.html',data=data)
 

def State0(wordEvaluated):
        if(wordEvaluated=='b'):
                return 1,False
        elif(wordEvaluated=='c'):
                return 3,False
        elif(wordEvaluated=='d'):
                return 4,True
        elif(wordEvaluated=='|'):
                return 0,True
        else:
                return -1,False
    
    
def State1(wordEvaluated):
    if(wordEvaluated=='a'):
        return 2,True 
    else:
        return -1,False
    
    
def State2(wordEvaluated):
    if(wordEvaluated=='b'):
        return 1,False
    elif(wordEvaluated=='c'):
        return 3,False
    elif(wordEvaluated=='d'):
        return 4,True
    else:
        return -1,False
    
    
def State3(wordEvaluated):
    if(wordEvaluated=='d'):
        return 4,True
    elif(wordEvaluated=='c'):
        return 3,False
    else:
        return -1,False
    
    
    
def State4(wordEvaluated):
    if(wordEvaluated=='d'):
        return 4,True
    elif(wordEvaluated=='c'):
        return 3,False
    else:
        return -1,False



def addStep(numberOfState):
    if(numberOfState==1):
        return "Q1"
    elif(numberOfState==2):
        return "Q2"
    elif(numberOfState==3):
        return "Q3"
    elif(numberOfState==4):
        return "Q4"




if __name__=='__main__':
    app.run(debug=False)


