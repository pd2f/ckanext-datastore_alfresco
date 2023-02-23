# encoding: utf-8

import ckan.plugins as plugins


def group_create(context, data_dict=None):
    return {'success': False, 'msg': 'nao pode'}


class DatastoreAlfrescoPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IAuthFunctions)

    def get_auth_functions(self):
        return {'group_create': group_create}
