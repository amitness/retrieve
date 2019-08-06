from tqdm import tqdm
import requests
import os
from zipfile import ZipFile

DEFAULT_CACHE_FOLDER = '.retrieve'
CHUNK_SIZE = 1024


def get_file_name(link):
    file_name = link.split('/')[-1]
    file_name = file_name.split('?')[0]
    return file_name

def get_file_size(link):
    response = requests.head(link)
    try:
        content_length = int(response.headers.get('Content-Length'))
    except Exception:
        content_length = None
    return content_length


def get_default_cache_path():
    HOME_DIR = os.path.expanduser('~')
    cache_dir = os.path.join(HOME_DIR, DEFAULT_CACHE_FOLDER)
    os.makedirs(cache_dir, exist_ok=True)
    return cache_dir


def extract_zip(source, destination):
    zip_file = ZipFile(source)
    zip_file.extractall(destination)


def download(link, destination):
    file_name = get_file_name(link)
    file_size = get_file_size(link)
    if file_size:
        progress_bar = tqdm(total=file_size, unit='B', unit_scale=True, desc=file_name)
    req = requests.get(link, stream=True)
    with open(destination, 'ab') as fp:
        for chunk in req.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                fp.write(chunk)
                if file_size:
                    progress_bar.update(CHUNK_SIZE)
    if file_size:
        progress_bar.close()


def url(link, path=None):
    file_name = get_file_name(link)
    if not path:
        path = get_default_cache_path()
    else:
        # Expand any '~' used in path
        path = os.path.expanduser(path)
        os.makedirs(path, exist_ok=True)
    target_path = os.path.join(path, file_name)
    final_path = target_path
    is_zip = file_name.endswith('.zip')
    if is_zip:
        extract_folder = file_name.replace('.zip', '')
        extracted_path = os.path.join(path, extract_folder)
        final_path = extracted_path
    if not os.path.exists(final_path):
        download(link, target_path)
        if is_zip:
            os.makedirs(extracted_path, exist_ok=True)
            extract_zip(target_path, extracted_path)
            final_path = extracted_path
    return final_path
