# yolo-gradio-app
ultalytics' YOLO + gradio WebUI

### To install [uv](https://docs.astral.sh/uv/getting-started/installation/):

#### For Linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### For Windows:
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### To setup project:
```
uv sync --extra build
```

### To run the app:
```
uvicorn src.main:app --reload
```
![Screenshot 2024-11-28 220429](https://github.com/user-attachments/assets/276fc8e2-b747-4815-90a4-910a40dfd737)
