
tracker_label = 'AGST';

tracker_command = generate_python_command('vot_wrapper', ...
    {'/home/wcz/Yang/AGST/pytracking/', ...
    '/media/wcz/datasets/yang/vot-toolkit/native/trax/support/python/',...
   '/home/wcz/Yang/AGST/' });

tracker_interpreter = 'python';

tracker_linkpath = {'/media/wcz/datasets/yang/vot-toolkit/native/trax/build/'};
