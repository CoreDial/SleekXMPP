"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2011  Nathanael C. Fritz
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

from sleekxmpp.stanza import Iq, StreamFeatures
from sleekxmpp.xmlstream import ElementBase, ET, register_stanza_plugin


class Session(ElementBase):

    """
    """

    name = 'session'
    namespace = 'urn:ietf:params:xml:ns:xmpp-session'
    interfaces = set()
    plugin_attrib = 'session'
