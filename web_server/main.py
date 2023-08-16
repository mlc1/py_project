import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()#Creamos la instacia

'''
Creamos el decorador y le decimos cual es la 
ruta por la cual desde la web van a poder ingresar
'''
@app.get('/',response_class=HTMLResponse)
def get_list():
    return"""
         <h1 style='text-align:center; color:blue'>Soy un titulo</h1>

    """

@app.get('/contact')
def get_list():
    
    return {'name': 'Juan'}





def run():
    store.get_categories()

if __name__ =='__main__':
    run()  
