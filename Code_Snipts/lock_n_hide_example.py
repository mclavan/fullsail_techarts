import pymel.core as pm

def selected_lock_n_hide(attrs=[]):
    current_selection = pm.ls(selection=True)
    for current_item in current_selection:
        lock_n_hide(current_item, attrs)
    
def lock_n_hide(obj, attrs=[]):
    for current_attr in attrs:
        lock_attr = obj.attr(current_attr)
        lock_attr.set(lock=True, keyable=False)



selected_lock_n_hide(['tx', 'ty', 'tz', 'sx', 'sy', 'sz'])

