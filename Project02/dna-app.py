import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('DNA-e-RNA.webp')

st.image(image, use_column_width=True)

st.write("""
# Aplicativo Web para contagem de nucleotídeos em DNA

***
""")

st.header('Insira a sequência de DNA')

sequence_input = ">DNA Query\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence input", sequence_input, height=200)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write("""
***
""")

st.header('INPUT DNA Query')
sequence

st.header('OUTPUT Contagem de nucleotídeos')

st.subheader('1. Print dictionary')
def DNAContagem_de_Nucleotideos(seq):
    d = dict([
        ('A', seq.count('A')),
        ('C', seq.count('C')),
        ('G', seq.count('G')),
        ('T', seq.count('T')),
    ])
    return d

X = DNAContagem_de_Nucleotideos(sequence)
X

st.subheader('2. Print text')
st.write('Existem ' + str(X['A']) + ' As')
st.write('Existem ' + str(X['C']) + ' Cs')
st.write('Existem ' + str(X['G']) + ' Gs')
st.write('Existem ' + str(X['T']) + ' Ts')

st.subheader('3. Print dataframe')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'Contagem'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'Nucleotídeo'})
st.write(df)

st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='Nucleotídeo',
    y='Contagem'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)