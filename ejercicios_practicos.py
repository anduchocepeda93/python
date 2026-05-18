otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso * 10000 // otros_cursos_max / 100
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

print(f'El curso de Dalto dura un {int(diferencia_con_min)}%  menos que el mas rapido')
print(f'El curso de Dalto dura un {diferencia_con_max}%  menos que el mas lento')
print(f'El curso de Dalto dura un {int(diferencia_con_promedio)}%  menos que el curso promedio')

crudo_promedio = 5
crudo_dalto = 3.5

diferencia_crudos = 100 - crudo_dalto / crudo_promedio * 100
vacio_promedio = 100 - otros_cursos_promedio / crudo_promedio * 100
vacio_promedio_dalto = 100 - dalto_curso / crudo_dalto * 100

print(f'El video en crudo de Dalto dura un {int(diferencia_crudos)}% menos que un video en crudo promedio');
print(f'Un curso promedio elimina un {int(vacio_promedio)}% de un video crudo');
print(f'El curso de Dalto elimina un {int(vacio_promedio_dalto)}% de un video crudo');
