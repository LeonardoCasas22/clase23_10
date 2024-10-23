idEnvio = input("Ingrese id: ")
medicamentos(idEnvio)


for codMed in medicamentos(idEnvio):

    lab = labo(codMed)
    med = prod(codMed)
    cant = cantidad(codMed)
    guardar(lab,med)
    actualizarStock(cant,codMed)

    if stock(codMed)< stockMin(codMed):
        emiteSolicitud(codMed)


