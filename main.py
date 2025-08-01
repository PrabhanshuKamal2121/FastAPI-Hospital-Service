from fastapi import FastAPI,Path,HTTPException,Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
import json 
from typing import Annotated,Literal,Optional

app = FastAPI()

class Patient(BaseModel):

    id : Annotated[str,Field(..., description = 'Enter patients id', examples = ['P001'])]
    name : Annotated[str,Field(..., description = 'enter patients name', examples = ['Nitish'])]
    city : Annotated[str,Field(..., description = 'city where the patient lives',examples = ['delhi'])] 
    age : Annotated[int,Field(..., gt=0,lt=120,description = 'age of patient')]
    gender : Annotated[Literal['male','female'],Field(..., description = 'gender of the patient', examples = ['male'])]
    height : Annotated[float,Field(...,gt=0, description = 'height of the patient in mtrs', examples = ['2.03'])]
    weight : Annotated[float,Field(...,gt=0, description = 'Weight of the patient in kgs', examples = ['75.05'])]

    @computed_field
    @property
    def bmi(self)->float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def final_verdict(self)->str:
        if self.bmi<18.5:
            return 'underweight'
        elif self.bmi <30:
            return 'Normal'
        else:
            return 'obese'
        
class PatientUpdate(BaseModel):
    name : Annotated[Optional[str],Field(default=None, description = 'enter patients name', examples = ['Nitish'])]
    city : Annotated[Optional[str],Field(default=None, description = 'city where the patient lives',examples = ['delhi'])] 
    age : Annotated[Optional[int],Field(default=None, gt=0,lt=120,description = 'age of patient')]
    gender : Annotated[Optional[Literal['male','female']],Field(default=None, description = 'gender of the patient', examples = ['male'])]
    height : Annotated[Optional[float],Field(default=None,gt=0, description = 'height of the patient in mtrs', examples = ['2.03'])]
    weight : Annotated[Optional[float],Field(default=None,gt=0, description = 'Weight of the patient in kgs', examples = ['75.05'])]

def load_data():
    with open('paitent.json','r') as f:
        data = json.load(f)

    return data 

def save_data(data):
    with open('paitent.json','w') as f:
        json.dump(data,f)

@app.get('/')
def hello():
    return{'message':'Hello, chai wale kahi keeeeee'}

@app.get('/about')
def about():
    return {'message':'Chai wale kahi keeeeee'}

@app.get('\view')
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id:str=Path(...,description='Id of patient in the db', example='P001')):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    return HTTPException(status_code = 404,detail = 'Patient not found')

@app.get('/sort')
def sort_patients(sort_by:str = Query(...,description = 'Sort in terms of height,weight,bmi'), order_by:str = Query(...,description = 'Order by in terms of asc or desc')):
    valid_fields = ['height','weight','bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail='Invalid sorting field, enter one from height,weight or bmi')
    
    order_fields=['asc','desc']

    if order_by not in order_fields:
        raise HTTPException(status_code=400,detail='Invalid order fields,enter one from asc or desc')
    
    data = load_data()
    sort_order=True if order_by== 'desc' else False
    sorted_data = sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse= sort_order)

    return sorted_data

@app.post('/create')
def create_paitient(patient: Patient):
    data = load_data()

    if patient.id in data:
        raise HTTPException(status_code=400,detail='This paitient already exists')
    
    data[patient.id] = patient.model_dump(exclude=['id'])

    save_data(data)

    return JSONResponse(status_code=201,content={'message':'patient created successfully'})

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id):
    
    data=load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404,detail='Invalid Patient ID')
    del data[patient_id]

    save_data(data)
    return JSONResponse(status_code=200,content={'message':'Successfully deleted patient'})


















@app.put('/edit/{patient_id}')
def update_patient(patient_id:str,updatePatient:PatientUpdate):
    data=load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404,detail='Invalid Patient ID')
    
    existing_patient_info = data[patient_id]

    #exclude_unset=True because when we give certain values other values tend to come as none and it will also get uptdated in data
    updated_patient_info=updatePatient.model_dump(exclude_unset=True)
    
    for key,value in updated_patient_info.items():
        existing_patient_info[key]=value
    
    
    existing_patient_info['id'] = patient_id
    patient_pydandic_obj = Patient(**existing_patient_info)
    existing_patient_info=patient_pydandic_obj.model_dump(exclude='id')

    data[patient_id]=existing_patient_info
    





    save_data(data) 
    return JSONResponse(status_code=201,content={'message':'patient updated successfully'})