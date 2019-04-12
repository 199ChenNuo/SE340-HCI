import sys
import bpy
import math

argv = sys.argv
argv = argv[argv.index("--") + 1:]

model_index = int(argv[0])
resolution_x = int(argv[1])
resolution_y = int(argv[2])
model_location =  argv[3]
output_dir = argv[4]
renderfile_path = argv[5]

# open render file
bpy.ops.wm.open_mainfile(filepath=renderfile_path)

# iput model
bpy.ops.import_scene.fbx(filepath = model_location)
bpy.ops.object.select_all(action='DESELECT')

# select model and join
for ob in bpy.context.scene.objects:
    if ob.type == 'MESH':
        ob.select = True
        bpy.context.scene.objects.active = ob
    else:
        ob.select = False

# check poll() to avoid exception.
if bpy.ops.object.join.poll():
    bpy.ops.object.join()

# move to origin point and resize
#bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")
bpy.context.object.location[0] = 0
bpy.context.object.location[1] = 0
bpy.context.object.location[2] = 0
#bpy.ops.transform.resize(value=(6,6,6), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH',proportional_size=1)

# render image, (four channel: R/G/B/Trans)
for m in range(3): # 三视图：正面/侧面/俯视
    if m==0:
        bpy.context.scene.camera = bpy.data.objects['Camera']
    else:
        bpy.context.scene.camera = bpy.data.objects['Camera.%03d' %m ]
    bpy.context.scene.render.resolution_x = resolution_x
    bpy.context.scene.render.resolution_y = resolution_y
    bpy.data.scenes["Scene"].render.alpha_mode = 'TRANSPARENT'
    bpy.data.scenes["Scene"].render.filepath = '{}m{}_{}_{}x{}.jpg'.format(output_dir, model_index, m, resolution_x, resolution_y)
    bpy.ops.render.render(write_still = True, use_viewport = True, layer=("0"))

# register in a file when one batch is ran through
# f = open('{}rendered_list_tmp.txt'.format(output_dir),'a')
# f.write('{}\n'.format(model_index))
# f.close()