from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serilizer import NoteSerializer
from .models import Notes

@api_view(['GET', 'POST'])
def getorCreateNotes(request):
    if request.method == "GET":
        return Response(getNotes())
    elif request.method == "POST":
        return Response(createNote(request))
    
def getNotes():
    notes = Notes.objects.all()
    serilizer = NoteSerializer(notes, many= True)
    return serilizer.data

# @api_view(['POST'])
def createNote(request):
    serilizer = NoteSerializer(data= request.data)
    if serilizer.is_valid():
        serilizer.save()
    return serilizer.data


@api_view(['GET', 'PUT', 'DELETE'])
def getorModifyNote(request, id):
    if request.method == "GET":
        return Response(getNote(id))
    elif request.method == "PUT":
        return Response(updateNote(request, id))
    elif request.method == "DELETE":
        return Response(deleteNote(id))

def getNote(id):
    notes = Notes.objects.get(id = id)
    serilizer = NoteSerializer(notes, many= False)
    return serilizer.data

# @api_view(['PUT'])
def updateNote(request, id):
    note = Notes.objects.get(id = id)
    serilizer = NoteSerializer(instance= note, data= request.data)
    if serilizer.is_valid():
        serilizer.save()
    return serilizer.data

# @api_view(['DELETE'])
def deleteNote(id):
    note = Notes.objects.get(id = id)
    note.delete()
    return "Note deleted successfully."

