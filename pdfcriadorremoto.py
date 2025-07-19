import streamlit as st
from PIL import Image
import os

st.title("🖼️ JPEG para PDF")
st.header("by Cariolano")
st.write("Selecione suas imagens e defina a qualidade do PDF.")

# Upload de múltiplas imagens
imagens = st.file_uploader("Escolha as imagens", type=["png", "jpg", "jpeg", "bmp", "tiff"], accept_multiple_files=True)

# Slider para definir a qualidade
qualidade = st.slider("Qualidade das imagens no PDF (1 = baixa, 100 = alta)", min_value=10, max_value=100, value=85)

# Nome do arquivo de saída
nome_pdf = st.text_input("Nome do arquivo PDF (sem extensão)", "documento")

if st.button("Converter para PDF"):
    if imagens:
        convertidas = []

        for imagem in imagens:
            img = Image.open(imagem).convert('RGB')
            # Compressão: salva temporariamente com qualidade definida
            img.save("temp.jpg", quality=qualidade)
            img_compressa = Image.open("temp.jpg").convert('RGB')
            convertidas.append(img_compressa)

        # Salva o PDF
        caminho_pdf = f"{nome_pdf}.pdf"
        convertidas[0].save(caminho_pdf, save_all=True, append_images=convertidas[1:])
        os.remove("temp.jpg")
        st.success(f"✅ PDF gerado com sucesso: {caminho_pdf}")
        with open(caminho_pdf, "rb") as f:
            st.download_button("📥 Baixar PDF", f, file_name=caminho_pdf)
    else:
        st.warning("⚠️ Nenhuma imagem foi selecionada.")
