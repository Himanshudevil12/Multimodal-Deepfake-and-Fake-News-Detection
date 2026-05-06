import tensorflow as tf
import numpy as np

def train_with_sensitivity(model, train_data, train_labels):
    # We tell the model: "Missing a FAKE is 5x worse than missing a REAL"
    # Class 0 = Fake, Class 1 = Real
    class_weights = {0: 5.0, 1: 1.0} 
    
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
        loss='binary_crossentropy',
        metrics=['accuracy', tf.keras.metrics.Recall()] # Recall is key for Fakes [cite: 310]
    )
    
    model.fit(train_data, train_labels, class_weight=class_weights, epochs=10)

def get_calibrated_prediction(model, video_input):
    raw_score = model.predict(video_input)
    
    # HARD THRESHOLD:
    # A video is ONLY "Real" if the model is 85% certain. 
    # Otherwise, we treat it as suspicious/Fake.
    if raw_score > 0.85:
        return "🟢 REAL", raw_score
    else:
        return "🔴 FAKE / DEEPFAKE", (1 - raw_score)