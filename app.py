import os
import pickle
import numpy as np
from tqdm import tqdm
from deepface import DeepFace

dataset_path = "dataset"

embeddings = []
filenames = []

for celebrity in os.listdir(dataset_path):

    celebrity_path = os.path.join(dataset_path, celebrity)

    if not os.path.isdir(celebrity_path):
        continue

    print(f"Processing {celebrity}")

    for img_name in tqdm(os.listdir(celebrity_path)):

        img_path = os.path.join(celebrity_path, img_name)

        try:

            embedding = DeepFace.represent(
                img_path=img_path,
                model_name="VGG-Face",
                detector_backend="mtcnn",
                enforce_detection=False
            )[0]["embedding"]

            embeddings.append(np.array(embedding))
            filenames.append(img_path)

        except Exception as e:
            print(img_path, e)


import streamlit as st
from deepface import DeepFace
import numpy as np
import os
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity

feature_list =embeddings


os.makedirs("uploads",exist_ok=True)

st.title("Which Bollywood Celebrity Are You?")

uploaded_image = st.file_uploader("Upload Image",type=["jpg","jpeg","png"])
def save_uploaded_image(uploaded_image):
    try:
        file_path = os.path.join("uploads", uploaded_image.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_image.getbuffer())

        return file_path

    except Exception as e:
        st.error(e)
        return None


def extract_embedding(img_path):

    embedding = DeepFace.represent(
        img_path=img_path,
        model_name="VGG-Face",
        detector_backend="mtcnn",
        enforce_detection=False
    )[0]["embedding"]

    return np.array(embedding)


def recommend(query_embedding):

    similarity = []

    for emb in feature_list:

        score = cosine_similarity(
            query_embedding.reshape(1,-1),
            emb.reshape(1,-1)
        )[0][0]

        similarity.append(score)

    index = np.argmax(similarity)

    return index, similarity[index]
    if uploaded_image is not None:

    image_path = save_uploaded_image(uploaded_image)

    image = Image.open(uploaded_image)

    st.image(image,width=300)

    with st.spinner("Finding your celebrity..."):

        query_embedding = extract_embedding(image_path)

        index,score = recommend(query_embedding)

        celebrity = os.path.basename(
            os.path.dirname(filenames[index])
        ).replace("_"," ")

        st.success(f"Seems like **{celebrity}**")

        st.write(f"Similarity : **{score:.3f}**")

        st.image(filenames[index],width=300)
