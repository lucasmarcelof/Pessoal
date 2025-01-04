from flask import Flask, render_template
import plotly.graph_objects as go
import random
from datetime import datetime, timedelta
import funcoes_banco 

app = Flask(__name__)

# Dados simulados para o gráfico
def generate_data():
    timestamps,valuescpu,valuesMemoria,valuesDisco = funcoes_banco.leitura_todos_dados()
    print(timestamps)
     #= [random.randint(50, 100) for _ in range(10)]
    #return timestamps[::-1], values[::-1]  # Reverter para ordem cronológica
    return timestamps, valuescpu,valuesMemoria,valuesDisco

@app.route('/')
def line_chart():
    # Gerar dados
    timestamps, valuesCPU,valuesMemoria,valuesDisco = generate_data()

    # Criar gráfico 1 com Plotly
    figCpu = go.Figure()
    figCpu.add_trace(go.Scatter(x=timestamps, y=valuesCPU, mode='lines+markers', name='Valores'))

    # Customização
    figCpu.update_layout(
        title="%Uso CPU",
        xaxis_title="Tempo",
        yaxis_title="Uso",
        template="plotly_dark"
    )

    # Retornar o HTML do gráfico
    chart_html_cpu = figCpu.to_html(full_html=False)

    # Criar gráfico 2 com Plotly
    figMemoria = go.Figure()
    figMemoria.add_trace(go.Scatter(x=timestamps, y=valuesMemoria, mode='lines+markers', name='Valores'))

    # Customização
    figMemoria.update_layout(
        title="%Uso Memória",
        xaxis_title="Tempo",
        yaxis_title="Uso",
        template="plotly_dark"
    )

    # Retornar o HTML do gráfico
    chart_html_memoria = figMemoria.to_html(full_html=False)
    return render_template('chart.html', chart_html=chart_html_cpu,chart_html_memoria = chart_html_memoria)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
