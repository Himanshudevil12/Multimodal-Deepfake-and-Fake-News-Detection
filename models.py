import tensorflow as tf
from tensorflow.keras import layers, models

def build_multimodal_model():
    # 1. Vision Stream (CNN + LSTM)
    vision_input = layers.Input(shape=(None, 128, 128, 3)) # Time-distributed frames
    x = layers.TimeDistributed(layers.Conv2D(32, (3, 3), activation='relu'))(vision_input)
    x = layers.TimeDistributed(layers.MaxPooling2D((2, 2)))(x)
    x = layers.TimeDistributed(layers.Flatten())(x)
    vision_output = layers.LSTM(64)(x)

    # 2. Text Stream (Dense Embedding)
    text_input = layers.Input(shape=(500,)) # Padded sequences
    y = layers.Embedding(input_dim=10000, output_dim=128)(text_input)
    text_output = layers.GlobalAveragePooling1D()(y)

    # 3. Fusion Layer
    combined = layers.concatenate([vision_output, text_output])
    final_output = layers.Dense(1, activation='sigmoid')(combined)

    model = models.Model(inputs=[vision_input, text_input], outputs=final_output)
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model