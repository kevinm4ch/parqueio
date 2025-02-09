from datetime import timezone
from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router, Schema
from .models import Patio

router = Router()

class PatioIn(Schema):
    descricao: str
    quantidade_vagas: int

class PatioOut(Schema):
    id: int
    descricao: str
    quantidade_vagas: int
    vagas_ocupadas: int

@router.get("/", response=List[PatioOut])
def listar_patios(request):
    qs = Patio.objects.all
    return qs

@router.get("/{patio_id}", response=PatioOut)
def buscar_patio(request, patio_id:int):
    patio = get_object_or_404(Patio, id=patio_id)
    return patio

@router.post("/")
def add_patio(request, payload: PatioIn):
    patio = Patio.objects.create(**payload.dict())
    patio.save()
    return {"id": patio.id}

@router.put("/{patio_id}")
def alt_patio(request, patio_id:int, payload: PatioIn):
    patio = get_object_or_404(Patio, id=patio_id)
    #Alterar as propriedade do elemento
    for attr, value in payload.dict().items():
        setattr(patio, attr, value)

    #Valida se a quantidade de vagas é maior ou igual o numero de vagas ocupadas
    if(patio.quantidade_vagas < patio.vagas_ocupadas):
        return {"success": False, "message": "Não foi possível alterar a quantidade  de vagas"}

    setattr(patio, "data_atualizacao", timezone.now())
    patio.save()
    return {"Success": True}

@router.delete("/{patio_id}")
def del_patio(request, patio_id:int):
    patio = get_object_or_404(Patio, id=patio_id)
    patio.delete()
    return {"success": True}



