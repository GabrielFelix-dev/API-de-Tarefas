#IMPORTAR O FASTAPI
from fastapi import FastAPI, HTTPException
#SERVER PARA DEFINIR O FORMATO DOS DADOS
from pydantic import BaseModel

#AJUDAR NA TIPAGEM
from typing import List, Optional

#CRIAR A API
app = FastAPI(title="API de Tarefas")

#MODELO DE DADOS
class tarefa(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    concluida: bool = False

#BANCO EM MEMORIA
db_tarefas = []

