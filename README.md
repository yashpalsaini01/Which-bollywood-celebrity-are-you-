# Which Bollywood Celebrity Are You? 🌟

A fun and interactive application that uses facial recognition and deep learning to match your face with a Bollywood celebrity!

## 📋 Description

This application uses advanced facial recognition technology powered by deep learning models to analyze your facial features and match them with similar Bollywood celebrities. Upload your photo, and the AI will tell you which Bollywood star you resemble the most!

## ✨ Features

- **Facial Recognition**: Advanced face detection and feature extraction
- **Deep Learning Powered**: Uses VGGFace ResNet50 for accurate facial embeddings
- **Instant Celebrity Match**: Get matched with a Bollywood celebrity in seconds
- **Image Upload Support**: Simply upload your photo via a user-friendly interface
- **Side-by-Side Comparison**: View your photo next to your celebrity match
- **Fast Processing**: Efficient similarity matching using cosine similarity

## 💻 Technologies Used

### Core Technologies:
- **Python** - Main programming language
- **Streamlit** - Interactive web application framework
- **Keras VGGFace** - Pre-trained facial recognition model (ResNet50)
- **MTCNN (Multi-task Cascaded Convolutional Networks)** - Face detection
- **OpenCV (cv2)** - Image processing
- **scikit-learn** - Cosine similarity for feature matching
- **PIL (Pillow)** - Image handling and manipulation
- **NumPy** - Numerical computations
- **Pickle** - Data serialization for embeddings storage

### Machine Learning Models:
- **VGGFace (ResNet50)**: Pre-trained model for extracting facial embeddings
- Trained on large-scale face datasets for accurate facial feature extraction

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip package manager
- Webcam or image files for input

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yashpalsaini01/Which-bollywood-celebrity-are-you-.git
cd Which-bollywood-celebrity-are-you-
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Download required data files:
   - `embedding.pkl` - Pre-computed facial embeddings of Bollywood celebrities
   - `filenames.pkl` - List of celebrity image filenames

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## 🎮 How to Use

1. Open the application
2. Click on "Choose an image" to upload your photo
3. The app will:
   - Detect your face using MTCNN
   - Extract facial features using VGGFace ResNet50
   - Compare your features with celebrity embeddings
   - Display your closest Bollywood celebrity match
4. View the side-by-side comparison of your photo and the matched celebrity

## 📊 How It Works

### Process Flow:
1. **Face Detection**: MTCNN detects and localizes face in the uploaded image
2. **Image Preprocessing**: Face is cropped and resized to 224x224 pixels
3. **Feature Extraction**: VGGFace ResNet50 extracts 2048-dimensional facial embeddings
4. **Similarity Matching**: Cosine similarity is computed between your features and pre-computed celebrity embeddings
5. **Result Display**: The celebrity with the highest similarity score is displayed as your match

## 📁 Project Structure

```
Which-bollywood-celebrity-are-you-/
├── app.py                    # Main Streamlit application
├── embedding.pkl             # Pre-computed facial embeddings
├── filenames.pkl             # Celebrity image filenames
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## 🔧 Requirements

```
streamlit>=1.0.0
opencv-python>=4.5.0
keras-vggface>=0.6
mtcnn>=0.1.0
pillow>=8.0.0
scikit-learn>=0.24.0
tensorflow>=2.0.0
numpy>=1.19.0
```

## 📱 Responsive Design

The Streamlit web application is responsive and works seamlessly on:
- Desktop browsers
- Tablets
- Mobile devices

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs or issues
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Yash Pal Saini**
- GitHub: [@yashpalsaini01](https://github.com/yashpalsaini01)

## 🙌 Acknowledgments

- VGGFace team for the pre-trained facial recognition model
- MTCNN for reliable face detection
- Streamlit for the excellent web framework
- All the Bollywood celebrities featured in this application

## ⚠️ Disclaimer

This application is for entertainment purposes only. The celebrity matches are based on facial similarity and should not be taken as accurate representations of actual resemblance.

---

**Enjoy discovering your Bollywood celebrity match! 🎬✨**
