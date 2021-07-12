"""
In order to have dry code, most of the util/helper function are defined in here.
"""

def return_json(status, msg):
    return_json = {
        "status": status,
        "msg": msg
    }
    return return_json