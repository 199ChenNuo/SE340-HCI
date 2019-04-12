
clear all
clc

% please update these parameteres before run
blender_location = '"D:\Blender Foundation\Blender\blender.exe"'; % change it to the blender setup directory in your machine
dataset_dir = 'D:\大三下\作业\HCI\Models\'; % change it to the directory where the model data are uncompressed
output_dir = 'D:\大三下\作业\HCI\render_output\'; % this is the default output directory, change it if you hope to output to other location

% static parameters
renderer_location = './render.py';

render_file = "./render.blend" ;

resolution_x = 512;
resolution_y = 512;
model_num = 20; % model numbers

% make the new file
if ~exist(output_dir,'dir') 
    mkdir(output_dir)
end

% rendering loop
for num = 0:model_num-1
    model_location = sprintf('%s%d.fbx',dataset_dir,num);
    command = sprintf('%s --background --python %s -- %d %d %d %s %s %s',blender_location,  renderer_location, num, resolution_x, resolution_y, model_location, output_dir, render_file);
    system(command);
    disp('==================================================')
    info = sprintf('model %d rendered.',num);
    disp(info);
    disp('==================================================')
end


disp('==================================================');
disp('All Finished!!');
disp('==================================================');