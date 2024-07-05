import gradio as gr
import joblib
import pandas as pd

modelo = joblib.load('./modelo_colesterol.pkl')

def predict(grupo_sanguineo, fumante, nivel_atividade, idade, peso, altura):
    _fumante = 'Sim' if fumante else 'Não'
    predicao_individual = {
        'grupo_sanguineo': [grupo_sanguineo],
        'fumante': [_fumante],
        'nivel_atividade': [nivel_atividade],
        'idade': [idade],
        'peso': [peso],
        'altura': [altura]
    }

    predict_df = pd.DataFrame(predicao_individual, index=[1])
    colesterol = modelo.predict(predict_df)

    return round(float(predict_colesterol[0]), 2)

demo = gr.Interface(
    fn=predict,
    inputs=[
        gr.Radio(['A', 'B', 'O', 'AB'], label='Grupo Sanguíneo'),
        gr.Checkbox(label='Fumante'),
        gr.Radio(['Baixo', 'Moderado', 'Alto'], label='Nível de Atividade'),
        gr.Slider(20, 90, step=1, label='Idade'),
        gr.Slider(40, 160, step=0.1, label='Peso'),
        gr.Slider(120, 200, step=1, label='Altura')
    ],
    outputs=['number']
    
)

demo.launch()
