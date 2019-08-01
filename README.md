# retrieve

![Code Sample](https://i.imgur.com/2vSkGIB.png)

No-frills library to download pre-trained models, cache it and return the local path.

## Installation
```bash
pip install -U retrieve
```

## Motivation
When using pre-trained ML models in your projects, majority of them require you to manually download the data/model weights and then specify the path in your code. Everyone in your team has to go through the same trouble of manually setting this up before they can run your models.

The idea with this library is automate this and make using pre-trained models as easy as possible.

## Usage
Pass the pre-trained model path to the retrieve.url(...) method and it will return you a filepath to the file. If the file is not already download, it is fetched and shows a progress of download.
```python
import retrieve

# URL for the pre-trained model
pretrained_model_url = '...'

# Get local path to the pre-trained model
path = retrieve.url(pretrained_model_url)
```
If source is a zip file, it's automatically extracted out and the extracted folder path is returned.
