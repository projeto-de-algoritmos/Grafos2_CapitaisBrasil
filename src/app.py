from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from src.grafo import Grafo, siglas, adjacencias
from src.dijkstra import dijkstra

grafo = Grafo(siglas, adjacencias)


# Lista de opções que aparecerão na caixa de seleção
lista_estados_partida = [
    '', 'AC', 'AL', 'AM', 'AP', 'BA', 'CE',
    'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT',
    'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN',
    'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO'
]

# Dicionário para cores usadas na interface
cores = {
    'preto': '#242323',
    'cinza': '#c1c4be',
    'cinza_claro': '#e6e1e5',
    'branco': '#ffffff',
    'azul': '#2176C1'
}


def selecionar(e):
    """
    Capta o evento associado a seleção de um estado
    na Combobox (caixa de seleção) do estado de partida.
    """

    # Limpa o campo do estado de destino caso
    # tenha o mesmo estado no campo do estado
    # de partida.
    if combo_estado_partida.get() == combo_estado_destino.get():
        combo_estado_destino.set('')

    # Limpa e reseta o campo do estado de destino
    # caso selecione a opção vazia no campo
    # do estado de partida.
    if combo_estado_partida.get() == '':
        combo_estado_destino.set('')
        combo_estado_destino.config(value=[''])

    # Ajusta a lista de opções de estados de destino
    # para não conter o estado que foi selecionado
    # como o de partida.
    else:
        estado = combo_estado_partida.get()
        estados_destino = lista_estados_partida.copy()
        estados_destino.pop(estados_destino.index(estado))
        estados_destino.pop(estados_destino.index(''))
        combo_estado_destino.config(value=estados_destino)


def calcular_trajeto():
    """
    Reage ao evento do clique no botão e
    calcula a distância entre os estados.
    """
    estado_partida = combo_estado_partida.get()
    estado_destino = combo_estado_destino.get()

    if estado_partida == '' or estado_destino == '':
        msg_calculo.config(text='Selecione os estados.')
        return

    estados_do_caminho, menor_distancia = dijkstra(grafo=grafo, estado_partida=estado_partida)

    msg_calculo.config(text=mensagem(estados_do_caminho, menor_distancia, estado_partida, estado_destino))


def mensagem(nos_do_caminho, menor_caminho, e_partida, e_chegada):
    estados = {
        'AC': 'Acre', 'AL': 'Alagoas', 'AM': 'Amazonas', 'AP': 'Amapá',
        'BA': 'Bahia', 'CE': 'Ceará', 'DF': 'Distrito Federal', 'ES': 'Espírito Santo',
        'GO': 'Goiás', 'MA': 'Maranhão', 'MG': 'Minas Gerais', 'MS': 'Mato Grosso do Sul',
        'MT': 'Mato Grosso', 'PA': 'Pará', 'PB': 'Paraíba', 'PE': 'Pernambuco', 'PI': 'Piauí',
        'PR': 'Paraná', 'RJ': 'Rio de Janeiro', 'RN': 'Rio Grande do Norte', 'RO': 'Rondônia',
        'RR': 'Roraima', 'RS': 'Rio Grande do Sul', 'SC': 'Santa Catarina', 'SE': 'Sergipe',
        'SP': 'São Paulo', 'TO': 'Tocantins'
    }
    capitais = {
        'AC': 'Rio Branco (AC)', 'AL': 'Maceió (AL)', 'AM': 'Manaus (AM)', 'AP': 'Macapá (AP)',
        'BA': 'Salvador (BA)', 'CE': 'Fortaleza (CE)', 'DF': 'Brasília (DF)', 'ES': 'Vitória (ES)',
        'GO': 'Goiânia (GO)', 'MA': 'São Luís (MA)', 'MG': 'Belo Horizonte (MG)', 'MS': 'Campo Grande (MS)',
        'MT': 'Cuiabá (MT)', 'PA': 'Belém (PA)', 'PB': 'João Pessoa (PB)', 'PE': 'Recife (PE)', 'PI': 'Teresina (PI)',
        'PR': 'Curitiba (PR)', 'RJ': 'Rio de Janeiro (RJ)', 'RN': 'Natal (RN)', 'RO': 'Porto Velho (RO)',
        'RR': 'Boa Vista (RR)', 'RS': 'Porto Alegre (RS)', 'SC': 'Florianópolis (SC)', 'SE': 'Aracaju (SE)',
        'SP': 'São Paulo (SP)', 'TO': 'Palmas (TO)'
    }

    caminho = []
    node = e_chegada
    while node != e_partida:
        caminho.append(node)
        node = nos_do_caminho[node]

    # Adicionando o nó (estado) inicial manualmente ao final da lista
    caminho.append(e_partida)

    capital = [capitais[i] for i in caminho]
    msg = f"""A menor distância por rodovias entre as capitais de {estados[e_partida]} e {estados[e_chegada]}, passando
pelas capitais de cada um dos outros estados é cerca de {menor_caminho[e_chegada]*1000:.0f} km.
{', '.join(reversed(capital))}"""

    return msg


if __name__ == "__main__":
    # Instância da janela
    app = Tk()
    app.title('Mapa Brasil')
    app.geometry('800x600')
    app.maxsize(1500, 650)
    app.config(bg=cores['cinza'])

    titulo = Label(app, text="Distância entre capitais", bg=cores['azul'], fg=cores['branco'], relief=RAISED)
    titulo.pack(ipady=5, fill='x')
    titulo.config(font=("Font", 30))


    # Frame para os campos de seleção e botão
    frame_selecao = Frame(app, bg=cores['cinza_claro'])
    frame_selecao.pack(pady=5)

    # Frame para seleção do estado de partida
    frame_partida = Frame(frame_selecao, bg=cores['branco'])
    frame_partida.grid(row=0, column=0, padx=10, pady=10)

    Label(frame_partida, text="Escolha o estado de partida", bg=cores['branco']).pack(side="top", pady=5)
    combo_estado_partida = ttk.Combobox(frame_partida, value=lista_estados_partida, width=30)
    combo_estado_partida.pack(side="bottom", padx=5, pady=5)
    combo_estado_partida.current(0)
    combo_estado_partida.bind("<<ComboboxSelected>>", selecionar)


    # Frame para seleção do estado de destino
    frame_destino = Frame(frame_selecao, bg=cores['branco'])
    frame_destino.grid(row=0, column=1, padx=10, pady=10)

    Label(frame_destino, text="Escolha o estado de destino", bg=cores['branco']).pack(side="top", pady=5)
    combo_estado_destino = ttk.Combobox(frame_destino, value=[''], width=30)
    combo_estado_destino.current(0)
    combo_estado_destino.pack(side="bottom", padx=5, pady=5)

    frame_botao = Frame(frame_selecao)
    botao_calcular = Button(frame_selecao, text="Calcular trajeto", command=calcular_trajeto)
    botao_calcular.grid(row=0, column=2, padx=10, pady=10)


    # Frame para a parte do mapa e da mensagem.
    bottom_frame = Frame(app, bg=cores['cinza'], width=600)
    bottom_frame.pack(pady=15)


    frame_mapa = Frame(bottom_frame, bg=cores['preto'])
    frame_mapa.pack(side="left")
    mapa_path = '../assets/mapaBR.jpg'
    img_mapa = ImageTk.PhotoImage(Image.open(mapa_path))
    Label(frame_mapa, image=img_mapa).grid(row=0, column=0, padx=5, pady=5)

    frame_msg = Frame(bottom_frame, bg=cores['cinza'])
    frame_msg.pack(side='top')
    msg_calculo = Label(frame_msg)
    msg_calculo.grid(row=0, column=0, padx=10, pady=5)

    app.mainloop()
