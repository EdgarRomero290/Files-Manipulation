from ntpath import join
import pandas as pd


def main():
    df=leerArchivo()
    df=agregarFiltro(df) 
    
    #VisualizarDatos(df) 
    exportarDatos(df)
    
#Funcion para agregar el archivo desde la carpeta Input
def leerArchivo():  
    import os
    print('Leyendo archivo...')
    inputCols=[3,4,5,6,7,12]  #Selecciona la colunmas a utilizar, Buscar forma de selecion mas dinamica

    path='Input'
    filename=input('Ingresar nombre de achivo: ')
    fullpath= os.path.join(path,filename) #Estas forma crea el path de forma inteligente
    
    df=pd.read_csv(fullpath+'.csv', header=0, usecols=inputCols)
    
    return df

#Funcion para aplicar el filtro de busqueda
def agregarFiltro(df):  
    print('Agregando Filtros')
    df=df[df['Payment']=='Cash']
    
    return df

# Funcion para visualizar los primeras 5 registros de cada columna
def visualizarDatos(df):    
    print('Visualizando los primeros 5 registros')
    
    dfCols=df.columns
    for col in dfCols:
        print(df[col].head(5))

#Funcion para exportar el dataframe ya filtra en forma de excel a la carpeta Output
def exportarDatos(df):    
    saveName=input('Ingresar nombre de archivo que desea guardar ')
    print('Exportando archivo')
    df.to_excel("Output\ "+saveName+".xlsx", index=None, header=True)

if __name__=="__main__":  #Se utiliza para establecer prioridad de ejecutacion 
    main()
    input('\tProceso finalizado, presionar ENTER')