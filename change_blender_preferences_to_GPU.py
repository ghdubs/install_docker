import bpy

bpy.context.preferences.addons['cycles'].preferences.compute_device_type = 'CUDA'

# Enable OptiX as the CUDA backend
bpy.context.preferences.addons['cycles'].preferences.get_devices()
bpy.context.preferences.addons['cycles'].preferences.compute_device = 'OPTIX'

# Enable only GPU devices and disable CPU devices
for device in bpy.context.preferences.addons['cycles'].preferences.devices:
    if device.type == 'CUDA':
        device.use = True
    elif device.type == 'OPTIX':
        device.use = True
    else:
        device.use = False

# Save the preferences
bpy.ops.wm.save_userpref()