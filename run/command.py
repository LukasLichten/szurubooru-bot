# All commands are handled in here

from . import api_handler
import json
from os import path

def mass_tag(settings):
    print('Running Mass Tagging...');

    if 'ARG_TAGS' not in settings:
        stop_early('No Tags specified');
    tags = settings['ARG_TAGS'];

    create_tags_category = ''; # '' means don't create tags and exit if tag is missing

    if 'ARG_CREATE_TAG' in settings:
        settings['ARG_CREATE_TAG'] = settings['ARG_CREATE_TAG'].lower();
    
    if 'ARG_CREATE_TAG' not in settings or settings['ARG_CREATE_TAG'] == 'true':
        # We are going to create Tags if necessary, so we need the tag category

        if 'ARG_TAG_CATEGORY' in settings:
            # user defined the category
            create_tags_category = settings['ARG_TAG_CATEGORY']; 
            (code,j) = api_handler.get(settings['API_URL']+'tag-category/'+create_tags_category, settings['HEADER']);
            if code != 200:
                stop_early('Tag-Category {0} does not exist, check your spelling, or either create it or remove the TAG_CATEGORY arg if you know the tags exist or to just create them in default'.format(t))
        else:
            # we have to find the default
            (code,j) = api_handler.get(settings['API_URL']+'tag-categories', settings['HEADER']);
            cat_list = j['results'];

            for cat in cat_list:
                if 'name' in cat and 'default' in cat and cat['default'] == True:
                    create_tags_category = cat['name'];
                    break;
    

    # Making sure the tags exist already
    for t in tags:
        (code,j) = api_handler.get(settings['API_URL']+'tag/'+t, settings['HEADER']);
        if code != 200:
            if create_tags_category == '':
                stop_early('Tag {0} does not exist, but tag creation is off'.format(t));
            
            # creating tag
            tag_dict = {"names":[t],"category":create_tags_category};
            (code,j) = api_handler.post(settings['API_URL']+'tags', settings['HEADER'], json.dumps(tag_dict));

            if code != 200:
                stop_early('Failed to create tag {0}, api gave reason: {1}'.format(t, j['description']))
            
            print('Tag {0} did not exist, was created in category {1}'.format(t,create_tags_category));
    
    print('Adding Tags {0}...'.format(tags));

    # Gathering the posts
    ids = get_post_ids(settings);
    
    #Processing the posts
    x = 1;
    for post_id in ids:
        (code,old_post) = api_handler.get(settings['API_URL']+'post/'+str(post_id), settings['HEADER']);
        if code == 200:
            edit_tag_list = [];
            if 'tags' in old_post:
                for t_entry in old_post["tags"]:
                    edit_tag_list.append(t_entry['names'][0]);
        
            # Iterating over the tags to add
            for t in tags:

                # Adding tag
                if t not in edit_tag_list:
                    edit_tag_list.append(t);
        
            new_post = {'version': old_post['version'], 'tags':edit_tag_list};

            (code,j) = api_handler.put(settings['API_URL']+'post/'+str(post_id), settings['HEADER'], json.dumps(new_post));
            if code != 200:
                stop_early('Failed to update post {0} ({1}/{2}), reason: {3}'.format(post_id, x, len(ids), j['description']));
        
            print('Done Post {0} ({1}/{2})'.format(post_id,x,len(ids)));
        else:
            print('Post not found, skipping post {0} ({1}/{2})'.format(post_id,x,len(ids)));
        x = x + 1;
            
    
    print('Mass Tagging Complete')

def image2notes(settings):
    print('Running Image2Notes...');

    if 'ARG_LANG' not in settings:
        settings['ARG_LANG'] = 'eng';

    try:
        from . import image_processing;

        # Gathering the posts
        ids = get_post_ids(settings);

        if 'DATA_PATH' not in settings:
            stop_early('Data Path not defined, but required');

        x = 1;
        for post_id in ids:
            (code,old_post) = api_handler.get(settings['API_URL']+'post/'+str(post_id), settings['HEADER']);
            
            if code == 200:
                file_path = settings['DATA_PATH'] + old_post['contentUrl'];

                if file_path.find('http') != -1: # external data source
                    if api_handler.get_code(file_path) != 200:
                        stop_early('File does not exist, make sure the data url is correct: {0}'.format(settings['DATA_PATH']));
                
                    file_path = api_handler.download_file(file_path, 'tmp/'+path.basename(file_path));
                else:
                    if path.exists(file_path):
                        stop_early('File does not exist, make sure the data path is correct: {0}'.format(settings['DATA_PATH']));

                # Gathering the text
                text = image_processing.image_2_text(file_path, settings['ARG_LANG']);

                # Updating notes if applies
                if text != '':
                    post_update = {'version': old_post['version'], 'notes': [{'polygon': [[0,0],[0,0],[0,0],[0,0]],'text': text}]};

                    (code,j) = api_handler.put(settings['API_URL']+'post/'+str(post_id), settings['HEADER'], json.dumps(post_update));
                    if code != 200:
                        stop_early('Failed to update post {0} ({1}/{2}), reason: {3}'.format(post_id, x, len(ids), j['description']));
            
                    print('Done Post {0} ({1}/{2}): {3}'.format(post_id,x,len(ids),text));
                else:
                    print('No Text, skipping post {0} ({1}/{2})'.format(post_id,x,len(ids)));
                

                # Delete Temporary file
                if file_path.startswith('tmp'):
                    path.os.remove(file_path);
            else:
                print('Post not found, skipping post {0} ({1}/{2})'.format(post_id,x,len(ids)));
            x = x + 1;



    except ModuleNotFoundError:
        stop_early('pytesseract python package is required for this functionality. Install it using pip. pytesseract is only a wrapper for tesseract, so before you run this and get a new error install tesseract-ocr via your package manager');
    
    

            
        



def get_post_ids(settings):
    if 'ARG_POSTS' not in settings:
        stop_early('No Posts specified');
    
    ids = [];
    for ele in settings['ARG_POSTS']:
        if ele.isdigit():
            ids.append(int(ele));
        else:
            ran = ele.split('-',maxsplit=1);
            if len(ran) < 2:
                stop_early('POSTS argument string maleformed');
            if not ran[0].isdigit() or not ran[1].isdigit():
                stop_early('POSTS argument string maleformed');
            
            ids.extend(range(int(ran[0]),int(ran[1])+1));
    
    return ids;

def stop_early(message):
    print('Terminal: ' + message);
    exit();