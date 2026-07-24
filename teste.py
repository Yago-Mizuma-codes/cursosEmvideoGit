class aluno:
    def __init__(self,name,note):
        self.nome=name
        self.nota=note

if __name__ =="__main__":
    x=aluno("joao",10.0)
    print("nome:"+x.nome)