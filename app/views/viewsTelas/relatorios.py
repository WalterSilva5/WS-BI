from django.shortcuts import render
from app.models import Vendedor
# Create your views here.
from django.http import HttpResponse
import psycopg2


def relatorios(request):
    return render(request, 'relatorios/relatorios.html')


def relatorios_vendas_por_vendedor(request):
    vendedores = list(Vendedor.objects.all().values())[:]
    dados = {"vendedores": vendedores}
    try:
        if request.POST["codigorca"] is not None:
            dados["codigorca"] = request.POST["codigorca"]
            dados["agrupamento"] = request.POST["agrupar"]
        if request.POST["agrupar"] == "mes":
            consulta = """SELECT sum(valor) valor, DATE_TRUNC('month',data) mes
                        FROM   app_venda_por_dia_por_vendedor
                        WHERE  vendedor_idvendedor = {}
                            AND data BETWEEN To_date('{}', 'YYYY-MM-DD') AND
                                                To_date('{}', 'YYYY-MM-DD')
                        GROUP  BY Date_trunc('month', data) order by DATE_TRUNC('month',data); """.format(request.POST["codigorca"], request.POST["data_inicial"], request.POST["data_final"])
            con = psycopg2.connect(
                host='localhost', database='frinexbi', user='postgres', password='frinexti')
            cur = con.cursor()
            cur.execute(consulta)
            val = cur.fetchall()
            valores = []
            for valor in val:
                valores.append(
                    ["{}/{}".format(str(valor[1])[5:7], str(valor[1])[2:4]), valor[0]])
            dados['valores'] = valores
            con.close()
        else:
            consulta = """
            SELECT valor,
                   data dia
            FROM   app_venda_por_dia_por_vendedor
            WHERE  vendedor_idvendedor = '{}'
                AND data BETWEEN To_date('{}', 'YYYY-MM-DD') AND
                                    To_date('{}', 'YYYY-MM-DD')
            ORDER  BY data
            """.format(request.POST["codigorca"], request.POST["data_inicial"], request.POST["data_final"])
            con = psycopg2.connect(
                host='localhost', database='frinexbi', user='postgres', password='frinexti')
            cur = con.cursor()
            cur.execute(consulta)
            val = cur.fetchall()
            valores = []
            for valor in val:
                valores.append(
                    ["{}/{}".format(str(valor[1])[8:10],str(valor[1])[5:7]), valor[0]])
            dados['valores'] = valores
            print(valores)
            con.close()
        # teste

        # fim teste

    except:
        print("não chegou aqui")

    return render(request, 'relatorios/vendas_por_vendedor.html', dados)
