import trimesh

file_name = 'zielplatte.stl'

mesh = trimesh.load(file_name)
bbox = mesh.bounding_box_oriented
# finde größte Fläche
facet_max_area_pos = bbox.facets_area.argmax()
norm_vector = {'x':[1,0,0], 'y':[0,1,0], 'z':[0,0,1]}

transform_matrix = trimesh.geometry.align_vectors(bbox.facets_normal[facet_max_area_pos], norm_vector['x'])
mesh.apply_transform(transform_matrix)
# new bbox
bbox = mesh.bounding_box_oriented
facet_max_area_pos = bbox.facets_area.argmax()
slice_location = bbox.facets_origin[facet_max_area_pos] # noch in den Körper versetzen, damit der Schnitt auch durch den Körper geht.

cross_section = mesh.slice(slice_location, norm_vector['x'])
