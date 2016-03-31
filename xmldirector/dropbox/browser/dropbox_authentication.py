# -*- coding: utf-8 -*-

################################################################
# xmldirector.dropbox
# (C) 2016,  Andreas Jung, www.zopyx.com, Tuebingen, Germany
################################################################


from dropbox import session

from zope.component import getUtility
from Products.Five.browser import BrowserView
from plone.registry.interfaces import IRegistry
from zope.annotation import IAnnotations

from xmldirector.dropbox.interfaces import IDropboxSettings


DROPBOX_KEY = 'xmldirector.dropbox.oauth_token'


class DropboxAuthentication(BrowserView):


    def __init__(self, context, request):
        super(DropboxAuthentication, self).__init__(context, request)
        oauth_token = self.request.get('oauth_token')
        if oauth_token:
            annotation = IAnnotations(self.context)
            annotation[DROPBOX_KEY] = oauth_token

    def get_oauth_token(self):
        annotation = IAnnotations(self.context)
        return annotation.get(DROPBOX_KEY)

    def deauthorize(self):
        annotation = IAnnotations(self.context)
        try:
            del annotation[DROPBOX_KEY]
        except KeyError:
            pass

        self.context.plone_utils.addPortalMessage(u'Dropbox access deauthorized')
        self.request.response.redirect(self.context.absolute_url() + '/authorize-dropbox')

    def get_oauth_url(self):

        registry = getUtility(IRegistry)
        settings = registry.forInterface(IDropboxSettings)
        s = session.DropboxSession(
                settings.dropbox_app_key, 
                settings.dropbox_app_secret, 
                'dropbox')
        t = s.obtain_request_token()
        authorize_url = s.build_authorize_url(t, self.context.absolute_url() + '/authorize-dropbox')
        return authorize_url
