# Example: The Box placed at -10 cm from the center on z-axis
#Using library FitsGeo
import fitsgeo as fg  # Alias to make it shorter

# Define materials from predefined databases
water = fg.Material.database("MAT_WATER", color="blue")

fg.create_scene(ax_length=5)  # Create scene with default settings

#Geomtry
box = fg.BOX([0, 0, -10], [5, 0, 0], [0, 5, 0], [0, 0, 5], name="Box", material=water)

#Cells
outer_c = fg.Cell([+box], "Outer Void", fg.MAT_OUTER)
box_c = fg.Cell([-box], "Box Cell", box.material, box.get_volume)

# Draw all surfaces with labels on centers
for s in fg.created_surfaces:
	s.draw(label_center=False)
