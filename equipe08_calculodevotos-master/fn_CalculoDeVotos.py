def fn_CalculaSomatorioVotos(vet_votos):
    return sum(vet_votos)

def fn_CalculoPorcentagem(vet_votos, soma_total):
    flt_porc_nulos = (vet_votos[0] / soma_total) * 100
    flt_porc_brancos = (vet_votos[1] / soma_total) * 100
    flt_porc_validos = (vet_votos[2] / soma_total) * 100

    return [flt_porc_nulos, flt_porc_brancos, flt_porc_validos]





