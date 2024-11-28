import os
import gradio as gr
from ultralytics import YOLO

from fastapi import FastAPI
app = FastAPI()


# Function to train YOLO model
def train_yolo(
    data_path, model_choice="yolo11s", epochs=10, img_size=640, batch_size=16
):
    if not os.path.exists(data_path):
        return "Error: The specified data file path does not exist."

    # Initialize YOLO model
    model = YOLO(model_choice)

    # Train the model
    model.train(data=data_path, epochs=epochs, imgsz=img_size, batch=batch_size)

    return f"Model trained successfully for {epochs} epochs with {model_choice}."


def create_gradio_interface():
    with gr.Blocks() as app:
        # Title
        gr.Markdown("# YOLO Training Gradio App")

        # Input fields
        data_file_path = gr.Textbox(
            label="Enter Dataset Path (data.yaml)",
            placeholder="/path/to/data.yaml",
            lines=1,
        )

        # train_data_path = gr.Textbox(
        #     label="Enter Train Data Path",
        #     placeholder="/path/to/train/folder",
        #     lines=1,
        # )

        # test_data_path = gr.Textbox(
        #     label="Enter Test Data Path",
        #     placeholder="/path/to/test/folder",
        #     lines=1,
        # )

        # val_data_path = gr.Textbox(
        #     label="Enter Val Data Path",
        #     placeholder="/path/to/val/folder",
        #     lines=1,
        # )

        model_choice = gr.Dropdown(
            choices=[
                "yolov5n",
                "yolov5s",
                "yolov5m",
                "yolov5l",
                "yolov5x",
                "yolov8n",
                "yolov8s",
                "yolov8m",
                "yolov8l",
                "yolov8x",
                "yolov9n",
                "yolov9s",
                "yolov9m",
                "yolov9l",
                "yolov9x",
                "yolov10n",
                "yolov10s",
                "yolov10m",
                "yolov10l",
                "yolov10x",
                "yolo11n",
                "yolo11s",
                "yolo11m",
                "yolo11l",
                "yolo11x",
            ],
            label="Select Model",
            value="yolo11s",
        )

        epochs = gr.Slider(minimum=1, maximum=100, label="Number of Epochs", value=1000, step=1)
        img_size = gr.Slider(minimum=320, maximum=1280, label="Image Size", value=640, step=1)
        batch_size = gr.Slider(minimum=1, maximum=64, label="Batch Size", value=16, step=1)

        # Output field
        output_text = gr.Textbox(label="Training Output")

        # Submit button
        submit_button = gr.Button("Train Model")

        # Define what happens on submit
        submit_button.click(
            fn=train_yolo,
            inputs=[data_file_path, model_choice, epochs, img_size, batch_size],
            outputs=output_text,
        )

    return app

gradio_app = create_gradio_interface()
app = gr.mount_gradio_app(app, gradio_app, path='/')