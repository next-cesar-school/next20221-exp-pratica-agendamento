from flask import Flask, Request, request, render_template, Response, url_for, redirect
import urllib.request, json
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clientes.sqlite3'

db = SQLAlchemy(app)

class Clientes(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(120))
    cpf = db.Column(db.Integer, unique = True, nullable = False)
    celular = db.Column(db.Integer)
    email = db.Column(db.String(60))

    def __init__(self, nome, cpf, celular, email):
            self.nome = nome
            self.cpf = cpf
            self.celular = celular
            self.email = email

@app.route('/clientes', methods=["GET"])
def lista_clientes():
    return render_template("clientes.html", clientes=Clientes.query.all())

@app.route('/cadastro', methods=["GET", "POST"])
def cadastra_clientes():
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')
    celular = request.form.get('celular')
    email = request.form.get('email')

    if request.method == 'POST':
        cliente = Clientes(nome, cpf, celular, email)
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for('lista_clientes'))
    return render_template("cadastra_clientes.html")

@app.route('/<int:id>/atualizacliente', methods=["GET", "POST"])
def atualizacliente(id):
    cliente = Clientes.query.filter_by(id=id).first()
    if request.method == "POST":
        nome = request.form['nome']
        cpf = request.form['cpf']
        celular = request.form['celular']
        email = request.form['email']

        Clientes.query.filter_by(id=id).update({"nome":nome, "cpf":cpf, "celular":celular, "email":email})
        db.session.commit()
        return redirect(url_for('lista_clientes'))    
    return render_template("atualizacliente.html", cliente=cliente)

@app.route('/<int:id>/removecliente')
def removecliente(id):
    cliente = Clientes.query.filter_by(id=id).first()
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('lista_clientes'))    
    

class Assistencias(db.Model):
    
    id = db.Column(db.Integer, primary_key = True) 
    nome = db.Column(db.String(60))
    endereco = db.Column(db.String(200))

    def __init__(self, nome, endereco):
            self.nome = nome
            self.endereco = endereco

@app.route('/assistencias')
def lista_assistencias():
    return render_template("assistencias.html", assistencias=Assistencias.query.all())

@app.route('/assistencias/cadastro', methods=["GET", "POST"])
def cadastro_assistencias():

    nome = request.form.get('nome')
    endereco = request.form.get('endereco')
   
    if request.method == 'POST':
        assistencias = Assistencias(nome, endereco)
        db.session.add(assistencias)
        db.session.commit()
        return redirect(url_for('lista_assistencias'))
    return render_template("cadastro_assistencias.html")

@app.route('/<int:id>/atualizaassistencia', methods=["GET", "POST"])
def atualizaassistencia(id):
    assistencia = Assistencias.query.filter_by(id=id).first()
    if request.method == "POST":
        nome = request.form['nome']
        endereco = request.form['endereco']
        
        Assistencias.query.filter_by(id=id).update({"nome":nome, "endereco":endereco})
        db.session.commit()
        return redirect(url_for('lista_assistencias'))    
    return render_template("atualizaassistencia.html", assistencia=assistencia)

@app.route('/<int:id>/removeassistencia')
def removeassistencia(id):
    assistencia = Assistencias.query.filter_by(id=id).first()
    db.session.delete(assistencia)
    db.session.commit()
    return redirect(url_for('lista_assistencias'))   
    

# class Agendamentos(db.Model):

#     protocolo = db.Column(db.Integer, primay_key = True, autoincrement=True)
#     data = db.Column(db.date)
#     horario = db.Column(db.time)
#     horario_fim = db.Column(db.time)
#     id_assistencia = db.Column(db.Integer, db.ForeignKey('assistencia.id'))
#     id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id'))
#     id_equipamento = db.Column(db.Integer, db.ForeignKey('equipamentos.id'))
# #    garantia = db.Column(db.String, nullable = False)



#     assistencia = db.relationship('Assistencias', foreign_keys = id_assistencia)
#     cliente = db.relationship('Clientes', foreign_keys = id_cliente)
#     equipamento = db.relationship('Equipamentos', foreign_keys = id_equipamento)

# def init(self, id, data, horario_inicio, horario_fim, id_assistencia, id_cliente, id_equipamento):
#             self.protocolo = protocolo
#             self.data = data
#             self.horario_inicio = horario_inicio 
#             self.horario_fim = horario_fim
#             self.id_assistencia = id_assistencia
#             self.id_cliente = id_cliente
#             self.id_equipamento = id_equipamento

# class Agendamentos(db.Model):
    
#     id = db.Column(db.Integer, primary_key = True)
#     nome = db.Column(db.String, nullable = False)
#     protocolo = db.Column(db.String(10), unique = True, nullable = False) 
#     status = db.Column(db.String(60))
#     assistencia = db.Column(db.String(30))
#     data = db.Column(db.String)
#     horario_inicio = db.Column(db.String)
#     horario_fim = db.Column(db.String)
#     equipamento = db.Column(db.String(60))
#     problema = db.Column(db.String(200))
   
#     def __init__(self, nome, protocolo, status, assistencia, data, horario_inicio, horario_fim, equipamento, problema):
#             self.nome = nome
#             self.protocolo = protocolo  
#             self.status = status
#             self.assistencia = assistencia
#             self.data = data
#             self.horario_inicio = horario_inicio 
#             self.horario_fim = horario_fim
#             self.equipamento = equipamento
#             self.problema = problema

# @app.route('/agendamentos', methods=["GET"])
# def lista_agendamentos():
#     return render_template("agendamentos.html", agendamentos=Agendamentos.query.all())

# @app.route('/agendamentos/cadastro', methods=["GET"])
# def formulario_agendamentos():
#     return render_template("cadastra_agendamentos.html")

# @app.route('/agendamentos/cadastro', methods=["POST"])
# def cadastra_agendamentos():
    
#     nome = request.form.get('nome')
#     protocolo = request.form.get('protocolo')
#     status = request.form.get('status')
#     assistencia = request.form.get('assistencia')
#     data = request.form.get('data')
#     horario_inicio = request.form.get('horario_inicio')
#     horario_fim = request.form.get('horario_fim')
#     equipamento = request.form.get('equipamento')
#     problema = request.form.get('problema')

#     if request.method == 'POST':
#         agendamento = Agendamentos(nome, protocolo, status, assistencia, data, horario_inicio, horario_fim, equipamento, problema)
#         db.session.add(agendamento)
#         db.session.commit()
#         return redirect(url_for('lista_agendamentos'))
#     return render_template("cadastra_agendamentos.html")

# FALTA CADASTRO (GABI)
# FALTA LISTAGEM DE AGENDAMENTO (ANDRE)
# FALTA DELEÇÃO AGENDAMENTO (ANDRE)
# FALTA HORÁRIO DISPONÍVEIS DE UMA ASSITÊNCIA ESPECÍFICA EM UMA DATA ESPECÍFICA (ANDRE)

class Equipamentos (db.Model):

    id = db.Column(db.Integer, primary_key = True)
    tipo = db.Column(db.String(60), nullable = False)
 
    def __init__ (self, tipo):
        self.tipo = tipo
 
@app.route('/equipamentos', methods=["GET"])
def lista_equipamentos():
    return render_template("equipamentos.html", equipamentos=Equipamentos.query.all())

@app.route('/equipamentos/cadastro', methods=["GET", "POST"])
def cadastro_equipamentos():

    tipo = request.form.get('tipo')
   
    if request.method == 'POST':
        equipamentos = Equipamentos(tipo)
        db.session.add(equipamentos)
        db.session.commit()
        return redirect(url_for('lista_equipamentos'))
    return render_template("cadastro_equipamentos.html")

@app.route('/<int:id>/atualizaequipamento', methods=["GET", "POST"])
def atualizaequipamento(id):
    equipamento = Equipamentos.query.filter_by(id=id).first()
    if request.method == "POST":
        tipo = request.form['tipo']
                
        Equipamentos.query.filter_by(id=id).update({"tipo":tipo})
        db.session.commit()
        return redirect(url_for('lista_equipamentos'))    
    return render_template("atualizaequipamento.html", equipamento=equipamento)

@app.route('/<int:id>/removeequipamento')
def removeequipamento(id):
    equipamento = Equipamentos.query.filter_by(id=id).first()
    db.session.delete(equipamento)
    db.session.commit()
    return redirect(url_for('lista_equipamentos'))   


#class Equipamentos (db.Model):

#    id = db.Column(db.Integer, primary_key = True)
#    tipo = db.Column(db.String(60), nullable = False)
#    data_compra = db.Column(db.Integer, nullable = False)
#    data_limite_garantia = db.Column(db.Integer, nullable = False)
#    data_ultimo_atendimento = db.Column(db.Integer)
#    problema = db.Column(db.Text, nullable = False)

#    def init(self, id, tipo, data_compra, data_limite_garantia, data_ultimo_atendimento, problema):
#        self.id = id
#        self.tipo = tipo
#        self.data_compra = data_compra
#        self.data_limite_garantia = data_limite_garantia
#        self.data_ultimo_atendimento = data_ultimo_atendimento
#        self.problema = problema

#    def repr(self):
#        return '<Tipo %r>' % self.tipo


if __name__ == "__main__":
        db.create_all()
        app.run(debug = True)


# http://127.0.0.1:5000


