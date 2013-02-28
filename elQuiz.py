import numpy as np

frecuencias = [20]
rango = np.arange(20)+1

filein = codecs.open("frecuencias"+sys.argv[1], "r", "utf8")
        
frecuencias = np.loadtxt(filein)        

m = np.polyfit(log(rango), log(frecuencias), 1)
        
k = m[0]

fileout = codecs.open("coeficientesDe"+sys.argv[1], "w", "utf8")
fileout.write("%s %f\n", sys.argv[1], k)

filein.close()
