import os
import sys
from src.exception import customException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

'''
قبل استخدام dataclass (كود تقليدي):
python
Copier
Modifier
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

# إنشاء كائن
p = Person("Ali", 25)
print(p)  # الناتج: Person(name=Ali, age=25)
بعد استخدام dataclass (طريقة أكثر كفاءة):
python
Copier
Modifier
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

# إنشاء كائن
p = Person("Ali", 25)
print(p)  # الناتج: Person(name='Ali', age=25)
✅ لم نحتج إلى كتابة __init__ أو __repr__ يدويًا!

(ب) جعل الحقول غير قابلة للتغيير (frozen=True)
يمكنك جعل الكائنات غير قابلة للتعديل بعد إنشائها، مثل الكائنات في NamedTuple.

python
Copier
Modifier
from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name: str
    age: int

p = Person("Ali", 25)
p.age = 30  # ❌ سيعطي خطأ لأن الكلاس "مجمد"

Ce module fournit un décorateur et des fonctions pour générer automatiquement les méthodes spéciales comme __init__() et __repr__() 
dans les Classes de Données définies par l’utilisateur.
'''


@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts',"train.csv")
    test_data_path:str=os.path.join('artifacts',"test.csv")
    raw_data_path:str=os.path.join('artifacts',"data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
             df=pd.read_csv('notebook\data\stud.csv')
             logging.info('Read the dataset as dataframe')

             os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

             '''
             import os

             path = "/home/user/documents/report.pdf"
             directory = os.path.dirname(path)

             print(directory)  # 🔹 الناتج: "/home/user/documents"
             '''

             df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

             logging.info("Train test split initiated")
             train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

             train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
             test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

             logging.info("Inmgestion of the data iss completed")

             return(
                 self.ingestion_config.train_data_path,
                 self.ingestion_config.test_data_path
             )
        except Exception as e:
            raise customException(e,sys)


if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
