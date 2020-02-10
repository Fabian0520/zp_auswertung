mesh laden.
BoundingBox (bb) mit mesh.bounding_box_oriented erzeugen
bb.facets_area liefert Fläche koplanarer, angrenzender faces
-> beiden größten sind die Stirnflächen -> Index im Array merken
bb.facets_normal liefert die Normalen dazu
Transformationsmatrix erzeugen und auf mesh anwenden

matrix = trimesh.geometry.align_vectors(bb.facets_normal[?], [?])

Rotationsmatrix aus zwei Vektoren berechnen, dann in Transformationsmatrix (4x4) umwandeln (compose_matrix oder so ähnlich)


