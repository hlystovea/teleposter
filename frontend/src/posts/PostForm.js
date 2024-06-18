import { useState } from 'react';
import {
  useMutation,
  useQueryClient,
} from 'react-query';
import Card from '../common/Card';

const base_url = process.env.REACT_APP_API_URL;

const createPost = async (postData) => {
  return await fetch(base_url + 'posts/', {
    method: 'POST',
    body: JSON.stringify(postData),
    headers: {
      'Content-Type': 'application/json',
    },
  })
  .then(response => {
      if (!response.ok) {
          throw new Error(response.text());
      }
      return response.json();
  })
  .catch(error => {
      console.log('Error: ', error);
      return null;
  });
};

const uploadFile = async (file) => {
    const fileForm = new FormData()
    fileForm.append('file', file)

    return fetch(base_url + 'files/upload/', {
        method: 'POST',
        body: fileForm
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(response.text());
        }
        return response.json();
    })
    .catch(error => {
        console.log('Error: ', error);
        return null;
    });
}

function PostForm({ text="", caption="" }) {
  const [fileValue, setFileValue] = useState("");
  const queryClient = useQueryClient();

  const mutation = useMutation(createPost, {
    onSuccess: () => {
      queryClient.invalidateQueries('posts');
    },
  });

  const onSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());
    data.files = data.files.split(',');
    mutation.mutate(data);
  };

  const onChangeFileInput = async (event) => {
    const file = event.target.closest('input').files?.[0];
    if (file && file.type.startsWith('image/')) {
        const uploadedFile = await uploadFile(file);
        if (!uploadFile) {
            console.log('File upload error');
            return ;
        }
        console.log('Файл загружен');
        setFileValue(uploadedFile.file_name);
    } else {
      console.log('Можно загружать только изображения');
      return false;
    }
  };

  return (
    <Card>
      <form action="" method="POST" onSubmit={onSubmit} value={text || caption}>
          <textarea className="text-input" name="text" autoFocus></textarea>
          <input name="file" type="file" accept="image/*" onChange={onChangeFileInput} />
          <input name="files" type="hidden" value={fileValue} />
          <button className="btn-save" name="saveButton" type="submit">
              Сохранить
          </button>
          <button className="btn-cancel" name="cancelButton" type="button">
              Отмена
          </button>
      </form>
    </Card>
  );
}

export default PostForm;
