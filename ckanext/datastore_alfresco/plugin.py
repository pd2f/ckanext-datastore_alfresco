import ckan.plugins as plugins
from ckanext.datastore.interfaces import IDatastoreBackend
from ckanext.datastore_alfresco.alfresco_rest import DatastoreAlfrescoBackend


class DatastoreAlfrescoPlugin(plugins.SingletonPlugin):
    plugins.implements(IDatastoreBackend)
    
    
    def register_backends(self):
        return {u'alfresco': DatastoreAlfrescoBackend}
