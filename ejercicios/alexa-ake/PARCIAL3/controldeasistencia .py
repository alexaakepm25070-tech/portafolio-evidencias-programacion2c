
asistencias = ["María", "José", "Karla", "María", "Diego", "José", "Karla", "Karla"]
alumnos_unicos = set(asistencias)
print("1. Alumnos que asistieron sin repetir:", alumnos_unicos)


materias_favoritas = {
    "María": "Biología",
    "José": "Geografía", 
    "Karla": "Artes",
    "Diego": "Química",
    "Fernanda": "Literatura"  
}

reporte_final = []
for alumno in alumnos_unicos:
    materia = materias_favoritas.get(alumno, "No registrada")
    reporte_final.append((alumno, materia))

print("\nReporte final de asistencia y materias:")
for alumno, materia in reporte_final:
    print(f"Alumno: {alumno} | Materia favorita: {materia}")


from collections import Counter
conteo = Counter(asistencias)
print("\nErrores de registro detectados:")
for alumno, veces in conteo.items():
    if veces > 1:
        print(f"{alumno} se registró {veces} veces por error")