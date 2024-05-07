from fastapi import APIRouter, HTTPException, UploadFile
from fastapi.responses import StreamingResponse

from schema.files import File
from services.files import save_file
from services.telegram import get_file, stream_file


router = APIRouter(prefix='/api/v1/files')


@router.get(
    '/{file_id}',
    response_class=StreamingResponse,
    summary='get a file',
    description='Returns the requested file',
    name='v1:files:file-retrieve',
)
async def get(file_id: str):
    file = await get_file(file_id)

    if file.file_path is None:
        raise HTTPException(status_code=404, detail='File not found')

    streaming_file = stream_file(file.file_path)

    return StreamingResponse(
        streaming_file,
        media_type='image/jpeg'
    )


@router.post(
    '/upload/',
    response_model=File,
    summary='upload the file',
    description='Uploads the file to the server',
    name='v1:files:file-upload',
)
async def upload_file(file: UploadFile):
    file_name = await save_file(file=file)
    return File(file_name=file_name)
