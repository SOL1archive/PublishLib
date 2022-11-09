from io import FileIO
from pathlib import Path

from .cond import Cond
from .action import Action

class Doc:
    def __init__(self, doc=None, path=None):
        if doc != None and path != None or \
            doc == None and path == None:
            raise RuntimeError('Use one of doc or path. Not both')

        if type(path) == str or type(path) == Path:
            if type(path) == str:
                with open(path, 'r') as f:
                    doc = f.read().split('\n')

            if type(path) == Path:
                with path.open() as f:
                    doc = f.read().split('\n')

            self.target_path = Path('.')

        if type(doc) == str or type(doc) == FileIO:
            if type(doc) == str:
                doc = doc.split('\n')

            if type(doc) == FileIO:
                doc = doc.read().split('\n')

        self.doc = []
        for i, line in enumerate(doc):
            self.doc.append((i, line))
        

    def save(self, file=None):
        if file == None:
            with open(file, 'w') as f:
                f.write(self.doc)
        
    def save_as(self, file):
        if type(file) == Path:
            with file.open() as f:
                f.write(self.doc)

        if type(file) == str:
            with open(file, 'w') as f:
                f.write(self.doc)

    def map(self, cond, action):
        if cond.is_init_cond:
            action(cond, self.doc)
        elif cond.is_end_cond:
            action(cond, self.doc)
        else:
            for i, _ in self.doc:
                if cond(i, self.doc):
                    self.doc = action(i, cond, self.doc)

class Pipeline:
    def __init__(self, pipeline_tuple):
        for cond, action in pipeline_tuple:
            if type(cond) != Cond or type(action) != Action:
                raise RuntimeError(f'{cond} is not Cond or {action} is not Action')

        self.pipeline = pipeline_tuple        
    
    def __call__(self, doc):
        for cond, action in self.pipeline:
            doc.map(cond, action)
