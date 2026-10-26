# etornam_quiz_2
JABISI MPONIGNAN RICHARD
PUIT/23110014

## Image Detection Model

Deployment health check: [Ultralytics image detection endpoint](https://predict-6adf8484f2520ee816ead250-dproatj77a-uk.a.run.app)

To run image inference from the project `.venv`, install the requirements, set your Ultralytics API key in PowerShell, and provide an image path:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
$env:ULTRALYTICS_API_KEY = "YOUR_API_KEY"
python test_image_detection.py path\to\image.jpg
```

The test client sends the image to the deployment's `/predict` endpoint. Keep your API key private and do not commit it.
