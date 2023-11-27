import urllib.request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import requests

# Tải nội dung của URL
def download_url(url):
    response = requests.get(url)
    return response.text

# Trích chọn đặc trưng từ URL
def extract_features(url):
    content = download_url(url)
    # Thực hiện trích chọn đặc trưng từ nội dung của URL (ví dụ: đếm số từ)
    vectorizer = CountVectorizer()
    features = vectorizer.fit_transform([content])
    return features

# Phát hiện (phân loại) URL độc hại
def detect_malicious_url(url):
    # Chuẩn bị dữ liệu huấn luyện
    malicious_urls = ['https://example.com/malicious1', 'https://example.com/malicious2']
    benign_urls = ['https://example.com/benign1', 'https://example.com/benign2']
    X = [extract_features(url) for url in malicious_urls + benign_urls]
    y = [1] * len(malicious_urls) + [0] * len(benign_urls)

    # Chia dữ liệu thành tập huấn luyện và tập kiểm tra
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Xây dựng mô hình phân loại (ví dụ: SVM)
    classifier = SVC()
    classifier.fit(X_train, y_train)

    # Dự đoán nhãn của URL đang được kiểm tra
    features = extract_features(url)
    prediction = classifier.predict(features)

    return prediction

# Thử nghiệm
url_to_check = 'https://example.com/url_to_check'  # Thay đổi URL thành một URL hợp lệ
prediction = detect_malicious_url(url_to_check)
print(f'URL "{url_to_check}" được dự đoán là: {"Độc hại" if prediction else "An toàn"}')