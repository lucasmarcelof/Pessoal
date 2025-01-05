from flask import Flask, render_template
import plotly.graph_objects as go
import funcoes_banco 

app = Flask(__name__)

# Dados simulados para o gráfico
def generate_data():
    timestamps,valuescpu,valuesMemoria,valuesDisco = funcoes_banco.leitura_todos_dados()
    #print(timestamps)
    return timestamps, valuescpu,valuesMemoria,valuesDisco

# Função para criar um gráfico Plotly
def create_plotly_figure(timestamps, values, title, yaxis_title):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=timestamps, y=values, mode='lines+markers', name='Valores'))
    fig.update_layout(
        title=title,
        xaxis_title="Tempo",
        yaxis_title=yaxis_title,
        template="plotly_dark"
    )
    return fig.to_html(full_html=False)

@app.route('/')
def line_chart():
    # Gerar dados
    timestamps, values_cpu, values_memoria, values_disco = generate_data()

    # Criar gráficos com Plotly
    chart_html_cpu = create_plotly_figure(timestamps, values_cpu, "%Uso CPU", "Uso")
    chart_html_memoria = create_plotly_figure(timestamps, values_memoria, "%Uso Memória", "Uso")

    # Renderizar template com gráficos
    return render_template('chart.html', chart_html=chart_html_cpu, chart_html_memoria=chart_html_memoria)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
