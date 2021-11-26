# 05-upload-data.py
from azureml.core import Workspace
ws = Workspace.from_config(path='./.azureml',_file_name='config.json')  ##nos conectamos a workspace
datastore = ws.get_default_datastore()          ##es el almacen de datos, donde se quieren ver los datos
datastore.upload(src_dir='./data',
                 target_path='datasets/cell_samples.csv',
                 overwrite=True)              ##propiedad de datastore