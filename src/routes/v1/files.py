from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from services.telegram import get_file, stream_file


router = APIRouter(prefix='/api/v1/files')


@router.get(
    '/{file_id}',
    response_class=StreamingResponse,
    summary='get a post',
    description='Responds a post',
    name='v1:posts:post-retrieve',
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
