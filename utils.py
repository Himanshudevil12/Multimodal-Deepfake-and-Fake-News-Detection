import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import seaborn as sns

def perform_pca_visualization(embeddings, labels, output_path='results/pca_clusters.png'):
    """Reduces high-dim text embeddings to 2D to show Real vs Fake clusters."""
    pca = PCA(n_components=2)
    reduced_data = pca.fit_transform(embeddings)
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=reduced_data[:, 0], y=reduced_data[:, 1], hue=labels, palette='viridis')
    plt.title("PCA Analysis: NLP Feature Separation")
    plt.savefig(output_path)
    plt.close()
    print(f"✅ PCA Visualization saved to {output_path}")

def analyze_svd_noise(image_gray, output_path='results/svd_spectrum.png'):
    """Performs SVD to analyze the singular value decay for deepfake detection."""
    U, S, Vt = np.linalg.svd(image_gray, full_matrices=False)
    
    plt.figure()
    plt.semilogy(S)
    plt.title("SVD Singular Value Spectrum (Noise Analysis)")
    plt.ylabel("Singular Value (Log Scale)")
    plt.xlabel("Rank")
    plt.savefig(output_path)
    plt.close()
    print(f"✅ SVD Analysis saved to {output_path}")