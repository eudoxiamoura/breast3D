from fastapi import FastAPI, File, UploadFile
from PIL import Image, ImageFilter
import io
from fastapi.responses import StreamingResponse

app = FastAPI()


@app.post("/process-image/")
async def process_image(file: UploadFile = File(...)):
    # Abra a imagem enviada
    image = Image.open(io.BytesIO(await file.read()))

    # Realize algum processamento (exemplo: converter para escala de cinza)
    processed_image = image.convert("L")

    # Salve a imagem em memória
    img_bytes = io.BytesIO()
    processed_image.save(img_bytes, format="JPEG")
    img_bytes.seek(0)

    return StreamingResponse(img_bytes, media_type="image/jpeg")
